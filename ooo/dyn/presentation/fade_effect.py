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
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.presentation.FadeEffect import (CLOCKWISE, CLOSE_HORIZONTAL, CLOSE_VERTICAL, COUNTERCLOCKWISE, DISSOLVE, FADE_FROM_BOTTOM, FADE_FROM_CENTER, FADE_FROM_LEFT, FADE_FROM_LOWERLEFT, FADE_FROM_LOWERRIGHT, FADE_FROM_RIGHT, FADE_FROM_TOP, FADE_FROM_UPPERLEFT, FADE_FROM_UPPERRIGHT, FADE_TO_CENTER, HORIZONTAL_CHECKERBOARD, HORIZONTAL_LINES, HORIZONTAL_STRIPES, MOVE_FROM_BOTTOM, MOVE_FROM_LEFT, MOVE_FROM_LOWERLEFT, MOVE_FROM_LOWERRIGHT, MOVE_FROM_RIGHT, MOVE_FROM_TOP, MOVE_FROM_UPPERLEFT, MOVE_FROM_UPPERRIGHT, NONE, OPEN_HORIZONTAL, OPEN_VERTICAL, RANDOM, ROLL_FROM_BOTTOM, ROLL_FROM_LEFT, ROLL_FROM_RIGHT, ROLL_FROM_TOP, SPIRALIN_LEFT, SPIRALIN_RIGHT, SPIRALOUT_LEFT, SPIRALOUT_RIGHT, STRETCH_FROM_BOTTOM, STRETCH_FROM_LEFT, STRETCH_FROM_RIGHT, STRETCH_FROM_TOP, UNCOVER_TO_BOTTOM, UNCOVER_TO_LEFT, UNCOVER_TO_LOWERLEFT, UNCOVER_TO_LOWERRIGHT, UNCOVER_TO_RIGHT, UNCOVER_TO_TOP, UNCOVER_TO_UPPERLEFT, UNCOVER_TO_UPPERRIGHT, VERTICAL_CHECKERBOARD, VERTICAL_LINES, VERTICAL_STRIPES, WAVYLINE_FROM_BOTTOM, WAVYLINE_FROM_LEFT, WAVYLINE_FROM_RIGHT, WAVYLINE_FROM_TOP)

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global FadeEffect
        _dict = {
            "CLOCKWISE": CLOCKWISE,
            "CLOSE_HORIZONTAL": CLOSE_HORIZONTAL,
            "CLOSE_VERTICAL": CLOSE_VERTICAL,
            "COUNTERCLOCKWISE": COUNTERCLOCKWISE,
            "DISSOLVE": DISSOLVE,
            "FADE_FROM_BOTTOM": FADE_FROM_BOTTOM,
            "FADE_FROM_CENTER": FADE_FROM_CENTER,
            "FADE_FROM_LEFT": FADE_FROM_LEFT,
            "FADE_FROM_LOWERLEFT": FADE_FROM_LOWERLEFT,
            "FADE_FROM_LOWERRIGHT": FADE_FROM_LOWERRIGHT,
            "FADE_FROM_RIGHT": FADE_FROM_RIGHT,
            "FADE_FROM_TOP": FADE_FROM_TOP,
            "FADE_FROM_UPPERLEFT": FADE_FROM_UPPERLEFT,
            "FADE_FROM_UPPERRIGHT": FADE_FROM_UPPERRIGHT,
            "FADE_TO_CENTER": FADE_TO_CENTER,
            "HORIZONTAL_CHECKERBOARD": HORIZONTAL_CHECKERBOARD,
            "HORIZONTAL_LINES": HORIZONTAL_LINES,
            "HORIZONTAL_STRIPES": HORIZONTAL_STRIPES,
            "MOVE_FROM_BOTTOM": MOVE_FROM_BOTTOM,
            "MOVE_FROM_LEFT": MOVE_FROM_LEFT,
            "MOVE_FROM_LOWERLEFT": MOVE_FROM_LOWERLEFT,
            "MOVE_FROM_LOWERRIGHT": MOVE_FROM_LOWERRIGHT,
            "MOVE_FROM_RIGHT": MOVE_FROM_RIGHT,
            "MOVE_FROM_TOP": MOVE_FROM_TOP,
            "MOVE_FROM_UPPERLEFT": MOVE_FROM_UPPERLEFT,
            "MOVE_FROM_UPPERRIGHT": MOVE_FROM_UPPERRIGHT,
            "NONE": NONE,
            "OPEN_HORIZONTAL": OPEN_HORIZONTAL,
            "OPEN_VERTICAL": OPEN_VERTICAL,
            "RANDOM": RANDOM,
            "ROLL_FROM_BOTTOM": ROLL_FROM_BOTTOM,
            "ROLL_FROM_LEFT": ROLL_FROM_LEFT,
            "ROLL_FROM_RIGHT": ROLL_FROM_RIGHT,
            "ROLL_FROM_TOP": ROLL_FROM_TOP,
            "SPIRALIN_LEFT": SPIRALIN_LEFT,
            "SPIRALIN_RIGHT": SPIRALIN_RIGHT,
            "SPIRALOUT_LEFT": SPIRALOUT_LEFT,
            "SPIRALOUT_RIGHT": SPIRALOUT_RIGHT,
            "STRETCH_FROM_BOTTOM": STRETCH_FROM_BOTTOM,
            "STRETCH_FROM_LEFT": STRETCH_FROM_LEFT,
            "STRETCH_FROM_RIGHT": STRETCH_FROM_RIGHT,
            "STRETCH_FROM_TOP": STRETCH_FROM_TOP,
            "UNCOVER_TO_BOTTOM": UNCOVER_TO_BOTTOM,
            "UNCOVER_TO_LEFT": UNCOVER_TO_LEFT,
            "UNCOVER_TO_LOWERLEFT": UNCOVER_TO_LOWERLEFT,
            "UNCOVER_TO_LOWERRIGHT": UNCOVER_TO_LOWERRIGHT,
            "UNCOVER_TO_RIGHT": UNCOVER_TO_RIGHT,
            "UNCOVER_TO_TOP": UNCOVER_TO_TOP,
            "UNCOVER_TO_UPPERLEFT": UNCOVER_TO_UPPERLEFT,
            "UNCOVER_TO_UPPERRIGHT": UNCOVER_TO_UPPERRIGHT,
            "VERTICAL_CHECKERBOARD": VERTICAL_CHECKERBOARD,
            "VERTICAL_LINES": VERTICAL_LINES,
            "VERTICAL_STRIPES": VERTICAL_STRIPES,
            "WAVYLINE_FROM_BOTTOM": WAVYLINE_FROM_BOTTOM,
            "WAVYLINE_FROM_LEFT": WAVYLINE_FROM_LEFT,
            "WAVYLINE_FROM_RIGHT": WAVYLINE_FROM_RIGHT,
            "WAVYLINE_FROM_TOP": WAVYLINE_FROM_TOP,
        }

        FadeEffect = type('FadeEffect', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(FadeEffect, k, v)
        setattr(FadeEffect, '__ooo_ns__', 'com.sun.star.presentation')
        setattr(FadeEffect, '__ooo_full_ns__', 'com.sun.star.presentation.FadeEffect')
        setattr(FadeEffect, '__ooo_type_name__', 'enum')
    _dynamic_enum()
else:
    from ...lo.presentation.fade_effect import FadeEffect as FadeEffect

__all__ = ['FadeEffect']

