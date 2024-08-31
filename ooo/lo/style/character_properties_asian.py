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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.style
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from com.sun.star.awt.FontSlant import FontSlantProto  # type: ignore

class CharacterPropertiesAsian(ABC):
    """
    Service Class

    This is a set of properties to describe the style of characters in Asian texts.

    See Also:
        `API CharacterPropertiesAsian <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterPropertiesAsian.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.CharacterPropertiesAsian'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
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
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
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
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
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
    def CharLocaleAsian(self) -> Locale_70d308fa:
        """
        contains the value of the locale.
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
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...


__all__ = ['CharacterPropertiesAsian']