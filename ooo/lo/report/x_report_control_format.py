# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.report
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..lang.locale import Locale as Locale_70d308fa
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5

class XReportControlFormat(ABC):
    """
    specifies a format condition for a control.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XReportControlFormat <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportControlFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XReportControlFormat'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XReportControlFormat'

    @abstractproperty
    def CharAutoKerning(self) -> bool:
        """
        optional property to determine whether the kerning tables from the current font are used.
        
        Automatic kerning applies a spacing in between certain pairs of characters to make the text look better.
        """

    @abstractproperty
    def CharCaseMap(self) -> int:
        """
        optional property which contains the value of the case-mapping of the text for formatting and displaying.
        """

    @abstractproperty
    def CharColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """

    @abstractproperty
    def CharCombineIsOn(self) -> bool:
        """
        determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """

    @abstractproperty
    def CharCombinePrefix(self) -> str:
        """
        contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """

    @abstractproperty
    def CharCombineSuffix(self) -> str:
        """
        contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """

    @abstractproperty
    def CharContoured(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a contour effect.
        """

    @abstractproperty
    def CharEmphasis(self) -> int:
        """
        contains the font emphasis value as com.sun.star.text.FontEmphasis.
        """

    @abstractproperty
    def CharEscapement(self) -> int:
        """
        specifies the percentage by which to raise/lower superscript/subscript characters.
        
        Negative values denote subscripts and positive values superscripts.
        """

    @abstractproperty
    def CharEscapementHeight(self) -> int:
        """
        This is the additional height used for subscript or superscript characters in units of percent.
        
        For subscript characters the value is negative and for superscript characters positive.
        """

    @abstractproperty
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """

    @abstractproperty
    def CharFontCharSet(self) -> int:
        """
        This attribute contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @abstractproperty
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @abstractproperty
    def CharFontCharSetComplex(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @abstractproperty
    def CharFontFamily(self) -> int:
        """
        This attribute contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @abstractproperty
    def CharFontFamilyAsian(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @abstractproperty
    def CharFontFamilyComplex(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @abstractproperty
    def CharFontName(self) -> str:
        """
        This attribute specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @abstractproperty
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @abstractproperty
    def CharFontNameComplex(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @abstractproperty
    def CharFontPitch(self) -> int:
        """
        This attribute contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @abstractproperty
    def CharFontPitchAsian(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @abstractproperty
    def CharFontPitchComplex(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @abstractproperty
    def CharFontStyleName(self) -> str:
        """
        This attribute contains the name of the font style.
        
        This attribute may be empty.
        """

    @abstractproperty
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """

    @abstractproperty
    def CharFontStyleNameComplex(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """

    @abstractproperty
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @abstractproperty
    def CharHeightAsian(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @abstractproperty
    def CharHeightComplex(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @abstractproperty
    def CharHidden(self) -> bool:
        """
        If this optional property is TRUE, then the characters are invisible.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def CharKerning(self) -> int:
        """
        optional property which contains the value of the kerning of the characters.
        """

    @abstractproperty
    def CharLocale(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @abstractproperty
    def CharLocaleAsian(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @abstractproperty
    def CharLocaleComplex(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @abstractproperty
    def CharPosture(self) -> 'FontSlant_849509ed':
        """
        This attribute contains the value of the posture of the document.
        """

    @abstractproperty
    def CharPostureAsian(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """

    @abstractproperty
    def CharPostureComplex(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """

    @abstractproperty
    def CharRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """

    @abstractproperty
    def CharRotation(self) -> int:
        """
        determines the rotation of a character in degree.
        
        Depending on the implementation only certain values may be allowed.
        """

    @abstractproperty
    def CharScaleWidth(self) -> int:
        """
        determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """

    @abstractproperty
    def CharShadowed(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a shadow effect.
        """

    @abstractproperty
    def CharStrikeout(self) -> int:
        """
        determines the type of the strike out of the character.
        """

    @abstractproperty
    def CharUnderline(self) -> int:
        """
        This attribute contains the value for the character underline.
        """

    @abstractproperty
    def CharUnderlineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """

    @abstractproperty
    def CharWeight(self) -> float:
        """
        This attribute contains the value of the font weight.
        """

    @abstractproperty
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """

    @abstractproperty
    def CharWeightComplex(self) -> float:
        """
        This property contains the value of the font weight.
        """

    @abstractproperty
    def CharWordMode(self) -> bool:
        """
        If this attribute is TRUE, the underline and strike-through properties are not applied to white spaces.
        """

    @abstractproperty
    def ControlBackground(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """

    @abstractproperty
    def ControlBackgroundTransparent(self) -> bool:
        """
        determines if the background color is set to transparent.
        """

    @abstractproperty
    def ControlTextEmphasis(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """

    @abstractproperty
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @abstractproperty
    def FontDescriptorAsian(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @abstractproperty
    def FontDescriptorComplex(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @abstractproperty
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink (if set).
        """

    @abstractproperty
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink (if set).
        """

    @abstractproperty
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink (if set).
        """

    @abstractproperty
    def ParaAdjust(self) -> int:
        """
        specifies the horizontal alignment of the text.
        """

    @abstractproperty
    def UnvisitedCharStyleName(self) -> str:
        """
        contains the character style name for unvisited hyperlinks.
        """

    @abstractproperty
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        """

    @abstractproperty
    def VisitedCharStyleName(self) -> str:
        """
        contains the character style name for visited hyperlinks.
        """


__all__ = ['XReportControlFormat']
