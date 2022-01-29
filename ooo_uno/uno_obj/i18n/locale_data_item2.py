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
import os
from .locale_data_item import LocaleDataItem as LocaleDataItem_beff0ba1
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class LocaleDataItem2(LocaleDataItem_beff0ba1):
    """
    Struct Class

    Locale specific data, derived from LocaleDataItem adding an alternative input decimal separator.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API LocaleDataItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LocaleDataItem2.html>`_


    Note:
        | At runtime LocaleDataItem2 will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | LocaleDataItem2 is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, decimalSeparatorAlternative: typing.Optional[str] = None):
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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global LocaleDataItem2
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('decimalSeparatorAlternative',)
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.i18n.LocaleDataItem2')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        LocaleDataItem2 = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['LocaleDataItem2']
