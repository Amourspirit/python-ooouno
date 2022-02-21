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
    from ....dyn.awt.tab.tab_page_activated_event import TabPageActivatedEvent as TabPageActivatedEvent
except ImportError:
    pass
try:
    from ....dyn.awt.tab.uno_control_tab_page import UnoControlTabPage as UnoControlTabPage
except ImportError:
    pass
try:
    from ....dyn.awt.tab.uno_control_tab_page_container import UnoControlTabPageContainer as UnoControlTabPageContainer
except ImportError:
    pass
try:
    from ....dyn.awt.tab.uno_control_tab_page_container_model import UnoControlTabPageContainerModel as UnoControlTabPageContainerModel
except ImportError:
    pass
try:
    from ....dyn.awt.tab.uno_control_tab_page_model import UnoControlTabPageModel as UnoControlTabPageModel
except ImportError:
    pass
try:
    from ....dyn.awt.tab.x_tab_page import XTabPage as XTabPage
except ImportError:
    pass
try:
    from ....dyn.awt.tab.x_tab_page_container import XTabPageContainer as XTabPageContainer
except ImportError:
    pass
try:
    from ....dyn.awt.tab.x_tab_page_container_listener import XTabPageContainerListener as XTabPageContainerListener
except ImportError:
    pass
try:
    from ....dyn.awt.tab.x_tab_page_container_model import XTabPageContainerModel as XTabPageContainerModel
except ImportError:
    pass
try:
    from ....dyn.awt.tab.x_tab_page_model import XTabPageModel as XTabPageModel
except ImportError:
    pass
