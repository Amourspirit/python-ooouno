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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .color import Color as Color_68e908c5
    from .x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class XNumberFormatter(XInterface_8f010a43):
    """
    represents a number formatter.

    See Also:
        `API XNumberFormatter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XNumberFormatter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XNumberFormatter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XNumberFormatter'

    @abstractmethod
    def attachNumberFormatsSupplier(self, xSupplier: 'XNumberFormatsSupplier_3afb0fb7') -> None:
        """
        attaches an XNumberFormatsSupplier to this NumberFormatter.
        
        This NumberFormatter will only use the NumberFormats specified in the attached XNumberFormatsSupplier. Without an attached XNumberFormatsSupplier, no formatting is possible.
        """
        ...
    @abstractmethod
    def convertNumberToString(self, nKey: int, fValue: float) -> str:
        """
        converts a number into a string.
        """
        ...
    @abstractmethod
    def convertStringToNumber(self, nKey: int, aString: str) -> float:
        """
        converts a string which contains a formatted number into a number.
        
        If this is a text format, the string will not be converted.

        Raises:
            com.sun.star.util.NotNumericException: ``NotNumericException``
        """
        ...
    @abstractmethod
    def detectNumberFormat(self, nKey: int, aString: str) -> int:
        """
        detects the number format in a string which contains a formatted number.

        Raises:
            com.sun.star.util.NotNumericException: ``NotNumericException``
        """
        ...
    @abstractmethod
    def formatString(self, nKey: int, aString: str) -> str:
        """
        converts a string into another string.
        """
        ...
    @abstractmethod
    def getInputString(self, nKey: int, fValue: float) -> str:
        """
        converts a number into a string with the specified format.
        
        This string can always be converted back to a number using the same format.
        """
        ...
    @abstractmethod
    def getNumberFormatsSupplier(self) -> 'XNumberFormatsSupplier_3afb0fb7':
        """
        """
        ...
    @abstractmethod
    def queryColorForNumber(self, nKey: int, fValue: float, aDefaultColor: 'Color_68e908c5') -> 'Color_68e908c5':
        """
        """
        ...
    @abstractmethod
    def queryColorForString(self, nKey: int, aString: str, aDefaultColor: 'Color_68e908c5') -> 'Color_68e908c5':
        """
        """
        ...

__all__ = ['XNumberFormatter']

