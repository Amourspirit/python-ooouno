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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler_7c171110
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class GraphicStorageHandler(XGraphicStorageHandler_7c171110):
    """
    Service Class

    Default implementation of XGraphicStorageHandler.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API GraphicStorageHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1GraphicStorageHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.GraphicStorageHandler'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithStorage(self, Storage: XStorage_8e460a32) -> None:
        """
        """
        ...

__all__ = ['GraphicStorageHandler']

