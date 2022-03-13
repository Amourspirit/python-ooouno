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
    from ...dyn.lang.array_index_out_of_bounds_exception import ArrayIndexOutOfBoundsException as ArrayIndexOutOfBoundsException
except ImportError:
    pass
try:
    from ...dyn.lang.class_not_found_exception import ClassNotFoundException as ClassNotFoundException
except ImportError:
    pass
try:
    from ...dyn.lang.disposed_exception import DisposedException as DisposedException
except ImportError:
    pass
try:
    from ...dyn.lang.event_object import EventObject as EventObject
except ImportError:
    pass
try:
    from ...dyn.lang.illegal_access_exception import IllegalAccessException as IllegalAccessException
except ImportError:
    pass
try:
    from ...dyn.lang.illegal_argument_exception import IllegalArgumentException as IllegalArgumentException
except ImportError:
    pass
try:
    from ...dyn.lang.index_out_of_bounds_exception import IndexOutOfBoundsException as IndexOutOfBoundsException
except ImportError:
    pass
try:
    from ...dyn.lang.invalid_listener_exception import InvalidListenerException as InvalidListenerException
except ImportError:
    pass
try:
    from ...dyn.lang.listener_exist_exception import ListenerExistException as ListenerExistException
except ImportError:
    pass
try:
    from ...dyn.lang.locale import Locale as Locale
except ImportError:
    pass
try:
    from ...dyn.lang.multi_service_factory import MultiServiceFactory as MultiServiceFactory
except ImportError:
    pass
try:
    from ...dyn.lang.no_such_field_exception import NoSuchFieldException as NoSuchFieldException
except ImportError:
    pass
try:
    from ...dyn.lang.no_such_method_exception import NoSuchMethodException as NoSuchMethodException
except ImportError:
    pass
try:
    from ...dyn.lang.no_support_exception import NoSupportException as NoSupportException
except ImportError:
    pass
try:
    from ...dyn.lang.not_initialized_exception import NotInitializedException as NotInitializedException
except ImportError:
    pass
try:
    from ...dyn.lang.null_pointer_exception import NullPointerException as NullPointerException
except ImportError:
    pass
try:
    from ...dyn.lang.registry_service_manager import RegistryServiceManager as RegistryServiceManager
except ImportError:
    pass
try:
    from ...dyn.lang.service_manager import ServiceManager as ServiceManager
except ImportError:
    pass
try:
    from ...dyn.lang.service_not_registered_exception import ServiceNotRegisteredException as ServiceNotRegisteredException
except ImportError:
    pass
try:
    from ...dyn.lang.system_dependent import SystemDependent as SystemDependent
except ImportError:
    pass
try:
    from ...dyn.lang.system_dependent import SystemDependentEnum as SystemDependentEnum
except ImportError:
    pass
try:
    from ...dyn.lang.wrapped_target_exception import WrappedTargetException as WrappedTargetException
except ImportError:
    pass
try:
    from ...dyn.lang.wrapped_target_runtime_exception import WrappedTargetRuntimeException as WrappedTargetRuntimeException
except ImportError:
    pass
try:
    from ...dyn.lang.x_component import XComponent as XComponent
except ImportError:
    pass
try:
    from ...dyn.lang.x_connection_point import XConnectionPoint as XConnectionPoint
except ImportError:
    pass
try:
    from ...dyn.lang.x_connection_point_container import XConnectionPointContainer as XConnectionPointContainer
except ImportError:
    pass
try:
    from ...dyn.lang.x_event_listener import XEventListener as XEventListener
except ImportError:
    pass
try:
    from ...dyn.lang.x_initialization import XInitialization as XInitialization
except ImportError:
    pass
try:
    from ...dyn.lang.x_localizable import XLocalizable as XLocalizable
except ImportError:
    pass
try:
    from ...dyn.lang.x_main import XMain as XMain
except ImportError:
    pass
try:
    from ...dyn.lang.x_multi_component_factory import XMultiComponentFactory as XMultiComponentFactory
except ImportError:
    pass
try:
    from ...dyn.lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory
except ImportError:
    pass
try:
    from ...dyn.lang.x_service_display_name import XServiceDisplayName as XServiceDisplayName
except ImportError:
    pass
try:
    from ...dyn.lang.x_service_info import XServiceInfo as XServiceInfo
except ImportError:
    pass
try:
    from ...dyn.lang.x_service_name import XServiceName as XServiceName
except ImportError:
    pass
try:
    from ...dyn.lang.x_single_component_factory import XSingleComponentFactory as XSingleComponentFactory
except ImportError:
    pass
try:
    from ...dyn.lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory
except ImportError:
    pass
try:
    from ...dyn.lang.x_type_provider import XTypeProvider as XTypeProvider
except ImportError:
    pass
try:
    from ...dyn.lang.x_uno_tunnel import XUnoTunnel as XUnoTunnel
except ImportError:
    pass
