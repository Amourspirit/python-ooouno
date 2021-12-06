# coding: utf-8
from enum import Enum
from typing import TYPE_CHECKING
from ...oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    # PushButtonType is string enum
    from com.sun.star.awt.FontSlant import NONE, OBLIQUE, ITALIC, DONTKNOW, REVERSE_OBLIQUE, REVERSE_ITALIC

class FontSlant(str, Enum):
    """
    used to specify the slant of a font.

    See Also:
        `API FontSlant <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#a362a86d3ebca4a201d13bc3e7b94340e>`_
    """
    NONE = 'NONE'
    """specifies a font without slant."""
    OBLIQUE = 'OBLIQUE'
    """specifies an oblique font (slant not designed into the font)."""
    ITALIC = 'ITALIC'
    """specifies an italic font (slant designed into the font)."""
    DONTKNOW = 'DONTKNOW'
    """
    specifies a font with an unknown slant.

    specifies that the menu item type is unknown.
    """
    REVERSE_OBLIQUE = 'REVERSE_OBLIQUE'
    """specifies a reverse oblique font (slant not designed into the font)."""
    REVERSE_ITALIC = 'REVERSE_ITALIC'
    """specifies a reverse italic font (slant designed into the font)."""

def _dynamic_enum():
    '''
    Dynamically add Enum names and value for enum
    
    It is possible that enum values could change, therefore dynamically create enum
    '''
    global FontSlant
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
        FontSlant = Enum('FontSlant', {
            "NONE": NONE.value,
            "OBLIQUE": OBLIQUE.value,
            "ITALIC": ITALIC.value,
            "DONTKNOW": DONTKNOW.value,
            "REVERSE_OBLIQUE": REVERSE_OBLIQUE.value,
            "REVERSE_ITALIC": REVERSE_ITALIC.value
        })
        FontSlant.__str__ = lambda self: self._value_


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['FontSlant']
