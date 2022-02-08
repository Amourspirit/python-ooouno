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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import TextDirection
else:
    from ...lo.rendering.text_direction import TextDirection as TextDirection


class TextDirectionEnum(IntEnum):
    """
    Enum of Const Class TextDirection

    Specifies main text direction in a text portion.
    
    This also changes the interpretation of the start point.
    
    **since**
    
        OOo 2.0
    """
    WEAK_LEFT_TO_RIGHT = TextDirection.WEAK_LEFT_TO_RIGHT
    """
    Reference point is left, main direction is from left to right.
    """
    STRONG_LEFT_TO_RIGHT = TextDirection.STRONG_LEFT_TO_RIGHT
    """
    Reference point is left, main direction is from left to right.
    """
    WEAK_RIGHT_TO_LEFT = TextDirection.WEAK_RIGHT_TO_LEFT
    """
    Reference point is right, main direction is from right to left.
    """
    STRONG_RIGHT_TO_LEFT = TextDirection.STRONG_RIGHT_TO_LEFT
    """
    Reference point is right, main direction is from right to left.
    """

__all__ = ['TextDirection', 'TextDirectionEnum']
