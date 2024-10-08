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
# Namespace: com.sun.star.accessibility
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_accessible_text import XAccessibleText as XAccessibleText_5b77105b
if typing.TYPE_CHECKING:
    from .text_segment import TextSegment as TextSegment_1e5b0ee8

class XAccessibleTextMarkup(XAccessibleText_5b77105b):
    """
    Implement this interface to expose the text markups of a text.
    
    The XAccessibleTextMarkup interface is the main interface to expose text markups in a text, typically of a text document, that are used to reference other (parts of) documents. For supporting the XAccessibleTextMarkup.getTextMarkupIndex() method of this interface and other character related methods of the XAccessibleTextMarkup interface, it is necessary to also support the XAccessibleText interface.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XAccessibleTextMarkup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleTextMarkup.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleTextMarkup'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleTextMarkup'

    @abstractmethod
    def getTextMarkup(self, TextMarkupIndex: int, TextMarkupType: int) -> TextSegment_1e5b0ee8:
        """
        Returns the text segment of the text markup of the given index and of the given text mark type.
        
        Throws IndexOutOfBoundsException, if given index is out of valid range.
        
        Throws IllegalArgumentException, if given text markup type is out of valid range.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getTextMarkupAtIndex(self, CharIndex: int, TextMarkupType: int) -> typing.Tuple[TextSegment_1e5b0ee8, ...]:
        """
        returns a sequence of the text segments of the text markups at the given character index and of the given text markup type.
        
        Throws IndexOutOfBoundsException, if given character index is out of range [0..number of characters in the text).
        
        Throws IllegalArgumentException, if given text markup type is out of valid range.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getTextMarkupCount(self, TextMarkupType: int) -> int:
        """
        Returns the number of text markup of the given text markup type of a text.
        
        Throws IllegalArgumentException, if given text markup type is out of valid range.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XAccessibleTextMarkup']

