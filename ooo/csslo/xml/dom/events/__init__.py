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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from .....lo.xml.dom.events.attr_change_type import AttrChangeType as AttrChangeType
from .....lo.xml.dom.events.event_exception import EventException as EventException
from .....lo.xml.dom.events.event_type import EventType as EventType
from .....lo.xml.dom.events.phase_type import PhaseType as PhaseType
from .....lo.xml.dom.events.x_document_event import XDocumentEvent as XDocumentEvent
from .....lo.xml.dom.events.x_event import XEvent as XEvent
from .....lo.xml.dom.events.x_event_listener import XEventListener as XEventListener
from .....lo.xml.dom.events.x_event_target import XEventTarget as XEventTarget
from .....lo.xml.dom.events.x_mouse_event import XMouseEvent as XMouseEvent
from .....lo.xml.dom.events.x_mutation_event import XMutationEvent as XMutationEvent
from .....lo.xml.dom.events.xui_event import XUIEvent as XUIEvent
