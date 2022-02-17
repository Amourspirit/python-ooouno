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
# Namespace: com.sun.star.table
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.table import TableBorder as UTableBorder
        # Dynamically create uno com.sun.star.table.TableBorder using uno
        global TableBorder

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.table.TableBorder'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.table'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.table.TableBorder'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(TopLine = UNO_NONE, IsTopLineValid = UNO_NONE, BottomLine = UNO_NONE, IsBottomLineValid = UNO_NONE, LeftLine = UNO_NONE, IsLeftLineValid = UNO_NONE, RightLine = UNO_NONE, IsRightLineValid = UNO_NONE, HorizontalLine = UNO_NONE, IsHorizontalLineValid = UNO_NONE, VerticalLine = UNO_NONE, IsVerticalLineValid = UNO_NONE, Distance = UNO_NONE, IsDistanceValid = UNO_NONE):
            ns = 'com.sun.star.table.TableBorder'
            if isinstance(TopLine, UTableBorder):
                inst = uno.createUnoStruct(ns, TopLine)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not TopLine is UNO_NONE:
                if getattr(struct, 'TopLine') != TopLine:
                    setattr(struct, 'TopLine', TopLine)
            if not IsTopLineValid is UNO_NONE:
                if getattr(struct, 'IsTopLineValid') != IsTopLineValid:
                    setattr(struct, 'IsTopLineValid', IsTopLineValid)
            if not BottomLine is UNO_NONE:
                if getattr(struct, 'BottomLine') != BottomLine:
                    setattr(struct, 'BottomLine', BottomLine)
            if not IsBottomLineValid is UNO_NONE:
                if getattr(struct, 'IsBottomLineValid') != IsBottomLineValid:
                    setattr(struct, 'IsBottomLineValid', IsBottomLineValid)
            if not LeftLine is UNO_NONE:
                if getattr(struct, 'LeftLine') != LeftLine:
                    setattr(struct, 'LeftLine', LeftLine)
            if not IsLeftLineValid is UNO_NONE:
                if getattr(struct, 'IsLeftLineValid') != IsLeftLineValid:
                    setattr(struct, 'IsLeftLineValid', IsLeftLineValid)
            if not RightLine is UNO_NONE:
                if getattr(struct, 'RightLine') != RightLine:
                    setattr(struct, 'RightLine', RightLine)
            if not IsRightLineValid is UNO_NONE:
                if getattr(struct, 'IsRightLineValid') != IsRightLineValid:
                    setattr(struct, 'IsRightLineValid', IsRightLineValid)
            if not HorizontalLine is UNO_NONE:
                if getattr(struct, 'HorizontalLine') != HorizontalLine:
                    setattr(struct, 'HorizontalLine', HorizontalLine)
            if not IsHorizontalLineValid is UNO_NONE:
                if getattr(struct, 'IsHorizontalLineValid') != IsHorizontalLineValid:
                    setattr(struct, 'IsHorizontalLineValid', IsHorizontalLineValid)
            if not VerticalLine is UNO_NONE:
                if getattr(struct, 'VerticalLine') != VerticalLine:
                    setattr(struct, 'VerticalLine', VerticalLine)
            if not IsVerticalLineValid is UNO_NONE:
                if getattr(struct, 'IsVerticalLineValid') != IsVerticalLineValid:
                    setattr(struct, 'IsVerticalLineValid', IsVerticalLineValid)
            if not Distance is UNO_NONE:
                if getattr(struct, 'Distance') != Distance:
                    setattr(struct, 'Distance', Distance)
            if not IsDistanceValid is UNO_NONE:
                if getattr(struct, 'IsDistanceValid') != IsDistanceValid:
                    setattr(struct, 'IsDistanceValid', IsDistanceValid)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        TableBorder = _struct_init

    _dynamic_struct()
else:
    from ...lo.table.table_border import TableBorder as TableBorder

__all__ = ['TableBorder']

