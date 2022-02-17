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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.sheet import DataPilotTableResultData as UDataPilotTableResultData
        # Dynamically create uno com.sun.star.sheet.DataPilotTableResultData using uno
        global DataPilotTableResultData

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.sheet.DataPilotTableResultData'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.sheet'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.sheet.DataPilotTableResultData'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(FieldFilters = UNO_NONE, DataFieldIndex = UNO_NONE, Result = UNO_NONE):
            ns = 'com.sun.star.sheet.DataPilotTableResultData'
            if isinstance(FieldFilters, UDataPilotTableResultData):
                inst = uno.createUnoStruct(ns, FieldFilters)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not FieldFilters is UNO_NONE:
                if getattr(struct, 'FieldFilters') != FieldFilters:
                    setattr(struct, 'FieldFilters', FieldFilters)
            if not DataFieldIndex is UNO_NONE:
                if getattr(struct, 'DataFieldIndex') != DataFieldIndex:
                    setattr(struct, 'DataFieldIndex', DataFieldIndex)
            if not Result is UNO_NONE:
                if getattr(struct, 'Result') != Result:
                    setattr(struct, 'Result', Result)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        DataPilotTableResultData = _struct_init

    _dynamic_struct()
else:
    from ...lo.sheet.data_pilot_table_result_data import DataPilotTableResultData as DataPilotTableResultData

__all__ = ['DataPilotTableResultData']
