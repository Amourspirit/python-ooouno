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
# Namespace: com.sun.star.linguistic2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XSpellAlternatives(XInterface_8f010a43):
    """
    Gives access to the results of failed spell checking attempts and may provide spelling alternatives.
    
    This is used by the com.sun.star.linguistic2.XSpellChecker.spell() function when the word was not found to be correct. Suggestions for other words to be used may be provided along with a failure-type that may specify why the word was not correct.

    See Also:
        `API XSpellAlternatives <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSpellAlternatives.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XSpellAlternatives'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XSpellAlternatives'

    @abstractmethod
    def getAlternatives(self) -> 'typing.Tuple[str, ...]':
        """
        """
    @abstractmethod
    def getAlternativesCount(self) -> int:
        """
        """
    @abstractmethod
    def getFailureType(self) -> int:
        """
        """
    @abstractmethod
    def getLocale(self) -> 'Locale_70d308fa':
        """
        """
    @abstractmethod
    def getWord(self) -> str:
        """
        """


__all__ = ['XSpellAlternatives']

