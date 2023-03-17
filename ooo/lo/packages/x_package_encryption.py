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
# Libre Office Version: 7.4
# Namespace: com.sun.star.packages
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35

class XPackageEncryption(XInterface_8f010a43):
    """
    Allows to transparently plug-in crypto for PackageStreams.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API XPackageEncryption <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1packages_1_1XPackageEncryption.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.packages'
    __ooo_full_ns__: str = 'com.sun.star.packages.XPackageEncryption'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.packages.XPackageEncryption'

    @abstractmethod
    def checkDataIntegrity(self) -> bool:
        """
        Check if decryption meta data is valid.
        
        Some implementations might for example check HMAC values here. Call this before trusting encrypted data.
        """
        ...
    @abstractmethod
    def createEncryptionData(self, rPassword: str) -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        Create key-value list of encryption meta data.
        
        After generateEncryptionKey() succeeded in setting up crypto, use this method to create requisite meta data. Depending on underlying crypto, this can be a salt, init vector, or other algorithm-specific information that needs to be stored alongside an encrypted document
        """
        ...
    @abstractmethod
    def decrypt(self, rxInputStream: 'XInputStream_98d40ab4', rxOutputStream: 'XOutputStream_a4e00b35') -> bool:
        """
        Decrypt document content.
        
        After crypto setup via readEncryptionInfo(), pipe package bits through encryption engine.

        * ``rxOutputStream`` is an out direction argument.
        """
        ...
    @abstractmethod
    def encrypt(self, rxInputStream: 'XInputStream_98d40ab4') -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        Encrypt given stream.
        
        After setting up crypto via setupEncryption(), use this method to encrypt content.
        """
        ...
    @abstractmethod
    def generateEncryptionKey(self, rPassword: str) -> bool:
        """
        Set or refresh encryption key.
        """
        ...
    @abstractmethod
    def readEncryptionInfo(self, rStreams: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> bool:
        """
        Read package crypto information.
        """
        ...
    @abstractmethod
    def setupEncryption(self, rMediaEncData: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> bool:
        """
        Set key-value list of encryption meta data.
        
        Use this method to setup requisite encryption meta data. Depending on the underlying crypto, this can be a salt, init vector, or other algorithm-specific information that needs to be stored alongside an encrypted document
        """
        ...

__all__ = ['XPackageEncryption']

