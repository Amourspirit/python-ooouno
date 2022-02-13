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
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.rendering import FloatingPointBitmapLayout as UFloatingPointBitmapLayout
        # Dynamically create uno com.sun.star.rendering.FloatingPointBitmapLayout using uno
        global FloatingPointBitmapLayout

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.rendering.FloatingPointBitmapLayout'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.rendering'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.rendering.FloatingPointBitmapLayout'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(ScanLines = UNO_NONE, ScanLineBytes = UNO_NONE, ScanLineStride = UNO_NONE, PlaneStride = UNO_NONE, ColorSpace = UNO_NONE, NumComponents = UNO_NONE, Endianness = UNO_NONE, Format = UNO_NONE):
            ns = 'com.sun.star.rendering.FloatingPointBitmapLayout'
            if isinstance(ScanLines, UFloatingPointBitmapLayout):
                inst = uno.createUnoStruct(ns, ScanLines)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not ScanLines is UNO_NONE:
                if getattr(struct, 'ScanLines') != ScanLines:
                    setattr(struct, 'ScanLines', ScanLines)
            if not ScanLineBytes is UNO_NONE:
                if getattr(struct, 'ScanLineBytes') != ScanLineBytes:
                    setattr(struct, 'ScanLineBytes', ScanLineBytes)
            if not ScanLineStride is UNO_NONE:
                if getattr(struct, 'ScanLineStride') != ScanLineStride:
                    setattr(struct, 'ScanLineStride', ScanLineStride)
            if not PlaneStride is UNO_NONE:
                if getattr(struct, 'PlaneStride') != PlaneStride:
                    setattr(struct, 'PlaneStride', PlaneStride)
            if not ColorSpace is UNO_NONE:
                if getattr(struct, 'ColorSpace') != ColorSpace:
                    setattr(struct, 'ColorSpace', ColorSpace)
            if not NumComponents is UNO_NONE:
                if getattr(struct, 'NumComponents') != NumComponents:
                    setattr(struct, 'NumComponents', NumComponents)
            if not Endianness is UNO_NONE:
                if getattr(struct, 'Endianness') != Endianness:
                    setattr(struct, 'Endianness', Endianness)
            if not Format is UNO_NONE:
                if getattr(struct, 'Format') != Format:
                    setattr(struct, 'Format', Format)
            _set_attr(struct)
            _set_fn_attr(struct)
            return struct
        _set_attr(_struct_init)
        FloatingPointBitmapLayout = _struct_init

    _dynamic_struct()
else:
    from ...lo.rendering.floating_point_bitmap_layout import FloatingPointBitmapLayout as FloatingPointBitmapLayout

__all__ = ['FloatingPointBitmapLayout']

