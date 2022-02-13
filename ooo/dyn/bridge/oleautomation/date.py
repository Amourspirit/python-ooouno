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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.bridge.oleautomation import Date as UDate
        # Dynamically create uno com.sun.star.bridge.oleautomation.Date using uno
        global Date

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.bridge.oleautomation'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.bridge.oleautomation.Date'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Value = UNO_NONE):
            ns = 'com.sun.star.bridge.oleautomation.Date'
            if isinstance(Value, UDate):
                inst = uno.createUnoStruct(ns, Value)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Value is UNO_NONE:
                if getattr(struct, 'Value') != Value:
                    setattr(struct, 'Value', Value)
            _set_attr(struct)
            return struct
        Date = _struct_init

    _dynamic_struct()
else:
    from ....lo.bridge.oleautomation.date import Date as Date

__all__ = ['Date']

