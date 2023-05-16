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
    from ...dyn.container.container_event import ContainerEvent as ContainerEvent
with suppress(ImportError):
    from ...dyn.container.element_exist_exception import ElementExistException as ElementExistException
with suppress(ImportError):
    from ...dyn.container.enumerable_map import EnumerableMap as EnumerableMap
with suppress(ImportError):
    from ...dyn.container.no_such_element_exception import NoSuchElementException as NoSuchElementException
with suppress(ImportError):
    from ...dyn.container.x_child import XChild as XChild
with suppress(ImportError):
    from ...dyn.container.x_component_enumeration import XComponentEnumeration as XComponentEnumeration
with suppress(ImportError):
    from ...dyn.container.x_component_enumeration_access import XComponentEnumerationAccess as XComponentEnumerationAccess
with suppress(ImportError):
    from ...dyn.container.x_container import XContainer as XContainer
with suppress(ImportError):
    from ...dyn.container.x_container_approve_broadcaster import XContainerApproveBroadcaster as XContainerApproveBroadcaster
with suppress(ImportError):
    from ...dyn.container.x_container_approve_listener import XContainerApproveListener as XContainerApproveListener
with suppress(ImportError):
    from ...dyn.container.x_container_listener import XContainerListener as XContainerListener
with suppress(ImportError):
    from ...dyn.container.x_container_query import XContainerQuery as XContainerQuery
with suppress(ImportError):
    from ...dyn.container.x_content_enumeration_access import XContentEnumerationAccess as XContentEnumerationAccess
with suppress(ImportError):
    from ...dyn.container.x_element_access import XElementAccess as XElementAccess
with suppress(ImportError):
    from ...dyn.container.x_enumerable_map import XEnumerableMap as XEnumerableMap
with suppress(ImportError):
    from ...dyn.container.x_enumeration import XEnumeration as XEnumeration
with suppress(ImportError):
    from ...dyn.container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess
with suppress(ImportError):
    from ...dyn.container.x_hierarchical_name import XHierarchicalName as XHierarchicalName
with suppress(ImportError):
    from ...dyn.container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess
with suppress(ImportError):
    from ...dyn.container.x_hierarchical_name_container import XHierarchicalNameContainer as XHierarchicalNameContainer
with suppress(ImportError):
    from ...dyn.container.x_hierarchical_name_replace import XHierarchicalNameReplace as XHierarchicalNameReplace
with suppress(ImportError):
    from ...dyn.container.x_identifier_access import XIdentifierAccess as XIdentifierAccess
with suppress(ImportError):
    from ...dyn.container.x_identifier_container import XIdentifierContainer as XIdentifierContainer
with suppress(ImportError):
    from ...dyn.container.x_identifier_replace import XIdentifierReplace as XIdentifierReplace
with suppress(ImportError):
    from ...dyn.container.x_implicit_id_access import XImplicitIDAccess as XImplicitIDAccess
with suppress(ImportError):
    from ...dyn.container.x_implicit_id_container import XImplicitIDContainer as XImplicitIDContainer
with suppress(ImportError):
    from ...dyn.container.x_implicit_id_replace import XImplicitIDReplace as XImplicitIDReplace
with suppress(ImportError):
    from ...dyn.container.x_index_access import XIndexAccess as XIndexAccess
with suppress(ImportError):
    from ...dyn.container.x_index_container import XIndexContainer as XIndexContainer
with suppress(ImportError):
    from ...dyn.container.x_index_replace import XIndexReplace as XIndexReplace
with suppress(ImportError):
    from ...dyn.container.x_map import XMap as XMap
with suppress(ImportError):
    from ...dyn.container.x_name_access import XNameAccess as XNameAccess
with suppress(ImportError):
    from ...dyn.container.x_name_container import XNameContainer as XNameContainer
with suppress(ImportError):
    from ...dyn.container.x_name_replace import XNameReplace as XNameReplace
with suppress(ImportError):
    from ...dyn.container.x_named import XNamed as XNamed
with suppress(ImportError):
    from ...dyn.container.x_set import XSet as XSet
with suppress(ImportError):
    from ...dyn.container.x_string_key_map import XStringKeyMap as XStringKeyMap
with suppress(ImportError):
    from ...dyn.container.x_unique_id_access import XUniqueIDAccess as XUniqueIDAccess
