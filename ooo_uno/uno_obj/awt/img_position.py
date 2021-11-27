# coding: utf-8
from ...base.const import ConstIntBase


class ImagePosition(ConstIntBase):
    """
    specifies the position of an image, relative to another object

    See Also:
        `API ImagePosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImagePosition.html>`_
    """
    ABOVE_CENTER = 7
    """specifies that the image should be positioned above and horizontally centered to the other object"""
    ABOVE_LEFT = 6
    """specifies that the image should be positioned above and left-aligned to the other object"""
    ABOVE_RIGHT = 8
    """specifies that the image should be positioned above and right-aligned to the other object"""
    BELOW_CENTER = 10
    """specifies that the image should be positioned below and horizontally centered to the other object"""
    BELOW_LEFT = 9
    """specifies that the image should be positioned below and left-aligned to the other object"""
    BELOW_RIGHT = 11
    """specifies that the image should be positioned below and right-aligned centered to the other object"""
    CENTERED = 12
    """specifies that the image should be horizontally and vertically centered to the other object."""
    LEFT_BOTTOM = 2
    """specifies that the image should be positioned at the left of, and bottom-aligned to, the other object"""
    LEFT_CENTER = 1
    """specifies that the image should be positioned at the left of, and vertically centered to, the other object"""
    LEFT_TOP = 0
    """specifies that the image should be positioned at the left of, and top-aligned to, the other object"""
    RightBottom = 5
    """specifies that the image should be positioned at the right of, and bottom-aligned to, the other object"""
    RIGHT_CENTER = 4
    """specifies that the image should be positioned at the right of, and vertically centered to, the other object"""
    RIGHT_TOP = 3
    """specifies that the image should be positioned at the right of, and top-aligned to, the other object"""
