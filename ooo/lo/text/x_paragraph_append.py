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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_text_range import XTextRange as XTextRange_9a910ab7

class XParagraphAppend(XInterface_8f010a43):
    """
    allows inserting and appending paragraphs.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XParagraphAppend <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XParagraphAppend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XParagraphAppend'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XParagraphAppend'

    @abstractmethod
    def finishParagraph(self, CharacterAndParagraphProperties: 'PropertyValues_d6470ce6') -> 'XTextRange_9a910ab7':
        """
        appends a new and empty paragraph at the end of the text.
        
        The properties are applied to the last paragraph before the new paragraph is inserted.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
    @abstractmethod
    def finishParagraphInsert(self, CharacterAndParagraphProperties: 'PropertyValues_d6470ce6', TextRange: 'XTextRange_9a910ab7') -> 'XTextRange_9a910ab7':
        """
        inserts a new and empty paragraph to the text at a given position.
        
        The properties are applied to the last paragraph before the new paragraph is inserted.
        
        **since**
        
            LibreOffice 4.0

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """

__all__ = ['XParagraphAppend']

