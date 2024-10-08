# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.bridge
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..uno.uik import Uik as Uik_4fac0783

class XBridgeSupplier(XInterface_8f010a43):
    """
    defines the interface for creating bridges to other object models.
    
    Because bridges sometimes can not be generated in an address space, the implementation needs to check the address space of the caller by comparing the machine and process ID against its own. These IDs are provided by the UNO runtime.
    
    All objects, whether they are part of the UNO object model or not, are carried in an any. The representation of this object is heavily model-dependent and has to be specified in the following list:
    
    Any implementation can supply its own bridges to other object models by implementing this interface and returning the bridge when the method is called with itself as the first parameter.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XBridgeSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XBridgeSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge'
    __ooo_full_ns__: str = 'com.sun.star.bridge.XBridgeSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.bridge.XBridgeSupplier'

    @abstractmethod
    def createBridge(self, modelDepObject: object, MachineId: Uik_4fac0783, ProcessId: int, sourceModelType: int, destModelType: int) -> object:
        """
        creates a bridge to provide an object of one object model with another.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XBridgeSupplier']

