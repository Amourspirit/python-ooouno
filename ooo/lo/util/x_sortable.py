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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XSortable(XInterface_8f010a43):
    """
    makes it possible to sort the contents of this object.
    
    The available properties describing the sort criteria are defined in the sort descriptor implemented by the object that implements this interface.
    
    There are older deprecated sort descriptors:
    
    And a new set of sort descriptors:
    
    Both types may be implemented by the same object. When calling the sort method however properties from different descriptors must not be mixed.

    See Also:
        `API XSortable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XSortable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XSortable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XSortable'

    @abstractmethod
    def createSortDescriptor(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        The set of properties is specific to the type of object that implements this interface. Therefore they can usually be used only for objects of that same type.
        """
    @abstractmethod
    def sort(self, xDescriptor: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        sorts the contents of the object according to the specified properties.
        
        The specified properties are usually the same or a subset of those obtained by calling createSortDescriptor() on the same type of object.
        """

__all__ = ['XSortable']

