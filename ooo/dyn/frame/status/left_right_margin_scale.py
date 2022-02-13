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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.frame.status import LeftRightMarginScale as ULeftRightMarginScale
        # Dynamically create uno com.sun.star.frame.status.LeftRightMarginScale using uno
        global LeftRightMarginScale

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.frame.status'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.frame.status.LeftRightMarginScale'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(TextLeft = UNO_NONE, Left = UNO_NONE, Right = UNO_NONE, FirstLine = UNO_NONE, ScaleLeft = UNO_NONE, ScaleRight = UNO_NONE, ScaleFirstLine = UNO_NONE, AutoFirstLine = UNO_NONE):
            ns = 'com.sun.star.frame.status.LeftRightMarginScale'
            if isinstance(TextLeft, ULeftRightMarginScale):
                inst = uno.createUnoStruct(ns, TextLeft)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not TextLeft is UNO_NONE:
                if getattr(struct, 'TextLeft') != TextLeft:
                    setattr(struct, 'TextLeft', TextLeft)
            if not Left is UNO_NONE:
                if getattr(struct, 'Left') != Left:
                    setattr(struct, 'Left', Left)
            if not Right is UNO_NONE:
                if getattr(struct, 'Right') != Right:
                    setattr(struct, 'Right', Right)
            if not FirstLine is UNO_NONE:
                if getattr(struct, 'FirstLine') != FirstLine:
                    setattr(struct, 'FirstLine', FirstLine)
            if not ScaleLeft is UNO_NONE:
                if getattr(struct, 'ScaleLeft') != ScaleLeft:
                    setattr(struct, 'ScaleLeft', ScaleLeft)
            if not ScaleRight is UNO_NONE:
                if getattr(struct, 'ScaleRight') != ScaleRight:
                    setattr(struct, 'ScaleRight', ScaleRight)
            if not ScaleFirstLine is UNO_NONE:
                if getattr(struct, 'ScaleFirstLine') != ScaleFirstLine:
                    setattr(struct, 'ScaleFirstLine', ScaleFirstLine)
            if not AutoFirstLine is UNO_NONE:
                if getattr(struct, 'AutoFirstLine') != AutoFirstLine:
                    setattr(struct, 'AutoFirstLine', AutoFirstLine)
            _set_attr(struct)
            return struct
        LeftRightMarginScale = _struct_init

    _dynamic_struct()
else:
    from ....lo.frame.status.left_right_margin_scale import LeftRightMarginScale as LeftRightMarginScale

__all__ = ['LeftRightMarginScale']

