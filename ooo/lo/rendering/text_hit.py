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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class TextHit(object):
    """
    Struct Class

    This structure contains hit information for XTextLayout.
    
    This structure is used from the XTextLayout interface to transport information regarding hit tests.
    
    **since**
    
        OOo 2.0

    See Also:
        `API TextHit <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1TextHit.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.TextHit'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.TextHit'
    """Literal Constant ``com.sun.star.rendering.TextHit``"""

    def __init__(self, EntryIndex: int = 0, IsLeadingEdge: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``EntryIndex`` can be another ``TextHit`` instance,
                in which case other named args are ignored.

        Arguments:
            EntryIndex (int, optional): EntryIndex value
            IsLeadingEdge (bool, optional): IsLeadingEdge value
        """
        if isinstance(EntryIndex, TextHit):
            oth: TextHit = EntryIndex
            self._entry_index = oth.EntryIndex
            self._is_leading_edge = oth.IsLeadingEdge
            return
        else:
            self._entry_index = EntryIndex
            self._is_leading_edge = IsLeadingEdge



    @property
    def EntryIndex(self) -> int:
        """
        This contains the entry index.
        
        The entry index is the index of the insertion point in the character sequence. The insertion point denotes positions between the actual characters in the string, and can thus have values ranging from 0 up to the number of characters in the string. Hereby, an index of 0 denotes an insertion position before the first character, and an index containing the number of characters denotes an insertion behind the last character.
        """
        return self._entry_index
    
    @EntryIndex.setter
    def EntryIndex(self, value: int) -> None:
        self._entry_index = value

    @property
    def IsLeadingEdge(self) -> bool:
        """
        This member denotes whether the hit was on the leading edge.
        
        Each character is divided in two halves, the leading and the trailing part. The leading edge is the part of the glyph encountered first when reading text of the corresponding language (i.e. the leading edge of an Arabic glyph is the right half of it, whereas it is the left half of a Latin character). If the hit was on the leading edge, this member is set to TRUE.
        """
        return self._is_leading_edge
    
    @IsLeadingEdge.setter
    def IsLeadingEdge(self, value: bool) -> None:
        self._is_leading_edge = value


__all__ = ['TextHit']
