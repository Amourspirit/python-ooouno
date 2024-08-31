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
# Namespace: com.sun.star.loader
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..registry.x_registry_key import XRegistryKey as XRegistryKey_e61a0d5b

class XImplementationLoader(XInterface_8f010a43):
    """
    handles activation (loading) of a UNO component.

    See Also:
        `API XImplementationLoader <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1loader_1_1XImplementationLoader.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.loader'
    __ooo_full_ns__: str = 'com.sun.star.loader.XImplementationLoader'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.loader.XImplementationLoader'

    @abstractmethod
    def activate(self, implementationName: str, implementationLoaderUrl: str, locationUrl: str, xKey: XRegistryKey_e61a0d5b) -> XInterface_8f010a43:
        """
        activates a concrete implementation within a component.
        
        Special loaders may define their own protocol (for instance an executable loader may need more than only one file url).

        Raises:
            com.sun.star.loader.CannotActivateFactoryException: ``CannotActivateFactoryException``
        """
        ...
    @abstractmethod
    def writeRegistryInfo(self, xKey: XRegistryKey_e61a0d5b, implementationLoaderUrl: str, locationUrl: str) -> bool:
        """
        writes a list of all implementations hosted by this component into a registry key.
        
        This method is called during registering a component.
        
        Special loaders may define their own protocol (for instance an executable loader may need more than only one file url).

        Raises:
            com.sun.star.registry.CannotRegisterImplementationException: ``CannotRegisterImplementationException``
        """
        ...

__all__ = ['XImplementationLoader']

