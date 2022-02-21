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
# Namespace: com.sun.star.presentation
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.presentation import ShapeAnimationSubType as ShapeAnimationSubType
    if hasattr(ShapeAnimationSubType, '_constants') and isinstance(ShapeAnimationSubType._constants, dict):
        ShapeAnimationSubType._constants['__ooo_ns__'] = 'com.sun.star.presentation'
        ShapeAnimationSubType._constants['__ooo_full_ns__'] = 'com.sun.star.presentation.ShapeAnimationSubType'
        ShapeAnimationSubType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ShapeAnimationSubTypeEnum
        ls = [f for f in dir(ShapeAnimationSubType) if not callable(getattr(ShapeAnimationSubType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ShapeAnimationSubType, name)
        ShapeAnimationSubTypeEnum = IntEnum('ShapeAnimationSubTypeEnum', _dict)
    build_enum()
else:
    from ...lo.presentation.shape_animation_sub_type import ShapeAnimationSubType as ShapeAnimationSubType

    class ShapeAnimationSubTypeEnum(IntEnum):
        """
        Enum of Const Class ShapeAnimationSubType

        Defines the whole shape or a subitem as a target for an effect.
        """
        AS_WHOLE = ShapeAnimationSubType.AS_WHOLE
        """
        the whole shape is a target
        """
        ONLY_BACKGROUND = ShapeAnimationSubType.ONLY_BACKGROUND
        """
        only the background is a target.
        
        The Background of a shape is the whole shape except all visible elements that are part of the shapes text.
        """
        ONLY_TEXT = ShapeAnimationSubType.ONLY_TEXT
        """
        only the text is a target.
        
        This includes all glyphs, font decorations and bullets.
        """

__all__ = ['ShapeAnimationSubType', 'ShapeAnimationSubTypeEnum']
