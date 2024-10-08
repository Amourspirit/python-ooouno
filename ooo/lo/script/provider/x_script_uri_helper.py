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
# Namespace: com.sun.star.script.provider
from __future__ import annotations
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XScriptURIHelper(XInterface_8f010a43):
    """
    This interface is used to help transform Scripting Framework storage locations to Scripting Framework script URIs and vice versa.

    See Also:
        `API XScriptURIHelper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1provider_1_1XScriptURIHelper.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script.provider'
    __ooo_full_ns__: str = 'com.sun.star.script.provider.XScriptURIHelper'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.provider.XScriptURIHelper'

    @abstractmethod
    def getRootStorageURI(self) -> str:
        """
        Obtain the root storage URI for this ScriptURIHelper.
        
        The resulting string can be used to access the storage for this using the Universal Content Broker
        """
        ...
    @abstractmethod
    def getScriptURI(self, storageURI: str) -> str:
        """
        Obtain the Scripting Framework script URI for a specific UCB URI.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getStorageURI(self, scriptURI: str) -> str:
        """
        Obtain the storage URI for a specific Scripting Framework script URI.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XScriptURIHelper']

