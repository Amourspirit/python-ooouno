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
from abc import abstractmethod
from .x_node import XNode as XNode_83fb09a5

class XCharacterData(XNode_83fb09a5):
    """

    See Also:
        `API XCharacterData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XCharacterData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XCharacterData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XCharacterData'

    @abstractmethod
    def appendData(self, arg: str) -> None:
        """
        Append the string to the end of the character data of the node.
        
        Throws: DOMException - NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def deleteData(self, offset: int, count: int) -> None:
        """
        Remove a range of 16-bit units from the node.
        
        Throws: DOMException - INDEX_SIZE_ERR: Raised if the specified offset is negative or greater than the number of 16-bit units in data, or if the specified count is negative. NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def getData(self) -> str:
        """
        Return the character data of the node that implements this interface.
        
        Throws: DOMException - NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly. DOMException - DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a DOMString variable on the implementation platform.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def getLength(self) -> int:
        """
        The number of 16-bit units that are available through data and the substringData method below.
        """
        ...
    @abstractmethod
    def insertData(self, offset: int, arg: str) -> None:
        """
        Insert a string at the specified 16-bit unit offset.
        
        Throws: DOMException - INDEX_SIZE_ERR: Raised if the specified offset is negative or greater than the number of 16-bit units in data. NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def replaceData(self, offset: int, count: int, arg: str) -> None:
        """
        Replace the characters starting at the specified 16-bit unit offset with the specified string.
        
        Throws; DOMException - INDEX_SIZE_ERR: Raised if the specified offset is negative or greater than the number of 16-bit units in data, or if the specified count is negative. NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def setData(self, data: str) -> None:
        """
        Set the character data of the node that implements this interface.
        
        Throws: DOMException - NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly. DOMException - DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a DOMString variable on the implementation platform.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def subStringData(self, offset: int, count: int) -> str:
        """
        Extracts a range of data from the node.
        
        Throws: DOMException - INDEX_SIZE_ERR: Raised if the specified offset is negative or greater than the number of 16-bit units in data, or if the specified count is negative. DOMSTRING_SIZE_ERR: Raised if the specified range of text does not fit into a DOMString.

        Raises:
            DOMException: ``DOMException``
        """
        ...

__all__ = ['XCharacterData']

