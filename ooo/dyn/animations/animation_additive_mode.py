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
from ...lo.animations.animation_additive_mode import AnimationAdditiveMode as AnimationAdditiveMode


class AnimationAdditiveModeEnum(IntEnum):
    """
    Enum of Const Class AnimationAdditiveMode

    Specifies the additive mode for the animation.
    """
    BASE = AnimationAdditiveMode.BASE
    SUM = AnimationAdditiveMode.SUM
    REPLACE = AnimationAdditiveMode.REPLACE
    MULTIPLY = AnimationAdditiveMode.MULTIPLY
    NONE = AnimationAdditiveMode.NONE

__all__ = ['AnimationAdditiveMode', 'AnimationAdditiveModeEnum']
