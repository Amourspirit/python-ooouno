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
        def init(self, FamilyType = UNO_NONE, SerifStyle = UNO_NONE, Weight = UNO_NONE, Proportion = UNO_NONE, Contrast = UNO_NONE, StrokeVariation = UNO_NONE, ArmStyle = UNO_NONE, Letterform = UNO_NONE, Midline = UNO_NONE, XHeight = UNO_NONE):
            if getattr(FamilyType, "__class__", None) == self.__class__:
                orig_init(self, FamilyType)
                return
            else:
                orig_init(self)
            if not FamilyType is UNO_NONE:
                if getattr(self, 'FamilyType') != FamilyType:
                    setattr(self, 'FamilyType', FamilyType)
            if not SerifStyle is UNO_NONE:
                if getattr(self, 'SerifStyle') != SerifStyle:
                    setattr(self, 'SerifStyle', SerifStyle)
            if not Weight is UNO_NONE:
                if getattr(self, 'Weight') != Weight:
                    setattr(self, 'Weight', Weight)
            if not Proportion is UNO_NONE:
                if getattr(self, 'Proportion') != Proportion:
                    setattr(self, 'Proportion', Proportion)
            if not Contrast is UNO_NONE:
                if getattr(self, 'Contrast') != Contrast:
                    setattr(self, 'Contrast', Contrast)
            if not StrokeVariation is UNO_NONE:
                if getattr(self, 'StrokeVariation') != StrokeVariation:
                    setattr(self, 'StrokeVariation', StrokeVariation)
            if not ArmStyle is UNO_NONE:
                if getattr(self, 'ArmStyle') != ArmStyle:
                    setattr(self, 'ArmStyle', ArmStyle)
            if not Letterform is UNO_NONE:
                if getattr(self, 'Letterform') != Letterform:
                    setattr(self, 'Letterform', Letterform)
            if not Midline is UNO_NONE:
                if getattr(self, 'Midline') != Midline:
                    setattr(self, 'Midline', Midline)
            if not XHeight is UNO_NONE:
                if getattr(self, 'XHeight') != XHeight:
                    setattr(self, 'XHeight', XHeight)

        type_name = 'com.sun.star.rendering.Panose'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.rendering'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    Panose = _get_class()


else:
    from ...lo.rendering.panose import Panose as Panose

__all__ = ['Panose']

