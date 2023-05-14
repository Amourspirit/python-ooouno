# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod, abstractproperty
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .cmis_property import CmisProperty as CmisProperty_e47d0d58
    from .cmis_version import CmisVersion as CmisVersion_d71c0cd9

class XCmisDocument(XInterface_8f010a43):
    """
    The document can provide access to CMIS properties and versions through this interface.

    See Also:
        `API XCmisDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XCmisDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XCmisDocument'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XCmisDocument'

    @abstractmethod
    def canCancelCheckOut(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def canCheckIn(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def canCheckOut(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def cancelCheckOut(self) -> None:
        """
        Cancel checked out document, this will discard all changes since check-out.
        """
        ...
    @abstractmethod
    def checkIn(self, isMajor: bool, comment: str) -> None:
        """
        Creates a new version of the document from the private working copy.
        """
        ...
    @abstractmethod
    def checkOut(self) -> None:
        """
        Check out the document into a private working copy on the server, and update the loaded document to reflect this change.
        """
        ...
    @abstractmethod
    def getAllVersions(self) -> 'typing.Tuple[CmisVersion_d71c0cd9, ...]':
        """
        """
        ...
    @abstractmethod
    def isVersionable(self) -> bool:
        """
        Tells whether a document can support versioning or not.
        """
        ...
    @abstractmethod
    def updateCmisProperties(self, cmisProperties: 'typing.Tuple[CmisProperty_e47d0d58, ...]') -> None:
        """
        """
        ...
    @abstractproperty
    def CmisProperties(self) -> 'typing.Tuple[CmisProperty_e47d0d58, ...]':
        """
        Contains the properties values named after their CMIS ID.
        """
        ...


__all__ = ['XCmisDocument']

