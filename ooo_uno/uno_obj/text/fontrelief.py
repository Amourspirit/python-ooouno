# coding: utf-8
from ...base.const import ConstIntBase


class FontRelief(ConstIntBase):
    """
    Determines the relief type of a font.

    See Also:
        `API FontRelief <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1FontRelief.html>`_
    """
    NONE = 0
    """no relief is used."""
    EMBOSSED = 1
    """the font relief is embossed."""
    ENGRAVED = 2
    """the font relief is engraved."""
