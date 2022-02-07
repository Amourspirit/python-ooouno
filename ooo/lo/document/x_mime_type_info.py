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
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMimeTypeInfo(XInterface_8f010a43):
    """
    provides information regarding which MIME types are supported by a filter.

    See Also:
        `API XMimeTypeInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XMimeTypeInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XMimeTypeInfo'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XMimeTypeInfo'

    @abstractmethod
    def getSupportedMimeTypeNames(self) -> 'typing.Tuple[str, ...]':
        """
        """
    @abstractmethod
    def supportsMimeType(self, MimeTypeName: str) -> bool:
        """
        asks whether a MIME type is supported or not.
        """

__all__ = ['XMimeTypeInfo']

