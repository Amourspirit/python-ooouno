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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .security_operation_status import SecurityOperationStatus as SecurityOperationStatus_b66e12b5
    from ..wrapper.xxml_element_wrapper import XXMLElementWrapper as XXMLElementWrapper_66c0107c

class XXMLSecurityTemplate(XInterface_8f010a43):
    """
    Interface of the XML security template.
    
    This interface represents a security template, which is the super interface of the XXMLSignatureTemplate interface and the XXMLEncryptionTemplate interface.

    See Also:
        `API XXMLSecurityTemplate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XXMLSecurityTemplate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XXMLSecurityTemplate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XXMLSecurityTemplate'

    @abstractmethod
    def getStatus(self) -> 'SecurityOperationStatus_b66e12b5':
        """
        Get the template status.
        """
        ...
    @abstractmethod
    def getTemplate(self) -> 'XXMLElementWrapper_66c0107c':
        """
        Get the XML signature element that represents the signature template.
        """
        ...
    @abstractmethod
    def setStatus(self, status: 'SecurityOperationStatus_b66e12b5') -> None:
        """
        Set the template status.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setTarget(self, aXmlElement: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Load the target XML element, i.e.
        
        the element to be signed

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setTemplate(self, aXmlElement: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Load a XML signature template from XML signature element.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XXMLSecurityTemplate']

