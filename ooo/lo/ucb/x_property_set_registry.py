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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_persistent_property_set import XPersistentPropertySet as XPersistentPropertySet_2b0c0f5c

class XPropertySetRegistry(XInterface_8f010a43):
    """
    A registry (storage medium) for persistent property sets.

    See Also:
        `API XPropertySetRegistry <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XPropertySetRegistry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XPropertySetRegistry'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XPropertySetRegistry'

    @abstractmethod
    def openPropertySet(self, key: str, create: bool) -> 'XPersistentPropertySet_2b0c0f5c':
        """
        creates a new or opens an existing property set in the registry.
        """
    @abstractmethod
    def removePropertySet(self, key: str) -> None:
        """
        removes a property set from the registry.
        """


__all__ = ['XPropertySetRegistry']

