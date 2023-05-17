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
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.Alignment import BOTTOM as ALIGNMENT_BOTTOM
    from com.sun.star.drawing.Alignment import BOTTOM_LEFT as ALIGNMENT_BOTTOM_LEFT
    from com.sun.star.drawing.Alignment import BOTTOM_RIGHT as ALIGNMENT_BOTTOM_RIGHT
    from com.sun.star.drawing.Alignment import CENTER as ALIGNMENT_CENTER
    from com.sun.star.drawing.Alignment import LEFT as ALIGNMENT_LEFT
    from com.sun.star.drawing.Alignment import RIGHT as ALIGNMENT_RIGHT
    from com.sun.star.drawing.Alignment import TOP as ALIGNMENT_TOP
    from com.sun.star.drawing.Alignment import TOP_LEFT as ALIGNMENT_TOP_LEFT
    from com.sun.star.drawing.Alignment import TOP_RIGHT as ALIGNMENT_TOP_RIGHT

    class Alignment(uno.Enum):
        """
        Enum Class


        See Also:
            `API Alignment <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#acdfaca60ec19c0265bac2692d7982726>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.Alignment', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.Alignment'
        __ooo_type_name__: str = 'enum'

        BOTTOM: Alignment = ALIGNMENT_BOTTOM
        """
        the connection line leaves the connected object from the bottom,
        
        The text is positioned below the main line.
        
        The bottom edge of the text is adjusted to the bottom edge of the shape.
        """
        BOTTOM_LEFT: Alignment = ALIGNMENT_BOTTOM_LEFT
        """
        """
        BOTTOM_RIGHT: Alignment = ALIGNMENT_BOTTOM_RIGHT
        """
        """
        CENTER: Alignment = ALIGNMENT_CENTER
        """
        The text is centered inside the shape.
        """
        LEFT: Alignment = ALIGNMENT_LEFT
        """
        the connection line leaves the connected object to the left,
        
        The left edge of the text is adjusted to the left edge of the shape.
        
        The text is positioned to the left.
        """
        RIGHT: Alignment = ALIGNMENT_RIGHT
        """
        the connection line leaves the connected object to the right,
        
        The right edge of the text is adjusted to the right edge of the shape.
        
        The text is positioned to the right.
        """
        TOP: Alignment = ALIGNMENT_TOP
        """
        the connection line leaves the connected object from the top,
        
        The text is positioned above the main line.
        
        The top edge of the text is adjusted to the top edge of the shape.
        """
        TOP_LEFT: Alignment = ALIGNMENT_TOP_LEFT
        """
        """
        TOP_RIGHT: Alignment = ALIGNMENT_TOP_RIGHT
        """
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class Alignment(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.Alignment", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.Alignment`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['Alignment']
