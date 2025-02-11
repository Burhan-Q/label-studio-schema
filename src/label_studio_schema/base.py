from pydantic import BaseModel

from label_studio_schema.tools.convert import into_xml


class BaseTag(BaseModel):
    """
    The base class for all tags in the Label Studio schema. It provides methods for converting the tag object to XML format.

    Methods:
    ---
        xml(no_defaults: bool = False) -> str:
            Convert the tag object to an XML string.
    """
    def xml(self, no_defaults: bool = False) -> str:
        """
        Converts the model instance into an XML string representation.

        Arguments:
        ---
            no_defaults (bool):
                If True, fields with default values will be excluded from the XML output. Defaults to False.

        Returns:
        ---
            str: The XML string representation of the model instance.
        """
        fields: list[str] = into_xml(self.model_dump(exclude_defaults=no_defaults))
        return f"<{self.__class__.__name__}{(' ' + ' '.join(fields) if fields else '')} />"

    def __str__(self) -> str:
        return self.xml()


class Control(BaseTag):
    """
    Tags that you can use to annotate the objects. For example, use labels for semantic and named entity tasks, choices for classification tasks, textarea for transcription tasks, and more.
    
    Attributes:
    ---
        name (str):
            The name of the control tag object.
        to_name (str):
            The name of the object to annotate.
    """
    name: str
    to_name: str

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key: str) -> str:
        raise NotImplementedError

    def __setitem__(self, key: str, value: str) -> None:
        raise NotImplementedError

    def __delitem__(self, key: str) -> None:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, key: str) -> bool:
        raise NotImplementedError

    def append(self, item: str) -> None:
        raise NotImplementedError


class Object(BaseTag):
    """
    Tags for data types, used to display elements in a task that can be labeled such as audio, HTML, images, paragraphs, text, and more.

    Attributes:
    ---
        name (str):
            The name of the object tag object.
        value (str):
            The value of the object tag object.
    """
    name: str
    value: str
