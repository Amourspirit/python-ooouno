# coding: utf-8
from ...base.const import ConstIntBase


class FontEmphasis(ConstIntBase):
    """
    Determines the type and position of an emphasis mark in Asian texts.

    See Also:
        `API FontEmphasis <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1FontEmphasis.html>`_
    """
    NONE = 0
    """no emphasis mark is used."""

    DOT_ABOVE = 1
    """a dot is set above (or right from vertical text) the text."""

    CIRCLE_ABOVE = 2
    """a circle is set above (or right from vertical text) the text."""

    DISK_ABOVE = 3
    """a disc is set above (or right from vertical text) the text."""

    ACCENT_ABOVE = 4
    """an accent is set above (or right from vertical text) the text."""

    DOT_BELOW = 11
    """a dot is set below (or left from vertical text) the text."""

    CIRCLE_BELOW = 12
    """a circle is set below (or left from vertical text) the text."""

    DISK_BELOW = 13
    """a disk is set below (or left from vertical text) the text."""

    ACCENT_BELOW = 14
    """an accent is set below (or left from vertical text) the text."""
