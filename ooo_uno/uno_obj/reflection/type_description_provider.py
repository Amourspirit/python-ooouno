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
# Libre Office Version: 7.2
# Namespace: com.sun.star.reflection
from ..container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess_9e2611b5
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_type_description_enumeration_access import XTypeDescriptionEnumerationAccess as XTypeDescriptionEnumerationAccess_8417168a

class TypeDescriptionProvider(XHierarchicalNameAccess_9e2611b5, XComponent_98dc0ab5, XTypeDescriptionEnumerationAccess_8417168a):
    """
    This service provides type descriptions, i.e.
    
    concrete service implementations read from source like the persistent registry database format.
    
    This old-style service definition mostly serves documentation purposes. It is not intended that an implementation of this service can be obtained at the global service manager using this service identifier.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TypeDescriptionProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1TypeDescriptionProvider.html>`_
    """


__all__ = ['TypeDescriptionProvider']

