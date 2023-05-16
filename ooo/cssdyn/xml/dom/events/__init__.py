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
    from .....dyn.xml.dom.events.attr_change_type import AttrChangeType as AttrChangeType
with suppress(ImportError):
    from .....dyn.xml.dom.events.event_exception import EventException as EventException
with suppress(ImportError):
    from .....dyn.xml.dom.events.event_type import EventType as EventType
with suppress(ImportError):
    from .....dyn.xml.dom.events.phase_type import PhaseType as PhaseType
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_document_event import XDocumentEvent as XDocumentEvent
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_event import XEvent as XEvent
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_event_listener import XEventListener as XEventListener
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_event_target import XEventTarget as XEventTarget
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_mouse_event import XMouseEvent as XMouseEvent
with suppress(ImportError):
    from .....dyn.xml.dom.events.x_mutation_event import XMutationEvent as XMutationEvent
with suppress(ImportError):
    from .....dyn.xml.dom.events.xui_event import XUIEvent as XUIEvent
