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
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class MeasureTextHorzPos(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.MeasureTextHorzPos", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.MeasureTextHorzPos`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.drawing.MeasureTextHorzPos import AUTO as MEASURE_TEXT_HORZ_POS_AUTO
        from com.sun.star.drawing.MeasureTextHorzPos import INSIDE as MEASURE_TEXT_HORZ_POS_INSIDE
        from com.sun.star.drawing.MeasureTextHorzPos import LEFTOUTSIDE as MEASURE_TEXT_HORZ_POS_LEFTOUTSIDE
        from com.sun.star.drawing.MeasureTextHorzPos import RIGHTOUTSIDE as MEASURE_TEXT_HORZ_POS_RIGHTOUTSIDE

        class MeasureTextHorzPos(uno.Enum):
            """
            Enum Class


            See Also:
                `API MeasureTextHorzPos <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a38140d53071a431128aa968be9ce4b7d>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.drawing.MeasureTextHorzPos', value)

            __ooo_ns__: str = 'com.sun.star.drawing'
            __ooo_full_ns__: str = 'com.sun.star.drawing.MeasureTextHorzPos'
            __ooo_type_name__: str = 'enum'

            AUTO = MEASURE_TEXT_HORZ_POS_AUTO
            """
            the connection point is chosen automatically,

            Set this to have the application select the best horizontal position for the text.
            """
            INSIDE = MEASURE_TEXT_HORZ_POS_INSIDE
            """
            """
            LEFTOUTSIDE = MEASURE_TEXT_HORZ_POS_LEFTOUTSIDE
            """
            """
            RIGHTOUTSIDE = MEASURE_TEXT_HORZ_POS_RIGHTOUTSIDE
            """
            """
    else:
        # keep document generators happy
        from ...lo.drawing.measure_text_horz_pos import MeasureTextHorzPos as MeasureTextHorzPos


__all__ = ['MeasureTextHorzPos']
