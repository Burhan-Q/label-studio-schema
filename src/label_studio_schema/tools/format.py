import xml.dom.minidom
from xml.parsers.expat import ExpatError


def clean_lines(s: str) -> str:
    """
    Remove leading and trailing whitespace from each line in the input string,
    and return a string with non-empty lines joined by newline characters.

    Arguments:
    ---
        s (str):
            The input string to be cleaned.

    Returns:
    ---
        str: A string with each line stripped of leading and trailing whitespace,
             and only non-empty lines included, joined by newline characters.
    """
    return "\n".join([line.strip() for line in s.splitlines() if line.strip()])


def format_xml_string(xml_string, indent_size=4) -> str:
    """
    Formats an XML string with the specified indentation size.
    
    Arguments:
    ---
        xml_string (str):
            The XML string to be formatted.
        indent_size (int, optional):
            The number of spaces to use for indentation. Defaults to 4.
    
    Returns:
    ---
        str: The formatted XML string.
    
    Raises:
    ---
        ExpatError: If there is an error parsing the XML string.
    """
    try:
        dom: xml.dom.minidom.Document = xml.dom.minidom.parseString(xml_string)
        return clean_lines(dom.toprettyxml(indent=" " * indent_size))

    except ExpatError as e:
        return f"Error parsing XML: {e}"
