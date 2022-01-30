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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.lang
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class Locale(object):
        """
        Struct Class

        object represents a specific geographical, political, or cultural region.
        
        An operation that requires a Locale to perform its task is called locale-sensitive and uses the Locale to tailor information for the user. For example, displaying a number is a locale-sensitive operation; the number should be formatted according to the customs/conventions of the user's native country, region, or culture.
        
        Because a Locale object is just an identifier for a region, no validity check is performed. If you want to see whether particular resources are available for the Locale, use the com.sun.star.resource.XLocale.getAvailableLocales() method to ask for the locales it supports.
        
        Each implementation that performs locale-sensitive operations allows you to get all the available objects of that type. Use the com.sun.star.resource.XLocale interface to set the locale.

        See Also:
            `API Locale <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1lang_1_1Locale.html>`_


        Note:
            | At runtime Locale will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | Locale is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Country: typing.Optional[str] = None, Language: typing.Optional[str] = None, Variant: typing.Optional[str] = None):
            self._country = Country
            self._language = Language
            self._variant = Variant

        @property
        def Country(self) -> str:
            """
            specifies an ISO 3166 Country Code.
            
            These codes are the upper-case two-letter codes as defined by ISO 3166-1. You can find a full list of these codes at a number of sites, such as:
            http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm.
            
            If this field contains an empty string, the meaning depends on the context.
            """
            return self._country
        
        @Country.setter
        def Country(self, value: str) -> None:
            self._country = value

        @property
        def Language(self) -> str:
            """
            specifies an ISO 639 Language Code.
            
            These codes are preferably the lower-case two-letter codes as defined by ISO 639-1, or three-letter codes as defined by ISO 639-3. You can find a full list of these codes at a number of sites, such as:
            http://sil.org/iso639-3/codes.asp.
            
            If this field contains an empty string, the meaning depends on the context.
            
            Since LibreOffice 4.2, if the locale can not be represented using only ISO 639 and ISO 3166 codes this field contains the ISO 639-3 reserved for local use code \"qlt\" and a BCP 47 language tag is present in the Variant field.
            """
            return self._language
        
        @Language.setter
        def Language(self, value: str) -> None:
            self._language = value

        @property
        def Variant(self) -> str:
            """
            specifies a BCP 47 Language Tag.
            
            Since LibreOffice 4.2, if the Language field is the code \"qlt\" this field contains the full BCP 47 language tag. If the Language field is not \"qlt\" this field is empty.
            
            You can find BCP 47 language tag resources at
            http://www.langtag.net/.
            
            Earlier versions of the documentation mentioned \"vendor and
            browser-specific\" codes but that was never supported. Use of any arbitrary strings in the Variant field that do not form a valid BCP 47 language tag is strongly deprecated.
            """
            return self._variant
        
        @Variant.setter
        def Variant(self, value: str) -> None:
            self._variant = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global Locale
        order = ('Country', 'Language', 'Variant')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.lang.Locale')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Locale = _struct_init

    _dynamic_struct()

__all__ = ['Locale']
