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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.ui import ContextMenuExecuteEvent as UContextMenuExecuteEvent
        # Dynamically create uno com.sun.star.ui.ContextMenuExecuteEvent using uno
        global ContextMenuExecuteEvent

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ui'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ui.ContextMenuExecuteEvent'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(SourceWindow = UNO_NONE, ExecutePosition = UNO_NONE, ActionTriggerContainer = UNO_NONE, Selection = UNO_NONE):
            ns = 'com.sun.star.ui.ContextMenuExecuteEvent'
            if isinstance(SourceWindow, UContextMenuExecuteEvent):
                inst = uno.createUnoStruct(ns, SourceWindow)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not SourceWindow is UNO_NONE:
                if getattr(struct, 'SourceWindow') != SourceWindow:
                    setattr(struct, 'SourceWindow', SourceWindow)
            if not ExecutePosition is UNO_NONE:
                if getattr(struct, 'ExecutePosition') != ExecutePosition:
                    setattr(struct, 'ExecutePosition', ExecutePosition)
            if not ActionTriggerContainer is UNO_NONE:
                if getattr(struct, 'ActionTriggerContainer') != ActionTriggerContainer:
                    setattr(struct, 'ActionTriggerContainer', ActionTriggerContainer)
            if not Selection is UNO_NONE:
                if getattr(struct, 'Selection') != Selection:
                    setattr(struct, 'Selection', Selection)
            _set_attr(struct)
            return struct
        ContextMenuExecuteEvent = _struct_init

    _dynamic_struct()
else:
    from ...lo.ui.context_menu_execute_event import ContextMenuExecuteEvent as ContextMenuExecuteEvent

__all__ = ['ContextMenuExecuteEvent']

