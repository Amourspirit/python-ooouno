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
from .locale_data_item import LocaleDataItem as LocaleDataItem_beff0ba1
import typing


class LocaleDataItem2(LocaleDataItem_beff0ba1):
    """
    Struct Class

    Locale specific data, derived from LocaleDataItem adding an alternative input decimal separator.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API LocaleDataItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LocaleDataItem2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.LocaleDataItem2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.LocaleDataItem2'
    """Literal Constant ``com.sun.star.i18n.LocaleDataItem2``"""

    def __init__(self, decimalSeparatorAlternative: str = '', **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``decimalSeparatorAlternative`` can be another ``LocaleDataItem2`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            decimalSeparatorAlternative (str, optional): decimalSeparatorAlternative value
        """
        super().__init__(**kwargs)
        if isinstance(decimalSeparatorAlternative, LocaleDataItem2):
            oth: LocaleDataItem2 = decimalSeparatorAlternative
            self._decimal_separator_alternative = oth.decimalSeparatorAlternative
            return
        else:
            self._decimal_separator_alternative = decimalSeparatorAlternative



    @property
    def decimalSeparatorAlternative(self) -> str:
        """
        Alternative input decimal separator, for example, \".\" if the regular locale dependent separator usually is not present on keyboards used with that locale.
        
        This separator is optional, an empty string denotes no alternative decimal separator shall be used.
        """
        return self._decimal_separator_alternative
    
    @decimalSeparatorAlternative.setter
    def decimalSeparatorAlternative(self, value: str) -> None:
        self._decimal_separator_alternative = value


__all__ = ['LocaleDataItem2']
