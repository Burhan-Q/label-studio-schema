from typing import Literal, Optional

from pydantic import BaseModel, Field


class BrushTag(BaseModel):
    """
    Brush Tag for Image Segmentation Labeling.

    Customize Label Studio with brush tags for image segmentation labeling for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single",
        description="Configure whether the data labeler can select one or multiple labels.",
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    smart: bool = Field(
        ..., description="Show smart tool for interactive pre-annotations."
    )
    smartOnly: bool = Field(
        ..., description="Only show smart tool for interactive pre-annotations."
    )


class BrushLabelsTag(BaseModel):
    """
    Brush Label Tag for Image Segmentation Labeling.

    Customize Label Studio with brush label tags for image segmentation labeling for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single",
        description="Configure whether the data labeler can select one or multiple labels.",
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )


class ChoiceTag(BaseModel):
    """
    Choice Tag for Single Choice Labels.

    Customize Label Studio with choice tags for simple classification tasks in machine learning and data science projects.
    """

    value: str = Field(..., description="Choice value.")
    selected: bool = Field(
        ...,
        description="Specify whether to preselect this choice on the labeling interface.",
    )
    alias: str = Field(
        ...,
        description="Alias for the choice. If used, the alias replaces the choice value in the annotation results. Alias does not display in the interface.",
    )
    style: Literal["style"] = Field(
        "...", description="CSS style of the checkbox element."
    )
    hotkey: str = Field(..., description="Hotkey for the selection.")
    html: str = Field(
        ...,
        description="Can be used to show enriched content, it has higher priority than `value`, however `value` will be used in the exported result (should be properly escaped).",
    )
    hint: str = Field(..., description="Hint for choice on hover.")
    color: str = Field(..., description="Color for Taxonomy item.")


class ChoicesTag(BaseModel):
    """
    Choices Tag for Multiple Choice Labels.

    Customize Label Studio with multiple choice labels for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the group of choices.")
    toName: str = Field(
        ..., description="Name of the data item that you want to label."
    )
    choice: Optional[Literal["single", "single-radio", "multiple"]] = Field(
        "single", description="Single or multi-class classification."
    )
    showInline: Optional[bool] = Field(
        False, description="Show choices in the same visual line."
    )
    required: Optional[bool] = Field(
        False, description="Validate whether a choice has been selected."
    )
    requiredMessage: str = Field(..., description="Show a message if validation fails.")
    visibleWhen: Literal[
        "region-selected", "no-region-selected", "choice-selected", "choice-unselected"
    ] = Field(
        "...",
        description="Control visibility of the choices. Can also be used with the `when*` parameters below to narrow down visibility.",
    )
    whenTagName: str = Field(
        ...,
        description="Use with `visibleWhen`. Narrow down visibility by name of the tag. For regions, use the name of the object tag, for choices, use the name of the `choices` tag.",
    )
    whenLabelValue: str = Field(
        ...,
        description="Use with `visibleWhen='region-selected'`. Narrow down visibility by label value. Multiple values can be separated with commas.",
    )
    whenChoiceValue: str = Field(
        ...,
        description="Use with `visibleWhen` (`'choice-selected'` or `'choice-unselected'`) and `whenTagName`, both are required. Narrow down visibility by choice value. Multiple values can be separated with commas.",
    )
    perRegion: bool = Field(
        ...,
        description="Use this tag to select a choice for a specific region instead of the entire task.",
    )
    perItem: bool = Field(
        ...,
        description="Use this tag to select a choice for a specific item inside the object instead of the whole object.",
    )
    value: str = Field(
        ...,
        description="Task data field containing a list of dynamically loaded choices (see example below).",
    )
    allowNested: bool = Field(
        ...,
        description="Allow to use `children` field in dynamic choices to nest them. Submitted result will contain array of arrays, every item is a list of values from topmost parent choice down to selected one.",
    )


class EllipseTag(BaseModel):
    """
    Ellipse Tag for Adding Elliptical Bounding Box to Images.

    Customize Label Studio with ellipse tags to add elliptical bounding boxes to images for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    opacity: Optional[float] = Field(0.6, description="Opacity of ellipse.")
    fillColor: str = Field(..., description="Ellipse fill color in hexadecimal.")
    strokeColor: Optional[str] = Field(
        "#f48a42", description="Stroke color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")
    canRotate: Optional[bool] = Field(
        True, description="Show or hide rotation control."
    )
    smart: bool = Field(
        ..., description="Show smart tool for interactive pre-annotations."
    )
    smartOnly: bool = Field(
        ..., description="Only show smart tool for interactive pre-annotations."
    )


class EllipseLabelsTag(BaseModel):
    """
    Ellipse Label Tag for Labeling Images with Elliptical Bounding Boxes.

    Customize Label Studio with the EllipseLabels tag to label images with elliptical bounding boxes for semantic image segmentation machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    opacity: Optional[float] = Field(0.6, description="Opacity of ellipse.")
    fillColor: str = Field(..., description="Ellipse fill color in hexadecimal.")
    strokeColor: str = Field(..., description="Stroke color in hexadecimal.")
    strokeWidth: Optional[int] = Field(1, description="Width of stroke.")
    canRotate: Optional[bool] = Field(True, description="Show or hide rotation option.")


class HyperTextLabelsTag(BaseModel):
    """
    Hypertext Label Tag to Create Labeled Hypertext (HTML).

    Customize Label Studio with the HyperTextLabels tag to label hypertext (HTML) for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the HTML element to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure if you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )


class KeyPointTag(BaseModel):
    """
    Keypoint Tag for Adding Keypoints to Images.

    Customize Label Studio with the KeyPoint tag to add key points to images for computer vision machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    opacity: Optional[float] = Field(0.9, description="Opacity of keypoint.")
    fillColor: Optional[str] = Field(
        "#8bad00", description="Keypoint fill color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")
    strokeColor: Optional[str] = Field(
        "#8bad00", description="Keypoint stroke color in hexadecimal."
    )
    smart: bool = Field(
        ..., description="Show smart tool for interactive pre-annotations."
    )
    smartOnly: bool = Field(
        ..., description="Only show smart tool for interactive pre-annotations."
    )
    snap: Optional[Literal["pixel", "none"]] = Field(
        "none", description="Snap keypoint to image pixels."
    )


class KeyPointLabelsTag(BaseModel):
    """
    Keypoint Label Tag for Labeling Keypoints.

    Customize Label Studio with the KeyPointLabels tag to label keypoints for computer vision machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    opacity: Optional[float] = Field(0.9, description="Opacity of the keypoint.")
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")
    snap: Optional[Literal["pixel", "none"]] = Field(
        "none", description="Snap keypoint to image pixels."
    )


class LabelTag(BaseModel):
    """
    Label Tag for Single Label Tags.

    Customize Label Studio with the Label tag to assign a single label to regions in a task for machine learning and data science projects.
    """

    value: str = Field(..., description="Value of the label.")
    selected: Optional[bool] = Field(
        False, description="Whether to preselect this label."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times this label can be used per task."
    )
    hint: str = Field(..., description="Hint for label on hover.")
    hotkey: str = Field(
        ...,
        description="Hotkey to use for the label. Automatically generated if not specified.",
    )
    alias: str = Field(..., description="Label alias.")
    showAlias: Optional[bool] = Field(
        False, description="Whether to show alias inside label text."
    )
    aliasStyle: Optional[str] = Field(
        "opacity:0.6", description="CSS style for the alias."
    )
    size: Optional[str] = Field("medium", description="Size of text in the label.")
    background: Optional[str] = Field(
        "#36B37E", description="Background color of an active label in hexadecimal."
    )
    selectedColor: Optional[str] = Field(
        "#ffffff", description="Color of text in an active label in hexadecimal."
    )
    granularity: Literal["symbol", "word"] = Field(
        "...",
        description="Set control based on symbol or word selection (only for Text).",
    )
    html: str = Field(
        ...,
        description="HTML code is used to display label button instead of raw text provided by `value` (should be properly escaped).",
    )
    category: Literal["int"] = Field(
        "...",
        description="Category is used in the export (in label-studio-converter lib) to make an order of labels for YOLO and COCO.",
    )


class MagicWandTag(BaseModel):
    """
    Magic Wand Tag for Quick Thresholded Flood Filling During Image Segmentation.

    Customize Label Studio with a Magic Wand tag to quickly click and drag to threshold flood fill image areas during image segmentation labeling for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    opacity: Optional[float] = Field(
        0.6, description="Opacity of the Magic Wand region during use."
    )
    blurradius: Optional[int] = Field(
        5,
        description="The edges of a Magic Wand region are blurred and simplified, this is the radius of the blur kernel.",
    )
    defaultthreshold: Optional[int] = Field(
        15,
        description="When the user initially clicks without dragging, how far a color has to be from the initial selected pixel to also be selected.",
    )


class NumberTag(BaseModel):
    """
    Number Tag to Numerically Classify.

    Customize Label Studio with the Number tag to numerically classify tasks in your machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the element that you want to label.")
    min: int = Field(..., description="Minimum number value.")
    max: int = Field(..., description="Maximum number value.")
    step: Optional[int] = Field(1, description="Step for value increment/decrement.")
    defaultValue: int = Field(
        ...,
        description="Default number value; will be added automatically to result for required fields.",
    )
    hotkey: str = Field(..., description="Hotkey for increasing number value.")
    required: Optional[bool] = Field(
        False, description="Whether number is required or not."
    )
    requiredMessage: str = Field(
        ..., description="Message to show if validation fails."
    )
    perRegion: bool = Field(
        ...,
        description="Use this tag to classify specific regions instead of the whole object.",
    )
    perItem: bool = Field(
        ...,
        description="Use this tag to classify specific items inside the object instead of the whole object.",
    )
    slider: Optional[bool] = Field(
        False,
        description="Use slider look instead of input; use min and max to add your constraints.",
    )


class PairwiseTag(BaseModel):
    """
    Pairwise Tag to Compare Objects.

    Customize Label Studio with the Pairwise tag for object comparison tasks for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(
        ..., description="Comma-separated names of the elements you want to compare."
    )
    selectionStyle: str = Field(..., description="Style for the selection.")


class ParagraphLabelsTag(BaseModel):
    """
    Paragraph Label Tag for Paragraph Labels.

    Customize Label Studio with paragraph labels for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the paragraph element to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )


class PolygonTag(BaseModel):
    """
    Polygon Tag for Adding Polygons to Images.

    Customize Label Studio with the Polygon tag by adding polygons to images for segmentation machine learning and data science projects.
    """

    name: str = Field(..., description="Name of tag.")
    toname: str = Field(..., description="Name of image to label.")
    opacity: Optional[int] = Field(0.6, description="Opacity of polygon.")
    fillColor: Optional[str] = Field(
        "transparent",
        description="Polygon fill color in hexadecimal or HTML color name.",
    )
    strokeColor: Optional[str] = Field(
        "#f48a42", description="Stroke color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(3, description="Width of stroke.")
    pointSize: Optional[Literal["small", "medium", "large"]] = Field(
        "small", description="Size of polygon handle points."
    )
    pointStyle: Optional[Literal["rectangle", "circle"]] = Field(
        "circle", description="Style of points."
    )
    smart: bool = Field(
        ..., description="Show smart tool for interactive pre-annotations."
    )
    smartOnly: bool = Field(
        ..., description="Only show smart tool for interactive pre-annotations."
    )
    snap: Optional[Literal["pixel", "none"]] = Field(
        "none", description="Snap polygon to image pixels."
    )


class PolygonLabelsTag(BaseModel):
    """
    Polygon Label Tag for Labeling Polygons in Images.

    Customize Label Studio with the PolygonLabels tag and label polygons in images for semantic segmentation machine learning and data science projects.
    """

    name: str = Field(..., description="Name of tag.")
    toName: str = Field(..., description="Name of image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    opacity: Optional[int] = Field(0.2, description="Opacity of polygon.")
    fillColor: str = Field(..., description="Polygon fill color in hexadecimal.")
    strokeColor: str = Field(..., description="Stroke color in hexadecimal.")
    strokeWidth: Optional[int] = Field(1, description="Width of stroke.")
    pointSize: Optional[Literal["small", "medium", "large"]] = Field(
        "medium", description="Size of polygon handle points."
    )
    pointStyle: Optional[Literal["rectangle", "circle"]] = Field(
        "rectangle", description="Style of points."
    )
    snap: Optional[Literal["pixel", "none"]] = Field(
        "none", description="Snap polygon to image pixels."
    )


class RankerTag(BaseModel):
    """
    Ranker Tag allows you to rank items in a List or, if Buckets are used, pick relevant items from a List.

    Customize Label Studio by sorting results for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="List tag name to connect to.")


class RatingTag(BaseModel):
    """
    Rating Tag for Ratings.

    Customize Label Studio to add ratings to tasks with the Rating tag in your machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the element that you want to label.")
    maxRating: Optional[int] = Field(5, description="Maximum rating value.")
    defaultValue: Optional[int] = Field(0, description="Default rating value.")
    size: Optional[Literal["small", "medium", "large"]] = Field(
        "medium", description="Rating icon size."
    )
    icon: Optional[Literal["star", "heart", "fire", "smile"]] = Field(
        "star", description="Rating icon."
    )
    hotkey: str = Field(..., description="HotKey for changing rating value.")
    required: Optional[bool] = Field(
        False, description="Whether rating validation is required."
    )
    requiredMessage: str = Field(
        ..., description="Message to show if validation fails."
    )
    perRegion: bool = Field(
        ..., description="Use this tag to rate regions instead of the whole object."
    )
    perItem: bool = Field(
        ...,
        description="Use this tag to rate items inside the object instead of the whole object.",
    )


class RectangleTag(BaseModel):
    """
    Rectangle Tag for Adding Rectangle Bounding Box to Images.

    Customize Label Studio with the Rectangle tag to add rectangle bounding boxes to images for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    opacity: Optional[float] = Field(0.6, description="Opacity of rectangle.")
    fillColor: str = Field(..., description="Rectangle fill color in hexadecimal.")
    strokeColor: Optional[str] = Field(
        "#f48a42", description="Stroke color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")
    canRotate: Optional[bool] = Field(
        True,
        description="Whether to show or hide rotation control. Note that the anchor point in the results is different than the anchor point used when rotating with the rotation tool. For more information, see [Rotation](/templates/image_bbox#Rotation).",
    )
    smart: bool = Field(
        ..., description="Show smart tool for interactive pre-annotations."
    )
    smartOnly: bool = Field(
        ..., description="Only show smart tool for interactive pre-annotations."
    )


class RectangleLabelsTag(BaseModel):
    """
    Rectangle Label Tag to Label Rectangle Bounding Box in Images.

    Customize Label Studio with the RectangleLabels tag and add labeled rectangle bounding boxes in images for semantic segmentation and object detection machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the image to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    opacity: Optional[float] = Field(0.6, description="Opacity of rectangle.")
    fillColor: str = Field(..., description="Rectangle fill color in hexadecimal.")
    strokeColor: str = Field(..., description="Stroke color in hexadecimal.")
    strokeWidth: Optional[int] = Field(1, description="Width of stroke.")
    canRotate: Optional[bool] = Field(
        True,
        description="Show or hide rotation control. Note that the anchor point in the results is different than the anchor point used when rotating with the rotation tool. For more information, see [Rotation](/templates/image_bbox#Rotation).",
    )


class RelationTag(BaseModel):
    """
    Relation Tag for a Single Relation.

    Customize Label Studio by using the Relation tag to add a single consistent label to relations between regions in machine learning and data science projects.
    """

    value: str = Field(..., description="Value of the relation.")
    background: str = Field(
        ..., description="Background color of the active label in hexadecimal."
    )


class RelationsTag(BaseModel):
    """
    Relations Tag for Multiple Relations.

    Customize Label Studio by adding labels to relationships between labeled regions for machine learning and data science projects.
    """

    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )


class ShortcutTag(BaseModel):
    """
    Shortcut Tag to Define Shortcuts.

    Customize Label Studio to define keyboard shortcuts and hotkeys to accelerate labeling for machine learning and data science projects.
    """

    value: str = Field(..., description="The value of the shortcut.")
    alias: str = Field(..., description="Shortcut alias.")
    hotkey: str = Field(..., description="Hotkey.")
    background: Optional[str] = Field(
        "#333333", description="Background color in hexadecimal."
    )


class TimelineLabelsTag(BaseModel):
    """
    TimelineLabels tag.

    Classify video frames using TimelineLabels.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the video element.")


class TimeSeriesLabelsTag(BaseModel):
    """
    Time Series Label Tag for Labeling Time Series Data.

    Customize Label Studio for with the TimeSeriesLabel tag to label time series data for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toname: str = Field(..., description="Name of the timeseries to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single", description="Configure whether you can select one or multiple labels."
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Show labels in the same visual line."
    )
    opacity: Optional[float] = Field(0.9, description="Opacity of the range.")
    fillColor: Optional[str] = Field(
        "transparent", description="Range fill color in hexadecimal or HTML color name."
    )
    strokeColor: Optional[str] = Field(
        "#f48a42", description="Stroke color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")


class VideoRectangleTag(BaseModel):
    """
    Video Tag for Video Labeling.

    Customize Label Studio with the Video tag for basic video annotation tasks for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the element to control (video).")


class LabelsTag(BaseModel):
    """
    Labels Tag for Labeling Regions.

    Customize Label Studio by using the Labels tag to provide a set of labels for labeling regions in tasks for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the element that you want to label.")
    choice: Optional[Literal["single", "multiple"]] = Field(
        "single",
        description="Configure whether you can select one or multiple labels for a region.",
    )
    maxUsages: int = Field(
        ..., description="Maximum number of times a label can be used per task."
    )
    showInline: Optional[bool] = Field(
        True, description="Whether to show labels in the same visual line."
    )
    opacity: Optional[float] = Field(
        0.6, description="Opacity of rectangle highlighting the label."
    )
    fillColor: str = Field(..., description="Rectangle fill color in hexadecimal.")
    strokeColor: Optional[str] = Field(
        "#f48a42", description="Stroke color in hexadecimal."
    )
    strokeWidth: Optional[int] = Field(1, description="Width of the stroke.")
    value: str = Field(
        ...,
        description="Task data field containing a list of dynamically loaded labels (see example below).",
    )


class TextAreaTag(BaseModel):
    """
    Textarea Tag for Text areas.

    Customize Label Studio with the TextArea tag to support audio transcription, image captioning, and OCR tasks for machine learning and data science projects.
    """

    name: str = Field(..., description="Name of the element.")
    toName: str = Field(..., description="Name of the element that you want to label.")
    value: str = Field(..., description="Pre-filled value.")
    label: str = Field(..., description="Label text.")
    placeholder: str = Field(..., description="Placeholder text.")
    maxSubmissions: str = Field(..., description="Maximum number of submissions.")
    editable: Optional[bool] = Field(
        False, description="Whether to display an editable textarea."
    )
    skipDuplicates: Optional[bool] = Field(
        False, description="Prevent duplicates in textarea inputs."
    )
    transcription: Optional[bool] = Field(
        False, description="If false, always show editor."
    )
    displayMode: Optional[Literal["tag", "region-list"]] = Field(
        "tag",
        description="Display mode for the textarea; region-list shows it for every region in regions list.",
    )
    rows: int = Field(..., description="Number of rows in the textarea.")
    required: Optional[bool] = Field(
        False, description="Validate whether content in textarea is required."
    )
    requiredMessage: str = Field(
        ..., description="Message to show if validation fails."
    )
    showSubmitButton: bool = Field(
        ...,
        description="Whether to show or hide the submit button. By default it shows when there are more than one rows of text, such as in textarea mode.",
    )
    perRegion: bool = Field(
        ..., description="Use this tag to label regions instead of whole objects."
    )
    perItem: bool = Field(
        ...,
        description="Use this tag to label items inside objects instead of whole objects.",
    )
