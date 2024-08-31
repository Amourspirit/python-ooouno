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
    from ....dyn.drawing.framework.anchor_binding_mode import AnchorBindingMode as AnchorBindingMode
with suppress(ImportError):
    from ....dyn.drawing.framework.basic_pane_factory import BasicPaneFactory as BasicPaneFactory
with suppress(ImportError):
    from ....dyn.drawing.framework.basic_tool_bar_factory import BasicToolBarFactory as BasicToolBarFactory
with suppress(ImportError):
    from ....dyn.drawing.framework.basic_view_factory import BasicViewFactory as BasicViewFactory
with suppress(ImportError):
    from ....dyn.drawing.framework.border_type import BorderType as BorderType
with suppress(ImportError):
    from ....dyn.drawing.framework.configuration_change_event import ConfigurationChangeEvent as ConfigurationChangeEvent
with suppress(ImportError):
    from ....dyn.drawing.framework.resource_activation_mode import ResourceActivationMode as ResourceActivationMode
with suppress(ImportError):
    from ....dyn.drawing.framework.resource_id import ResourceId as ResourceId
with suppress(ImportError):
    from ....dyn.drawing.framework.tab_bar_button import TabBarButton as TabBarButton
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration import XConfiguration as XConfiguration
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration_change_listener import XConfigurationChangeListener as XConfigurationChangeListener
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration_change_request import XConfigurationChangeRequest as XConfigurationChangeRequest
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration_controller import XConfigurationController as XConfigurationController
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration_controller_broadcaster import XConfigurationControllerBroadcaster as XConfigurationControllerBroadcaster
with suppress(ImportError):
    from ....dyn.drawing.framework.x_configuration_controller_request_queue import XConfigurationControllerRequestQueue as XConfigurationControllerRequestQueue
with suppress(ImportError):
    from ....dyn.drawing.framework.x_controller_manager import XControllerManager as XControllerManager
with suppress(ImportError):
    from ....dyn.drawing.framework.x_module_controller import XModuleController as XModuleController
with suppress(ImportError):
    from ....dyn.drawing.framework.x_pane import XPane as XPane
with suppress(ImportError):
    from ....dyn.drawing.framework.x_pane2 import XPane2 as XPane2
with suppress(ImportError):
    from ....dyn.drawing.framework.x_pane_border_painter import XPaneBorderPainter as XPaneBorderPainter
with suppress(ImportError):
    from ....dyn.drawing.framework.x_relocatable_resource import XRelocatableResource as XRelocatableResource
with suppress(ImportError):
    from ....dyn.drawing.framework.x_resource import XResource as XResource
with suppress(ImportError):
    from ....dyn.drawing.framework.x_resource_factory import XResourceFactory as XResourceFactory
with suppress(ImportError):
    from ....dyn.drawing.framework.x_resource_factory_manager import XResourceFactoryManager as XResourceFactoryManager
with suppress(ImportError):
    from ....dyn.drawing.framework.x_resource_id import XResourceId as XResourceId
with suppress(ImportError):
    from ....dyn.drawing.framework.x_tab_bar import XTabBar as XTabBar
with suppress(ImportError):
    from ....dyn.drawing.framework.x_tool_bar import XToolBar as XToolBar
with suppress(ImportError):
    from ....dyn.drawing.framework.x_view import XView as XView
