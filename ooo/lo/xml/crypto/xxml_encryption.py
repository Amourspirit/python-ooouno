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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_security_environment import XSecurityEnvironment as XSecurityEnvironment_7ead116d
    from .xxml_encryption_template import XXMLEncryptionTemplate as XXMLEncryptionTemplate_9c6511d8
    from .xxml_security_context import XXMLSecurityContext as XXMLSecurityContext_681010ae

class XXMLEncryption(XInterface_8f010a43):
    """
    Interface of XML encryption.
    
    This interface represents a XML encryptor or decryptor.
    
    The encryptor or decryptor concrete a key by retrieve security context and encryption template.
    
    In some cases, the encryptor or decryptor can determine and locate the EncryptedKey from the encryption template by dereference the RetrievalMethod inside EncryptedData.
    
    In some cases, the EncryptedKey need to be clearly pointed out by the encryption template.

    See Also:
        `API XXMLEncryption <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XXMLEncryption.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XXMLEncryption'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XXMLEncryption'

    @abstractmethod
    def decrypt(self, aTemplate: 'XXMLEncryptionTemplate_9c6511d8', aContext: 'XXMLSecurityContext_681010ae') -> 'XXMLEncryptionTemplate_9c6511d8':
        """
        Perform decryption in the environment of encryption template and context.

        Raises:
            : ````
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
        ...
    @abstractmethod
    def encrypt(self, aTemplate: 'XXMLEncryptionTemplate_9c6511d8', aEnvironment: 'XSecurityEnvironment_7ead116d') -> 'XXMLEncryptionTemplate_9c6511d8':
        """
        Perform encryption in the environment of encryption template and context.

        Raises:
            : ````
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
        ...

__all__ = ['XXMLEncryption']

