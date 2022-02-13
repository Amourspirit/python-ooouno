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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.util import Date as UDate
        # Dynamically create uno com.sun.star.util.Date using uno
        global Date

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.util'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.util.Date'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Day = UNO_NONE, Month = UNO_NONE, Year = UNO_NONE):
            ns = 'com.sun.star.util.Date'
            if isinstance(Day, UDate):
                inst = uno.createUnoStruct(ns, Day)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Day is UNO_NONE:
                if getattr(struct, 'Day') != Day:
                    setattr(struct, 'Day', Day)
            if not Month is UNO_NONE:
                if getattr(struct, 'Month') != Month:
                    setattr(struct, 'Month', Month)
            if not Year is UNO_NONE:
                if getattr(struct, 'Year') != Year:
                    setattr(struct, 'Year', Year)
            _set_attr(struct)
            return struct
        Date = _struct_init

    _dynamic_struct()
else:
    from ...lo.util.date import Date as Date

__all__ = ['Date']

