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
# Libre Office Version: 7.3
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .text_conversion_result import TextConversionResult as TextConversionResult_12d10e92
    from ..lang.locale import Locale as Locale_70d308fa

class XTextConversion(XInterface_8f010a43):
    """
    Method to convert text from one type to another.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XTextConversion <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XTextConversion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XTextConversion'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XTextConversion'

    @abstractmethod
    def getConversion(self, aText: str, nStartPos: int, nLength: int, Locale: 'Locale_70d308fa', nTextConversionType: int, nTextConversionOptions: int) -> str:
        """
        Method to search dictionaries for the conversion candidate, if there are multiple candidates, it will return first one.
        
        This is for the conversion in non-interactive mode.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def getConversions(self, aText: str, nStartPos: int, nLength: int, Locale: 'Locale_70d308fa', nTextConversionType: int, nTextConversionOptions: int) -> 'TextConversionResult_12d10e92':
        """
        Method to search dictionaries for the conversion candidates.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def interactiveConversion(self, Locale: 'Locale_70d308fa', nTextConversionType: int, nTextConversionOptions: int) -> bool:
        """
        Method to query if the conversion type should be interactive or non-interactive mode.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...

__all__ = ['XTextConversion']

