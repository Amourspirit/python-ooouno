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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, AffineTransform = UNO_NONE, Alpha = UNO_NONE, NumberOfHatchPolygons = UNO_NONE, Bitmap = UNO_NONE, Gradient = UNO_NONE, Hatching = UNO_NONE, HatchAttributes = UNO_NONE, RepeatModeX = UNO_NONE, RepeatModeY = UNO_NONE):
            if getattr(AffineTransform, "__class__", None) == self.__class__:
                orig_init(self, AffineTransform)
                return
            else:
                orig_init(self)
            if not AffineTransform is UNO_NONE:
                if getattr(self, 'AffineTransform') != AffineTransform:
                    setattr(self, 'AffineTransform', AffineTransform)
            if not Alpha is UNO_NONE:
                if getattr(self, 'Alpha') != Alpha:
                    setattr(self, 'Alpha', Alpha)
            if not NumberOfHatchPolygons is UNO_NONE:
                if getattr(self, 'NumberOfHatchPolygons') != NumberOfHatchPolygons:
                    setattr(self, 'NumberOfHatchPolygons', NumberOfHatchPolygons)
            if not Bitmap is UNO_NONE:
                if getattr(self, 'Bitmap') != Bitmap:
                    setattr(self, 'Bitmap', Bitmap)
            if not Gradient is UNO_NONE:
                if getattr(self, 'Gradient') != Gradient:
                    setattr(self, 'Gradient', Gradient)
            if not Hatching is UNO_NONE:
                if getattr(self, 'Hatching') != Hatching:
                    setattr(self, 'Hatching', Hatching)
            if not HatchAttributes is UNO_NONE:
                if getattr(self, 'HatchAttributes') != HatchAttributes:
                    setattr(self, 'HatchAttributes', HatchAttributes)
            if not RepeatModeX is UNO_NONE:
                if getattr(self, 'RepeatModeX') != RepeatModeX:
                    setattr(self, 'RepeatModeX', RepeatModeX)
            if not RepeatModeY is UNO_NONE:
                if getattr(self, 'RepeatModeY') != RepeatModeY:
                    setattr(self, 'RepeatModeY', RepeatModeY)

        type_name = 'com.sun.star.rendering.Texture'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.rendering'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    Texture = _get_class()


else:
    from ...lo.rendering.texture import Texture as Texture

__all__ = ['Texture']

