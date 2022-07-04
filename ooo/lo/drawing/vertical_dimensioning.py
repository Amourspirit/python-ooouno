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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from enum import Enum


class VerticalDimensioning(Enum):
    """
    Enum Class

    

    See Also:
        `API VerticalDimensioning <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a3d694e7ac991a1dc3541f7d166f0b126>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.VerticalDimensioning'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.VerticalDimensioning'

    AUTO = 'AUTO'
    """
    the connection point is chosen automatically,
    
    Set this to have the application select the best horizontal position for the text.
    """
    BOTTOM = 'BOTTOM'
    """
    the connection line leaves the connected object from the bottom,
    
    The text is positioned below the main line.
    
    The bottom edge of the text is adjusted to the bottom edge of the shape.
    """
    CENTERED = 'CENTERED'
    """
    The text is positioned at the center.
    
    The text is positioned over the main line.
    """
    TOP = 'TOP'
    """
    the connection line leaves the connected object from the top,
    
    The text is positioned above the main line.
    
    The top edge of the text is adjusted to the top edge of the shape.
    """

__all__ = ['VerticalDimensioning']

