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
# Namespace: com.sun.star.awt.grid
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.awt.grid import GridColumnEvent as UGridColumnEvent
        # Dynamically create uno com.sun.star.awt.grid.GridColumnEvent using uno
        global GridColumnEvent

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.awt.grid'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.awt.grid.GridColumnEvent'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(AttributeName = UNO_NONE, OldValue = UNO_NONE, NewValue = UNO_NONE, ColumnIndex = UNO_NONE, **kwargs):
            ns = 'com.sun.star.awt.grid.GridColumnEvent'
            if isinstance(AttributeName, UGridColumnEvent):
                inst = uno.createUnoStruct(ns, AttributeName)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not AttributeName is UNO_NONE:
                if getattr(struct, 'AttributeName') != AttributeName:
                    setattr(struct, 'AttributeName', AttributeName)
            if not OldValue is UNO_NONE:
                if getattr(struct, 'OldValue') != OldValue:
                    setattr(struct, 'OldValue', OldValue)
            if not NewValue is UNO_NONE:
                if getattr(struct, 'NewValue') != NewValue:
                    setattr(struct, 'NewValue', NewValue)
            if not ColumnIndex is UNO_NONE:
                if getattr(struct, 'ColumnIndex') != ColumnIndex:
                    setattr(struct, 'ColumnIndex', ColumnIndex)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(ex, k, v)
            _set_attr(struct)
            return struct
        GridColumnEvent = _struct_init

    _dynamic_struct()
else:
    from ....lo.awt.grid.grid_column_event import GridColumnEvent as GridColumnEvent

__all__ = ['GridColumnEvent']

