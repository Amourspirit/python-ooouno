# coding: utf-8
from ...base.const import ConstIntBase


class FontFamily(ConstIntBase):
    """
    These values are used to specify the general kind of font.

    See Also:
        `API FontFamily <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontFamily.html>`_
    """
    DONTKNOW = 0
    """specifies an unknown font family."""
    DECORATIVE = 1
    """specifies the family of decorative fonts."""
    MODERN = 2
    """specifies the family of modern fonts."""
    ROMAN = 3
    """specifies the family roman fonts(with serifs)."""
    SCRIPT = 4
    """specifies the family of script fonts."""
    SWISS = 5
    """specifies the family roman fonts(without serifs)."""
    SYSTEM = 6
    """specifies the family system fonts."""
