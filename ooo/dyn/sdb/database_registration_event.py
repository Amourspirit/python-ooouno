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
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.sdb import DatabaseRegistrationEvent as UDatabaseRegistrationEvent
        # Dynamically create uno com.sun.star.sdb.DatabaseRegistrationEvent using uno
        global DatabaseRegistrationEvent

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.sdb.DatabaseRegistrationEvent'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.sdb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.sdb.DatabaseRegistrationEvent'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Name = UNO_NONE, OldLocation = UNO_NONE, NewLocation = UNO_NONE, **kwargs):
            ns = 'com.sun.star.sdb.DatabaseRegistrationEvent'
            if isinstance(Name, UDatabaseRegistrationEvent):
                inst = uno.createUnoStruct(ns, Name)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Name is UNO_NONE:
                if getattr(struct, 'Name') != Name:
                    setattr(struct, 'Name', Name)
            if not OldLocation is UNO_NONE:
                if getattr(struct, 'OldLocation') != OldLocation:
                    setattr(struct, 'OldLocation', OldLocation)
            if not NewLocation is UNO_NONE:
                if getattr(struct, 'NewLocation') != NewLocation:
                    setattr(struct, 'NewLocation', NewLocation)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(ex, k, v)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        DatabaseRegistrationEvent = _struct_init

    _dynamic_struct()
else:
    from ...lo.sdb.database_registration_event import DatabaseRegistrationEvent as DatabaseRegistrationEvent

__all__ = ['DatabaseRegistrationEvent']

