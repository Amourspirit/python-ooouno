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
# Namespace: com.sun.star.script
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_introspection_access import XIntrospectionAccess as XIntrospectionAccess_2a050f2c

class XInvocation(XInterface_8f010a43):
    """
    gives access to an object's methods and properties.
    
    Container access is available through com.sun.star.container.XIndexContainer, com.sun.star.container.XNameContainer and com.sun.star.container.XEnumerationAccess.

    See Also:
        `API XInvocation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XInvocation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XInvocation'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XInvocation'

    @abstractmethod
    def getIntrospection(self) -> 'XIntrospectionAccess_2a050f2c':
        """
        returns the introspection from this object or NULL if the object does not provide this information.
        """
    @abstractmethod
    def getValue(self, aPropertyName: str) -> object:
        """
        returns the value of the property with the specified name.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
    @abstractmethod
    def hasMethod(self, aName: str) -> bool:
        """
        returns TRUE if the method with the specified name exists, else FALSE.
        
        This optimizes the calling sequence ( XInvocation.hasMethod(), XInvocation.invoke() )!
        """
    @abstractmethod
    def hasProperty(self, aName: str) -> bool:
        """
        returns TRUE if the property with the specified name exists, else FALSE.
        """
    @abstractmethod
    def invoke(self, aFunctionName: str, aParams: 'typing.Tuple[object, ...]', aOutParamIndex: 'typing.Tuple[int, ...]', aOutParam: 'typing.Tuple[object, ...]') -> object:
        """
        provides access to methods exposed by an object.
        
        Example: aOutParamIndex == { 1, 4 } means that aOutParam[0] contains the out value of the aParams[1] parameter and aOutParam[1] contains the out value of the aParams[4] parameter.

        * ``aOutParamIndex`` is an out direction argument.
        * ``aOutParam`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
    @abstractmethod
    def setValue(self, aPropertyName: str, aValue: object) -> None:
        """
        sets a value to the property with the specified name.
        
        If the underlying object implements an com.sun.star.container.XNameContainer, then this method will insert the value if there is no such aPropertyName.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """

__all__ = ['XInvocation']

