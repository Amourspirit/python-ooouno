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
    from ...dyn.reflection.core_reflection import CoreReflection as CoreReflection
except ImportError:
    pass
try:
    from ...dyn.reflection.field_access_mode import FieldAccessMode as FieldAccessMode
except ImportError:
    pass
try:
    from ...dyn.reflection.invalid_type_name_exception import InvalidTypeNameException as InvalidTypeNameException
except ImportError:
    pass
try:
    from ...dyn.reflection.invocation_target_exception import InvocationTargetException as InvocationTargetException
except ImportError:
    pass
try:
    from ...dyn.reflection.method_mode import MethodMode as MethodMode
except ImportError:
    pass
try:
    from ...dyn.reflection.no_such_type_name_exception import NoSuchTypeNameException as NoSuchTypeNameException
except ImportError:
    pass
try:
    from ...dyn.reflection.param_info import ParamInfo as ParamInfo
except ImportError:
    pass
try:
    from ...dyn.reflection.param_mode import ParamMode as ParamMode
except ImportError:
    pass
try:
    from ...dyn.reflection.proxy_factory import ProxyFactory as ProxyFactory
except ImportError:
    pass
try:
    from ...dyn.reflection.type_description_manager import TypeDescriptionManager as TypeDescriptionManager
except ImportError:
    pass
try:
    from ...dyn.reflection.type_description_provider import TypeDescriptionProvider as TypeDescriptionProvider
except ImportError:
    pass
try:
    from ...dyn.reflection.type_description_search_depth import TypeDescriptionSearchDepth as TypeDescriptionSearchDepth
except ImportError:
    pass
try:
    from ...dyn.reflection.x_array_type_description import XArrayTypeDescription as XArrayTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_compound_type_description import XCompoundTypeDescription as XCompoundTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_constant_type_description import XConstantTypeDescription as XConstantTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_constants_type_description import XConstantsTypeDescription as XConstantsTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_enum_type_description import XEnumTypeDescription as XEnumTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_array import XIdlArray as XIdlArray
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_class import XIdlClass as XIdlClass
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_class_provider import XIdlClassProvider as XIdlClassProvider
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_field import XIdlField as XIdlField
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_field2 import XIdlField2 as XIdlField2
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_member import XIdlMember as XIdlMember
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_method import XIdlMethod as XIdlMethod
except ImportError:
    pass
try:
    from ...dyn.reflection.x_idl_reflection import XIdlReflection as XIdlReflection
except ImportError:
    pass
try:
    from ...dyn.reflection.x_indirect_type_description import XIndirectTypeDescription as XIndirectTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_attribute_type_description import XInterfaceAttributeTypeDescription as XInterfaceAttributeTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_attribute_type_description2 import XInterfaceAttributeTypeDescription2 as XInterfaceAttributeTypeDescription2
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_member_type_description import XInterfaceMemberTypeDescription as XInterfaceMemberTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_method_type_description import XInterfaceMethodTypeDescription as XInterfaceMethodTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_type_description import XInterfaceTypeDescription as XInterfaceTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_interface_type_description2 import XInterfaceTypeDescription2 as XInterfaceTypeDescription2
except ImportError:
    pass
try:
    from ...dyn.reflection.x_method_parameter import XMethodParameter as XMethodParameter
except ImportError:
    pass
try:
    from ...dyn.reflection.x_module_type_description import XModuleTypeDescription as XModuleTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_parameter import XParameter as XParameter
except ImportError:
    pass
try:
    from ...dyn.reflection.x_property_type_description import XPropertyTypeDescription as XPropertyTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_proxy_factory import XProxyFactory as XProxyFactory
except ImportError:
    pass
try:
    from ...dyn.reflection.x_published import XPublished as XPublished
except ImportError:
    pass
try:
    from ...dyn.reflection.x_service_constructor_description import XServiceConstructorDescription as XServiceConstructorDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_service_type_description import XServiceTypeDescription as XServiceTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_service_type_description2 import XServiceTypeDescription2 as XServiceTypeDescription2
except ImportError:
    pass
try:
    from ...dyn.reflection.x_singleton_type_description import XSingletonTypeDescription as XSingletonTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_singleton_type_description2 import XSingletonTypeDescription2 as XSingletonTypeDescription2
except ImportError:
    pass
try:
    from ...dyn.reflection.x_struct_type_description import XStructTypeDescription as XStructTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_type_description import XTypeDescription as XTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.x_type_description_enumeration import XTypeDescriptionEnumeration as XTypeDescriptionEnumeration
except ImportError:
    pass
try:
    from ...dyn.reflection.x_type_description_enumeration_access import XTypeDescriptionEnumerationAccess as XTypeDescriptionEnumerationAccess
except ImportError:
    pass
try:
    from ...dyn.reflection.x_union_type_description import XUnionTypeDescription as XUnionTypeDescription
except ImportError:
    pass
try:
    from ...dyn.reflection.the_core_reflection import theCoreReflection as theCoreReflection
except ImportError:
    pass
