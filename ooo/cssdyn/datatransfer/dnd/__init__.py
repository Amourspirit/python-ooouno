# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ....dyn.datatransfer.dnd.dnd_constants import DNDConstants as DNDConstants
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.dnd_constants import DNDConstantsEnum as DNDConstantsEnum
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drag_gesture_event import DragGestureEvent as DragGestureEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drag_source_drag_event import DragSourceDragEvent as DragSourceDragEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drag_source_drop_event import DragSourceDropEvent as DragSourceDropEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drag_source_event import DragSourceEvent as DragSourceEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drop_target_drag_enter_event import DropTargetDragEnterEvent as DropTargetDragEnterEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drop_target_drag_event import DropTargetDragEvent as DropTargetDragEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drop_target_drop_event import DropTargetDropEvent as DropTargetDropEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.drop_target_event import DropTargetEvent as DropTargetEvent
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.invalid_dnd_operation_exception import InvalidDNDOperationException as InvalidDNDOperationException
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.ole_drag_source import OleDragSource as OleDragSource
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.ole_drop_target import OleDropTarget as OleDropTarget
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x11_drag_source import X11DragSource as X11DragSource
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x11_drop_target import X11DropTarget as X11DropTarget
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_autoscroll import XAutoscroll as XAutoscroll
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drag_gesture_listener import XDragGestureListener as XDragGestureListener
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drag_gesture_recognizer import XDragGestureRecognizer as XDragGestureRecognizer
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drag_source import XDragSource as XDragSource
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drag_source_context import XDragSourceContext as XDragSourceContext
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drag_source_listener import XDragSourceListener as XDragSourceListener
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drop_target import XDropTarget as XDropTarget
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drop_target_drag_context import XDropTargetDragContext as XDropTargetDragContext
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drop_target_drop_context import XDropTargetDropContext as XDropTargetDropContext
with suppress(ImportError):
    from ....dyn.datatransfer.dnd.x_drop_target_listener import XDropTargetListener as XDropTargetListener
