"""Converters for Label Studio schema."""


def str_from_bool(value: bool, lower: bool = True) -> str:
    """
    Convert a boolean value to its string representation.

    Arguments:
        value (bool):
            The boolean value to convert.
        lower (bool, optional):
            If True, return the string in lowercase. If False, return the string in uppercase. Defaults to True.

    Returns:
    ---
        str: The string representation of the boolean value.
    """
    return str(value).lower() if lower else str(value).upper()


def snake2camel(s: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Arguments:
    ---
        s (str):
        The input string in snake_case format.

    Returns:
    ---
        str: The converted string in camelCase format.
    """
    return "".join(w.capitalize() if n else w.lower() for n, w in enumerate(s.split("_")))


def into_xml(model_dict: dict, ignore: set[str]) -> list[str]:
    """
    Converts a dictionary into a list of XML attribute strings, ignoring specified keys.

    Arguments:
    ---
        model_dict (dict):
            The dictionary to convert, where keys are attribute names and values are attribute values.
        ignore (set[str]):
            A set of keys to ignore during conversion.

    Returns:
    ---
        list[str]: A list of strings representing XML attributes in the format 'key="value"'.
    """
    res = []
    ignore = set(list(ignore)) or set()
    for k, v in model_dict.items():
        if v is not None and (v or isinstance(v, bool)) and k not in ignore:
            k: str = snake2camel(k)
            v = str_from_bool(v) if isinstance(v, bool) else v
            res.append(f'{k}="{v}"')
    return res
