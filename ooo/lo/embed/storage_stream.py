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
# Namespace: com.sun.star.embed
from __future__ import annotations
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource_8cdf11a3
from ..io.x_seekable import XSeekable as XSeekable_79540954
from ..io.x_stream import XStream as XStream_678908a4
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class StorageStream(XPropertySet_bc180bfa, XEncryptionProtectedSource_8cdf11a3, XSeekable_79540954, XStream_678908a4, XComponent_98dc0ab5):
    """
    Service Class

    This is a service that represents a stream that can be provided by XStorage.openStreamElement() call implemented by Storage service.
    
    In case a stream is open with read-write access only one instance of the stream can exist.

    See Also:
        `API StorageStream <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1StorageStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.StorageStream'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def IsCompressed(self) -> bool:
        """
        specifies if the stream should be compressed next time it is stored.
        """
        ...

    @property
    @abstractmethod
    def IsEncrypted(self) -> bool:
        """
        allows to detect if the stream is encrypted.
        
        The property value TRUE means that the stream is currently encrypted. FALSE - the stream is not encrypted.
        
        If somebody sets a password explicitly by using XEncryptionProtectedSource interface the value is automatically set to TRUE. If the interface is used to remove the encryption - the value is automatically set to FALSE.
        """
        ...

    @property
    @abstractmethod
    def MediaType(self) -> str:
        """
        allows to get and set media type of the stream.
        """
        ...

    @property
    @abstractmethod
    def Size(self) -> int:
        """
        allows to detect size of the stream in bytes.
        """
        ...

    @property
    @abstractmethod
    def UseCommonStoragePasswordEncryption(self) -> bool:
        """
        specifies whether the stream will become encrypted next time the common storage password holder is committed.
        
        The property value TRUE means that the stream will become encrypted after the closest storage in the parent hierarchy, that has common storage password, is committed. FALSE - the stream will not react to commit of such a storage.
        
        In case stream is not encrypted and the property is set to TRUE, the stream will stay non-encrypted until the closest storage in the parent hierarchy, that has common storage password, is committed. On the commit the stream will be encrypted with the common storage password. If there is no such storage in the hierarchy the stream will not be encrypted at all. Thus this property must be set very carefully.
        
        If somebody sets a password explicitly by using XEncryptionProtectedSource interface the value is automatically set to FALSE and the stream becomes encrypted with specified password immediately.
        
        In case stream is encrypted one and the value is set to TRUE the stream becomes non-encrypted until the common storage password holder is committed. The data about previously set password ( if any ) will be removed and the stream can be accessed as non-encrypted stream.
        """
        ...


__all__ = ['StorageStream']

