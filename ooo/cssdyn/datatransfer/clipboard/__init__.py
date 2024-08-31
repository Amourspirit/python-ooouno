# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
    from ....dyn.datatransfer.clipboard.clipboard_event import ClipboardEvent as ClipboardEvent
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.clipboard_manager import ClipboardManager as ClipboardManager
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.generic_clipboard import GenericClipboard as GenericClipboard
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.lok_clipboard import LokClipboard as LokClipboard
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.rendering_capabilities import RenderingCapabilities as RenderingCapabilities
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.rendering_capabilities import RenderingCapabilitiesEnum as RenderingCapabilitiesEnum
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.system_clipboard import SystemClipboard as SystemClipboard
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard import XClipboard as XClipboard
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_ex import XClipboardEx as XClipboardEx
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_factory import XClipboardFactory as XClipboardFactory
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_listener import XClipboardListener as XClipboardListener
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_manager import XClipboardManager as XClipboardManager
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_notifier import XClipboardNotifier as XClipboardNotifier
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_clipboard_owner import XClipboardOwner as XClipboardOwner
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_flushable_clipboard import XFlushableClipboard as XFlushableClipboard
with suppress(ImportError):
    from ....dyn.datatransfer.clipboard.x_system_clipboard import XSystemClipboard as XSystemClipboard
