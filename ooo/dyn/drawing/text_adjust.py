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

    from com.sun.star.drawing.TextAdjust import BLOCK as TEXT_ADJUST_BLOCK
    from com.sun.star.drawing.TextAdjust import CENTER as TEXT_ADJUST_CENTER
    from com.sun.star.drawing.TextAdjust import LEFT as TEXT_ADJUST_LEFT
    from com.sun.star.drawing.TextAdjust import RIGHT as TEXT_ADJUST_RIGHT
    from com.sun.star.drawing.TextAdjust import STRETCH as TEXT_ADJUST_STRETCH

    class TextAdjust(uno.Enum):
        """
        Enum Class


        See Also:
            `API TextAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adf031187199b98bb1b6581c7e69d4810>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.TextAdjust', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.TextAdjust'
        __ooo_type_name__: str = 'enum'

        BLOCK: TextAdjust = TEXT_ADJUST_BLOCK
        """
        The text extends from the left to the right edge of the shape.
        
        The text extends from the top to the bottom edge of the shape.
        """
        CENTER: TextAdjust = TEXT_ADJUST_CENTER
        """
        The text is centered inside the shape.
        """
        LEFT: TextAdjust = TEXT_ADJUST_LEFT
        """
        the connection line leaves the connected object to the left,
        
        The left edge of the text is adjusted to the left edge of the shape.
        
        The text is positioned to the left.
        """
        RIGHT: TextAdjust = TEXT_ADJUST_RIGHT
        """
        the connection line leaves the connected object to the right,
        
        The right edge of the text is adjusted to the right edge of the shape.
        
        The text is positioned to the right.
        """
        STRETCH: TextAdjust = TEXT_ADJUST_STRETCH
        """
        the bitmap is stretched to fill the area.
        
        The text is stretched so that the longest line goes from the left to the right edge of the shape.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TextAdjust(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.TextAdjust", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.TextAdjust`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TextAdjust']
