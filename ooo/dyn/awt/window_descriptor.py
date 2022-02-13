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
        from com.sun.star.awt import WindowDescriptor as UWindowDescriptor
        # Dynamically create uno com.sun.star.awt.WindowDescriptor using uno
        global WindowDescriptor

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.awt.WindowDescriptor'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.awt'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.awt.WindowDescriptor'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Type = UNO_NONE, WindowServiceName = UNO_NONE, Parent = UNO_NONE, ParentIndex = UNO_NONE, Bounds = UNO_NONE, WindowAttributes = UNO_NONE):
            ns = 'com.sun.star.awt.WindowDescriptor'
            if isinstance(Type, UWindowDescriptor):
                inst = uno.createUnoStruct(ns, Type)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Type is UNO_NONE:
                if getattr(struct, 'Type') != Type:
                    setattr(struct, 'Type', Type)
            if not WindowServiceName is UNO_NONE:
                if getattr(struct, 'WindowServiceName') != WindowServiceName:
                    setattr(struct, 'WindowServiceName', WindowServiceName)
            if not Parent is UNO_NONE:
                if getattr(struct, 'Parent') != Parent:
                    setattr(struct, 'Parent', Parent)
            if not ParentIndex is UNO_NONE:
                if getattr(struct, 'ParentIndex') != ParentIndex:
                    setattr(struct, 'ParentIndex', ParentIndex)
            if not Bounds is UNO_NONE:
                if getattr(struct, 'Bounds') != Bounds:
                    setattr(struct, 'Bounds', Bounds)
            if not WindowAttributes is UNO_NONE:
                if getattr(struct, 'WindowAttributes') != WindowAttributes:
                    setattr(struct, 'WindowAttributes', WindowAttributes)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        WindowDescriptor = _struct_init

    _dynamic_struct()
else:
    from ...lo.awt.window_descriptor import WindowDescriptor as WindowDescriptor

__all__ = ['WindowDescriptor']

