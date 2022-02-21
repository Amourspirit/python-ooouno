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
    from ...dyn.frame.app_dispatch_provider import AppDispatchProvider as AppDispatchProvider
except ImportError:
    pass
try:
    from ...dyn.frame.auto_recovery import AutoRecovery as AutoRecovery
except ImportError:
    pass
try:
    from ...dyn.frame.bibliography import Bibliography as Bibliography
except ImportError:
    pass
try:
    from ...dyn.frame.border_widths import BorderWidths as BorderWidths
except ImportError:
    pass
try:
    from ...dyn.frame.command_group import CommandGroup as CommandGroup
except ImportError:
    pass
try:
    from ...dyn.frame.command_group import CommandGroupEnum as CommandGroupEnum
except ImportError:
    pass
try:
    from ...dyn.frame.components import Components as Components
except ImportError:
    pass
try:
    from ...dyn.frame.content_handler import ContentHandler as ContentHandler
except ImportError:
    pass
try:
    from ...dyn.frame.content_handler_factory import ContentHandlerFactory as ContentHandlerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.control_command import ControlCommand as ControlCommand
except ImportError:
    pass
try:
    from ...dyn.frame.control_event import ControlEvent as ControlEvent
except ImportError:
    pass
try:
    from ...dyn.frame.controller import Controller as Controller
except ImportError:
    pass
try:
    from ...dyn.frame.desktop import Desktop as Desktop
except ImportError:
    pass
try:
    from ...dyn.frame.desktop_task import DesktopTask as DesktopTask
except ImportError:
    pass
try:
    from ...dyn.frame.desktop_tasks import DesktopTasks as DesktopTasks
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_descriptor import DispatchDescriptor as DispatchDescriptor
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_helper import DispatchHelper as DispatchHelper
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_information import DispatchInformation as DispatchInformation
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_provider import DispatchProvider as DispatchProvider
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_recorder import DispatchRecorder as DispatchRecorder
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_recorder_supplier import DispatchRecorderSupplier as DispatchRecorderSupplier
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_result_event import DispatchResultEvent as DispatchResultEvent
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_result_state import DispatchResultState as DispatchResultState
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_result_state import DispatchResultStateEnum as DispatchResultStateEnum
except ImportError:
    pass
try:
    from ...dyn.frame.dispatch_statement import DispatchStatement as DispatchStatement
except ImportError:
    pass
try:
    from ...dyn.frame.document_templates import DocumentTemplates as DocumentTemplates
except ImportError:
    pass
try:
    from ...dyn.frame.double_initialization_exception import DoubleInitializationException as DoubleInitializationException
except ImportError:
    pass
try:
    from ...dyn.frame.feature_state_event import FeatureStateEvent as FeatureStateEvent
except ImportError:
    pass
try:
    from ...dyn.frame.frame import Frame as Frame
except ImportError:
    pass
try:
    from ...dyn.frame.frame_action import FrameAction as FrameAction
except ImportError:
    pass
try:
    from ...dyn.frame.frame_action_event import FrameActionEvent as FrameActionEvent
except ImportError:
    pass
try:
    from ...dyn.frame.frame_control import FrameControl as FrameControl
except ImportError:
    pass
try:
    from ...dyn.frame.frame_loader import FrameLoader as FrameLoader
except ImportError:
    pass
try:
    from ...dyn.frame.frame_loader_factory import FrameLoaderFactory as FrameLoaderFactory
except ImportError:
    pass
try:
    from ...dyn.frame.frame_search_flag import FrameSearchFlag as FrameSearchFlag
except ImportError:
    pass
try:
    from ...dyn.frame.frame_search_flag import FrameSearchFlagEnum as FrameSearchFlagEnum
except ImportError:
    pass
try:
    from ...dyn.frame.frames_container import FramesContainer as FramesContainer
except ImportError:
    pass
try:
    from ...dyn.frame.global_event_broadcaster import GlobalEventBroadcaster as GlobalEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.frame.illegal_argument_io_exception import IllegalArgumentIOException as IllegalArgumentIOException
except ImportError:
    pass
try:
    from ...dyn.frame.infobar_type import InfobarType as InfobarType
except ImportError:
    pass
try:
    from ...dyn.frame.infobar_type import InfobarTypeEnum as InfobarTypeEnum
except ImportError:
    pass
try:
    from ...dyn.frame.layout_manager import LayoutManager as LayoutManager
except ImportError:
    pass
try:
    from ...dyn.frame.layout_manager_events import LayoutManagerEvents as LayoutManagerEvents
except ImportError:
    pass
try:
    from ...dyn.frame.layout_manager_events import LayoutManagerEventsEnum as LayoutManagerEventsEnum
except ImportError:
    pass
try:
    from ...dyn.frame.media_type_detection_helper import MediaTypeDetectionHelper as MediaTypeDetectionHelper
except ImportError:
    pass
try:
    from ...dyn.frame.module_manager import ModuleManager as ModuleManager
except ImportError:
    pass
try:
    from ...dyn.frame.office_frame_loader import OfficeFrameLoader as OfficeFrameLoader
except ImportError:
    pass
try:
    from ...dyn.frame.popup_menu_controller import PopupMenuController as PopupMenuController
except ImportError:
    pass
try:
    from ...dyn.frame.popup_menu_controller_factory import PopupMenuControllerFactory as PopupMenuControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.protocol_handler import ProtocolHandler as ProtocolHandler
except ImportError:
    pass
try:
    from ...dyn.frame.session_listener import SessionListener as SessionListener
except ImportError:
    pass
try:
    from ...dyn.frame.session_manager import SessionManager as SessionManager
except ImportError:
    pass
try:
    from ...dyn.frame.settings import Settings as Settings
except ImportError:
    pass
try:
    from ...dyn.frame.start_module import StartModule as StartModule
except ImportError:
    pass
try:
    from ...dyn.frame.statusbar_controller import StatusbarController as StatusbarController
except ImportError:
    pass
try:
    from ...dyn.frame.statusbar_controller_factory import StatusbarControllerFactory as StatusbarControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.synchronous_frame_loader import SynchronousFrameLoader as SynchronousFrameLoader
except ImportError:
    pass
try:
    from ...dyn.frame.task import Task as Task
except ImportError:
    pass
try:
    from ...dyn.frame.task_creator import TaskCreator as TaskCreator
except ImportError:
    pass
try:
    from ...dyn.frame.template_access import TemplateAccess as TemplateAccess
except ImportError:
    pass
try:
    from ...dyn.frame.termination_veto_exception import TerminationVetoException as TerminationVetoException
except ImportError:
    pass
try:
    from ...dyn.frame.title_changed_event import TitleChangedEvent as TitleChangedEvent
except ImportError:
    pass
try:
    from ...dyn.frame.toolbar_controller import ToolbarController as ToolbarController
except ImportError:
    pass
try:
    from ...dyn.frame.toolbar_controller_factory import ToolbarControllerFactory as ToolbarControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.transient_documents_document_content_factory import TransientDocumentsDocumentContentFactory as TransientDocumentsDocumentContentFactory
except ImportError:
    pass
try:
    from ...dyn.frame.ui_command_description import UICommandDescription as UICommandDescription
except ImportError:
    pass
try:
    from ...dyn.frame.unknown_module_exception import UnknownModuleException as UnknownModuleException
except ImportError:
    pass
try:
    from ...dyn.frame.untitled_numbers_const import UntitledNumbersConst as UntitledNumbersConst
except ImportError:
    pass
try:
    from ...dyn.frame.untitled_numbers_const import UntitledNumbersConstEnum as UntitledNumbersConstEnum
except ImportError:
    pass
try:
    from ...dyn.frame.window_arrange import WindowArrange as WindowArrange
except ImportError:
    pass
try:
    from ...dyn.frame.window_arrange import WindowArrangeEnum as WindowArrangeEnum
except ImportError:
    pass
try:
    from ...dyn.frame.x_app_dispatch_provider import XAppDispatchProvider as XAppDispatchProvider
except ImportError:
    pass
try:
    from ...dyn.frame.x_border_resize_listener import XBorderResizeListener as XBorderResizeListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_browse_history_registry import XBrowseHistoryRegistry as XBrowseHistoryRegistry
except ImportError:
    pass
try:
    from ...dyn.frame.x_component_loader import XComponentLoader as XComponentLoader
except ImportError:
    pass
try:
    from ...dyn.frame.x_component_registry import XComponentRegistry as XComponentRegistry
except ImportError:
    pass
try:
    from ...dyn.frame.x_config_manager import XConfigManager as XConfigManager
except ImportError:
    pass
try:
    from ...dyn.frame.x_control_notification_listener import XControlNotificationListener as XControlNotificationListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_controller import XController as XController
except ImportError:
    pass
try:
    from ...dyn.frame.x_controller2 import XController2 as XController2
except ImportError:
    pass
try:
    from ...dyn.frame.x_controller_border import XControllerBorder as XControllerBorder
except ImportError:
    pass
try:
    from ...dyn.frame.x_desktop import XDesktop as XDesktop
except ImportError:
    pass
try:
    from ...dyn.frame.x_desktop2 import XDesktop2 as XDesktop2
except ImportError:
    pass
try:
    from ...dyn.frame.x_desktop_task import XDesktopTask as XDesktopTask
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch import XDispatch as XDispatch
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_helper import XDispatchHelper as XDispatchHelper
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_information_provider import XDispatchInformationProvider as XDispatchInformationProvider
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_provider import XDispatchProvider as XDispatchProvider
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_provider_interception import XDispatchProviderInterception as XDispatchProviderInterception
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_provider_interceptor import XDispatchProviderInterceptor as XDispatchProviderInterceptor
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_recorder import XDispatchRecorder as XDispatchRecorder
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_recorder_supplier import XDispatchRecorderSupplier as XDispatchRecorderSupplier
except ImportError:
    pass
try:
    from ...dyn.frame.x_dispatch_result_listener import XDispatchResultListener as XDispatchResultListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_document_templates import XDocumentTemplates as XDocumentTemplates
except ImportError:
    pass
try:
    from ...dyn.frame.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
except ImportError:
    pass
try:
    from ...dyn.frame.x_filter_detect import XFilterDetect as XFilterDetect
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame import XFrame as XFrame
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame2 import XFrame2 as XFrame2
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame_action_listener import XFrameActionListener as XFrameActionListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame_loader import XFrameLoader as XFrameLoader
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame_loader_query import XFrameLoaderQuery as XFrameLoaderQuery
except ImportError:
    pass
try:
    from ...dyn.frame.x_frame_set_model import XFrameSetModel as XFrameSetModel
except ImportError:
    pass
try:
    from ...dyn.frame.x_frames import XFrames as XFrames
except ImportError:
    pass
try:
    from ...dyn.frame.x_frames_supplier import XFramesSupplier as XFramesSupplier
except ImportError:
    pass
try:
    from ...dyn.frame.x_global_event_broadcaster import XGlobalEventBroadcaster as XGlobalEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.frame.x_infobar_provider import XInfobarProvider as XInfobarProvider
except ImportError:
    pass
try:
    from ...dyn.frame.x_interceptor_info import XInterceptorInfo as XInterceptorInfo
except ImportError:
    pass
try:
    from ...dyn.frame.x_layout_manager import XLayoutManager as XLayoutManager
except ImportError:
    pass
try:
    from ...dyn.frame.x_layout_manager2 import XLayoutManager2 as XLayoutManager2
except ImportError:
    pass
try:
    from ...dyn.frame.x_layout_manager_event_broadcaster import XLayoutManagerEventBroadcaster as XLayoutManagerEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.frame.x_layout_manager_listener import XLayoutManagerListener as XLayoutManagerListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_load_event_listener import XLoadEventListener as XLoadEventListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_loadable import XLoadable as XLoadable
except ImportError:
    pass
try:
    from ...dyn.frame.x_loader_factory import XLoaderFactory as XLoaderFactory
except ImportError:
    pass
try:
    from ...dyn.frame.x_menu_bar_acceptor import XMenuBarAcceptor as XMenuBarAcceptor
except ImportError:
    pass
try:
    from ...dyn.frame.x_menu_bar_merging_acceptor import XMenuBarMergingAcceptor as XMenuBarMergingAcceptor
except ImportError:
    pass
try:
    from ...dyn.frame.x_model import XModel as XModel
except ImportError:
    pass
try:
    from ...dyn.frame.x_model2 import XModel2 as XModel2
except ImportError:
    pass
try:
    from ...dyn.frame.x_model3 import XModel3 as XModel3
except ImportError:
    pass
try:
    from ...dyn.frame.x_module import XModule as XModule
except ImportError:
    pass
try:
    from ...dyn.frame.x_module_manager import XModuleManager as XModuleManager
except ImportError:
    pass
try:
    from ...dyn.frame.x_module_manager2 import XModuleManager2 as XModuleManager2
except ImportError:
    pass
try:
    from ...dyn.frame.x_notifying_dispatch import XNotifyingDispatch as XNotifyingDispatch
except ImportError:
    pass
try:
    from ...dyn.frame.x_popup_menu_controller import XPopupMenuController as XPopupMenuController
except ImportError:
    pass
try:
    from ...dyn.frame.x_recordable_dispatch import XRecordableDispatch as XRecordableDispatch
except ImportError:
    pass
try:
    from ...dyn.frame.x_session_manager_client import XSessionManagerClient as XSessionManagerClient
except ImportError:
    pass
try:
    from ...dyn.frame.x_session_manager_listener import XSessionManagerListener as XSessionManagerListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_session_manager_listener2 import XSessionManagerListener2 as XSessionManagerListener2
except ImportError:
    pass
try:
    from ...dyn.frame.x_status_listener import XStatusListener as XStatusListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_statusbar_controller import XStatusbarController as XStatusbarController
except ImportError:
    pass
try:
    from ...dyn.frame.x_storable import XStorable as XStorable
except ImportError:
    pass
try:
    from ...dyn.frame.x_storable2 import XStorable2 as XStorable2
except ImportError:
    pass
try:
    from ...dyn.frame.x_sub_toolbar_controller import XSubToolbarController as XSubToolbarController
except ImportError:
    pass
try:
    from ...dyn.frame.x_synchronous_dispatch import XSynchronousDispatch as XSynchronousDispatch
except ImportError:
    pass
try:
    from ...dyn.frame.x_synchronous_frame_loader import XSynchronousFrameLoader as XSynchronousFrameLoader
except ImportError:
    pass
try:
    from ...dyn.frame.x_task import XTask as XTask
except ImportError:
    pass
try:
    from ...dyn.frame.x_tasks_supplier import XTasksSupplier as XTasksSupplier
except ImportError:
    pass
try:
    from ...dyn.frame.x_terminate_listener import XTerminateListener as XTerminateListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_terminate_listener2 import XTerminateListener2 as XTerminateListener2
except ImportError:
    pass
try:
    from ...dyn.frame.x_title import XTitle as XTitle
except ImportError:
    pass
try:
    from ...dyn.frame.x_title_change_broadcaster import XTitleChangeBroadcaster as XTitleChangeBroadcaster
except ImportError:
    pass
try:
    from ...dyn.frame.x_title_change_listener import XTitleChangeListener as XTitleChangeListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_toolbar_controller import XToolbarController as XToolbarController
except ImportError:
    pass
try:
    from ...dyn.frame.x_toolbar_controller_listener import XToolbarControllerListener as XToolbarControllerListener
except ImportError:
    pass
try:
    from ...dyn.frame.x_transient_documents_document_content_factory import XTransientDocumentsDocumentContentFactory as XTransientDocumentsDocumentContentFactory
except ImportError:
    pass
try:
    from ...dyn.frame.x_transient_documents_document_content_identifier_factory import XTransientDocumentsDocumentContentIdentifierFactory as XTransientDocumentsDocumentContentIdentifierFactory
except ImportError:
    pass
try:
    from ...dyn.frame.xui_controller_factory import XUIControllerFactory as XUIControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.xui_controller_registration import XUIControllerRegistration as XUIControllerRegistration
except ImportError:
    pass
try:
    from ...dyn.frame.x_untitled_numbers import XUntitledNumbers as XUntitledNumbers
except ImportError:
    pass
try:
    from ...dyn.frame.x_url_list import XUrlList as XUrlList
except ImportError:
    pass
try:
    from ...dyn.frame.x_window_arranger import XWindowArranger as XWindowArranger
except ImportError:
    pass
try:
    from ...dyn.frame.the_auto_recovery import theAutoRecovery as theAutoRecovery
except ImportError:
    pass
try:
    from ...dyn.frame.the_desktop import theDesktop as theDesktop
except ImportError:
    pass
try:
    from ...dyn.frame.the_global_event_broadcaster import theGlobalEventBroadcaster as theGlobalEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.frame.the_popup_menu_controller_factory import thePopupMenuControllerFactory as thePopupMenuControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.the_statusbar_controller_factory import theStatusbarControllerFactory as theStatusbarControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.the_toolbar_controller_factory import theToolbarControllerFactory as theToolbarControllerFactory
except ImportError:
    pass
try:
    from ...dyn.frame.the_ui_command_description import theUICommandDescription as theUICommandDescription
except ImportError:
    pass
