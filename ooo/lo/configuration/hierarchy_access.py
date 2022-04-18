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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.configuration
from ..beans.x_exact_name import XExactName as XExactName_a3310adf
from ..beans.x_multi_property_states import XMultiPropertyStates as XMultiPropertyStates_2a3e0f4d
from ..beans.x_property_set_info import XPropertySetInfo as XPropertySetInfo_efa90d86
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess_9e2611b5
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6

class HierarchyAccess(XExactName_a3310adf, XMultiPropertyStates_2a3e0f4d, XPropertySetInfo_efa90d86, XPropertyState_d55c0ccf, XContainer_d6fb0cc6, XHierarchicalNameAccess_9e2611b5, XNameAccess_e2ab0cf6):
    """
    Service Class

    provides access to a hierarchy of descendant elements.
    
    Subnodes are accessed by their name. Values that are direct or indirect descendants of this tree node can be retrieved. Non-value subnodes can be navigated using container interfaces. Other interfaces provide access to information about this node. Changes to values in the subtree can be monitored by event listeners.
    
    Elements of this container that are not simple values are similar containers themselves, thus (recursively) forming a hierarchical tree.
    
    Implementations of this service usually also implement service HierarchyElement, which concerns the complementary role of being accessible as an element of the hierarchy.

    See Also:
        `API HierarchyAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1HierarchyAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.HierarchyAccess'
    __ooo_type_name__: str = 'service'



__all__ = ['HierarchyAccess']

