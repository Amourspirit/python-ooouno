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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ....dyn.datatransfer.dnd.dnd_constants import DNDConstants as DNDConstants
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.dnd_constants import DNDConstantsEnum as DNDConstantsEnum
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drag_gesture_event import DragGestureEvent as DragGestureEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drag_source_drag_event import DragSourceDragEvent as DragSourceDragEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drag_source_drop_event import DragSourceDropEvent as DragSourceDropEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drag_source_event import DragSourceEvent as DragSourceEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drop_target_drag_enter_event import DropTargetDragEnterEvent as DropTargetDragEnterEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drop_target_drag_event import DropTargetDragEvent as DropTargetDragEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drop_target_drop_event import DropTargetDropEvent as DropTargetDropEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.drop_target_event import DropTargetEvent as DropTargetEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.invalid_dnd_operation_exception import InvalidDNDOperationException as InvalidDNDOperationException
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.ole_drag_source import OleDragSource as OleDragSource
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.ole_drop_target import OleDropTarget as OleDropTarget
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x11_drag_source import X11DragSource as X11DragSource
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x11_drop_target import X11DropTarget as X11DropTarget
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_autoscroll import XAutoscroll as XAutoscroll
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drag_gesture_listener import XDragGestureListener as XDragGestureListener
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drag_gesture_recognizer import XDragGestureRecognizer as XDragGestureRecognizer
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drag_source import XDragSource as XDragSource
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drag_source_context import XDragSourceContext as XDragSourceContext
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drag_source_listener import XDragSourceListener as XDragSourceListener
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drop_target import XDropTarget as XDropTarget
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drop_target_drag_context import XDropTargetDragContext as XDropTargetDragContext
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drop_target_drop_context import XDropTargetDropContext as XDropTargetDropContext
except ImportError:
    pass
try:
    from ....dyn.datatransfer.dnd.x_drop_target_listener import XDropTargetListener as XDropTargetListener
except ImportError:
    pass
