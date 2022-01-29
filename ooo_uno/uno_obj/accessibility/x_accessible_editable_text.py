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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from .x_accessible_text import XAccessibleText as XAccessibleText_5b77105b
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XAccessibleEditableText(XAccessibleText_5b77105b):
    """
    Implement this interface to give read and write access to a text representation.
    
    This interface is typically used in conjunction with the XAccessibleText interface and extents it about the ability to modify the text represented by that interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleEditableText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleEditableText.html>`_
    """

    @abstractmethod
    def cutText(self, nStartIndex: int, nEndIndex: int) -> bool:
        """
        Copies the text range into the clipboard.
        
        The specified text between and including the two given indices is copied into the system clipboard and is deleted afterwards from the text represented by this object. This is equivalent to calling first XAccessibleText.copyText() and then XAccessibleEditableText.deleteText() with the given start and end indices.
        
        The text indices are interpreted like those in the XAccessibleText.getTextRange() method.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def deleteText(self, nStartIndex: int, nEndIndex: int) -> bool:
        """
        Deletes a range of text.
        
        The text between and including the two given indices is deleted from the text represented by this object.
        
        The text indices are interpreted like those in the XAccessibleText.getTextRange() method.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def insertText(self, sText: str, nIndex: int) -> bool:
        """
        Inserts text at the specified position.
        
        The specified string is inserted at the given index into the text represented by this object.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def pasteText(self, nIndex: int) -> bool:
        """
        Pastes text from the clipboard.
        
        The text in the system clipboard is pasted into the text represented by this object at the given index. This method is similar to the XAccessibleEditableText.insertText() method. If the index is not valid then the system clipboard text is not inserted.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def replaceText(self, nStartIndex: int, nEndIndex: int, sReplacement: str) -> bool:
        """
        Replaces text.
        
        The text between the two given indices is replaced by the specified replacement string. This method is equivalent to calling first XAccessibleEditableText.deleteText() with the two indices and afterwards calling XAccessibleEditableText.insertText() with the replacement text and the start index.
        
        The text indices are interpreted like those in the XAccessibleText.getTextRange() method.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def setAttributes(self, nStartIndex: int, nEndIndex: int, aAttributeSet: 'typing.List[PropertyValue_c9610c73]') -> bool:
        """
        Replaces the attributes of a text range by the given set of attributes.
        
        Sets the attributes for the text between and including the two given indices to those given. The old attributes of this text portion are replaced by the new list of attributes.
        
        The text indices are interpreted like those in the XAccessibleText.getTextRange() method.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def setText(self, sText: str) -> bool:
        """
        Replaces the whole text with the given text.
        
        The text content of this object is set to the given string.
        """

__all__ = ['XAccessibleEditableText']

