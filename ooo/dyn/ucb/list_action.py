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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.ucb import ListAction as UListAction
        # Dynamically create uno com.sun.star.ucb.ListAction using uno
        global ListAction

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.ListAction'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Position = UNO_NONE, Count = UNO_NONE, ListActionType = UNO_NONE, ActionInfo = UNO_NONE):
            ns = 'com.sun.star.ucb.ListAction'
            if isinstance(Position, UListAction):
                inst = uno.createUnoStruct(ns, Position)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Position is UNO_NONE:
                if getattr(struct, 'Position') != Position:
                    setattr(struct, 'Position', Position)
            if not Count is UNO_NONE:
                if getattr(struct, 'Count') != Count:
                    setattr(struct, 'Count', Count)
            if not ListActionType is UNO_NONE:
                if getattr(struct, 'ListActionType') != ListActionType:
                    setattr(struct, 'ListActionType', ListActionType)
            if not ActionInfo is UNO_NONE:
                if getattr(struct, 'ActionInfo') != ActionInfo:
                    setattr(struct, 'ActionInfo', ActionInfo)
            _set_attr(struct)
            return struct
        ListAction = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.list_action import ListAction as ListAction

__all__ = ['ListAction']

