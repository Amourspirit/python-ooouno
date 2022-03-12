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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class LanguageCountryInfo(object):
    """
    Struct Class

    The language and country identifiers and descriptive names of the loaded locale data returned by XLocaleData.getLanguageCountryInfo().

    See Also:
        `API LanguageCountryInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LanguageCountryInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.LanguageCountryInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.LanguageCountryInfo'
    """Literal Constant ``com.sun.star.i18n.LanguageCountryInfo``"""

    def __init__(self, Language: typing.Optional[str] = '', LanguageDefaultName: typing.Optional[str] = '', Country: typing.Optional[str] = '', CountryDefaultName: typing.Optional[str] = '', Variant: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Language (str, optional): Language value.
            LanguageDefaultName (str, optional): LanguageDefaultName value.
            Country (str, optional): Country value.
            CountryDefaultName (str, optional): CountryDefaultName value.
            Variant (str, optional): Variant value.
        """
        super().__init__()
        kargs = {
            "Language": Language,
            "LanguageDefaultName": LanguageDefaultName,
            "Country": Country,
            "CountryDefaultName": CountryDefaultName,
            "Variant": Variant,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._language = kwargs["Language"]
        self._language_default_name = kwargs["LanguageDefaultName"]
        self._country = kwargs["Country"]
        self._country_default_name = kwargs["CountryDefaultName"]
        self._variant = kwargs["Variant"]


    @property
    def Language(self) -> str:
        """
        ISO-639 language code, for example, \"en\" or \"de\".
        """
        return self._language
    
    @Language.setter
    def Language(self, value: str) -> None:
        self._language = value

    @property
    def LanguageDefaultName(self) -> str:
        """
        Descriptive language name, for example, \"English\" or \"German\".
        """
        return self._language_default_name
    
    @LanguageDefaultName.setter
    def LanguageDefaultName(self, value: str) -> None:
        self._language_default_name = value

    @property
    def Country(self) -> str:
        """
        ISO-3166 country code, for example, \"US\" or \"DE\".
        """
        return self._country
    
    @Country.setter
    def Country(self, value: str) -> None:
        self._country = value

    @property
    def CountryDefaultName(self) -> str:
        """
        Descriptive country name, for example, \"United States\" or \"Germany\".
        """
        return self._country_default_name
    
    @CountryDefaultName.setter
    def CountryDefaultName(self, value: str) -> None:
        self._country_default_name = value

    @property
    def Variant(self) -> str:
        """
        A variant name.
        """
        return self._variant
    
    @Variant.setter
    def Variant(self, value: str) -> None:
        self._variant = value


__all__ = ['LanguageCountryInfo']
