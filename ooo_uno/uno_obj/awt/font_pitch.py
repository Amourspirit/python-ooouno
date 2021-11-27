# coding: utf-8
from ...base.const import ConstIntBase


class FontPitch(ConstIntBase):
    """
    These values are used to specify whether the width of a character is fixed or variable.

    See Also:
        `API FontPitchEnum <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontPitch.html>`_
    """
    DONTKNOW = 0
    """specifies that the pitch for this font is unknown."""
    FIXED = 1
    """specifies a font with a fixed character width."""
    VARIABLE = 2
    """specifies a font with a variable character width."""
