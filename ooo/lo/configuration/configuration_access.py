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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.configuration
from __future__ import annotations
from .access_root_element import AccessRootElement as AccessRootElement_7fef1140
from .group_access import GroupAccess as GroupAccess_1f8f0edf
from .group_element import GroupElement as GroupElement_2f2a0f57
from .set_access import SetAccess as SetAccess_1ae0dfe
from .set_element import SetElement as SetElement_10680e76

class ConfigurationAccess(AccessRootElement_7fef1140, GroupAccess_1f8f0edf, GroupElement_2f2a0f57, SetAccess_1ae0dfe, SetElement_10680e76):
    """
    Service Class

    provides read access to a fragment of the configuration hierarchy.
    
    Values that are direct or indirect descendants of a root element can be retrieved and, if themselves objects, navigated. Other interfaces provide access to information about this element and its context. Changes to values in the hierarchy can be monitored by event listeners.
    
    Descendants of this service also implement this service.
    
    Ultimately the configuration holds values. These values are organized into a hierarchy using structural elements. The structure is defined in advance in a schema. Necessary information from the schema is stored in the configuration repository itself and is accessible through an implementation of this service.
    
    Two different kinds of structural elements are used in the configuration hierarchy:
    
    Objects in the configuration hierarchy, for example, implementations of this service, can thus be classified in the following ways:
    
    Several types of simple values can be used in the configuration. In addition to the basic (scalar) types, sequences of the basic types are supported. The basic types are:
    
    Within templates an additional type any can occur. When such a template is used to create a new SetElement, the type of the element is initially reported as any (having no value). When the value of such an element is first set, it will assume the type used.
    
    If the schema marks a value as nullable (which is indicated by attribute com.sun.star.beans.PropertyAttribute.MAYBEVOID ), its contents may be NULL.
    
    The configuration should support explicit access to default values (implementing com.sun.star.beans.XPropertyState and com.sun.star.beans.XPropertyWithState).

    See Also:
        `API ConfigurationAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1ConfigurationAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.ConfigurationAccess'
    __ooo_type_name__: str = 'service'


__all__ = ['ConfigurationAccess']

