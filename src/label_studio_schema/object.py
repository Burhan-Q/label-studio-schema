from typing import Literal, Optional

from pydantic import BaseModel, Field


class AudioTag(BaseModel):
    """
    Audio Tag for Labeling Audio.

    Customize Label Studio to label audio data for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(
        ..., description="Data field containing path or a URL to the audio."
    )
    hotkey: str = Field(..., description="Hotkey used to play or pause audio.")
    cursorwidth: Optional[str] = Field(
        "1", description="Audio pane cursor width. It is measured in pixels."
    )
    cursorcolor: Optional[str] = Field(
        "#333",
        description="Audio pane cursor color. The color should be specified in hex decimal string.",
    )


class HyperTextTag(BaseModel):
    """
    Hypertext Tags for Hypertext Markup (HTML).

    Label Studio Hypertext Tags customize Label Studio for hypertext markup (HTML) for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(..., description="Value of the element.")
    valueType: Optional[Literal["url", "text"]] = Field(
        "text",
        description="Whether the text is stored directly in uploaded data or needs to be loaded from a URL.",
    )
    inline: Optional[bool] = Field(
        False,
        description="Whether to embed HTML directly in Label Studio or use an iframe.",
    )
    saveTextResult: Literal["yes", "no"] = Field(
        "...",
        description="Whether to store labeled text along with the results. By default, doesn't store text for `valueType=url`.",
    )
    encoding: Literal["none", "base64", "base64unicode"] = Field(
        "...", description="How to decode values from encoded strings."
    )
    selectionEnabled: Optional[bool] = Field(
        True, description="Enable or disable selection."
    )
    clickableLinks: Optional[bool] = Field(
        False,
        description="Whether to allow opening resources from links in the hypertext markup.",
    )
    highlightColor: str = Field(
        ...,
        description="Hex string with highlight color, if not provided uses the labels color.",
    )
    showLabels: bool = Field(
        ...,
        description="Whether or not to show labels next to the region; unset (by default) — use editor settings; true/false — override settings.",
    )
    granularity: Literal["symbol", "word", "sentence", "paragraph"] = Field(
        "...", description="Control region selection granularity."
    )


class ListTag(BaseModel):
    """
    List Tag displays items of the same type, like articles, search results, etc.

    Customize Label Studio by displaying similar items from task data for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(
        ...,
        description="Data field containing a JSON with array of objects (id, title, body) to rank.",
    )
    title: str = Field(..., description="Title of the list.")


class TableTag(BaseModel):
    """
    Table Tag to Display Keys & Values in Tables.

    Customize Label Studio by displaying key-value pairs in tasks for machine learning and data science projects.
    """

    value: str = Field(
        ..., description="Data field value containing JSON type for Table."
    )
    valueType: str = Field(..., description="Value to define the data type in Table.")


class TextTag(BaseModel):
    """
    Text Tags for Text Objects.

    Customize Label Studio with the Text tag to annotate text for NLP and NER machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(..., description="Data field containing text or a UR.")
    valueType: Optional[Literal["url", "text"]] = Field(
        "text",
        description="Whether the text is stored directly in uploaded data or needs to be loaded from a URL.",
    )
    saveTextResult: Literal["yes", "no"] = Field(
        "...",
        description="Whether to store labeled text along with the results. By default, doesn't store text for `valueType=url`.",
    )
    encoding: Literal["none", "base64", "base64unicode"] = Field(
        "...", description="How to decode values from encoded strings."
    )
    selectionEnabled: Optional[bool] = Field(
        True, description="Enable or disable selection."
    )
    highlightColor: str = Field(
        ...,
        description="Hex string with highlight color, if not provided uses the labels color.",
    )
    showLabels: bool = Field(
        ...,
        description="Whether or not to show labels next to the region; unset (by default) — use editor settings; true/false — override settings.",
    )
    granularity: Literal["symbol", "word", "sentence", "paragraph"] = Field(
        "...", description="Control region selection granularity."
    )


class TimeSeriesTag(BaseModel):
    """
    Time Series Tags for Time Series Data.

    Customize Label Studio with the TimeSeries tag to annotate time series data for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(
        ...,
        description="Key used to look up the data, either URLs for your time-series if valueType=url, otherwise expects JSON.",
    )
    valueType: Optional[Literal["url", "json"]] = Field(
        "url",
        description="Format of time series data provided. If set to 'url' then Label Studio loads value references inside `value` key, otherwise it expects JSON.",
    )
    timeColumn: str = Field(
        ...,
        description="Column name or index that provides temporal values. If your time series data has no temporal column then one is automatically generated.",
    )
    timeFormat: str = Field(
        ...,
        description="Pattern used to parse values inside timeColumn, parsing is provided by d3, and follows `strftime` implementation.",
    )
    timeDisplayFormat: str = Field(
        ...,
        description="Format used to display temporal value. Can be a number or a date. If a temporal column is a date, use strftime to format it. If it's a number, use [d3 number](https://github.com/d3/d3-format#locale_format) formatting.",
    )
    durationDisplayFormat: str = Field(
        ...,
        description="Format used to display temporal duration value for brush range. If the temporal column is a date, use strftime to format it. If it's a number, use [d3 number](https://github.com/d3/d3-format#locale_format) formatting.",
    )
    sep: str = Field(..., description="=,] Separator for your CSV file.")
    overviewChannels: str = Field(
        ...,
        description="Comma-separated list of channel names or indexes displayed in overview.",
    )
    overviewWidth: Optional[str] = Field(
        "25", description="%] Default width of overview window in percents."
    )
    fixedScale: Optional[bool] = Field(
        False,
        description="Whether to scale y-axis to the maximum to fit all the values. If false, current view scales to fit only the displayed values.",
    )


class ImageTag(BaseModel):
    """
    Image Tags for Images.

    Customize Label Studio with the Image tag to annotate images for computer vision machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(
        ..., description="Data field containing a path or URL to the image."
    )
    valueList: str = Field(
        ...,
        description="References a variable that holds a list of image URLs. For an example, see the [Multi-Page Document Annotation](/templates/multi-page-document-annotation) template.",
    )
    smoothing: bool = Field(
        ..., description="Enable smoothing, by default it uses user settings."
    )
    width: Optional[str] = Field("100", description="%]              - Image width.")
    maxWidth: Optional[str] = Field("750px", description="Maximum image width.")
    zoom: Optional[bool] = Field(
        False, description="Enable zooming an image with the mouse wheel."
    )
    negativeZoom: Optional[bool] = Field(
        False, description="Enable zooming out an image."
    )
    zoomBy: Optional[float] = Field(1.1, description="Scale factor.")
    grid: Optional[bool] = Field(False, description="Whether to show a grid.")
    gridSize: Optional[int] = Field(30, description="Specify size of the grid.")
    gridColor: Optional[str] = Field(
        "#EEEEF4", description="Color of the grid in hex, opacity is 0.15."
    )
    zoomControl: Optional[bool] = Field(
        False, description="Show zoom controls in toolbar."
    )
    brightnessControl: Optional[bool] = Field(
        False, description="Show brightness control in toolbar."
    )
    contrastControl: Optional[bool] = Field(
        False, description="Show contrast control in toolbar."
    )
    rotateControl: Optional[bool] = Field(
        False, description="Show rotate control in toolbar."
    )
    crosshair: Optional[bool] = Field(False, description="Show crosshair cursor.")
    horizontalAlignment: Optional[Literal["left", "center", "right"]] = Field(
        "left",
        description="Where to align image horizontally. Can be one of 'left', 'center', or 'right'.",
    )
    verticalAlignment: Optional[Literal["top", "center", "bottom"]] = Field(
        "top",
        description="Where to align image vertically. Can be one of 'top', 'center', or 'bottom'.",
    )
    defaultZoom: Optional[Literal["auto", "original", "fit"]] = Field(
        "fit",
        description="Specify the initial zoom of the image within the viewport while preserving its ratio. Can be one of 'auto', 'original', or 'fit'.",
    )
    crossOrigin: Optional[Literal["none", "anonymous", "use-credentials"]] = Field(
        "none",
        description="Configures CORS cross domain behavior for this image, either 'none', 'anonymous', or 'use-credentials', similar to [DOM `img` crossOrigin property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/crossOrigin).",
    )


class VideoTag(BaseModel):
    """
    Video Tag for Video Labeling.

    Customize Label Studio with the Video tag for basic video annotation tasks for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    value: str = Field(..., description="URL of the video.")
    frameRate: Optional[int] = Field(
        24,
        description="video frame rate per second; default is 24; can use task data like `$fps`.",
    )
    sync: str = Field(..., description="object name to sync with.")
    muted: Optional[bool] = Field(False, description="muted video.")
    height: Optional[int] = Field(600, description="height of the video player.")
    timelineHeight: Optional[int] = Field(
        64, description="height of the timeline with regions."
    )
