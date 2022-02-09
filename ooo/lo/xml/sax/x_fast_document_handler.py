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
# Namespace: com.sun.star.xml.sax
import typing
from abc import abstractmethod
from .x_fast_context_handler import XFastContextHandler as XFastContextHandler_361e0f5c
if typing.TYPE_CHECKING:
    from .x_locator import XLocator as XLocator_a3fb0aff

class XFastDocumentHandler(XFastContextHandler_361e0f5c):
    """
    receives notification of sax document events from a XFastParser
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XFastDocumentHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastDocumentHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.XFastDocumentHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.sax.XFastDocumentHandler'

    @abstractmethod
    def endDocument(self) -> None:
        """
        called by the parser after the last XML element of a stream is processed.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def processingInstruction(self, aTarget: str, aData: str) -> None:
        """
        receives notification of a processing instruction.
        
        **since**
        
            LibreOffice 6.0

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def setDocumentLocator(self, xLocator: 'XLocator_a3fb0aff') -> None:
        """
        receives an object for locating the origin of SAX document events.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def startDocument(self) -> None:
        """
        called by the parser when parsing of an XML stream is started.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """


__all__ = ['XFastDocumentHandler']

