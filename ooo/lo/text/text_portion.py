# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet_7bd4114e
from .text_range import TextRange as TextRange_90540a5f
if typing.TYPE_CHECKING:
    from .x_footnote import XFootnote as XFootnote_901e0a73
    from .x_text_content import XTextContent as XTextContent_b16e0ba5
    from .x_text_field import XTextField as XTextField_9a630aae

class TextPortion(TextRange_90540a5f, XTolerantMultiPropertySet_7bd4114e):
    """
    Service Class

    A TextPortion is a piece of text within a paragraph that does not contain changes of its attributes inside.
    
    It is created by an enumeration implemented in a paragraph service. It may be used to export the content of the paragraph to an external document format.
    
    **since**
    
        OOo 2.0

    See Also:
        `API TextPortion <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextPortion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextPortion'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Bookmark(self) -> 'XTextContent_b16e0ba5':
        """
        contains the bookmark of a text portion of type Bookmark.
        """
        ...

    @abstractproperty
    def ControlCharacter(self) -> int:
        """
        contains the control character of a text portion of type ControlCharacter.
        """
        ...

    @abstractproperty
    def DocumentIndexMark(self) -> 'XTextContent_b16e0ba5':
        """
        contains the document index mark of a text portion of type DocumentIndexMark.
        """
        ...

    @abstractproperty
    def Footnote(self) -> 'XFootnote_901e0a73':
        """
        contains the footnote of a text portion of type Footnote.
        """
        ...

    @abstractproperty
    def InContentMetadata(self) -> 'XTextContent_b16e0ba5':
        """
        contains the text range of a text portion of type InContentMetadata.
        
        **since**
        
            OOo 3.2
        """
        ...

    @abstractproperty
    def IsCollapsed(self) -> bool:
        """
        contains whether the portion is a point only.
        """
        ...

    @abstractproperty
    def IsStart(self) -> bool:
        """
        contains whether the portion is the start of the portion.
        
        This is used for portions which are represented by 2 TextPortion objects (e.g., DocmentIndexMark).
        """
        ...

    @abstractproperty
    def ReferenceMark(self) -> 'XTextContent_b16e0ba5':
        """
        contains the bookmark of a text portion of type ReferenceMark.
        """
        ...

    @abstractproperty
    def TextField(self) -> 'XTextField_9a630aae':
        """
        contains the text field of a text portion of type TextField.
        """
        ...

    @abstractproperty
    def TextPortionType(self) -> str:
        """
        contains the type of the text portion.
        
        Valid content type names are:
        
        For Reference marks, document index marks, etc., 2 text portions will be generated, one for the start position and one for the end position.
        """
        ...


__all__ = ['TextPortion']

