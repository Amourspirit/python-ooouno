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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing
from abc import abstractmethod
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..io.x_stream import XStream as XStream_678908a4

class XStorage(XNameAccess_e2ab0cf6, XComponent_98dc0ab5):
    """
    This interface represents main storage functionality.

    See Also:
        `API XStorage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XStorage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XStorage'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XStorage'

    @abstractmethod
    def cloneEncryptedStreamElement(self, sStreamName: str, sPassword: str) -> XStream_678908a4:
        """
        allows to get readonly copy of a child encrypted stream with password.
        
        If storage does not allow any encryption this method will always throw com.sun.star.packages.NoEncryptionException.
        
        The stream is open in readonly mode so the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.
        
        This method allows to specify reading password for the child stream explicitly.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def cloneStreamElement(self, sStreamName: str) -> XStream_678908a4:
        """
        allows to get readonly copy of a child stream of the storage.
        
        The stream is open in readonly mode so the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def copyElementTo(self, sElementName: str, xDest: XStorage, sNewName: str) -> None:
        """
        allows to copy an entry from one storage to another.
        
        If target element supports transacted mode it must be committed by this method after successful copying.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def copyLastCommitTo(self, xTargetStorage: XStorage) -> None:
        """
        allows to get copy of this storage at the state of its last commit.
        
        This method makes sense only for services implementations that allow transaction in the storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def copyStorageElementLastCommitTo(self, sStorName: str, xTargetStorage: XStorage) -> None:
        """
        allows to get copy of a child storage at the state of its last commit.
        
        This method makes sense only for services implementations that allow transaction in the storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def copyToStorage(self, xDest: XStorage) -> None:
        """
        allows to copy current storage to another one
        
        The destination storage contents are overwritten. After the successful copying the target storage is automatically committed if it implements transacted access.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def isStorageElement(self, sElementName: str) -> bool:
        """
        allows to check if an element is a child storage with specified name.
        
        In case there is no child element with such name an exception will be thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
        """
        ...
    @abstractmethod
    def isStreamElement(self, sElementName: str) -> bool:
        """
        allows to check if an element is a child stream with specified name.
        
        In case there is no child element with such name an exception will be thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
        """
        ...
    @abstractmethod
    def moveElementTo(self, sElementName: str, xDest: XStorage, sNewName: str) -> None:
        """
        allows to move an entry from one storage to another.
        
        If target element supports transacted mode it must be committed by this method after successful moving.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def openEncryptedStreamElement(self, sStreamName: str, nOpenMode: int, sPassword: str) -> XStream_678908a4:
        """
        allows to get access to a child encrypted stream with password.
        
        If storage does not allow any encryption this method will always throw com.sun.star.packages.NoEncryptionException.
        
        In case the stream is open in readonly mode the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def openStorageElement(self, sStorName: str, nOpenMode: int) -> XStorage:
        """
        allows to get access to a child storage.
        
        The opened substorage must support specified in \"nOpenMode\" access modes. It can support \"read\" mode in addition. But any child element can support one of those modes only in case this mode is supported by parent storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def openStreamElement(self, sStreamName: str, nOpenMode: int) -> XStream_678908a4:
        """
        allows to get access to a child stream of the storage.
        
        In case the stream is open in readonly mode the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def removeElement(self, sElementName: str) -> None:
        """
        removes an element from a storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def renameElement(self, sElementName: str, sNewName: str) -> None:
        """
        renames an element in a storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...

__all__ = ['XStorage']

