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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from enum import Enum


class LineEndType(Enum):
    """
    Enum Class

    

    See Also:
        `API LineEndType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#aa4142382acc18a0dd48cc4a563e2d168>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.LineEndType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.LineEndType'

    ARROW = 'ARROW'
    """
    the line uses an arrow for the line end.
    """
    CIRCLE = 'CIRCLE'
    """
    the line uses a circle for the line end.
    """
    NONE = 'NONE'
    """
    the area is not filled.
    
    The text size is only defined by the font properties.
    
    Don't animate this text.
    
    the line is hidden.
    
    the joint between lines will not be connected
    
    the line has no special end.
    """
    SPECIAL = 'SPECIAL'
    """
    not implemented, yet.
    
    deprecated
    """
    SQUARE = 'SQUARE'
    """
    the line will get a half square as additional cap
    
    the line uses a square for the line end.
    """

__all__ = ['LineEndType']

