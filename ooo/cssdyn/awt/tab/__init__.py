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
    from ....dyn.awt.tab.tab_page_activated_event import TabPageActivatedEvent as TabPageActivatedEvent
with suppress(ImportError):
    from ....dyn.awt.tab.uno_control_tab_page import UnoControlTabPage as UnoControlTabPage
with suppress(ImportError):
    from ....dyn.awt.tab.uno_control_tab_page_container import UnoControlTabPageContainer as UnoControlTabPageContainer
with suppress(ImportError):
    from ....dyn.awt.tab.uno_control_tab_page_container_model import UnoControlTabPageContainerModel as UnoControlTabPageContainerModel
with suppress(ImportError):
    from ....dyn.awt.tab.uno_control_tab_page_model import UnoControlTabPageModel as UnoControlTabPageModel
with suppress(ImportError):
    from ....dyn.awt.tab.x_tab_page import XTabPage as XTabPage
with suppress(ImportError):
    from ....dyn.awt.tab.x_tab_page_container import XTabPageContainer as XTabPageContainer
with suppress(ImportError):
    from ....dyn.awt.tab.x_tab_page_container_listener import XTabPageContainerListener as XTabPageContainerListener
with suppress(ImportError):
    from ....dyn.awt.tab.x_tab_page_container_model import XTabPageContainerModel as XTabPageContainerModel
with suppress(ImportError):
    from ....dyn.awt.tab.x_tab_page_model import XTabPageModel as XTabPageModel
