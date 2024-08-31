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
    from ...dyn.frame.app_dispatch_provider import AppDispatchProvider as AppDispatchProvider
with suppress(ImportError):
    from ...dyn.frame.auto_recovery import AutoRecovery as AutoRecovery
with suppress(ImportError):
    from ...dyn.frame.bibliography import Bibliography as Bibliography
with suppress(ImportError):
    from ...dyn.frame.border_widths import BorderWidths as BorderWidths
with suppress(ImportError):
    from ...dyn.frame.command_group import CommandGroup as CommandGroup
with suppress(ImportError):
    from ...dyn.frame.command_group import CommandGroupEnum as CommandGroupEnum
with suppress(ImportError):
    from ...dyn.frame.components import Components as Components
with suppress(ImportError):
    from ...dyn.frame.content_handler import ContentHandler as ContentHandler
with suppress(ImportError):
    from ...dyn.frame.content_handler_factory import ContentHandlerFactory as ContentHandlerFactory
with suppress(ImportError):
    from ...dyn.frame.control_command import ControlCommand as ControlCommand
with suppress(ImportError):
    from ...dyn.frame.control_event import ControlEvent as ControlEvent
with suppress(ImportError):
    from ...dyn.frame.controller import Controller as Controller
with suppress(ImportError):
    from ...dyn.frame.desktop import Desktop as Desktop
with suppress(ImportError):
    from ...dyn.frame.desktop_task import DesktopTask as DesktopTask
with suppress(ImportError):
    from ...dyn.frame.desktop_tasks import DesktopTasks as DesktopTasks
with suppress(ImportError):
    from ...dyn.frame.dispatch_descriptor import DispatchDescriptor as DispatchDescriptor
with suppress(ImportError):
    from ...dyn.frame.dispatch_helper import DispatchHelper as DispatchHelper
with suppress(ImportError):
    from ...dyn.frame.dispatch_information import DispatchInformation as DispatchInformation
with suppress(ImportError):
    from ...dyn.frame.dispatch_provider import DispatchProvider as DispatchProvider
with suppress(ImportError):
    from ...dyn.frame.dispatch_recorder import DispatchRecorder as DispatchRecorder
with suppress(ImportError):
    from ...dyn.frame.dispatch_recorder_supplier import DispatchRecorderSupplier as DispatchRecorderSupplier
with suppress(ImportError):
    from ...dyn.frame.dispatch_result_event import DispatchResultEvent as DispatchResultEvent
with suppress(ImportError):
    from ...dyn.frame.dispatch_result_state import DispatchResultState as DispatchResultState
with suppress(ImportError):
    from ...dyn.frame.dispatch_result_state import DispatchResultStateEnum as DispatchResultStateEnum
with suppress(ImportError):
    from ...dyn.frame.dispatch_statement import DispatchStatement as DispatchStatement
with suppress(ImportError):
    from ...dyn.frame.document_templates import DocumentTemplates as DocumentTemplates
with suppress(ImportError):
    from ...dyn.frame.double_initialization_exception import DoubleInitializationException as DoubleInitializationException
with suppress(ImportError):
    from ...dyn.frame.feature_state_event import FeatureStateEvent as FeatureStateEvent
with suppress(ImportError):
    from ...dyn.frame.frame import Frame as Frame
with suppress(ImportError):
    from ...dyn.frame.frame_action import FrameAction as FrameAction
with suppress(ImportError):
    from ...dyn.frame.frame_action_event import FrameActionEvent as FrameActionEvent
with suppress(ImportError):
    from ...dyn.frame.frame_control import FrameControl as FrameControl
with suppress(ImportError):
    from ...dyn.frame.frame_loader import FrameLoader as FrameLoader
with suppress(ImportError):
    from ...dyn.frame.frame_loader_factory import FrameLoaderFactory as FrameLoaderFactory
with suppress(ImportError):
    from ...dyn.frame.frame_search_flag import FrameSearchFlag as FrameSearchFlag
with suppress(ImportError):
    from ...dyn.frame.frame_search_flag import FrameSearchFlagEnum as FrameSearchFlagEnum
with suppress(ImportError):
    from ...dyn.frame.frames_container import FramesContainer as FramesContainer
with suppress(ImportError):
    from ...dyn.frame.global_event_broadcaster import GlobalEventBroadcaster as GlobalEventBroadcaster
with suppress(ImportError):
    from ...dyn.frame.illegal_argument_io_exception import IllegalArgumentIOException as IllegalArgumentIOException
with suppress(ImportError):
    from ...dyn.frame.infobar_type import InfobarType as InfobarType
with suppress(ImportError):
    from ...dyn.frame.infobar_type import InfobarTypeEnum as InfobarTypeEnum
with suppress(ImportError):
    from ...dyn.frame.layout_manager import LayoutManager as LayoutManager
with suppress(ImportError):
    from ...dyn.frame.layout_manager_events import LayoutManagerEvents as LayoutManagerEvents
with suppress(ImportError):
    from ...dyn.frame.layout_manager_events import LayoutManagerEventsEnum as LayoutManagerEventsEnum
with suppress(ImportError):
    from ...dyn.frame.media_type_detection_helper import MediaTypeDetectionHelper as MediaTypeDetectionHelper
with suppress(ImportError):
    from ...dyn.frame.module_manager import ModuleManager as ModuleManager
with suppress(ImportError):
    from ...dyn.frame.office_frame_loader import OfficeFrameLoader as OfficeFrameLoader
with suppress(ImportError):
    from ...dyn.frame.popup_menu_controller import PopupMenuController as PopupMenuController
with suppress(ImportError):
    from ...dyn.frame.popup_menu_controller_factory import PopupMenuControllerFactory as PopupMenuControllerFactory
with suppress(ImportError):
    from ...dyn.frame.protocol_handler import ProtocolHandler as ProtocolHandler
with suppress(ImportError):
    from ...dyn.frame.session_listener import SessionListener as SessionListener
with suppress(ImportError):
    from ...dyn.frame.session_manager import SessionManager as SessionManager
with suppress(ImportError):
    from ...dyn.frame.settings import Settings as Settings
with suppress(ImportError):
    from ...dyn.frame.start_module import StartModule as StartModule
with suppress(ImportError):
    from ...dyn.frame.statusbar_controller import StatusbarController as StatusbarController
with suppress(ImportError):
    from ...dyn.frame.statusbar_controller_factory import StatusbarControllerFactory as StatusbarControllerFactory
with suppress(ImportError):
    from ...dyn.frame.synchronous_frame_loader import SynchronousFrameLoader as SynchronousFrameLoader
with suppress(ImportError):
    from ...dyn.frame.task import Task as Task
with suppress(ImportError):
    from ...dyn.frame.task_creator import TaskCreator as TaskCreator
with suppress(ImportError):
    from ...dyn.frame.template_access import TemplateAccess as TemplateAccess
with suppress(ImportError):
    from ...dyn.frame.termination_veto_exception import TerminationVetoException as TerminationVetoException
with suppress(ImportError):
    from ...dyn.frame.title_changed_event import TitleChangedEvent as TitleChangedEvent
with suppress(ImportError):
    from ...dyn.frame.toolbar_controller import ToolbarController as ToolbarController
with suppress(ImportError):
    from ...dyn.frame.toolbar_controller_factory import ToolbarControllerFactory as ToolbarControllerFactory
with suppress(ImportError):
    from ...dyn.frame.transient_documents_document_content_factory import TransientDocumentsDocumentContentFactory as TransientDocumentsDocumentContentFactory
with suppress(ImportError):
    from ...dyn.frame.ui_command_description import UICommandDescription as UICommandDescription
with suppress(ImportError):
    from ...dyn.frame.unknown_module_exception import UnknownModuleException as UnknownModuleException
with suppress(ImportError):
    from ...dyn.frame.untitled_numbers_const import UntitledNumbersConst as UntitledNumbersConst
with suppress(ImportError):
    from ...dyn.frame.untitled_numbers_const import UntitledNumbersConstEnum as UntitledNumbersConstEnum
with suppress(ImportError):
    from ...dyn.frame.window_arrange import WindowArrange as WindowArrange
with suppress(ImportError):
    from ...dyn.frame.window_arrange import WindowArrangeEnum as WindowArrangeEnum
with suppress(ImportError):
    from ...dyn.frame.x_app_dispatch_provider import XAppDispatchProvider as XAppDispatchProvider
with suppress(ImportError):
    from ...dyn.frame.x_border_resize_listener import XBorderResizeListener as XBorderResizeListener
with suppress(ImportError):
    from ...dyn.frame.x_browse_history_registry import XBrowseHistoryRegistry as XBrowseHistoryRegistry
with suppress(ImportError):
    from ...dyn.frame.x_component_loader import XComponentLoader as XComponentLoader
with suppress(ImportError):
    from ...dyn.frame.x_component_registry import XComponentRegistry as XComponentRegistry
with suppress(ImportError):
    from ...dyn.frame.x_config_manager import XConfigManager as XConfigManager
with suppress(ImportError):
    from ...dyn.frame.x_control_notification_listener import XControlNotificationListener as XControlNotificationListener
with suppress(ImportError):
    from ...dyn.frame.x_controller import XController as XController
with suppress(ImportError):
    from ...dyn.frame.x_controller2 import XController2 as XController2
with suppress(ImportError):
    from ...dyn.frame.x_controller_border import XControllerBorder as XControllerBorder
with suppress(ImportError):
    from ...dyn.frame.x_desktop import XDesktop as XDesktop
with suppress(ImportError):
    from ...dyn.frame.x_desktop2 import XDesktop2 as XDesktop2
with suppress(ImportError):
    from ...dyn.frame.x_desktop_task import XDesktopTask as XDesktopTask
with suppress(ImportError):
    from ...dyn.frame.x_dispatch import XDispatch as XDispatch
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_helper import XDispatchHelper as XDispatchHelper
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_information_provider import XDispatchInformationProvider as XDispatchInformationProvider
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_provider import XDispatchProvider as XDispatchProvider
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_provider_interception import XDispatchProviderInterception as XDispatchProviderInterception
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_provider_interceptor import XDispatchProviderInterceptor as XDispatchProviderInterceptor
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_recorder import XDispatchRecorder as XDispatchRecorder
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_recorder_supplier import XDispatchRecorderSupplier as XDispatchRecorderSupplier
with suppress(ImportError):
    from ...dyn.frame.x_dispatch_result_listener import XDispatchResultListener as XDispatchResultListener
with suppress(ImportError):
    from ...dyn.frame.x_document_templates import XDocumentTemplates as XDocumentTemplates
with suppress(ImportError):
    from ...dyn.frame.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
with suppress(ImportError):
    from ...dyn.frame.x_filter_detect import XFilterDetect as XFilterDetect
with suppress(ImportError):
    from ...dyn.frame.x_frame import XFrame as XFrame
with suppress(ImportError):
    from ...dyn.frame.x_frame2 import XFrame2 as XFrame2
with suppress(ImportError):
    from ...dyn.frame.x_frame_action_listener import XFrameActionListener as XFrameActionListener
with suppress(ImportError):
    from ...dyn.frame.x_frame_loader import XFrameLoader as XFrameLoader
with suppress(ImportError):
    from ...dyn.frame.x_frame_loader_query import XFrameLoaderQuery as XFrameLoaderQuery
with suppress(ImportError):
    from ...dyn.frame.x_frame_set_model import XFrameSetModel as XFrameSetModel
with suppress(ImportError):
    from ...dyn.frame.x_frames import XFrames as XFrames
with suppress(ImportError):
    from ...dyn.frame.x_frames_supplier import XFramesSupplier as XFramesSupplier
with suppress(ImportError):
    from ...dyn.frame.x_global_event_broadcaster import XGlobalEventBroadcaster as XGlobalEventBroadcaster
with suppress(ImportError):
    from ...dyn.frame.x_infobar_provider import XInfobarProvider as XInfobarProvider
with suppress(ImportError):
    from ...dyn.frame.x_interceptor_info import XInterceptorInfo as XInterceptorInfo
with suppress(ImportError):
    from ...dyn.frame.x_layout_manager import XLayoutManager as XLayoutManager
with suppress(ImportError):
    from ...dyn.frame.x_layout_manager2 import XLayoutManager2 as XLayoutManager2
with suppress(ImportError):
    from ...dyn.frame.x_layout_manager_event_broadcaster import XLayoutManagerEventBroadcaster as XLayoutManagerEventBroadcaster
with suppress(ImportError):
    from ...dyn.frame.x_layout_manager_listener import XLayoutManagerListener as XLayoutManagerListener
with suppress(ImportError):
    from ...dyn.frame.x_load_event_listener import XLoadEventListener as XLoadEventListener
with suppress(ImportError):
    from ...dyn.frame.x_loadable import XLoadable as XLoadable
with suppress(ImportError):
    from ...dyn.frame.x_loader_factory import XLoaderFactory as XLoaderFactory
with suppress(ImportError):
    from ...dyn.frame.x_menu_bar_acceptor import XMenuBarAcceptor as XMenuBarAcceptor
with suppress(ImportError):
    from ...dyn.frame.x_menu_bar_merging_acceptor import XMenuBarMergingAcceptor as XMenuBarMergingAcceptor
with suppress(ImportError):
    from ...dyn.frame.x_model import XModel as XModel
with suppress(ImportError):
    from ...dyn.frame.x_model2 import XModel2 as XModel2
with suppress(ImportError):
    from ...dyn.frame.x_model3 import XModel3 as XModel3
with suppress(ImportError):
    from ...dyn.frame.x_module import XModule as XModule
with suppress(ImportError):
    from ...dyn.frame.x_module_manager import XModuleManager as XModuleManager
with suppress(ImportError):
    from ...dyn.frame.x_module_manager2 import XModuleManager2 as XModuleManager2
with suppress(ImportError):
    from ...dyn.frame.x_notifying_dispatch import XNotifyingDispatch as XNotifyingDispatch
with suppress(ImportError):
    from ...dyn.frame.x_popup_menu_controller import XPopupMenuController as XPopupMenuController
with suppress(ImportError):
    from ...dyn.frame.x_recordable_dispatch import XRecordableDispatch as XRecordableDispatch
with suppress(ImportError):
    from ...dyn.frame.x_session_manager_client import XSessionManagerClient as XSessionManagerClient
with suppress(ImportError):
    from ...dyn.frame.x_session_manager_listener import XSessionManagerListener as XSessionManagerListener
with suppress(ImportError):
    from ...dyn.frame.x_session_manager_listener2 import XSessionManagerListener2 as XSessionManagerListener2
with suppress(ImportError):
    from ...dyn.frame.x_status_listener import XStatusListener as XStatusListener
with suppress(ImportError):
    from ...dyn.frame.x_statusbar_controller import XStatusbarController as XStatusbarController
with suppress(ImportError):
    from ...dyn.frame.x_storable import XStorable as XStorable
with suppress(ImportError):
    from ...dyn.frame.x_storable2 import XStorable2 as XStorable2
with suppress(ImportError):
    from ...dyn.frame.x_sub_toolbar_controller import XSubToolbarController as XSubToolbarController
with suppress(ImportError):
    from ...dyn.frame.x_synchronous_dispatch import XSynchronousDispatch as XSynchronousDispatch
with suppress(ImportError):
    from ...dyn.frame.x_synchronous_frame_loader import XSynchronousFrameLoader as XSynchronousFrameLoader
with suppress(ImportError):
    from ...dyn.frame.x_task import XTask as XTask
with suppress(ImportError):
    from ...dyn.frame.x_tasks_supplier import XTasksSupplier as XTasksSupplier
with suppress(ImportError):
    from ...dyn.frame.x_terminate_listener import XTerminateListener as XTerminateListener
with suppress(ImportError):
    from ...dyn.frame.x_terminate_listener2 import XTerminateListener2 as XTerminateListener2
with suppress(ImportError):
    from ...dyn.frame.x_title import XTitle as XTitle
with suppress(ImportError):
    from ...dyn.frame.x_title_change_broadcaster import XTitleChangeBroadcaster as XTitleChangeBroadcaster
with suppress(ImportError):
    from ...dyn.frame.x_title_change_listener import XTitleChangeListener as XTitleChangeListener
with suppress(ImportError):
    from ...dyn.frame.x_toolbar_controller import XToolbarController as XToolbarController
with suppress(ImportError):
    from ...dyn.frame.x_toolbar_controller_listener import XToolbarControllerListener as XToolbarControllerListener
with suppress(ImportError):
    from ...dyn.frame.x_transient_documents_document_content_factory import XTransientDocumentsDocumentContentFactory as XTransientDocumentsDocumentContentFactory
with suppress(ImportError):
    from ...dyn.frame.x_transient_documents_document_content_identifier_factory import XTransientDocumentsDocumentContentIdentifierFactory as XTransientDocumentsDocumentContentIdentifierFactory
with suppress(ImportError):
    from ...dyn.frame.xui_controller_factory import XUIControllerFactory as XUIControllerFactory
with suppress(ImportError):
    from ...dyn.frame.xui_controller_registration import XUIControllerRegistration as XUIControllerRegistration
with suppress(ImportError):
    from ...dyn.frame.x_untitled_numbers import XUntitledNumbers as XUntitledNumbers
with suppress(ImportError):
    from ...dyn.frame.x_url_list import XUrlList as XUrlList
with suppress(ImportError):
    from ...dyn.frame.x_window_arranger import XWindowArranger as XWindowArranger
with suppress(ImportError):
    from ...dyn.frame.the_auto_recovery import theAutoRecovery as theAutoRecovery
with suppress(ImportError):
    from ...dyn.frame.the_desktop import theDesktop as theDesktop
with suppress(ImportError):
    from ...dyn.frame.the_global_event_broadcaster import theGlobalEventBroadcaster as theGlobalEventBroadcaster
with suppress(ImportError):
    from ...dyn.frame.the_popup_menu_controller_factory import thePopupMenuControllerFactory as thePopupMenuControllerFactory
with suppress(ImportError):
    from ...dyn.frame.the_statusbar_controller_factory import theStatusbarControllerFactory as theStatusbarControllerFactory
with suppress(ImportError):
    from ...dyn.frame.the_toolbar_controller_factory import theToolbarControllerFactory as theToolbarControllerFactory
with suppress(ImportError):
    from ...dyn.frame.the_ui_command_description import theUICommandDescription as theUICommandDescription
