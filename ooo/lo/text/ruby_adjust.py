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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
from enum import Enum


class RubyAdjust(Enum):
    """
    Enum Class

    

    See Also:
        `API RubyAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text.html#adf417fe4b45f486fe88af93ad0b59efb>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.RubyAdjust'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.text.RubyAdjust'

    BLOCK = 'BLOCK'
    """
    adjusted to both borders / stretched
    """
    CENTER = 'CENTER'
    """
    the object is adjusted to the center.
    
    centric adjusted.
    """
    INDENT_BLOCK = 'INDENT_BLOCK'
    """
    adjusted to both borders except for a small indent on both sides
    """
    LEFT = 'LEFT'
    """
    the object is left adjusted.
    
    text flows to the left side of the object.
    
    adjusted to the left.
    """
    RIGHT = 'RIGHT'
    """
    the object is right adjusted.
    
    text flows to the right side of the object.
    
    adjusted to the right.
    """

__all__ = ['RubyAdjust']

