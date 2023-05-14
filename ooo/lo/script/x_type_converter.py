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
# Namespace: com.sun.star.script
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..uno.type_class import TypeClass as TypeClass_853109f2

class XTypeConverter(XInterface_8f010a43):
    """
    Interface to provide standard type conversions.

    See Also:
        `API XTypeConverter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XTypeConverter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XTypeConverter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XTypeConverter'

    @abstractmethod
    def convertTo(self, aFrom: object, xDestinationType: object) -> object:
        """
        Converts the value aFrom to the specified type xDestinationType.
        
        Throws a CannotConvertException if the conversion failed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
        """
        ...
    @abstractmethod
    def convertToSimpleType(self, aFrom: object, aDestinationType: 'TypeClass_853109f2') -> object:
        """
        Converts the value aFrom to the specified simple type aDestinationType.
        
        Throws a CannotConvertException if the conversion failed and a com.sun.star.lang.IllegalArgumentException if the destination com.sun.star.uno.TypeClass is not simple, e.g. not long or byte.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
        """
        ...

__all__ = ['XTypeConverter']

