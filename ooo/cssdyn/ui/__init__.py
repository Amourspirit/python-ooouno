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
    from ...dyn.ui.action_trigger import ActionTrigger as ActionTrigger
except ImportError:
    pass
try:
    from ...dyn.ui.action_trigger_container import ActionTriggerContainer as ActionTriggerContainer
except ImportError:
    pass
try:
    from ...dyn.ui.action_trigger_separator import ActionTriggerSeparator as ActionTriggerSeparator
except ImportError:
    pass
try:
    from ...dyn.ui.action_trigger_separator_type import ActionTriggerSeparatorType as ActionTriggerSeparatorType
except ImportError:
    pass
try:
    from ...dyn.ui.action_trigger_separator_type import ActionTriggerSeparatorTypeEnum as ActionTriggerSeparatorTypeEnum
except ImportError:
    pass
try:
    from ...dyn.ui.address_book_source_dialog import AddressBookSourceDialog as AddressBookSourceDialog
except ImportError:
    pass
try:
    from ...dyn.ui.configurable_ui_element import ConfigurableUIElement as ConfigurableUIElement
except ImportError:
    pass
try:
    from ...dyn.ui.configuration_event import ConfigurationEvent as ConfigurationEvent
except ImportError:
    pass
try:
    from ...dyn.ui.context_change_event_multiplexer import ContextChangeEventMultiplexer as ContextChangeEventMultiplexer
except ImportError:
    pass
try:
    from ...dyn.ui.context_change_event_object import ContextChangeEventObject as ContextChangeEventObject
except ImportError:
    pass
try:
    from ...dyn.ui.context_menu_execute_event import ContextMenuExecuteEvent as ContextMenuExecuteEvent
except ImportError:
    pass
try:
    from ...dyn.ui.context_menu_interceptor_action import ContextMenuInterceptorAction as ContextMenuInterceptorAction
except ImportError:
    pass
try:
    from ...dyn.ui.docking_area import DockingArea as DockingArea
except ImportError:
    pass
try:
    from ...dyn.ui.document_accelerator_configuration import DocumentAcceleratorConfiguration as DocumentAcceleratorConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.global_accelerator_configuration import GlobalAcceleratorConfiguration as GlobalAcceleratorConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.image_manager import ImageManager as ImageManager
except ImportError:
    pass
try:
    from ...dyn.ui.image_type import ImageType as ImageType
except ImportError:
    pass
try:
    from ...dyn.ui.image_type import ImageTypeEnum as ImageTypeEnum
except ImportError:
    pass
try:
    from ...dyn.ui.item_descriptor import ItemDescriptor as ItemDescriptor
except ImportError:
    pass
try:
    from ...dyn.ui.item_style import ItemStyle as ItemStyle
except ImportError:
    pass
try:
    from ...dyn.ui.item_style import ItemStyleEnum as ItemStyleEnum
except ImportError:
    pass
try:
    from ...dyn.ui.item_type import ItemType as ItemType
except ImportError:
    pass
try:
    from ...dyn.ui.item_type import ItemTypeEnum as ItemTypeEnum
except ImportError:
    pass
try:
    from ...dyn.ui.layout_size import LayoutSize as LayoutSize
except ImportError:
    pass
try:
    from ...dyn.ui.module_accelerator_configuration import ModuleAcceleratorConfiguration as ModuleAcceleratorConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.module_ui_category_description import ModuleUICategoryDescription as ModuleUICategoryDescription
except ImportError:
    pass
try:
    from ...dyn.ui.module_ui_command_description import ModuleUICommandDescription as ModuleUICommandDescription
except ImportError:
    pass
try:
    from ...dyn.ui.module_ui_configuration_manager import ModuleUIConfigurationManager as ModuleUIConfigurationManager
except ImportError:
    pass
try:
    from ...dyn.ui.module_ui_configuration_manager_supplier import ModuleUIConfigurationManagerSupplier as ModuleUIConfigurationManagerSupplier
except ImportError:
    pass
try:
    from ...dyn.ui.module_window_state_configuration import ModuleWindowStateConfiguration as ModuleWindowStateConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.ui_category_description import UICategoryDescription as UICategoryDescription
except ImportError:
    pass
try:
    from ...dyn.ui.ui_configuration_manager import UIConfigurationManager as UIConfigurationManager
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element import UIElement as UIElement
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element_factory import UIElementFactory as UIElementFactory
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element_factory_manager import UIElementFactoryManager as UIElementFactoryManager
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element_settings import UIElementSettings as UIElementSettings
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element_type import UIElementType as UIElementType
except ImportError:
    pass
try:
    from ...dyn.ui.ui_element_type import UIElementTypeEnum as UIElementTypeEnum
except ImportError:
    pass
try:
    from ...dyn.ui.window_content_factory import WindowContentFactory as WindowContentFactory
except ImportError:
    pass
try:
    from ...dyn.ui.window_content_factory_manager import WindowContentFactoryManager as WindowContentFactoryManager
except ImportError:
    pass
try:
    from ...dyn.ui.window_state_configuration import WindowStateConfiguration as WindowStateConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.x_accelerator_configuration import XAcceleratorConfiguration as XAcceleratorConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.x_context_change_event_listener import XContextChangeEventListener as XContextChangeEventListener
except ImportError:
    pass
try:
    from ...dyn.ui.x_context_change_event_multiplexer import XContextChangeEventMultiplexer as XContextChangeEventMultiplexer
except ImportError:
    pass
try:
    from ...dyn.ui.x_context_menu_interception import XContextMenuInterception as XContextMenuInterception
except ImportError:
    pass
try:
    from ...dyn.ui.x_context_menu_interceptor import XContextMenuInterceptor as XContextMenuInterceptor
except ImportError:
    pass
try:
    from ...dyn.ui.x_deck import XDeck as XDeck
except ImportError:
    pass
try:
    from ...dyn.ui.x_decks import XDecks as XDecks
except ImportError:
    pass
try:
    from ...dyn.ui.x_docking_area_acceptor import XDockingAreaAcceptor as XDockingAreaAcceptor
except ImportError:
    pass
try:
    from ...dyn.ui.x_image_manager import XImageManager as XImageManager
except ImportError:
    pass
try:
    from ...dyn.ui.x_module_ui_configuration_manager import XModuleUIConfigurationManager as XModuleUIConfigurationManager
except ImportError:
    pass
try:
    from ...dyn.ui.x_module_ui_configuration_manager2 import XModuleUIConfigurationManager2 as XModuleUIConfigurationManager2
except ImportError:
    pass
try:
    from ...dyn.ui.x_module_ui_configuration_manager_supplier import XModuleUIConfigurationManagerSupplier as XModuleUIConfigurationManagerSupplier
except ImportError:
    pass
try:
    from ...dyn.ui.x_panel import XPanel as XPanel
except ImportError:
    pass
try:
    from ...dyn.ui.x_panels import XPanels as XPanels
except ImportError:
    pass
try:
    from ...dyn.ui.x_sidebar import XSidebar as XSidebar
except ImportError:
    pass
try:
    from ...dyn.ui.x_sidebar_panel import XSidebarPanel as XSidebarPanel
except ImportError:
    pass
try:
    from ...dyn.ui.x_sidebar_provider import XSidebarProvider as XSidebarProvider
except ImportError:
    pass
try:
    from ...dyn.ui.x_statusbar_item import XStatusbarItem as XStatusbarItem
except ImportError:
    pass
try:
    from ...dyn.ui.x_tool_panel import XToolPanel as XToolPanel
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration import XUIConfiguration as XUIConfiguration
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_listener import XUIConfigurationListener as XUIConfigurationListener
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_manager import XUIConfigurationManager as XUIConfigurationManager
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_manager2 import XUIConfigurationManager2 as XUIConfigurationManager2
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_manager_supplier import XUIConfigurationManagerSupplier as XUIConfigurationManagerSupplier
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_persistence import XUIConfigurationPersistence as XUIConfigurationPersistence
except ImportError:
    pass
try:
    from ...dyn.ui.xui_configuration_storage import XUIConfigurationStorage as XUIConfigurationStorage
except ImportError:
    pass
try:
    from ...dyn.ui.xui_element import XUIElement as XUIElement
except ImportError:
    pass
try:
    from ...dyn.ui.xui_element_factory import XUIElementFactory as XUIElementFactory
except ImportError:
    pass
try:
    from ...dyn.ui.xui_element_factory_manager import XUIElementFactoryManager as XUIElementFactoryManager
except ImportError:
    pass
try:
    from ...dyn.ui.xui_element_factory_registration import XUIElementFactoryRegistration as XUIElementFactoryRegistration
except ImportError:
    pass
try:
    from ...dyn.ui.xui_element_settings import XUIElementSettings as XUIElementSettings
except ImportError:
    pass
try:
    from ...dyn.ui.xui_function_listener import XUIFunctionListener as XUIFunctionListener
except ImportError:
    pass
try:
    from ...dyn.ui.x_update_model import XUpdateModel as XUpdateModel
except ImportError:
    pass
try:
    from ...dyn.ui.the_module_ui_configuration_manager_supplier import theModuleUIConfigurationManagerSupplier as theModuleUIConfigurationManagerSupplier
except ImportError:
    pass
try:
    from ...dyn.ui.the_ui_category_description import theUICategoryDescription as theUICategoryDescription
except ImportError:
    pass
try:
    from ...dyn.ui.the_ui_element_factory_manager import theUIElementFactoryManager as theUIElementFactoryManager
except ImportError:
    pass
try:
    from ...dyn.ui.the_window_content_factory_manager import theWindowContentFactoryManager as theWindowContentFactoryManager
except ImportError:
    pass
try:
    from ...dyn.ui.the_window_state_configuration import theWindowStateConfiguration as theWindowStateConfiguration
except ImportError:
    pass
