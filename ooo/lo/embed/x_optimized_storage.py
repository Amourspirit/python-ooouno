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
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_stream import XStream as XStream_678908a4

class XOptimizedStorage(ABC):
    """
    This is a temporary interface that is introduced to temporarily optimize the document storing process.
    
    PLEASE DO NOT USE IT, it might change in any time and will be deprecated soon! Another solution will be introduced as final one.

    See Also:
        `API XOptimizedStorage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XOptimizedStorage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XOptimizedStorage'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XOptimizedStorage'

    @abstractmethod
    def attachToURL(self, sURL: str, bReadOnly: bool) -> None:
        """
        allows to switch storage persistence to the provided URL.
        
        The caller is responsible to be sure that the file referenced by the URL contains the same contents as the stream the storage is based currently. Thus using of this method is very dangerous and should be avoided when possible. It is applicable only for root storages.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def copyElementDirectlyTo(self, sSourceName: str, xTargetStorage: XOptimizedStorage, sTargetName: str) -> None:
        """
        allows to copy storage element directly, not guaranteed to work.

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
    def copyStreamElementData(self, sStreamName: str, xTargetStream: XStream_678908a4) -> None:
        """
        fills the provided stream with the last flushed version of data from the child stream of the storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def getElementPropertyValue(self, sElementName: str, sPropertyName: str) -> object:
        """
        allows to get property of the child element with the specified name.
        
        The implementation of the method might allow to access only subset of the supported by element properties.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def insertRawNonEncrStreamElementDirect(self, sStreamName: str, xInStream: XInputStream_98d40ab4) -> None:
        """
        allows to insert a raw stream representing non-encrypted stream with header.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoRawFormatException: ``NoRawFormatException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def insertStreamElementDirect(self, sStreamName: str, xInStream: XInputStream_98d40ab4, aProperties: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        allows to insert a stream to the storage directly.
        
        The stream must stay alive till the storage is committed.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def writeAndAttachToStream(self, xStream: XStream_678908a4) -> None:
        """
        allows to switch storage persistence to the provided stream.
        
        The stream will be filled by the storage. If an empty reference is provided, the storage will create a temporary stream to switch to itself. It is applicable only for root storages.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...

__all__ = ['XOptimizedStorage']

