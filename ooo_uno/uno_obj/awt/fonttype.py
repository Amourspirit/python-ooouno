# coding: utf-8
from ...base.const import ConstIntBase


class FontType(ConstIntBase):
    """
    These values are used to specify the technology of the font representation.
    
    See Also:
        `API FontType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontType.html>`_
    """
    DONTKNOW = 0
    """The type of the font is not known."""

    RASTER = 1
    """specifies a raster font."""

    DEVICE = 2
    """specifies a device font."""

    SCALABLE = 4
    """specifies a scalable font."""
