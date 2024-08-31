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
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XSupportedLocales(XInterface_8f010a43):
    """
    Offers information about which languages are supported by the object.
    
    This interface has to be implemented by com.sun.star.linguistic2.SpellChecker, com.sun.star.linguistic2.Hyphenator and com.sun.star.linguistic2.Thesaurus implementations in order to be queried for the languages they can use.

    See Also:
        `API XSupportedLocales <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSupportedLocales.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XSupportedLocales'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XSupportedLocales'

    @abstractmethod
    def getLocales(self) -> typing.Tuple[Locale_70d308fa, ...]:
        """
        """
        ...
    @abstractmethod
    def hasLocale(self, aLocale: Locale_70d308fa) -> bool:
        """
        """
        ...

__all__ = ['XSupportedLocales']

