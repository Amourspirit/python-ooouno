# coding: utf-8
from ...base.const import ConstIntBase


class FontStrikeout(ConstIntBase):
    """
    These values are used to specify the kind of strikeout.

    See Also:
        `API FontStrikeout <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontStrikeout.html>`_
    """
    NONE = 0
    """specifies not to strike out the characters."""

    SINGLE = 1
    """specifies to strike out the characters with a single line."""

    DOUBLE = 2
    """specifies to strike out the characters with a double line."""

    DONTKNOW = 3
    """The strikeout mode is not specified."""

    BOLD = 4
    """specifies to strike out the characters with a bold line."""

    SLASH = 5
    """specifies to strike out the characters with slashes."""

    X = 6
    """specifies to strike out the characters with X's."""
