# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.report
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..lang.locale import Locale as Locale_70d308fa
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.awt.FontSlant import FontSlantProto  # type: ignore
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto  # type: ignore

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

    @property
    @abstractmethod
    def CharAutoKerning(self) -> bool:
        """
        optional property to determine whether the kerning tables from the current font are used.
        
        Automatic kerning applies a spacing in between certain pairs of characters to make the text look better.
        """
        ...

    @property
    @abstractmethod
    def CharCaseMap(self) -> int:
        """
        optional property which contains the value of the case-mapping of the text for formatting and displaying.
        """
        ...

    @property
    @abstractmethod
    def CharColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def CharCombineIsOn(self) -> bool:
        """
        determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """
        ...

    @property
    @abstractmethod
    def CharCombinePrefix(self) -> str:
        """
        contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """
        ...

    @property
    @abstractmethod
    def CharCombineSuffix(self) -> str:
        """
        contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """
        ...

    @property
    @abstractmethod
    def CharContoured(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a contour effect.
        """
        ...

    @property
    @abstractmethod
    def CharEmphasis(self) -> int:
        """
        contains the font emphasis value as com.sun.star.text.FontEmphasis.
        """
        ...

    @property
    @abstractmethod
    def CharEscapement(self) -> int:
        """
        specifies the percentage by which to raise/lower superscript/subscript characters.
        
        Negative values denote subscripts and positive values superscripts.
        """
        ...

    @property
    @abstractmethod
    def CharEscapementHeight(self) -> int:
        """
        This is the additional height used for subscript or superscript characters in units of percent.
        
        For subscript characters the value is negative and for superscript characters positive.
        """
        ...

    @property
    @abstractmethod
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSet(self) -> int:
        """
        This attribute contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSetComplex(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...

    @property
    @abstractmethod
    def CharFontFamily(self) -> int:
        """
        This attribute contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...

    @property
    @abstractmethod
    def CharFontFamilyAsian(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...

    @property
    @abstractmethod
    def CharFontFamilyComplex(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...

    @property
    @abstractmethod
    def CharFontName(self) -> str:
        """
        This attribute specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...

    @property
    @abstractmethod
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...

    @property
    @abstractmethod
    def CharFontNameComplex(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitch(self) -> int:
        """
        This attribute contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitchAsian(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitchComplex(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleName(self) -> str:
        """
        This attribute contains the name of the font style.
        
        This attribute may be empty.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleNameComplex(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...

    @property
    @abstractmethod
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...

    @property
    @abstractmethod
    def CharHeightAsian(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...

    @property
    @abstractmethod
    def CharHeightComplex(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...

    @property
    @abstractmethod
    def CharHidden(self) -> bool:
        """
        If this optional property is TRUE, then the characters are invisible.
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def CharKerning(self) -> int:
        """
        optional property which contains the value of the kerning of the characters.
        """
        ...

    @property
    @abstractmethod
    def CharLocale(self) -> Locale_70d308fa:
        """
        contains the value of the locale.
        """
        ...

    @property
    @abstractmethod
    def CharLocaleAsian(self) -> Locale_70d308fa:
        """
        contains the value of the locale.
        """
        ...

    @property
    @abstractmethod
    def CharLocaleComplex(self) -> Locale_70d308fa:
        """
        contains the value of the locale.
        """
        ...

    @property
    @abstractmethod
    def CharPosture(self) -> FontSlantProto:
        """
        This attribute contains the value of the posture of the document.
        """
        ...

    @property
    @abstractmethod
    def CharPostureAsian(self) -> FontSlantProto:
        """
        This property contains the value of the posture of the document.
        """
        ...

    @property
    @abstractmethod
    def CharPostureComplex(self) -> FontSlantProto:
        """
        This property contains the value of the posture of the document.
        """
        ...

    @property
    @abstractmethod
    def CharRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def CharRotation(self) -> int:
        """
        determines the rotation of a character in degree.
        
        Depending on the implementation only certain values may be allowed.
        """
        ...

    @property
    @abstractmethod
    def CharScaleWidth(self) -> int:
        """
        determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """
        ...

    @property
    @abstractmethod
    def CharShadowed(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a shadow effect.
        """
        ...

    @property
    @abstractmethod
    def CharStrikeout(self) -> int:
        """
        determines the type of the strike out of the character.
        """
        ...

    @property
    @abstractmethod
    def CharUnderline(self) -> int:
        """
        This attribute contains the value for the character underline.
        """
        ...

    @property
    @abstractmethod
    def CharUnderlineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def CharWeight(self) -> float:
        """
        This attribute contains the value of the font weight.
        """
        ...

    @property
    @abstractmethod
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...

    @property
    @abstractmethod
    def CharWeightComplex(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...

    @property
    @abstractmethod
    def CharWordMode(self) -> bool:
        """
        If this attribute is TRUE, the underline and strike-through properties are not applied to white spaces.
        """
        ...

    @property
    @abstractmethod
    def ControlBackground(self) -> Color_68e908c5:
        """
        specifies the background color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def ControlBackgroundTransparent(self) -> bool:
        """
        determines if the background color is set to transparent.
        """
        ...

    @property
    @abstractmethod
    def ControlTextEmphasis(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def FontDescriptorAsian(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def FontDescriptorComplex(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink (if set).
        """
        ...

    @property
    @abstractmethod
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink (if set).
        """
        ...

    @property
    @abstractmethod
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink (if set).
        """
        ...

    @property
    @abstractmethod
    def ParaAdjust(self) -> int:
        """
        specifies the horizontal alignment of the text.
        """
        ...

    @property
    @abstractmethod
    def UnvisitedCharStyleName(self) -> str:
        """
        contains the character style name for unvisited hyperlinks.
        """
        ...

    @property
    @abstractmethod
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def VisitedCharStyleName(self) -> str:
        """
        contains the character style name for visited hyperlinks.
        """
        ...


__all__ = ['XReportControlFormat']