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
    from ...dyn.container.container_event import ContainerEvent as ContainerEvent
except ImportError:
    pass
try:
    from ...dyn.container.element_exist_exception import ElementExistException as ElementExistException
except ImportError:
    pass
try:
    from ...dyn.container.enumerable_map import EnumerableMap as EnumerableMap
except ImportError:
    pass
try:
    from ...dyn.container.no_such_element_exception import NoSuchElementException as NoSuchElementException
except ImportError:
    pass
try:
    from ...dyn.container.x_child import XChild as XChild
except ImportError:
    pass
try:
    from ...dyn.container.x_component_enumeration import XComponentEnumeration as XComponentEnumeration
except ImportError:
    pass
try:
    from ...dyn.container.x_component_enumeration_access import XComponentEnumerationAccess as XComponentEnumerationAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_container import XContainer as XContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_container_approve_broadcaster import XContainerApproveBroadcaster as XContainerApproveBroadcaster
except ImportError:
    pass
try:
    from ...dyn.container.x_container_approve_listener import XContainerApproveListener as XContainerApproveListener
except ImportError:
    pass
try:
    from ...dyn.container.x_container_listener import XContainerListener as XContainerListener
except ImportError:
    pass
try:
    from ...dyn.container.x_container_query import XContainerQuery as XContainerQuery
except ImportError:
    pass
try:
    from ...dyn.container.x_content_enumeration_access import XContentEnumerationAccess as XContentEnumerationAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_element_access import XElementAccess as XElementAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_enumerable_map import XEnumerableMap as XEnumerableMap
except ImportError:
    pass
try:
    from ...dyn.container.x_enumeration import XEnumeration as XEnumeration
except ImportError:
    pass
try:
    from ...dyn.container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_hierarchical_name import XHierarchicalName as XHierarchicalName
except ImportError:
    pass
try:
    from ...dyn.container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_hierarchical_name_container import XHierarchicalNameContainer as XHierarchicalNameContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_hierarchical_name_replace import XHierarchicalNameReplace as XHierarchicalNameReplace
except ImportError:
    pass
try:
    from ...dyn.container.x_identifier_access import XIdentifierAccess as XIdentifierAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_identifier_container import XIdentifierContainer as XIdentifierContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_identifier_replace import XIdentifierReplace as XIdentifierReplace
except ImportError:
    pass
try:
    from ...dyn.container.x_implicit_id_access import XImplicitIDAccess as XImplicitIDAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_implicit_id_container import XImplicitIDContainer as XImplicitIDContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_implicit_id_replace import XImplicitIDReplace as XImplicitIDReplace
except ImportError:
    pass
try:
    from ...dyn.container.x_index_access import XIndexAccess as XIndexAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_index_container import XIndexContainer as XIndexContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_index_replace import XIndexReplace as XIndexReplace
except ImportError:
    pass
try:
    from ...dyn.container.x_map import XMap as XMap
except ImportError:
    pass
try:
    from ...dyn.container.x_name_access import XNameAccess as XNameAccess
except ImportError:
    pass
try:
    from ...dyn.container.x_name_container import XNameContainer as XNameContainer
except ImportError:
    pass
try:
    from ...dyn.container.x_name_replace import XNameReplace as XNameReplace
except ImportError:
    pass
try:
    from ...dyn.container.x_named import XNamed as XNamed
except ImportError:
    pass
try:
    from ...dyn.container.x_set import XSet as XSet
except ImportError:
    pass
try:
    from ...dyn.container.x_string_key_map import XStringKeyMap as XStringKeyMap
except ImportError:
    pass
try:
    from ...dyn.container.x_unique_id_access import XUniqueIDAccess as XUniqueIDAccess
except ImportError:
    pass
