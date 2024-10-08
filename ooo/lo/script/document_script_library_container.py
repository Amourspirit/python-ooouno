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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.script
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_storage_based_library_container import XStorageBasedLibraryContainer as XStorageBasedLibraryContainer_d72a1321
if typing.TYPE_CHECKING:
    from ..document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument_6b1310b2

class DocumentScriptLibraryContainer(XStorageBasedLibraryContainer_d72a1321):
    """
    Service Class

    defines a container of StarBasic script libraries, which is to be made persistent in a sub storage of a document storage.
    
    **since**
    
        OOo 2.3

    See Also:
        `API DocumentScriptLibraryContainer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1script_1_1DocumentScriptLibraryContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.DocumentScriptLibraryContainer'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, Document: XStorageBasedDocument_6b1310b2) -> None:
        """
        creates an instance of the DocumentScriptLibraryContainer, belonging to a document
        
        The current storage of the document will be set as initial root storage (see XPersistentLibraryContainer.RootStorage) of the container.
        
        Usually, you will only create a DocumentScriptLibraryContainer within the implementation of the document to which the container should belong.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createWithURL(self, URL: str) -> None:
        """
        """
        ...

__all__ = ['DocumentScriptLibraryContainer']

