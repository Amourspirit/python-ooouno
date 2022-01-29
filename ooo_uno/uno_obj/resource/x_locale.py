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
# Namespace: com.sun.star.resource
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XLocale(XInterface_8f010a43):
    """
    offers some operations on com.sun.star.lang.Locale structures.

    See Also:
        `API XLocale <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XLocale.html>`_
    """

    @abstractmethod
    def create(self, aLanguage: str, aCountry: str, aVariant: str) -> 'Locale_70d308fa':
        """
        creates a locale from language, country, and variant.
        
        NOTE: ISO 639 is not a stable standard; some of the language codes it defines (specifically iw, ji, and in) have changed. This constructor accepts both the old codes (iw, ji, and in) and the new codes (he, yi, and id), but all other API on XLocale will return only the NEW codes.
        
        Note: The Java class Locale returns the old codes.
        """
    @abstractmethod
    def equals(self, l1: 'Locale_70d308fa', l2: 'Locale_70d308fa') -> bool:
        """
        A locale is deemed equal to another locale with identical language, country, and variant, and unequal to all other objects.
        """
    @abstractmethod
    def getAvailableLocales(self) -> 'typing.List[Locale_70d308fa]':
        """
        """
    @abstractmethod
    def getDefault(self) -> 'Locale_70d308fa':
        """
        the common method of getting the current default locale.
        
        It is used for the presentation (for menus, dialogs, etc.). It is, generally, set once when your applet or application is initialized, then never reset. (If you do reset the default locale, you probably want to reload your GUI, so that the change is reflected in your interface.)
        
        More advanced programs allow users to use different locales for different fields, for example, in a spreadsheet.
        
        Note that the initial setting will match the host system.
        """
    @abstractmethod
    def getDisplayCountry(self, locale: 'Locale_70d308fa', inLocale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayCountry_Default(self, locale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayLanguage(self, locale: 'Locale_70d308fa', inLocale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayLanguage_Default(self, locale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayName(self, locale: 'Locale_70d308fa', inLocale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayName_Default(self, locale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayVariant(self, locale: 'Locale_70d308fa', inLocale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getDisplayVariant_Default(self, locale: 'Locale_70d308fa') -> str:
        """
        """
    @abstractmethod
    def getISO3Country(self, locale: 'Locale_70d308fa') -> str:
        """

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
        """
    @abstractmethod
    def getISO3Language(self, locale: 'Locale_70d308fa') -> str:
        """

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
        """
    @abstractmethod
    def getISOCountries(self) -> 'typing.List[str]':
        """
        """
    @abstractmethod
    def getISOLanguages(self) -> 'typing.List[str]':
        """
        """
    @abstractmethod
    def getLanguagesForCountry(self, country: str) -> 'typing.List[str]':
        """
        """
    @abstractmethod
    def setDefault(self, newLocale: 'Locale_70d308fa') -> None:
        """
        sets the default locale for the whole environment.
        
        It is normally set once at the beginning of an application, then never reset. setDefault does not reset the host locale.
        """

__all__ = ['XLocale']

