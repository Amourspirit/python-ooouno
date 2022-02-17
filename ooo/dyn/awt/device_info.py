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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.awt import DeviceInfo as UDeviceInfo
        # Dynamically create uno com.sun.star.awt.DeviceInfo using uno
        global DeviceInfo

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.awt.DeviceInfo'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.awt'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.awt.DeviceInfo'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Width = UNO_NONE, Height = UNO_NONE, LeftInset = UNO_NONE, TopInset = UNO_NONE, RightInset = UNO_NONE, BottomInset = UNO_NONE, PixelPerMeterX = UNO_NONE, PixelPerMeterY = UNO_NONE, BitsPerPixel = UNO_NONE, Capabilities = UNO_NONE):
            ns = 'com.sun.star.awt.DeviceInfo'
            if isinstance(Width, UDeviceInfo):
                inst = uno.createUnoStruct(ns, Width)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Width is UNO_NONE:
                if getattr(struct, 'Width') != Width:
                    setattr(struct, 'Width', Width)
            if not Height is UNO_NONE:
                if getattr(struct, 'Height') != Height:
                    setattr(struct, 'Height', Height)
            if not LeftInset is UNO_NONE:
                if getattr(struct, 'LeftInset') != LeftInset:
                    setattr(struct, 'LeftInset', LeftInset)
            if not TopInset is UNO_NONE:
                if getattr(struct, 'TopInset') != TopInset:
                    setattr(struct, 'TopInset', TopInset)
            if not RightInset is UNO_NONE:
                if getattr(struct, 'RightInset') != RightInset:
                    setattr(struct, 'RightInset', RightInset)
            if not BottomInset is UNO_NONE:
                if getattr(struct, 'BottomInset') != BottomInset:
                    setattr(struct, 'BottomInset', BottomInset)
            if not PixelPerMeterX is UNO_NONE:
                if getattr(struct, 'PixelPerMeterX') != PixelPerMeterX:
                    setattr(struct, 'PixelPerMeterX', PixelPerMeterX)
            if not PixelPerMeterY is UNO_NONE:
                if getattr(struct, 'PixelPerMeterY') != PixelPerMeterY:
                    setattr(struct, 'PixelPerMeterY', PixelPerMeterY)
            if not BitsPerPixel is UNO_NONE:
                if getattr(struct, 'BitsPerPixel') != BitsPerPixel:
                    setattr(struct, 'BitsPerPixel', BitsPerPixel)
            if not Capabilities is UNO_NONE:
                if getattr(struct, 'Capabilities') != Capabilities:
                    setattr(struct, 'Capabilities', Capabilities)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        DeviceInfo = _struct_init

    _dynamic_struct()
else:
    from ...lo.awt.device_info import DeviceInfo as DeviceInfo

__all__ = ['DeviceInfo']
