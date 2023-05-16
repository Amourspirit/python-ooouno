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
    from ...dyn.reflection.core_reflection import CoreReflection as CoreReflection
with suppress(ImportError):
    from ...dyn.reflection.field_access_mode import FieldAccessMode as FieldAccessMode
with suppress(ImportError):
    from ...dyn.reflection.invalid_type_name_exception import InvalidTypeNameException as InvalidTypeNameException
with suppress(ImportError):
    from ...dyn.reflection.invocation_target_exception import InvocationTargetException as InvocationTargetException
with suppress(ImportError):
    from ...dyn.reflection.method_mode import MethodMode as MethodMode
with suppress(ImportError):
    from ...dyn.reflection.no_such_type_name_exception import NoSuchTypeNameException as NoSuchTypeNameException
with suppress(ImportError):
    from ...dyn.reflection.param_info import ParamInfo as ParamInfo
with suppress(ImportError):
    from ...dyn.reflection.param_mode import ParamMode as ParamMode
with suppress(ImportError):
    from ...dyn.reflection.proxy_factory import ProxyFactory as ProxyFactory
with suppress(ImportError):
    from ...dyn.reflection.type_description_manager import TypeDescriptionManager as TypeDescriptionManager
with suppress(ImportError):
    from ...dyn.reflection.type_description_provider import TypeDescriptionProvider as TypeDescriptionProvider
with suppress(ImportError):
    from ...dyn.reflection.type_description_search_depth import TypeDescriptionSearchDepth as TypeDescriptionSearchDepth
with suppress(ImportError):
    from ...dyn.reflection.x_array_type_description import XArrayTypeDescription as XArrayTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_compound_type_description import XCompoundTypeDescription as XCompoundTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_constant_type_description import XConstantTypeDescription as XConstantTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_constants_type_description import XConstantsTypeDescription as XConstantsTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_enum_type_description import XEnumTypeDescription as XEnumTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_idl_array import XIdlArray as XIdlArray
with suppress(ImportError):
    from ...dyn.reflection.x_idl_class import XIdlClass as XIdlClass
with suppress(ImportError):
    from ...dyn.reflection.x_idl_class_provider import XIdlClassProvider as XIdlClassProvider
with suppress(ImportError):
    from ...dyn.reflection.x_idl_field import XIdlField as XIdlField
with suppress(ImportError):
    from ...dyn.reflection.x_idl_field2 import XIdlField2 as XIdlField2
with suppress(ImportError):
    from ...dyn.reflection.x_idl_member import XIdlMember as XIdlMember
with suppress(ImportError):
    from ...dyn.reflection.x_idl_method import XIdlMethod as XIdlMethod
with suppress(ImportError):
    from ...dyn.reflection.x_idl_reflection import XIdlReflection as XIdlReflection
with suppress(ImportError):
    from ...dyn.reflection.x_indirect_type_description import XIndirectTypeDescription as XIndirectTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_interface_attribute_type_description import XInterfaceAttributeTypeDescription as XInterfaceAttributeTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_interface_attribute_type_description2 import XInterfaceAttributeTypeDescription2 as XInterfaceAttributeTypeDescription2
with suppress(ImportError):
    from ...dyn.reflection.x_interface_member_type_description import XInterfaceMemberTypeDescription as XInterfaceMemberTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_interface_method_type_description import XInterfaceMethodTypeDescription as XInterfaceMethodTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_interface_type_description import XInterfaceTypeDescription as XInterfaceTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_interface_type_description2 import XInterfaceTypeDescription2 as XInterfaceTypeDescription2
with suppress(ImportError):
    from ...dyn.reflection.x_method_parameter import XMethodParameter as XMethodParameter
with suppress(ImportError):
    from ...dyn.reflection.x_module_type_description import XModuleTypeDescription as XModuleTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_parameter import XParameter as XParameter
with suppress(ImportError):
    from ...dyn.reflection.x_property_type_description import XPropertyTypeDescription as XPropertyTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_proxy_factory import XProxyFactory as XProxyFactory
with suppress(ImportError):
    from ...dyn.reflection.x_published import XPublished as XPublished
with suppress(ImportError):
    from ...dyn.reflection.x_service_constructor_description import XServiceConstructorDescription as XServiceConstructorDescription
with suppress(ImportError):
    from ...dyn.reflection.x_service_type_description import XServiceTypeDescription as XServiceTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_service_type_description2 import XServiceTypeDescription2 as XServiceTypeDescription2
with suppress(ImportError):
    from ...dyn.reflection.x_singleton_type_description import XSingletonTypeDescription as XSingletonTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_singleton_type_description2 import XSingletonTypeDescription2 as XSingletonTypeDescription2
with suppress(ImportError):
    from ...dyn.reflection.x_struct_type_description import XStructTypeDescription as XStructTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_type_description import XTypeDescription as XTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.x_type_description_enumeration import XTypeDescriptionEnumeration as XTypeDescriptionEnumeration
with suppress(ImportError):
    from ...dyn.reflection.x_type_description_enumeration_access import XTypeDescriptionEnumerationAccess as XTypeDescriptionEnumerationAccess
with suppress(ImportError):
    from ...dyn.reflection.x_union_type_description import XUnionTypeDescription as XUnionTypeDescription
with suppress(ImportError):
    from ...dyn.reflection.the_core_reflection import theCoreReflection as theCoreReflection
