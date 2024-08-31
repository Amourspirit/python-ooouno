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
    from ...dyn.beans.get_direct_property_tolerant_result import GetDirectPropertyTolerantResult as GetDirectPropertyTolerantResult
with suppress(ImportError):
    from ...dyn.beans.get_property_tolerant_result import GetPropertyTolerantResult as GetPropertyTolerantResult
with suppress(ImportError):
    from ...dyn.beans.illegal_type_exception import IllegalTypeException as IllegalTypeException
with suppress(ImportError):
    from ...dyn.beans.introspection import Introspection as Introspection
with suppress(ImportError):
    from ...dyn.beans.introspection_exception import IntrospectionException as IntrospectionException
with suppress(ImportError):
    from ...dyn.beans.method_concept import MethodConcept as MethodConcept
with suppress(ImportError):
    from ...dyn.beans.method_concept import MethodConceptEnum as MethodConceptEnum
with suppress(ImportError):
    from ...dyn.beans.named_value import NamedValue as NamedValue
with suppress(ImportError):
    from ...dyn.beans.not_removeable_exception import NotRemoveableException as NotRemoveableException
with suppress(ImportError):
    from ...dyn.beans.property import Property as Property
with suppress(ImportError):
    from ...dyn.beans.property_attribute import PropertyAttribute as PropertyAttribute
with suppress(ImportError):
    from ...dyn.beans.property_attribute import PropertyAttributeEnum as PropertyAttributeEnum
with suppress(ImportError):
    from ...dyn.beans.property_bag import PropertyBag as PropertyBag
with suppress(ImportError):
    from ...dyn.beans.property_change_event import PropertyChangeEvent as PropertyChangeEvent
with suppress(ImportError):
    from ...dyn.beans.property_concept import PropertyConcept as PropertyConcept
with suppress(ImportError):
    from ...dyn.beans.property_concept import PropertyConceptEnum as PropertyConceptEnum
with suppress(ImportError):
    from ...dyn.beans.property_exist_exception import PropertyExistException as PropertyExistException
with suppress(ImportError):
    from ...dyn.beans.property_set import PropertySet as PropertySet
with suppress(ImportError):
    from ...dyn.beans.property_set_info_change import PropertySetInfoChange as PropertySetInfoChange
with suppress(ImportError):
    from ...dyn.beans.property_set_info_change import PropertySetInfoChangeEnum as PropertySetInfoChangeEnum
with suppress(ImportError):
    from ...dyn.beans.property_set_info_change_event import PropertySetInfoChangeEvent as PropertySetInfoChangeEvent
with suppress(ImportError):
    from ...dyn.beans.property_state import PropertyState as PropertyState
with suppress(ImportError):
    from ...dyn.beans.property_state_change_event import PropertyStateChangeEvent as PropertyStateChangeEvent
with suppress(ImportError):
    from ...dyn.beans.property_value import PropertyValue as PropertyValue
with suppress(ImportError):
    from ...dyn.beans.property_values import PropertyValues as PropertyValues
with suppress(ImportError):
    from ...dyn.beans.property_veto_exception import PropertyVetoException as PropertyVetoException
with suppress(ImportError):
    from ...dyn.beans.set_property_tolerant_failed import SetPropertyTolerantFailed as SetPropertyTolerantFailed
with suppress(ImportError):
    from ...dyn.beans.string_pair import StringPair as StringPair
with suppress(ImportError):
    from ...dyn.beans.tolerant_property_set_result_type import TolerantPropertySetResultType as TolerantPropertySetResultType
with suppress(ImportError):
    from ...dyn.beans.tolerant_property_set_result_type import TolerantPropertySetResultTypeEnum as TolerantPropertySetResultTypeEnum
with suppress(ImportError):
    from ...dyn.beans.unknown_property_exception import UnknownPropertyException as UnknownPropertyException
with suppress(ImportError):
    from ...dyn.beans.x_exact_name import XExactName as XExactName
with suppress(ImportError):
    from ...dyn.beans.x_fast_property_set import XFastPropertySet as XFastPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_hierarchical_property_set import XHierarchicalPropertySet as XHierarchicalPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_hierarchical_property_set_info import XHierarchicalPropertySetInfo as XHierarchicalPropertySetInfo
with suppress(ImportError):
    from ...dyn.beans.x_introspection import XIntrospection as XIntrospection
with suppress(ImportError):
    from ...dyn.beans.x_introspection_access import XIntrospectionAccess as XIntrospectionAccess
with suppress(ImportError):
    from ...dyn.beans.x_material_holder import XMaterialHolder as XMaterialHolder
with suppress(ImportError):
    from ...dyn.beans.x_multi_hierarchical_property_set import XMultiHierarchicalPropertySet as XMultiHierarchicalPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_multi_property_set import XMultiPropertySet as XMultiPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_multi_property_states import XMultiPropertyStates as XMultiPropertyStates
with suppress(ImportError):
    from ...dyn.beans.x_properties_change_listener import XPropertiesChangeListener as XPropertiesChangeListener
with suppress(ImportError):
    from ...dyn.beans.x_properties_change_notifier import XPropertiesChangeNotifier as XPropertiesChangeNotifier
with suppress(ImportError):
    from ...dyn.beans.x_property import XProperty as XProperty
with suppress(ImportError):
    from ...dyn.beans.x_property_access import XPropertyAccess as XPropertyAccess
with suppress(ImportError):
    from ...dyn.beans.x_property_bag import XPropertyBag as XPropertyBag
with suppress(ImportError):
    from ...dyn.beans.x_property_change_listener import XPropertyChangeListener as XPropertyChangeListener
with suppress(ImportError):
    from ...dyn.beans.x_property_container import XPropertyContainer as XPropertyContainer
with suppress(ImportError):
    from ...dyn.beans.x_property_set import XPropertySet as XPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_property_set_info import XPropertySetInfo as XPropertySetInfo
with suppress(ImportError):
    from ...dyn.beans.x_property_set_info_change_listener import XPropertySetInfoChangeListener as XPropertySetInfoChangeListener
with suppress(ImportError):
    from ...dyn.beans.x_property_set_info_change_notifier import XPropertySetInfoChangeNotifier as XPropertySetInfoChangeNotifier
with suppress(ImportError):
    from ...dyn.beans.x_property_set_option import XPropertySetOption as XPropertySetOption
with suppress(ImportError):
    from ...dyn.beans.x_property_state import XPropertyState as XPropertyState
with suppress(ImportError):
    from ...dyn.beans.x_property_state_change_listener import XPropertyStateChangeListener as XPropertyStateChangeListener
with suppress(ImportError):
    from ...dyn.beans.x_property_with_state import XPropertyWithState as XPropertyWithState
with suppress(ImportError):
    from ...dyn.beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet
with suppress(ImportError):
    from ...dyn.beans.x_vetoable_change_listener import XVetoableChangeListener as XVetoableChangeListener
with suppress(ImportError):
    from ...dyn.beans.the_introspection import theIntrospection as theIntrospection
