"""
Parse the tags in the Label Studio schema and generate Pydantic models.
"""

import re
from pathlib import Path
from typing import Generator, LiteralString

from label_studio_schema import LS_REPO, ROOT

INDENT: str = " " * 4
TAGS_DIR: Path = LS_REPO / "web/libs/editor/src/tags"
DOCS_DIR: Path = LS_REPO / "docs/source/tags"  # cross check
FILES: Generator[Path, None, None] = TAGS_DIR.rglob("*.js*")
DOCS_FILES: list[Path] = [
    f for f in DOCS_DIR.rglob("*.md") if f.stem != "index"
]  # ignore index.md and tags not found here

TAG_NAME: re.Pattern[str] = re.compile(r"@name(.*)")
TAG_META_TITLE: re.Pattern[str] = re.compile(r"@meta_title(.*)")
TAG_DESC: re.Pattern[str] = re.compile(r"@meta_description(.*)")
MULTILINE_COMMENT: re.Pattern[str] = re.compile(r"/\*\*(.*?)\*/", re.DOTALL)
TAG_ARG_RGX: re.Pattern[str] = re.compile(
    r"@param\s\{([-a-zA-Z0-9|]+=?)\}\s\[?(\w+)(=[a-zA-Z-0-9.#:]+)?\]?(.*)\n"
)
TAG_MODEL_RGX: re.Pattern[str] = re.compile(r"types.model\((.*?)\);", re.DOTALL)
TYPE_CONVERT: dict[str, str] = {
    "string": "str",
    "number": "int",
    "float": "float",
    "boolean": "bool",
    "array": "list",
    "object": "dict",
    "function": "Callable",
    "null": "None",
}


def convert_arg_types(type_list: list[str], is_optional: bool, arg_default: str) -> tuple[str, str]:
    arg_types = "|".join([TYPE_CONVERT.get(t, "str") for t in type_list])

    if arg_types == "bool" and is_optional:
        arg_default = arg_default == "true" and arg_default != "false"
    elif arg_types == "str" and is_optional:
        arg_default = (
            f'"{arg_default}"' if arg_default not in ["...", "None"] else arg_default
        )

    if not all(t in TYPE_CONVERT for t in type_list):
        arg_types = (
            f"{'Optional[' if is_optional else ''}Literal["
            + ", ".join([f'"{t}"' for t in type_list])
            + f"]{']' if is_optional else ''}"
        )
        arg_default: str = f'"{arg_default}"'
    elif is_optional:
        arg_types: str = f"Optional[{arg_types}]"

    return arg_default, arg_types


def make_args(args: list[tuple[str]]) -> list[str]:
    is_opt = False
    str_args = []
    for arg in args:
        arg_type, arg_name, arg_default, arg_desc = arg

        arg_name: str = str(arg_name).strip() if arg_name else ""
        arg_desc = str(arg_desc).strip().strip("- ") if arg_desc else ""

        arg_desc: str = arg_desc if arg_desc.endswith(".") else arg_desc + "."
        arg_desc = arg_desc.replace('"', "'")
        is_opt: bool = "=" in str(arg_default)

        arg_default = str(arg_default).strip("").strip("=") if arg_default else None
        if is_opt and arg_default is None:
            arg_default: str = "None"
        elif not is_opt and arg_default is None:
            arg_default: str = "..."

        _types: list[str] = [t.strip("=") for t in arg_type.split("|")]
        arg_default, arg_types = convert_arg_types(
            _types,
            is_opt,
            arg_default,
        )

        str_args.append(
            f'{INDENT}{arg_name}: {arg_types} = Field({arg_default}, description="{arg_desc}")'
        )

    return str_args


def files2keep(file: Path) -> bool:
    return (
        "__" not in file.stem
        and file.stem.lower() in [f.stem.lower() for f in DOCS_FILES]
        and (file.parent.name == "visual" if file.stem.lower() == "view" else True)
    )  # NOTE object/RichText/view.jsx not properly filtered


base_imports: str = "\n".join(["from typing import Literal, Optional", ""])
third_party_imports: str = "\n".join(["from pydantic import BaseModel, Field", ""])
local_imports: str = "\n".join([""])

_imports: LiteralString = (
    base_imports + "\n" + third_party_imports + "\n" + local_imports
)

py_files = {}
for file in filter(files2keep, FILES):
    text = file.read_text("utf-8")
    tag_dir: str = file.parent.relative_to(TAGS_DIR).parts
    tag_dir = tag_dir[0] if tag_dir else "control"

    comment: re.Match[str] | None = MULTILINE_COMMENT.search(text)

    if comment is not None:
        comment = str(comment.group(1)).strip()
        comment += "\n" if not str(comment).endswith("\n") else ""

        if name := TAG_NAME.search(comment):
            name: str = str(name.group(1)).strip() if name else file.stem

        if meta_title := TAG_META_TITLE.search(comment):
            meta_title: str = (
                str(meta_title.group(1)).strip()
                + ("" if str(meta_title.group()).endswith(".") else ".")
                if meta_title
                else ""
            )

        if meta_desc := TAG_DESC.search(comment):
            meta_desc: str = str(meta_desc.group(1)).strip() if meta_desc else ""

            args: list[tuple[str]] = TAG_ARG_RGX.findall(comment)
            if args:
                arg_block: str = "\n".join(make_args(args))
            else:
                arg_block = ""

            if arg_block:
                if not (meta_title or meta_desc):
                    meta_title: str = str(comment).splitlines()[0].strip("*").strip()
                doc_str = (
                    f'{INDENT}"""\n{INDENT}{meta_title}\n\n{INDENT}{meta_desc}\n{INDENT}"""\n'
                    if meta_desc
                    else f'{INDENT}"""\n{INDENT}{meta_title}\n{INDENT}"""\n'
                )
                text_out: str = (
                    f"class {file.stem}Tag(BaseModel):\n{doc_str}{arg_block}\n"
                )
                key = tag_dir + ".py"
                if key in py_files:
                    py_files[key] += f"\n\n{text_out}"
                else:
                    py_files[key] = f"{_imports}\n" + text_out

# Write to files
for k, v in py_files.items():
    (ROOT / k).write_text(v, "utf-8")
