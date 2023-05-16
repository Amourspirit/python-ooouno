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
    from ...dyn.lang.array_index_out_of_bounds_exception import ArrayIndexOutOfBoundsException as ArrayIndexOutOfBoundsException
with suppress(ImportError):
    from ...dyn.lang.class_not_found_exception import ClassNotFoundException as ClassNotFoundException
with suppress(ImportError):
    from ...dyn.lang.disposed_exception import DisposedException as DisposedException
with suppress(ImportError):
    from ...dyn.lang.event_object import EventObject as EventObject
with suppress(ImportError):
    from ...dyn.lang.illegal_access_exception import IllegalAccessException as IllegalAccessException
with suppress(ImportError):
    from ...dyn.lang.illegal_argument_exception import IllegalArgumentException as IllegalArgumentException
with suppress(ImportError):
    from ...dyn.lang.index_out_of_bounds_exception import IndexOutOfBoundsException as IndexOutOfBoundsException
with suppress(ImportError):
    from ...dyn.lang.invalid_listener_exception import InvalidListenerException as InvalidListenerException
with suppress(ImportError):
    from ...dyn.lang.listener_exist_exception import ListenerExistException as ListenerExistException
with suppress(ImportError):
    from ...dyn.lang.locale import Locale as Locale
with suppress(ImportError):
    from ...dyn.lang.multi_service_factory import MultiServiceFactory as MultiServiceFactory
with suppress(ImportError):
    from ...dyn.lang.no_such_field_exception import NoSuchFieldException as NoSuchFieldException
with suppress(ImportError):
    from ...dyn.lang.no_such_method_exception import NoSuchMethodException as NoSuchMethodException
with suppress(ImportError):
    from ...dyn.lang.no_support_exception import NoSupportException as NoSupportException
with suppress(ImportError):
    from ...dyn.lang.not_initialized_exception import NotInitializedException as NotInitializedException
with suppress(ImportError):
    from ...dyn.lang.null_pointer_exception import NullPointerException as NullPointerException
with suppress(ImportError):
    from ...dyn.lang.registry_service_manager import RegistryServiceManager as RegistryServiceManager
with suppress(ImportError):
    from ...dyn.lang.service_manager import ServiceManager as ServiceManager
with suppress(ImportError):
    from ...dyn.lang.service_not_registered_exception import ServiceNotRegisteredException as ServiceNotRegisteredException
with suppress(ImportError):
    from ...dyn.lang.system_dependent import SystemDependent as SystemDependent
with suppress(ImportError):
    from ...dyn.lang.system_dependent import SystemDependentEnum as SystemDependentEnum
with suppress(ImportError):
    from ...dyn.lang.wrapped_target_exception import WrappedTargetException as WrappedTargetException
with suppress(ImportError):
    from ...dyn.lang.wrapped_target_runtime_exception import WrappedTargetRuntimeException as WrappedTargetRuntimeException
with suppress(ImportError):
    from ...dyn.lang.x_component import XComponent as XComponent
with suppress(ImportError):
    from ...dyn.lang.x_connection_point import XConnectionPoint as XConnectionPoint
with suppress(ImportError):
    from ...dyn.lang.x_connection_point_container import XConnectionPointContainer as XConnectionPointContainer
with suppress(ImportError):
    from ...dyn.lang.x_event_listener import XEventListener as XEventListener
with suppress(ImportError):
    from ...dyn.lang.x_initialization import XInitialization as XInitialization
with suppress(ImportError):
    from ...dyn.lang.x_localizable import XLocalizable as XLocalizable
with suppress(ImportError):
    from ...dyn.lang.x_main import XMain as XMain
with suppress(ImportError):
    from ...dyn.lang.x_multi_component_factory import XMultiComponentFactory as XMultiComponentFactory
with suppress(ImportError):
    from ...dyn.lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory
with suppress(ImportError):
    from ...dyn.lang.x_service_display_name import XServiceDisplayName as XServiceDisplayName
with suppress(ImportError):
    from ...dyn.lang.x_service_info import XServiceInfo as XServiceInfo
with suppress(ImportError):
    from ...dyn.lang.x_service_name import XServiceName as XServiceName
with suppress(ImportError):
    from ...dyn.lang.x_single_component_factory import XSingleComponentFactory as XSingleComponentFactory
with suppress(ImportError):
    from ...dyn.lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory
with suppress(ImportError):
    from ...dyn.lang.x_type_provider import XTypeProvider as XTypeProvider
with suppress(ImportError):
    from ...dyn.lang.x_uno_tunnel import XUnoTunnel as XUnoTunnel
