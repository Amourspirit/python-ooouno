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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.configuration
from .access_root_element import AccessRootElement as AccessRootElement_7fef1140
from ..util.x_changes_batch import XChangesBatch as XChangesBatch_bb3b0bb9

class UpdateRootElement(AccessRootElement_7fef1140, XChangesBatch_bb3b0bb9):
    """
    Service Class

    provides update control for a hierarchy of configuration items and information about the hierarchy as a whole as well as its root.
    
    Extends AccessRootElement by adding support for collecting changes and applying them to a backend store as a single batch.
    
    An implementation represents the root of a partial hierarchy. [See the documentation for AccessRootElement]. The hierarchy in turn is a view onto a fragment of persistent data tree that can be accessed through several such views, or even several processes, simultaneously.
    
    Elements of the hierarchy, such as descendants of this root element, may support modification by providing appropriate interfaces. Changes done this way initially only affect these objects themselves and other objects within the same hierarchy, such as other descendants of this root element.
    
    The accumulated changes within this hierarchy can be managed using com.sun.star.util.XChangesBatch. Pending changes will become persistent and visible from other overlapping hierarchies only when com.sun.star.util.XChangesBatch.commitChanges() is called. If the hierarchy is disposed or discarded without committing changes, the changes will be lost.

    See Also:
        `API UpdateRootElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1UpdateRootElement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.UpdateRootElement'
    __ooo_type_name__: str = 'service'


__all__ = ['UpdateRootElement']

