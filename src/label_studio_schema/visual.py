from typing import Literal, Optional

from pydantic import BaseModel, Field


class FilterTag(BaseModel):
    """
    Filter Tag for Filter Search.

    Customize Label Studio with the Filter tag to filter labels to accelerate labeling for machine learning and data science projects.
    """

    placeholder: str = Field(
        ..., description="='Quick Filter']      - Placeholder text for filter."
    )
    minlength: Optional[int] = Field(3, description="Size of the filter.")
    style: str = Field(..., description="CSS style of the string.")
    hotkey: str = Field(
        ..., description="Hotkey to use to focus on the filter text area."
    )


class HeaderTag(BaseModel):
    """
    Header Tag to Show Headers.

    Customize Label Studio with the Header tag to display a header for a labeling task for machine learning and data science projects.
    """

    value: str = Field(
        ...,
        description="Text of header, either static text or the field name in data to use for the header.",
    )
    size: Optional[int] = Field(
        4, description="Level of header on a page, used to control size of the text."
    )
    style: str = Field(..., description="CSS style for the header.")
    underline: Optional[bool] = Field(
        False, description="Whether to underline the header."
    )


class StyleTag(BaseModel):
    """
    Style Tag to use CSS Styles.

    Customize Label Studio with CSS styles to modify the labeling interface for machine learning and data science projects.
    """

    CSS: str = Field(..., description="property]  - CSS property and value to apply.")


class ViewTag(BaseModel):
    """
    View Tag for Defining How Blocks are Displayed.

    Customize how blocks are displayed on the labeling interface in Label Studio for machine learning and data science projects.
    """

    display: Literal["block", "inline"] = Field("...", description=".")
    style: str = Field(..., description="CSS style string.")
    className: str = Field(
        ..., description="Class name of the CSS style to apply. Use with the Style tag."
    )
    idAttr: str = Field(..., description="Unique ID attribute to use in CSS.")
    visibleWhen: Literal[
        "region-selected", "choice-selected", "no-region-selected", "choice-unselected"
    ] = Field(
        "...",
        description="Control visibility of the content. Can also be used with the `when*` parameters below to narrow visibility.",
    )
    whenTagName: str = Field(
        ...,
        description="Use with `visibleWhen`. Narrow down visibility by tag name. For regions, use the name of the object tag, for choices, use the name of the `choices` tag.",
    )
    whenLabelValue: str = Field(
        ...,
        description="Use with `visibleWhen='region-selected'`. Narrow down visibility by label value. Multiple values can be separated with commas.",
    )
    whenChoiceValue: str = Field(
        ...,
        description="Use with `visibleWhen` (`'choice-selected'` or `'choice-unselected'`) and `whenTagName`, both are required. Narrow down visibility by choice value. Multiple values can be separated with commas.",
    )
