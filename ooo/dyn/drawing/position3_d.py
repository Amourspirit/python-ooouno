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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.drawing import Position3D as UPosition3D
        # Dynamically create uno com.sun.star.drawing.Position3D using uno
        global Position3D

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.drawing'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.drawing.Position3D'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(PositionX = UNO_NONE, PositionY = UNO_NONE, PositionZ = UNO_NONE):
            ns = 'com.sun.star.drawing.Position3D'
            if isinstance(PositionX, UPosition3D):
                inst = uno.createUnoStruct(ns, PositionX)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not PositionX is UNO_NONE:
                if getattr(struct, 'PositionX') != PositionX:
                    setattr(struct, 'PositionX', PositionX)
            if not PositionY is UNO_NONE:
                if getattr(struct, 'PositionY') != PositionY:
                    setattr(struct, 'PositionY', PositionY)
            if not PositionZ is UNO_NONE:
                if getattr(struct, 'PositionZ') != PositionZ:
                    setattr(struct, 'PositionZ', PositionZ)
            _set_attr(struct)
            return struct
        Position3D = _struct_init

    _dynamic_struct()
else:
    from ...lo.drawing.position3_d import Position3D as Position3D

__all__ = ['Position3D']

