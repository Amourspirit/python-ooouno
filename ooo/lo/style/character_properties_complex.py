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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.style
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..lang.locale import Locale as Locale_70d308fa

class CharacterPropertiesComplex(ABC):
    """
    Service Class

    This is a set of properties to describe the style of characters in complex texts.

    See Also:
        `API CharacterPropertiesComplex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterPropertiesComplex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.CharacterPropertiesComplex'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CharFontCharSetComplex(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @abstractproperty
    def CharFontFamilyComplex(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @abstractproperty
    def CharFontNameComplex(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @abstractproperty
    def CharFontPitchComplex(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @abstractproperty
    def CharFontStyleNameComplex(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """

    @abstractproperty
    def CharHeightComplex(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @abstractproperty
    def CharLocaleComplex(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @abstractproperty
    def CharPostureComplex(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """

    @abstractproperty
    def CharWeightComplex(self) -> float:
        """
        This property contains the value of the font weight.
        """



__all__ = ['CharacterPropertiesComplex']

