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
    from ...dyn.ui.action_trigger import ActionTrigger as ActionTrigger
with suppress(ImportError):
    from ...dyn.ui.action_trigger_container import ActionTriggerContainer as ActionTriggerContainer
with suppress(ImportError):
    from ...dyn.ui.action_trigger_separator import ActionTriggerSeparator as ActionTriggerSeparator
with suppress(ImportError):
    from ...dyn.ui.action_trigger_separator_type import ActionTriggerSeparatorType as ActionTriggerSeparatorType
with suppress(ImportError):
    from ...dyn.ui.action_trigger_separator_type import ActionTriggerSeparatorTypeEnum as ActionTriggerSeparatorTypeEnum
with suppress(ImportError):
    from ...dyn.ui.address_book_source_dialog import AddressBookSourceDialog as AddressBookSourceDialog
with suppress(ImportError):
    from ...dyn.ui.configurable_ui_element import ConfigurableUIElement as ConfigurableUIElement
with suppress(ImportError):
    from ...dyn.ui.configuration_event import ConfigurationEvent as ConfigurationEvent
with suppress(ImportError):
    from ...dyn.ui.context_change_event_multiplexer import ContextChangeEventMultiplexer as ContextChangeEventMultiplexer
with suppress(ImportError):
    from ...dyn.ui.context_change_event_object import ContextChangeEventObject as ContextChangeEventObject
with suppress(ImportError):
    from ...dyn.ui.context_menu_execute_event import ContextMenuExecuteEvent as ContextMenuExecuteEvent
with suppress(ImportError):
    from ...dyn.ui.context_menu_interceptor_action import ContextMenuInterceptorAction as ContextMenuInterceptorAction
with suppress(ImportError):
    from ...dyn.ui.docking_area import DockingArea as DockingArea
with suppress(ImportError):
    from ...dyn.ui.document_accelerator_configuration import DocumentAcceleratorConfiguration as DocumentAcceleratorConfiguration
with suppress(ImportError):
    from ...dyn.ui.global_accelerator_configuration import GlobalAcceleratorConfiguration as GlobalAcceleratorConfiguration
with suppress(ImportError):
    from ...dyn.ui.image_manager import ImageManager as ImageManager
with suppress(ImportError):
    from ...dyn.ui.image_type import ImageType as ImageType
with suppress(ImportError):
    from ...dyn.ui.image_type import ImageTypeEnum as ImageTypeEnum
with suppress(ImportError):
    from ...dyn.ui.item_descriptor import ItemDescriptor as ItemDescriptor
with suppress(ImportError):
    from ...dyn.ui.item_style import ItemStyle as ItemStyle
with suppress(ImportError):
    from ...dyn.ui.item_style import ItemStyleEnum as ItemStyleEnum
with suppress(ImportError):
    from ...dyn.ui.item_type import ItemType as ItemType
with suppress(ImportError):
    from ...dyn.ui.item_type import ItemTypeEnum as ItemTypeEnum
with suppress(ImportError):
    from ...dyn.ui.layout_size import LayoutSize as LayoutSize
with suppress(ImportError):
    from ...dyn.ui.module_accelerator_configuration import ModuleAcceleratorConfiguration as ModuleAcceleratorConfiguration
with suppress(ImportError):
    from ...dyn.ui.module_ui_category_description import ModuleUICategoryDescription as ModuleUICategoryDescription
with suppress(ImportError):
    from ...dyn.ui.module_ui_command_description import ModuleUICommandDescription as ModuleUICommandDescription
with suppress(ImportError):
    from ...dyn.ui.module_ui_configuration_manager import ModuleUIConfigurationManager as ModuleUIConfigurationManager
with suppress(ImportError):
    from ...dyn.ui.module_ui_configuration_manager_supplier import ModuleUIConfigurationManagerSupplier as ModuleUIConfigurationManagerSupplier
with suppress(ImportError):
    from ...dyn.ui.module_window_state_configuration import ModuleWindowStateConfiguration as ModuleWindowStateConfiguration
with suppress(ImportError):
    from ...dyn.ui.ui_category_description import UICategoryDescription as UICategoryDescription
with suppress(ImportError):
    from ...dyn.ui.ui_configuration_manager import UIConfigurationManager as UIConfigurationManager
with suppress(ImportError):
    from ...dyn.ui.ui_element import UIElement as UIElement
with suppress(ImportError):
    from ...dyn.ui.ui_element_factory import UIElementFactory as UIElementFactory
with suppress(ImportError):
    from ...dyn.ui.ui_element_factory_manager import UIElementFactoryManager as UIElementFactoryManager
with suppress(ImportError):
    from ...dyn.ui.ui_element_settings import UIElementSettings as UIElementSettings
with suppress(ImportError):
    from ...dyn.ui.ui_element_type import UIElementType as UIElementType
with suppress(ImportError):
    from ...dyn.ui.ui_element_type import UIElementTypeEnum as UIElementTypeEnum
with suppress(ImportError):
    from ...dyn.ui.window_content_factory import WindowContentFactory as WindowContentFactory
with suppress(ImportError):
    from ...dyn.ui.window_content_factory_manager import WindowContentFactoryManager as WindowContentFactoryManager
with suppress(ImportError):
    from ...dyn.ui.window_state_configuration import WindowStateConfiguration as WindowStateConfiguration
with suppress(ImportError):
    from ...dyn.ui.x_accelerator_configuration import XAcceleratorConfiguration as XAcceleratorConfiguration
with suppress(ImportError):
    from ...dyn.ui.x_context_change_event_listener import XContextChangeEventListener as XContextChangeEventListener
with suppress(ImportError):
    from ...dyn.ui.x_context_change_event_multiplexer import XContextChangeEventMultiplexer as XContextChangeEventMultiplexer
with suppress(ImportError):
    from ...dyn.ui.x_context_menu_interception import XContextMenuInterception as XContextMenuInterception
with suppress(ImportError):
    from ...dyn.ui.x_context_menu_interceptor import XContextMenuInterceptor as XContextMenuInterceptor
with suppress(ImportError):
    from ...dyn.ui.x_deck import XDeck as XDeck
with suppress(ImportError):
    from ...dyn.ui.x_decks import XDecks as XDecks
with suppress(ImportError):
    from ...dyn.ui.x_docking_area_acceptor import XDockingAreaAcceptor as XDockingAreaAcceptor
with suppress(ImportError):
    from ...dyn.ui.x_image_manager import XImageManager as XImageManager
with suppress(ImportError):
    from ...dyn.ui.x_module_ui_configuration_manager import XModuleUIConfigurationManager as XModuleUIConfigurationManager
with suppress(ImportError):
    from ...dyn.ui.x_module_ui_configuration_manager2 import XModuleUIConfigurationManager2 as XModuleUIConfigurationManager2
with suppress(ImportError):
    from ...dyn.ui.x_module_ui_configuration_manager_supplier import XModuleUIConfigurationManagerSupplier as XModuleUIConfigurationManagerSupplier
with suppress(ImportError):
    from ...dyn.ui.x_panel import XPanel as XPanel
with suppress(ImportError):
    from ...dyn.ui.x_panels import XPanels as XPanels
with suppress(ImportError):
    from ...dyn.ui.x_sidebar import XSidebar as XSidebar
with suppress(ImportError):
    from ...dyn.ui.x_sidebar_panel import XSidebarPanel as XSidebarPanel
with suppress(ImportError):
    from ...dyn.ui.x_sidebar_provider import XSidebarProvider as XSidebarProvider
with suppress(ImportError):
    from ...dyn.ui.x_statusbar_item import XStatusbarItem as XStatusbarItem
with suppress(ImportError):
    from ...dyn.ui.x_tool_panel import XToolPanel as XToolPanel
with suppress(ImportError):
    from ...dyn.ui.xui_configuration import XUIConfiguration as XUIConfiguration
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_listener import XUIConfigurationListener as XUIConfigurationListener
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_manager import XUIConfigurationManager as XUIConfigurationManager
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_manager2 import XUIConfigurationManager2 as XUIConfigurationManager2
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_manager_supplier import XUIConfigurationManagerSupplier as XUIConfigurationManagerSupplier
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_persistence import XUIConfigurationPersistence as XUIConfigurationPersistence
with suppress(ImportError):
    from ...dyn.ui.xui_configuration_storage import XUIConfigurationStorage as XUIConfigurationStorage
with suppress(ImportError):
    from ...dyn.ui.xui_element import XUIElement as XUIElement
with suppress(ImportError):
    from ...dyn.ui.xui_element_factory import XUIElementFactory as XUIElementFactory
with suppress(ImportError):
    from ...dyn.ui.xui_element_factory_manager import XUIElementFactoryManager as XUIElementFactoryManager
with suppress(ImportError):
    from ...dyn.ui.xui_element_factory_registration import XUIElementFactoryRegistration as XUIElementFactoryRegistration
with suppress(ImportError):
    from ...dyn.ui.xui_element_settings import XUIElementSettings as XUIElementSettings
with suppress(ImportError):
    from ...dyn.ui.xui_function_listener import XUIFunctionListener as XUIFunctionListener
with suppress(ImportError):
    from ...dyn.ui.x_update_model import XUpdateModel as XUpdateModel
with suppress(ImportError):
    from ...dyn.ui.the_module_ui_configuration_manager_supplier import theModuleUIConfigurationManagerSupplier as theModuleUIConfigurationManagerSupplier
with suppress(ImportError):
    from ...dyn.ui.the_ui_category_description import theUICategoryDescription as theUICategoryDescription
with suppress(ImportError):
    from ...dyn.ui.the_ui_element_factory_manager import theUIElementFactoryManager as theUIElementFactoryManager
with suppress(ImportError):
    from ...dyn.ui.the_window_content_factory_manager import theWindowContentFactoryManager as theWindowContentFactoryManager
with suppress(ImportError):
    from ...dyn.ui.the_window_state_configuration import theWindowStateConfiguration as theWindowStateConfiguration
