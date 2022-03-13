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
    from ...dyn.script.all_event_object import AllEventObject as AllEventObject
except ImportError:
    pass
try:
    from ...dyn.script.all_listener_adapter import AllListenerAdapter as AllListenerAdapter
except ImportError:
    pass
try:
    from ...dyn.script.array_wrapper import ArrayWrapper as ArrayWrapper
except ImportError:
    pass
try:
    from ...dyn.script.basic_error_exception import BasicErrorException as BasicErrorException
except ImportError:
    pass
try:
    from ...dyn.script.cannot_convert_exception import CannotConvertException as CannotConvertException
except ImportError:
    pass
try:
    from ...dyn.script.cannot_create_adapter_exception import CannotCreateAdapterException as CannotCreateAdapterException
except ImportError:
    pass
try:
    from ...dyn.script.context_information import ContextInformation as ContextInformation
except ImportError:
    pass
try:
    from ...dyn.script.converter import Converter as Converter
except ImportError:
    pass
try:
    from ...dyn.script.document_dialog_library_container import DocumentDialogLibraryContainer as DocumentDialogLibraryContainer
except ImportError:
    pass
try:
    from ...dyn.script.document_script_library_container import DocumentScriptLibraryContainer as DocumentScriptLibraryContainer
except ImportError:
    pass
try:
    from ...dyn.script.engine import Engine as Engine
except ImportError:
    pass
try:
    from ...dyn.script.event_listener import EventListener as EventListener
except ImportError:
    pass
try:
    from ...dyn.script.fail_reason import FailReason as FailReason
except ImportError:
    pass
try:
    from ...dyn.script.fail_reason import FailReasonEnum as FailReasonEnum
except ImportError:
    pass
try:
    from ...dyn.script.finish_engine_event import FinishEngineEvent as FinishEngineEvent
except ImportError:
    pass
try:
    from ...dyn.script.finish_reason import FinishReason as FinishReason
except ImportError:
    pass
try:
    from ...dyn.script.interrupt_engine_event import InterruptEngineEvent as InterruptEngineEvent
except ImportError:
    pass
try:
    from ...dyn.script.interrupt_reason import InterruptReason as InterruptReason
except ImportError:
    pass
try:
    from ...dyn.script.invocation import Invocation as Invocation
except ImportError:
    pass
try:
    from ...dyn.script.invocation_adapter_factory import InvocationAdapterFactory as InvocationAdapterFactory
except ImportError:
    pass
try:
    from ...dyn.script.invocation_info import InvocationInfo as InvocationInfo
except ImportError:
    pass
try:
    from ...dyn.script.java_script import JavaScript as JavaScript
except ImportError:
    pass
try:
    from ...dyn.script.library_not_loaded_exception import LibraryNotLoadedException as LibraryNotLoadedException
except ImportError:
    pass
try:
    from ...dyn.script.member_type import MemberType as MemberType
except ImportError:
    pass
try:
    from ...dyn.script.module_info import ModuleInfo as ModuleInfo
except ImportError:
    pass
try:
    from ...dyn.script.module_size_exceeded_request import ModuleSizeExceededRequest as ModuleSizeExceededRequest
except ImportError:
    pass
try:
    from ...dyn.script.module_type import ModuleType as ModuleType
except ImportError:
    pass
try:
    from ...dyn.script.module_type import ModuleTypeEnum as ModuleTypeEnum
except ImportError:
    pass
try:
    from ...dyn.script.native_object_wrapper import NativeObjectWrapper as NativeObjectWrapper
except ImportError:
    pass
try:
    from ...dyn.script.script_event import ScriptEvent as ScriptEvent
except ImportError:
    pass
try:
    from ...dyn.script.script_event_descriptor import ScriptEventDescriptor as ScriptEventDescriptor
except ImportError:
    pass
try:
    from ...dyn.script.x_all_listener import XAllListener as XAllListener
except ImportError:
    pass
try:
    from ...dyn.script.x_all_listener_adapter_service import XAllListenerAdapterService as XAllListenerAdapterService
except ImportError:
    pass
try:
    from ...dyn.script.x_automation_invocation import XAutomationInvocation as XAutomationInvocation
except ImportError:
    pass
try:
    from ...dyn.script.x_debugging import XDebugging as XDebugging
except ImportError:
    pass
try:
    from ...dyn.script.x_default_method import XDefaultMethod as XDefaultMethod
except ImportError:
    pass
try:
    from ...dyn.script.x_default_property import XDefaultProperty as XDefaultProperty
except ImportError:
    pass
try:
    from ...dyn.script.x_direct_invocation import XDirectInvocation as XDirectInvocation
except ImportError:
    pass
try:
    from ...dyn.script.x_engine import XEngine as XEngine
except ImportError:
    pass
try:
    from ...dyn.script.x_engine_listener import XEngineListener as XEngineListener
except ImportError:
    pass
try:
    from ...dyn.script.x_error_query import XErrorQuery as XErrorQuery
except ImportError:
    pass
try:
    from ...dyn.script.x_event_attacher import XEventAttacher as XEventAttacher
except ImportError:
    pass
try:
    from ...dyn.script.x_event_attacher2 import XEventAttacher2 as XEventAttacher2
except ImportError:
    pass
try:
    from ...dyn.script.x_event_attacher_manager import XEventAttacherManager as XEventAttacherManager
except ImportError:
    pass
try:
    from ...dyn.script.x_invocation import XInvocation as XInvocation
except ImportError:
    pass
try:
    from ...dyn.script.x_invocation2 import XInvocation2 as XInvocation2
except ImportError:
    pass
try:
    from ...dyn.script.x_invocation_adapter_factory import XInvocationAdapterFactory as XInvocationAdapterFactory
except ImportError:
    pass
try:
    from ...dyn.script.x_invocation_adapter_factory2 import XInvocationAdapterFactory2 as XInvocationAdapterFactory2
except ImportError:
    pass
try:
    from ...dyn.script.x_library_access import XLibraryAccess as XLibraryAccess
except ImportError:
    pass
try:
    from ...dyn.script.x_library_container import XLibraryContainer as XLibraryContainer
except ImportError:
    pass
try:
    from ...dyn.script.x_library_container2 import XLibraryContainer2 as XLibraryContainer2
except ImportError:
    pass
try:
    from ...dyn.script.x_library_container3 import XLibraryContainer3 as XLibraryContainer3
except ImportError:
    pass
try:
    from ...dyn.script.x_library_container_export import XLibraryContainerExport as XLibraryContainerExport
except ImportError:
    pass
try:
    from ...dyn.script.x_library_container_password import XLibraryContainerPassword as XLibraryContainerPassword
except ImportError:
    pass
try:
    from ...dyn.script.x_library_query_executable import XLibraryQueryExecutable as XLibraryQueryExecutable
except ImportError:
    pass
try:
    from ...dyn.script.x_persistent_library_container import XPersistentLibraryContainer as XPersistentLibraryContainer
except ImportError:
    pass
try:
    from ...dyn.script.x_script_events_attacher import XScriptEventsAttacher as XScriptEventsAttacher
except ImportError:
    pass
try:
    from ...dyn.script.x_script_events_supplier import XScriptEventsSupplier as XScriptEventsSupplier
except ImportError:
    pass
try:
    from ...dyn.script.x_script_listener import XScriptListener as XScriptListener
except ImportError:
    pass
try:
    from ...dyn.script.x_service_documenter import XServiceDocumenter as XServiceDocumenter
except ImportError:
    pass
try:
    from ...dyn.script.x_star_basic_access import XStarBasicAccess as XStarBasicAccess
except ImportError:
    pass
try:
    from ...dyn.script.x_star_basic_dialog_info import XStarBasicDialogInfo as XStarBasicDialogInfo
except ImportError:
    pass
try:
    from ...dyn.script.x_star_basic_library_info import XStarBasicLibraryInfo as XStarBasicLibraryInfo
except ImportError:
    pass
try:
    from ...dyn.script.x_star_basic_module_info import XStarBasicModuleInfo as XStarBasicModuleInfo
except ImportError:
    pass
try:
    from ...dyn.script.x_storage_based_library_container import XStorageBasedLibraryContainer as XStorageBasedLibraryContainer
except ImportError:
    pass
try:
    from ...dyn.script.x_type_converter import XTypeConverter as XTypeConverter
except ImportError:
    pass
try:
    from ...dyn.script.the_service_documenter import theServiceDocumenter as theServiceDocumenter
except ImportError:
    pass
