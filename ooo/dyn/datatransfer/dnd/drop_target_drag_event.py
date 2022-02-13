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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.datatransfer.dnd import DropTargetDragEvent as UDropTargetDragEvent
        # Dynamically create uno com.sun.star.datatransfer.dnd.DropTargetDragEvent using uno
        global DropTargetDragEvent

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.datatransfer.dnd'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.datatransfer.dnd.DropTargetDragEvent'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Context = UNO_NONE, DropAction = UNO_NONE, LocationX = UNO_NONE, LocationY = UNO_NONE, SourceActions = UNO_NONE, **kwargs):
            ns = 'com.sun.star.datatransfer.dnd.DropTargetDragEvent'
            if isinstance(Context, UDropTargetDragEvent):
                inst = uno.createUnoStruct(ns, Context)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Context is UNO_NONE:
                if getattr(struct, 'Context') != Context:
                    setattr(struct, 'Context', Context)
            if not DropAction is UNO_NONE:
                if getattr(struct, 'DropAction') != DropAction:
                    setattr(struct, 'DropAction', DropAction)
            if not LocationX is UNO_NONE:
                if getattr(struct, 'LocationX') != LocationX:
                    setattr(struct, 'LocationX', LocationX)
            if not LocationY is UNO_NONE:
                if getattr(struct, 'LocationY') != LocationY:
                    setattr(struct, 'LocationY', LocationY)
            if not SourceActions is UNO_NONE:
                if getattr(struct, 'SourceActions') != SourceActions:
                    setattr(struct, 'SourceActions', SourceActions)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(ex, k, v)
            _set_attr(struct)
            return struct
        DropTargetDragEvent = _struct_init

    _dynamic_struct()
else:
    from ....lo.datatransfer.dnd.drop_target_drag_event import DropTargetDragEvent as DropTargetDragEvent

__all__ = ['DropTargetDragEvent']

