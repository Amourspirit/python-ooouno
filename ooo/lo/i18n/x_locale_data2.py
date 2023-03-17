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
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from .x_locale_data import XLocaleData as XLocaleData_9d100a6a
if typing.TYPE_CHECKING:
    from .currency2 import Currency2 as Currency2_89e809c5
    from ..lang.locale import Locale as Locale_70d308fa

class XLocaleData2(XLocaleData_9d100a6a):
    """
    Access locale specific data.
    
    Derived from com.sun.star.i18n.XLocaleData and provides an additional method to return a sequence of all com.sun.star.i18n.Currency2 elements available for that locale.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XLocaleData2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XLocaleData2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XLocaleData2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XLocaleData2'

    @abstractmethod
    def getAllCurrencies2(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[Currency2_89e809c5, ...]':
        """
        returns all LC_CURRENCY currencies for a locale.
        """
        ...

__all__ = ['XLocaleData2']

