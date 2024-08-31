# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ShadingPattern(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.ShadingPattern", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.ShadingPattern``"""
        pass

    class ShadingPatternEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.ShadingPattern", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.ShadingPattern`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.drawing import ShadingPattern as ShadingPattern
    else:
        # keep document generators happy
        from ...lo.drawing.shading_pattern import ShadingPattern as ShadingPattern

    class ShadingPatternEnum(IntEnum):
        """
        Enum of Const Class ShadingPattern

        The ShadingPattern determines the background color pattern against which characters and graphics are displayed, typically in tables.
        
        The color can be no color or it can be a specific color with a transparency or pattern value.
        """
        CLEAR = ShadingPattern.CLEAR
        SOLID = ShadingPattern.SOLID
        PCT5 = ShadingPattern.PCT5
        PCT10 = ShadingPattern.PCT10
        PCT20 = ShadingPattern.PCT20
        PCT25 = ShadingPattern.PCT25
        PCT30 = ShadingPattern.PCT30
        PCT40 = ShadingPattern.PCT40
        PCT50 = ShadingPattern.PCT50
        PCT60 = ShadingPattern.PCT60
        PCT70 = ShadingPattern.PCT70
        PCT75 = ShadingPattern.PCT75
        PCT80 = ShadingPattern.PCT80
        PCT90 = ShadingPattern.PCT90
        HORZ_STRIPE = ShadingPattern.HORZ_STRIPE
        VERT_STRIPE = ShadingPattern.VERT_STRIPE
        REVERSE_DIAG_STRIPE = ShadingPattern.REVERSE_DIAG_STRIPE
        DIAG_STRIPE = ShadingPattern.DIAG_STRIPE
        HORZ_CROSS = ShadingPattern.HORZ_CROSS
        DIAG_CROSS = ShadingPattern.DIAG_CROSS
        THIN_HORZ_STRIPE = ShadingPattern.THIN_HORZ_STRIPE
        THIN_VERT_STRIPE = ShadingPattern.THIN_VERT_STRIPE
        THIN_REVERSE_DIAG_STRIPE = ShadingPattern.THIN_REVERSE_DIAG_STRIPE
        THIN_DIAG_STRIPE = ShadingPattern.THIN_DIAG_STRIPE
        THIN_HORZ_CROSS = ShadingPattern.THIN_HORZ_CROSS
        THIN_DIAG_CROSS = ShadingPattern.THIN_DIAG_CROSS
        UNUSED_1 = ShadingPattern.UNUSED_1
        UNUSED_2 = ShadingPattern.UNUSED_2
        UNUSED_3 = ShadingPattern.UNUSED_3
        UNUSED_4 = ShadingPattern.UNUSED_4
        UNUSED_5 = ShadingPattern.UNUSED_5
        UNUSED_6 = ShadingPattern.UNUSED_6
        UNUSED_7 = ShadingPattern.UNUSED_7
        UNUSED_8 = ShadingPattern.UNUSED_8
        UNUSED_9 = ShadingPattern.UNUSED_9
        PCT2 = ShadingPattern.PCT2
        PCT7 = ShadingPattern.PCT7
        PCT12 = ShadingPattern.PCT12
        PCT15 = ShadingPattern.PCT15
        PCT17 = ShadingPattern.PCT17
        PCT22 = ShadingPattern.PCT22
        PCT27 = ShadingPattern.PCT27
        PCT32 = ShadingPattern.PCT32
        PCT35 = ShadingPattern.PCT35
        PCT37 = ShadingPattern.PCT37
        PCT42 = ShadingPattern.PCT42
        PCT45 = ShadingPattern.PCT45
        PCT47 = ShadingPattern.PCT47
        PCT52 = ShadingPattern.PCT52
        PCT55 = ShadingPattern.PCT55
        PCT57 = ShadingPattern.PCT57
        PCT62 = ShadingPattern.PCT62
        PCT65 = ShadingPattern.PCT65
        PCT67 = ShadingPattern.PCT67
        PCT72 = ShadingPattern.PCT72
        PCT77 = ShadingPattern.PCT77
        PCT82 = ShadingPattern.PCT82
        PCT85 = ShadingPattern.PCT85
        PCT87 = ShadingPattern.PCT87
        PCT92 = ShadingPattern.PCT92
        PCT95 = ShadingPattern.PCT95
        PCT97 = ShadingPattern.PCT97
        NIL = ShadingPattern.NIL

__all__ = ['ShadingPattern', 'ShadingPatternEnum']
