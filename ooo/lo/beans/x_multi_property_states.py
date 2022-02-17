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
# Namespace: com.sun.star.beans
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .property_state import PropertyState as PropertyState_c97b0c77

class XMultiPropertyStates(XInterface_8f010a43):
    """
    makes it possible to query information about the state of one or more properties.
    
    The state of a property contains information about the source of the value, e.g. the object itself, a default or a stylesheet. For more information see PropertyState.

    See Also:
        `API XMultiPropertyStates <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XMultiPropertyStates.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XMultiPropertyStates'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XMultiPropertyStates'

    @abstractmethod
    def getPropertyDefaults(self, aPropertyNames: 'typing.Tuple[str, ...]') -> 'typing.Tuple[object, ...]':
        """
        If no default exists, is not known, or is void, then the return type at the corresponding position in the sequence returned is void.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def getPropertyStates(self, aPropertyName: 'typing.Tuple[str, ...]') -> 'typing.Tuple[PropertyState_c97b0c77, ...]':
        """
        The order of the states is correlating to the order of the given property names.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
    @abstractmethod
    def setAllPropertiesToDefault(self) -> None:
        """
        sets all properties to their default values.
        
        Each value depends on the implementation of this interface. If it is a bound property, you must change the value before the change events are fired. If it is a constrained property, you must fire the vetoable event before you change the property value.
        """
    @abstractmethod
    def setPropertiesToDefault(self, aPropertyNames: 'typing.Tuple[str, ...]') -> None:
        """
        sets the specified properties to their default values.
        
        Each value depends on the implementation of this interface. If it is a bound property, you must change the value before the change events are fired. If it is a constrained property, you must fire the vetoable event before you change the property value.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """

__all__ = ['XMultiPropertyStates']
