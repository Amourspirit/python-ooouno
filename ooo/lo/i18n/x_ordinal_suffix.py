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
# Namespace: com.sun.star.i18n
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XOrdinalSuffix(XInterface_8f010a43):
    """
    provides access to locale specific ordinal suffix systems.
    
    **since**
    
        OOo 2.2

    See Also:
        `API XOrdinalSuffix <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XOrdinalSuffix.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XOrdinalSuffix'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XOrdinalSuffix'

    @abstractmethod
    def getOrdinalSuffix(self, nNumber: int, aLocale: Locale_70d308fa) -> typing.Tuple[str, ...]:
        """
        Returns all the possible ordinal suffixes for the number.
        
        This method will provide \"<b>st</b>\", \"<b>nd</b>\", \"<b>rd</b>\", \"<b>th</b>\" for an English locale, depending on the provided number. In some locales like French, Italian or Spanish it ca return several suffixes for one number.
        
        Examples: for the number '1', the values will be st in English, but er and re in French. All these values may depend on the underlying version of ICU.
        """
        ...

__all__ = ['XOrdinalSuffix']

