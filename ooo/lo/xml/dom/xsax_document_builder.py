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
# Namespace: com.sun.star.xml.dom
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_document import XDocument as XDocument_aebc0b5e
    from .x_document_fragment import XDocumentFragment as XDocumentFragment_17850e92
    from com.sun.star.xml.dom.SAXDocumentBuilderState import SAXDocumentBuilderStateProto  # type: ignore

class XSAXDocumentBuilder(XInterface_8f010a43):
    """
    Builds a new dom tree

    See Also:
        `API XSAXDocumentBuilder <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XSAXDocumentBuilder.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XSAXDocumentBuilder'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XSAXDocumentBuilder'

    @abstractmethod
    def endDocumentFragment(self) -> None:
        """
        """
        ...
    @abstractmethod
    def getDocument(self) -> XDocument_aebc0b5e:
        """
        """
        ...
    @abstractmethod
    def getDocumentFragment(self) -> XDocumentFragment_17850e92:
        """
        """
        ...
    @abstractmethod
    def getState(self) -> SAXDocumentBuilderStateProto:
        """
        """
        ...
    @abstractmethod
    def reset(self) -> None:
        """
        """
        ...
    @abstractmethod
    def startDocumentFragment(self, ownerDoc: XDocument_aebc0b5e) -> None:
        """
        """
        ...

__all__ = ['XSAXDocumentBuilder']