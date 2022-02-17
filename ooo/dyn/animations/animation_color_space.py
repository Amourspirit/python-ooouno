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
# Namespace: com.sun.star.animations
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.animations import AnimationColorSpace as AnimationColorSpace
else:
    from ...lo.animations.animation_color_space import AnimationColorSpace as AnimationColorSpace


class AnimationColorSpaceEnum(IntEnum):
    """
    Enum of Const Class AnimationColorSpace

    defines the color space that is used for interpolation.
    
    This does not change how colors are interpreted but how to interpolate from one color to another.
    """
    RGB = AnimationColorSpace.RGB
    """
    defines that the RGB color space is used for interpolation.
    """
    HSL = AnimationColorSpace.HSL
    """
    defines that the HSL color space is used for interpolation.
    """

__all__ = ['AnimationColorSpace', 'AnimationColorSpaceEnum']