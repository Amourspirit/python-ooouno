# coding: utf-8
from typing import Any, TYPE_CHECKING
from abc import ABC, abstractproperty
if TYPE_CHECKING:
    from .font_slant import FontSlant

# https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1FontDescriptor.html#a7ee9065718e6628dc7791b756fa6c0f9


class IFontDescriptor(ABC):
    """
    describes the characteristics of a font.
    
    See Also:
        `API FontDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1FontDescriptor.html#a7ee9065718e6628dc7791b756fa6c0f9>`_
    """

    @abstractproperty
    def CharacterWidth(self) -> float:
        """
        Specifies the character width.

        Depending on the specified width, a font that supports this width may be selected.
        The value is expressed as a percentage.
        """

    @abstractproperty
    def CharSet(self) -> int:
        """
        Specifies the character set which is supported by the font.
        """

    @abstractproperty
    def Family(self) -> int:
        """
        specifies the general style of the font.
        """

    @abstractproperty
    def Height(self) -> int:
        """
        specifies the height of the font in the measure of the destination.
        """

    @abstractproperty
    def Kerning(self) -> bool:
        """
        For requesting, it specifies if there is a kerning table available.

        For selecting, it specifies if the kerning table is to be used.
        """

    @abstractproperty
    def Name(self) -> str:
        """
        specifies the exact name of the font.
        """

    @abstractproperty
    def Orientation(self) -> float:
        """
        specifies the rotation of the font.

        The unit of measure is degrees; 0 is the baseline.
        """

    @abstractproperty
    def Pitch(self) -> int:
        """
        specifies the pitch of the font.
        """

    @abstractproperty
    def Slant(self) -> 'FontSlant':
        """
        Specifies Slant
        """

    @abstractproperty
    def Strikeout(self) -> int:
        """
        Specifies Strikeout
        """

    @abstractproperty
    def StyleName(self) -> str:
        """
        specifies the style name of the font.
        """

    @abstractproperty
    def Type(self) -> int:
        """
        Specifies Type
        """

    @abstractproperty
    def Underline(self) -> int:
        """
        specifies the kind of underlining.
        """

    @abstractproperty
    def Weight(self) -> float:
        """
        specifies the thickness of the line.

        Depending on the specified weight, a font that supports this thickness may be selected.
        The value is expressed as a percentage.
        """

    @abstractproperty
    def Width(self) -> int:
        """
        specifies the width of the font in the measure of the destination.
        """

    @abstractproperty
    def WordLineMode(self) -> bool:
        """
        specifies if only words get underlined.

        ``True`` means that only non-space characters get underlined,
        ``False`` means that the spacing also gets underlined.
        """
