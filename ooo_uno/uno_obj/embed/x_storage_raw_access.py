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
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XStorageRawAccess(ABC):
    """
    This interface represents main storage functionality.

    See Also:
        `API XStorageRawAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XStorageRawAccess.html>`_
    """

    @abstractmethod
    def getPlainRawStreamElement(self, sStreamName: str) -> 'XInputStream_98d40ab4':
        """
        allows to get a plain raw stream representing a package stream.
        
        This method returns a stream from the package as it is stored there, without any decompression/description and etc. This method can be helpful to check file consistency, for example by signing.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
    @abstractmethod
    def getRawEncrStreamElement(self, sStreamName: str) -> 'XInputStream_98d40ab4':
        """
        allows to get a raw stream representing encrypted stream with header.
        
        This method allows to transport encrypted streams without decryption. Mainly this method is introduced to allow to copy one encrypted storage stream to another without decryption. It is not recommended to use this method outside of storage implementation since different storages implementation could have different encryption format. If the method is used outside of storage implementation the user code is responsible to get sure that the raw format of source and target storages is the same.
        
        The difference of this method from the previous one is that it handles only encrypted streams. The contents of returned by these methods streams can differ for the same entry, since this method can add additional data into the stream to allow successful insertion.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
    @abstractmethod
    def insertRawEncrStreamElement(self, sStreamName: str, xInStream: 'XInputStream_98d40ab4') -> None:
        """
        allows to insert a raw stream representing encrypted stream with header.
        
        This method allows to insert a stream retrieved by XStorageRawAccess.getRawEncrStreamElement() into a storage.
        
        This method allows to transport encrypted streams without decryption. Mainly this method is introduced to allow to copy one encrypted storage stream to another without decryption. It is not recommended to use this method outside of storage implementation since different storages implementation could have different encryption format.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoRawFormatException: ``NoRawFormatException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """

__all__ = ['XStorageRawAccess']

