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
    from ...dyn.beans.ambiguous import Ambiguous as Ambiguous
except ImportError:
    pass
try:
    from ...dyn.beans.defaulted import Defaulted as Defaulted
except ImportError:
    pass
try:
    from ...dyn.beans.get_direct_property_tolerant_result import GetDirectPropertyTolerantResult as GetDirectPropertyTolerantResult
except ImportError:
    pass
try:
    from ...dyn.beans.get_property_tolerant_result import GetPropertyTolerantResult as GetPropertyTolerantResult
except ImportError:
    pass
try:
    from ...dyn.beans.illegal_type_exception import IllegalTypeException as IllegalTypeException
except ImportError:
    pass
try:
    from ...dyn.beans.introspection import Introspection as Introspection
except ImportError:
    pass
try:
    from ...dyn.beans.introspection_exception import IntrospectionException as IntrospectionException
except ImportError:
    pass
try:
    from ...dyn.beans.method_concept import MethodConcept as MethodConcept
except ImportError:
    pass
try:
    from ...dyn.beans.method_concept import MethodConceptEnum as MethodConceptEnum
except ImportError:
    pass
try:
    from ...dyn.beans.named_value import NamedValue as NamedValue
except ImportError:
    pass
try:
    from ...dyn.beans.not_removeable_exception import NotRemoveableException as NotRemoveableException
except ImportError:
    pass
try:
    from ...dyn.beans.optional import Optional as Optional
except ImportError:
    pass
try:
    from ...dyn.beans.pair import Pair as Pair
except ImportError:
    pass
try:
    from ...dyn.beans.property import Property as Property
except ImportError:
    pass
try:
    from ...dyn.beans.property_attribute import PropertyAttribute as PropertyAttribute
except ImportError:
    pass
try:
    from ...dyn.beans.property_attribute import PropertyAttributeEnum as PropertyAttributeEnum
except ImportError:
    pass
try:
    from ...dyn.beans.property_bag import PropertyBag as PropertyBag
except ImportError:
    pass
try:
    from ...dyn.beans.property_change_event import PropertyChangeEvent as PropertyChangeEvent
except ImportError:
    pass
try:
    from ...dyn.beans.property_concept import PropertyConcept as PropertyConcept
except ImportError:
    pass
try:
    from ...dyn.beans.property_concept import PropertyConceptEnum as PropertyConceptEnum
except ImportError:
    pass
try:
    from ...dyn.beans.property_exist_exception import PropertyExistException as PropertyExistException
except ImportError:
    pass
try:
    from ...dyn.beans.property_set import PropertySet as PropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.property_set_info_change import PropertySetInfoChange as PropertySetInfoChange
except ImportError:
    pass
try:
    from ...dyn.beans.property_set_info_change import PropertySetInfoChangeEnum as PropertySetInfoChangeEnum
except ImportError:
    pass
try:
    from ...dyn.beans.property_set_info_change_event import PropertySetInfoChangeEvent as PropertySetInfoChangeEvent
except ImportError:
    pass
try:
    from ...dyn.beans.property_state import PropertyState as PropertyState
except ImportError:
    pass
try:
    from ...dyn.beans.property_state_change_event import PropertyStateChangeEvent as PropertyStateChangeEvent
except ImportError:
    pass
try:
    from ...dyn.beans.property_value import PropertyValue as PropertyValue
except ImportError:
    pass
try:
    from ...dyn.beans.property_values import PropertyValues as PropertyValues
except ImportError:
    pass
try:
    from ...dyn.beans.property_veto_exception import PropertyVetoException as PropertyVetoException
except ImportError:
    pass
try:
    from ...dyn.beans.set_property_tolerant_failed import SetPropertyTolerantFailed as SetPropertyTolerantFailed
except ImportError:
    pass
try:
    from ...dyn.beans.string_pair import StringPair as StringPair
except ImportError:
    pass
try:
    from ...dyn.beans.tolerant_property_set_result_type import TolerantPropertySetResultType as TolerantPropertySetResultType
except ImportError:
    pass
try:
    from ...dyn.beans.tolerant_property_set_result_type import TolerantPropertySetResultTypeEnum as TolerantPropertySetResultTypeEnum
except ImportError:
    pass
try:
    from ...dyn.beans.unknown_property_exception import UnknownPropertyException as UnknownPropertyException
except ImportError:
    pass
try:
    from ...dyn.beans.x_exact_name import XExactName as XExactName
except ImportError:
    pass
try:
    from ...dyn.beans.x_fast_property_set import XFastPropertySet as XFastPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_hierarchical_property_set import XHierarchicalPropertySet as XHierarchicalPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_hierarchical_property_set_info import XHierarchicalPropertySetInfo as XHierarchicalPropertySetInfo
except ImportError:
    pass
try:
    from ...dyn.beans.x_introspection import XIntrospection as XIntrospection
except ImportError:
    pass
try:
    from ...dyn.beans.x_introspection_access import XIntrospectionAccess as XIntrospectionAccess
except ImportError:
    pass
try:
    from ...dyn.beans.x_material_holder import XMaterialHolder as XMaterialHolder
except ImportError:
    pass
try:
    from ...dyn.beans.x_multi_hierarchical_property_set import XMultiHierarchicalPropertySet as XMultiHierarchicalPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_multi_property_set import XMultiPropertySet as XMultiPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_multi_property_states import XMultiPropertyStates as XMultiPropertyStates
except ImportError:
    pass
try:
    from ...dyn.beans.x_properties_change_listener import XPropertiesChangeListener as XPropertiesChangeListener
except ImportError:
    pass
try:
    from ...dyn.beans.x_properties_change_notifier import XPropertiesChangeNotifier as XPropertiesChangeNotifier
except ImportError:
    pass
try:
    from ...dyn.beans.x_property import XProperty as XProperty
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_access import XPropertyAccess as XPropertyAccess
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_bag import XPropertyBag as XPropertyBag
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_change_listener import XPropertyChangeListener as XPropertyChangeListener
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_container import XPropertyContainer as XPropertyContainer
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_set import XPropertySet as XPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_set_info import XPropertySetInfo as XPropertySetInfo
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_set_info_change_listener import XPropertySetInfoChangeListener as XPropertySetInfoChangeListener
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_set_info_change_notifier import XPropertySetInfoChangeNotifier as XPropertySetInfoChangeNotifier
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_set_option import XPropertySetOption as XPropertySetOption
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_state import XPropertyState as XPropertyState
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_state_change_listener import XPropertyStateChangeListener as XPropertyStateChangeListener
except ImportError:
    pass
try:
    from ...dyn.beans.x_property_with_state import XPropertyWithState as XPropertyWithState
except ImportError:
    pass
try:
    from ...dyn.beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet
except ImportError:
    pass
try:
    from ...dyn.beans.x_vetoable_change_listener import XVetoableChangeListener as XVetoableChangeListener
except ImportError:
    pass
try:
    from ...dyn.beans.the_introspection import theIntrospection as theIntrospection
except ImportError:
    pass
