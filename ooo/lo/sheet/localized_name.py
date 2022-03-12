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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..lang.locale import Locale as Locale_70d308fa


class LocalizedName(object):
    """
    Struct Class

    A name that is valid for a specified locale.

    See Also:
        `API LocalizedName <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1LocalizedName.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.LocalizedName'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.LocalizedName'
    """Literal Constant ``com.sun.star.sheet.LocalizedName``"""

    def __init__(self, Locale: typing.Optional[Locale_70d308fa] = UNO_NONE, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Locale (Locale, optional): Locale value.
            Name (str, optional): Name value.
        """
        super().__init__()
        kargs = {
            "Locale": Locale,
            "Name": Name,
        }
        if kargs["Locale"] is UNO_NONE:
            kargs["Locale"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._locale = kwargs["Locale"]
        self._name = kwargs["Name"]


    @property
    def Locale(self) -> Locale_70d308fa:
        """
        The locale for which this name is valid.
        """
        return self._locale
    
    @Locale.setter
    def Locale(self, value: Locale_70d308fa) -> None:
        self._locale = value

    @property
    def Name(self) -> str:
        """
        The name itself.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['LocalizedName']
