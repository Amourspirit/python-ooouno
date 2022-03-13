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
    from ....dyn.drawing.framework.anchor_binding_mode import AnchorBindingMode as AnchorBindingMode
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.basic_pane_factory import BasicPaneFactory as BasicPaneFactory
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.basic_tool_bar_factory import BasicToolBarFactory as BasicToolBarFactory
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.basic_view_factory import BasicViewFactory as BasicViewFactory
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.border_type import BorderType as BorderType
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.configuration import Configuration as Configuration
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.configuration_change_event import ConfigurationChangeEvent as ConfigurationChangeEvent
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.configuration_controller import ConfigurationController as ConfigurationController
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.module_controller import ModuleController as ModuleController
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.resource_activation_mode import ResourceActivationMode as ResourceActivationMode
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.resource_id import ResourceId as ResourceId
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.tab_bar_button import TabBarButton as TabBarButton
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration import XConfiguration as XConfiguration
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration_change_listener import XConfigurationChangeListener as XConfigurationChangeListener
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration_change_request import XConfigurationChangeRequest as XConfigurationChangeRequest
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration_controller import XConfigurationController as XConfigurationController
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration_controller_broadcaster import XConfigurationControllerBroadcaster as XConfigurationControllerBroadcaster
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_configuration_controller_request_queue import XConfigurationControllerRequestQueue as XConfigurationControllerRequestQueue
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_controller_manager import XControllerManager as XControllerManager
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_module_controller import XModuleController as XModuleController
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_pane import XPane as XPane
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_pane2 import XPane2 as XPane2
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_pane_border_painter import XPaneBorderPainter as XPaneBorderPainter
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_relocatable_resource import XRelocatableResource as XRelocatableResource
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_resource import XResource as XResource
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_resource_factory import XResourceFactory as XResourceFactory
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_resource_factory_manager import XResourceFactoryManager as XResourceFactoryManager
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_resource_id import XResourceId as XResourceId
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_tab_bar import XTabBar as XTabBar
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_tool_bar import XToolBar as XToolBar
except ImportError:
    pass
try:
    from ....dyn.drawing.framework.x_view import XView as XView
except ImportError:
    pass
