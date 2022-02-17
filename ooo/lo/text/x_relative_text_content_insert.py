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
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_text_content import XTextContent as XTextContent_b16e0ba5

class XRelativeTextContentInsert(XInterface_8f010a43):
    """
    makes it possible to insert new text contents before or after existing text contents.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XRelativeTextContentInsert <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XRelativeTextContentInsert.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XRelativeTextContentInsert'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XRelativeTextContentInsert'

    @abstractmethod
    def insertTextContentAfter(self, xNewContent: 'XTextContent_b16e0ba5', xPredecessor: 'XTextContent_b16e0ba5') -> None:
        """
        inserts text the new text content after the predecessor argument.
        
        This is helpful to insert paragraphs after text tables especially in headers, footers or text frames.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def insertTextContentBefore(self, xNewContent: 'XTextContent_b16e0ba5', xSuccessor: 'XTextContent_b16e0ba5') -> None:
        """
        inserts text the new text content before of the successor argument.
        
        This is helpful to insert paragraphs before of text tables.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XRelativeTextContentInsert']
