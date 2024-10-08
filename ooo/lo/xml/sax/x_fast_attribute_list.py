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
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..attribute import Attribute as Attribute_85880a0d
    from ..fast_attribute import FastAttribute as FastAttribute_b07f0b9b

class XFastAttributeList(XInterface_8f010a43):
    """
    a container for the attributes of an XML element.
    
    Attributes are separated into known attributes and unknown attributes.
    
    Known attributes have a local name that is known to the XFastTokenHandler registered at the XFastParser which created the sax event containing this attributes. If an attribute also has a namespace, that must be registered at the XFastParser, else this attribute is also unknown even if the local name is known.

    See Also:
        `API XFastAttributeList <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastAttributeList.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.XFastAttributeList'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.sax.XFastAttributeList'

    @abstractmethod
    def getFastAttributes(self) -> typing.Tuple[FastAttribute_b07f0b9b, ...]:
        """
        returns a sequence of attributes which names and or namespaces URLS are translated to tokens.
        """
        ...
    @abstractmethod
    def getOptionalValue(self, Token: int) -> str:
        """
        retrieves the value of an attribute.
        
        If the attribute name has a namespace that was registered with the XFastParser, Token contains the integer token of the attributes local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.
        """
        ...
    @abstractmethod
    def getOptionalValueToken(self, Token: int, Default: int) -> int:
        """
        retrieves the token of an attribute value.
        
        If the attribute name has a namespace that was registered with the XFastParser, Token contains the integer token of the attributes local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.
        """
        ...
    @abstractmethod
    def getUnknownAttributes(self) -> typing.Tuple[Attribute_85880a0d, ...]:
        """
        returns a sequence of attributes which names and or namespaces URLS can not be translated to tokens.
        """
        ...
    @abstractmethod
    def getValue(self, Token: int) -> str:
        """
        retrieves the value of an attribute.
        
        If the attribute name has a namespace that was registered with the XFastParser, Token contains the integer token of the attributes local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.

        Raises:
            SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def getValueToken(self, Token: int) -> int:
        """
        retrieves the token of an attribute value.
        
        If the attribute name has a namespace that was registered with the XFastParser, Token contains the integer token of the attributes local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.

        Raises:
            SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def hasAttribute(self, Token: int) -> bool:
        """
        checks if an attribute is available.
        
        If the attribute name has a namespace that was registered with the XFastParser, Token contains the integer token of the attributes local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.
        """
        ...

__all__ = ['XFastAttributeList']

