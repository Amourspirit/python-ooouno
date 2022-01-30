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
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.drawing.Alignment import (BOTTOM, BOTTOM_LEFT, BOTTOM_RIGHT, CENTER, LEFT, RIGHT, TOP, TOP_LEFT, TOP_RIGHT)

if TYPE_CHECKING or _DYNAMIC is False:


    class Alignment(Enum):
        """
        Enum Class

        

        See Also:
            `API Alignment <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#acdfaca60ec19c0265bac2692d7982726>`_
        """
        BOTTOM = 'BOTTOM'
        """
        the connection line leaves the connected object from the bottom,
        
        The text is positioned below the main line.
        
        The bottom edge of the text is adjusted to the bottom edge of the shape.
        """
        BOTTOM_LEFT = 'BOTTOM_LEFT'
        """
        """
        BOTTOM_RIGHT = 'BOTTOM_RIGHT'
        """
        """
        CENTER = 'CENTER'
        """
        The text is centered inside the shape.
        """
        LEFT = 'LEFT'
        """
        the connection line leaves the connected object to the left,
        
        The left edge of the text is adjusted to the left edge of the shape.
        
        The text is positioned to the left.
        """
        RIGHT = 'RIGHT'
        """
        the connection line leaves the connected object to the right,
        
        The right edge of the text is adjusted to the right edge of the shape.
        
        The text is positioned to the right.
        """
        TOP = 'TOP'
        """
        the connection line leaves the connected object from the top,
        
        The text is positioned above the main line.
        
        The top edge of the text is adjusted to the top edge of the shape.
        """
        TOP_LEFT = 'TOP_LEFT'
        """
        """
        TOP_RIGHT = 'TOP_RIGHT'
        """
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global Alignment
        _dict = {
            "BOTTOM": BOTTOM,
            "BOTTOM_LEFT": BOTTOM_LEFT,
            "BOTTOM_RIGHT": BOTTOM_RIGHT,
            "CENTER": CENTER,
            "LEFT": LEFT,
            "RIGHT": RIGHT,
            "TOP": TOP,
            "TOP_LEFT": TOP_LEFT,
            "TOP_RIGHT": TOP_RIGHT,
        }

        Alignment = type('Alignment', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(Alignment, k, v)

    _dynamic_enum()

__all__ = ['Alignment']

