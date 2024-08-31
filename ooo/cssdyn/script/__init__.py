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
    from ...dyn.script.all_event_object import AllEventObject as AllEventObject
with suppress(ImportError):
    from ...dyn.script.all_listener_adapter import AllListenerAdapter as AllListenerAdapter
with suppress(ImportError):
    from ...dyn.script.array_wrapper import ArrayWrapper as ArrayWrapper
with suppress(ImportError):
    from ...dyn.script.basic_error_exception import BasicErrorException as BasicErrorException
with suppress(ImportError):
    from ...dyn.script.cannot_convert_exception import CannotConvertException as CannotConvertException
with suppress(ImportError):
    from ...dyn.script.cannot_create_adapter_exception import CannotCreateAdapterException as CannotCreateAdapterException
with suppress(ImportError):
    from ...dyn.script.context_information import ContextInformation as ContextInformation
with suppress(ImportError):
    from ...dyn.script.converter import Converter as Converter
with suppress(ImportError):
    from ...dyn.script.document_dialog_library_container import DocumentDialogLibraryContainer as DocumentDialogLibraryContainer
with suppress(ImportError):
    from ...dyn.script.document_script_library_container import DocumentScriptLibraryContainer as DocumentScriptLibraryContainer
with suppress(ImportError):
    from ...dyn.script.engine import Engine as Engine
with suppress(ImportError):
    from ...dyn.script.event_listener import EventListener as EventListener
with suppress(ImportError):
    from ...dyn.script.fail_reason import FailReason as FailReason
with suppress(ImportError):
    from ...dyn.script.fail_reason import FailReasonEnum as FailReasonEnum
with suppress(ImportError):
    from ...dyn.script.finish_engine_event import FinishEngineEvent as FinishEngineEvent
with suppress(ImportError):
    from ...dyn.script.finish_reason import FinishReason as FinishReason
with suppress(ImportError):
    from ...dyn.script.interrupt_engine_event import InterruptEngineEvent as InterruptEngineEvent
with suppress(ImportError):
    from ...dyn.script.interrupt_reason import InterruptReason as InterruptReason
with suppress(ImportError):
    from ...dyn.script.invocation import Invocation as Invocation
with suppress(ImportError):
    from ...dyn.script.invocation_adapter_factory import InvocationAdapterFactory as InvocationAdapterFactory
with suppress(ImportError):
    from ...dyn.script.invocation_info import InvocationInfo as InvocationInfo
with suppress(ImportError):
    from ...dyn.script.java_script import JavaScript as JavaScript
with suppress(ImportError):
    from ...dyn.script.library_not_loaded_exception import LibraryNotLoadedException as LibraryNotLoadedException
with suppress(ImportError):
    from ...dyn.script.member_type import MemberType as MemberType
with suppress(ImportError):
    from ...dyn.script.module_info import ModuleInfo as ModuleInfo
with suppress(ImportError):
    from ...dyn.script.module_size_exceeded_request import ModuleSizeExceededRequest as ModuleSizeExceededRequest
with suppress(ImportError):
    from ...dyn.script.module_type import ModuleType as ModuleType
with suppress(ImportError):
    from ...dyn.script.module_type import ModuleTypeEnum as ModuleTypeEnum
with suppress(ImportError):
    from ...dyn.script.native_object_wrapper import NativeObjectWrapper as NativeObjectWrapper
with suppress(ImportError):
    from ...dyn.script.script_event import ScriptEvent as ScriptEvent
with suppress(ImportError):
    from ...dyn.script.script_event_descriptor import ScriptEventDescriptor as ScriptEventDescriptor
with suppress(ImportError):
    from ...dyn.script.x_all_listener import XAllListener as XAllListener
with suppress(ImportError):
    from ...dyn.script.x_all_listener_adapter_service import XAllListenerAdapterService as XAllListenerAdapterService
with suppress(ImportError):
    from ...dyn.script.x_automation_invocation import XAutomationInvocation as XAutomationInvocation
with suppress(ImportError):
    from ...dyn.script.x_debugging import XDebugging as XDebugging
with suppress(ImportError):
    from ...dyn.script.x_default_method import XDefaultMethod as XDefaultMethod
with suppress(ImportError):
    from ...dyn.script.x_default_property import XDefaultProperty as XDefaultProperty
with suppress(ImportError):
    from ...dyn.script.x_direct_invocation import XDirectInvocation as XDirectInvocation
with suppress(ImportError):
    from ...dyn.script.x_engine import XEngine as XEngine
with suppress(ImportError):
    from ...dyn.script.x_engine_listener import XEngineListener as XEngineListener
with suppress(ImportError):
    from ...dyn.script.x_error_query import XErrorQuery as XErrorQuery
with suppress(ImportError):
    from ...dyn.script.x_event_attacher import XEventAttacher as XEventAttacher
with suppress(ImportError):
    from ...dyn.script.x_event_attacher2 import XEventAttacher2 as XEventAttacher2
with suppress(ImportError):
    from ...dyn.script.x_event_attacher_manager import XEventAttacherManager as XEventAttacherManager
with suppress(ImportError):
    from ...dyn.script.x_invocation import XInvocation as XInvocation
with suppress(ImportError):
    from ...dyn.script.x_invocation2 import XInvocation2 as XInvocation2
with suppress(ImportError):
    from ...dyn.script.x_invocation_adapter_factory import XInvocationAdapterFactory as XInvocationAdapterFactory
with suppress(ImportError):
    from ...dyn.script.x_invocation_adapter_factory2 import XInvocationAdapterFactory2 as XInvocationAdapterFactory2
with suppress(ImportError):
    from ...dyn.script.x_library_access import XLibraryAccess as XLibraryAccess
with suppress(ImportError):
    from ...dyn.script.x_library_container import XLibraryContainer as XLibraryContainer
with suppress(ImportError):
    from ...dyn.script.x_library_container2 import XLibraryContainer2 as XLibraryContainer2
with suppress(ImportError):
    from ...dyn.script.x_library_container3 import XLibraryContainer3 as XLibraryContainer3
with suppress(ImportError):
    from ...dyn.script.x_library_container_export import XLibraryContainerExport as XLibraryContainerExport
with suppress(ImportError):
    from ...dyn.script.x_library_container_password import XLibraryContainerPassword as XLibraryContainerPassword
with suppress(ImportError):
    from ...dyn.script.x_library_query_executable import XLibraryQueryExecutable as XLibraryQueryExecutable
with suppress(ImportError):
    from ...dyn.script.x_persistent_library_container import XPersistentLibraryContainer as XPersistentLibraryContainer
with suppress(ImportError):
    from ...dyn.script.x_script_events_attacher import XScriptEventsAttacher as XScriptEventsAttacher
with suppress(ImportError):
    from ...dyn.script.x_script_events_supplier import XScriptEventsSupplier as XScriptEventsSupplier
with suppress(ImportError):
    from ...dyn.script.x_script_listener import XScriptListener as XScriptListener
with suppress(ImportError):
    from ...dyn.script.x_service_documenter import XServiceDocumenter as XServiceDocumenter
with suppress(ImportError):
    from ...dyn.script.x_star_basic_access import XStarBasicAccess as XStarBasicAccess
with suppress(ImportError):
    from ...dyn.script.x_star_basic_dialog_info import XStarBasicDialogInfo as XStarBasicDialogInfo
with suppress(ImportError):
    from ...dyn.script.x_star_basic_library_info import XStarBasicLibraryInfo as XStarBasicLibraryInfo
with suppress(ImportError):
    from ...dyn.script.x_star_basic_module_info import XStarBasicModuleInfo as XStarBasicModuleInfo
with suppress(ImportError):
    from ...dyn.script.x_storage_based_library_container import XStorageBasedLibraryContainer as XStorageBasedLibraryContainer
with suppress(ImportError):
    from ...dyn.script.x_type_converter import XTypeConverter as XTypeConverter
with suppress(ImportError):
    from ...dyn.script.the_service_documenter import theServiceDocumenter as theServiceDocumenter
