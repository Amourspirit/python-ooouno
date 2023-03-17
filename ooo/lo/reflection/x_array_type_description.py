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
# Namespace: com.sun.star.reflection
import uno
from abc import abstractmethod
from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1

class XArrayTypeDescription(XTypeDescription_3c210fb1):
    """
    Deprecated, UNOIDL does not have an array concept.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XArrayTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XArrayTypeDescription.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XArrayTypeDescription'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XArrayTypeDescription'

    @abstractmethod
    def getDimensions(self) -> uno.ByteSequence:
        """
        Returns dimensions of array (same length as getNumberOfDimensions()).
        """
        ...
    @abstractmethod
    def getNumberOfDimensions(self) -> int:
        """
        Returns the number of dimensions of the array.
        """
        ...
    @abstractmethod
    def getType(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the element type of the array.
        """
        ...

__all__ = ['XArrayTypeDescription']

