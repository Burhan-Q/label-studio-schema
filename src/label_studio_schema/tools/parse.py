"""
Parse the tags in the Label Studio schema and generate Pydantic models.
"""

import re
from pathlib import Path
from typing import Generator, Literal, LiteralString

from label_studio_schema import LS_REPO, ROOT


TAGS_DIR: Path = LS_REPO / "web/libs/editor/src/tags"
DOCS_DIR: Path = LS_REPO / "docs/source/tags"  # cross check
FILES: Generator[Path, None, None] = TAGS_DIR.rglob("*.js*")
DOCS_FILES: Generator[Path, None, None] = DOCS_DIR.rglob(
    "*.md"
)  # ignore index.md and tags not found here

TAG_NAME: re.Pattern[str] = re.compile(r"@name(.*)")
TAG_META_TITLE: re.Pattern[str] = re.compile(r"@meta_title(.*)")
TAG_DESC: re.Pattern[str] = re.compile(r"@meta_description(.*)")
TAG_ARG_RGX: re.Pattern[str] = re.compile(
    r"@param\s\{([-a-zA-Z0-9|]+=?)\}\s\[?(\w+)(=[a-zA-Z-0-9.#:]+)?\]?(.*)\n"
)
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
            arg_default: Literal["None"] = "None"
        elif not is_opt and arg_default is None:
            arg_default: Literal["..."] = "..."

        _types: list[str] = [t.strip("=") for t in arg_type.split("|")]
        if all(t in TYPE_CONVERT for t in _types):  # could be literals
            arg_types: str = "|".join([TYPE_CONVERT.get(str(t), "str") for t in _types])
            # if is_opt and arg_types:
            #     arg_types: str = f"Optional[{arg_types}]"
            if arg_types == "bool" and is_opt:
                arg_default: bool = arg_default == "true" and arg_default != "false"
            if arg_types == "str" and is_opt:
                arg_default: str = (
                    f'"{arg_default}"'
                    if arg_default not in ["...", "None"]
                    else arg_default
                )
            if arg_types and is_opt:
                arg_types: str = f"Optional[{arg_types}]"
        else:
            arg_types: str = (
                f"{'Optional[' if is_opt else ''}Literal["
                + ", ".join([f'"{t}"' for t in _types])
                + f"]{']' if is_opt else ''}"
            )
            arg_default: str = f'"{arg_default}"'

        str_args.append(
            f'    {arg_name}: {arg_types} = Field({arg_default}, description="{arg_desc}")'
        )

    return str_args


base_imports: str = "\n".join(["from typing import Literal, Optional", ""])
third_party_imports: str = "\n".join(["from pydantic import BaseModel, Field", ""])
local_imports: str = "\n".join([""])

_imports: LiteralString = (
    base_imports + "\n" + third_party_imports + "\n" + local_imports
)

for file in FILES:
    if "__" in file.name:
        continue

    text = file.read_text("utf-8")
    tag_dir: str = file.parent.relative_to(TAGS_DIR).name

    if name := TAG_NAME.search(text):
        name = name.group(1).strip() if name else file.stem

    if meta_title := TAG_META_TITLE.search(text):
        meta_title = (
            meta_title.group(1).strip()
            + ("" if meta_title.group().endswith(".") else ".")
            if meta_title
            else ""
        )

    if meta_desc := TAG_DESC.search(text):
        meta_desc = meta_desc.group(1).strip() if meta_desc else ""

    args: list[tuple[str]] = TAG_ARG_RGX.findall(text)
    if args:
        arg_block: str = "\n".join(make_args(args))
    else:
        arg_block = ""

    if arg_block:
        text_out: str = (
            f"{_imports}"
            f"class {file.stem}Tag(BaseModel):\n"
            f'    """\n    {meta_title}\n\n    {meta_desc}"""\n'
            f"{arg_block}"
            "\n"
        )
        save_to = ROOT / tag_dir
        if not save_to.exists():
            save_to.mkdir()
        (save_to / f"{file.stem}.py").write_text(text_out, "utf-8")
