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
# Namespace: com.sun.star.xml.sax
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ...beans.string_pair import StringPair as StringPair_a4bc0b14
    from .x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class XSAXSerializable(ABC):
    """
    serializes a DOM tree by generating SAX events.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XSAXSerializable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XSAXSerializable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.XSAXSerializable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.sax.XSAXSerializable'

    @abstractmethod
    def serialize(self, handler: XDocumentHandler_9b90e28, namespaces: typing.Tuple[StringPair_a4bc0b14, ...]) -> None:
        """
        serializes an object (e.g.
        
        a DOM tree) that represents an XML document by generating SAX events.
        
        This is necessary mostly because the DOM implementation does not permit attaching namespaces declarations directly to nodes, which may lead to duplicate namespace declarations on export, and thus larger documents. Note that the first part of each tuple is the prefix, e.g. \"office\", and the second is the full namespace URI.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...

__all__ = ['XSAXSerializable']

