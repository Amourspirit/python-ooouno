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
    from ....dyn.datatransfer.clipboard.clipboard_event import ClipboardEvent as ClipboardEvent
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.clipboard_manager import ClipboardManager as ClipboardManager
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.generic_clipboard import GenericClipboard as GenericClipboard
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.rendering_capabilities import RenderingCapabilities as RenderingCapabilities
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.rendering_capabilities import RenderingCapabilitiesEnum as RenderingCapabilitiesEnum
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.system_clipboard import SystemClipboard as SystemClipboard
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard import XClipboard as XClipboard
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_ex import XClipboardEx as XClipboardEx
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_factory import XClipboardFactory as XClipboardFactory
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_listener import XClipboardListener as XClipboardListener
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_manager import XClipboardManager as XClipboardManager
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_notifier import XClipboardNotifier as XClipboardNotifier
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_clipboard_owner import XClipboardOwner as XClipboardOwner
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_flushable_clipboard import XFlushableClipboard as XFlushableClipboard
except ImportError:
    pass
try:
    from ....dyn.datatransfer.clipboard.x_system_clipboard import XSystemClipboard as XSystemClipboard
except ImportError:
    pass
