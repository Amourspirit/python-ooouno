# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_supported_languages import XSupportedLanguages as XSupportedLanguages_7dbd112a
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_spell_alternatives import XSpellAlternatives as XSpellAlternatives_6ad110bf

class XSpellChecker1(XSupportedLanguages_7dbd112a):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSpellChecker1 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSpellChecker1.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XSpellChecker1'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XSpellChecker1'

    @abstractmethod
    def isValid(self, aWord: str, nLanguage: int, aProperties: PropertyValues_d6470ce6) -> bool:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def spell(self, aWord: str, nLanguage: int, aProperties: PropertyValues_d6470ce6) -> XSpellAlternatives_6ad110bf:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XSpellChecker1']


