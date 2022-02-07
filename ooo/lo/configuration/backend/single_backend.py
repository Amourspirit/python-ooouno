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
# Namespace: com.sun.star.configuration.backend
from .x_backend_entities import XBackendEntities as XBackendEntities_fecf13bb
from .x_multi_layer_stratum import XMultiLayerStratum as XMultiLayerStratum_2a5314c6
from .x_schema_supplier import XSchemaSupplier as XSchemaSupplier_eca11373

class SingleBackend(XBackendEntities_fecf13bb, XMultiLayerStratum_2a5314c6, XSchemaSupplier_eca11373):
    """
    Service Class

    is a configuration storage backends containing a complete configuration database, including user data, default or policy layers and schemata.
    
    Configuration data is organized into layers which are selected by components and entities.
    
    Components are characterized by configuration schemas. A component contains configuration data for a particular application domain or software module.
    
    Entities are organized hierarchically in organizations, groups, roles and individual users. Each element of the associated hierarchy corresponds to a layer that applies to an entity.
    
    Layers contains data for multiple components associated to a single entity.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SingleBackend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1SingleBackend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.SingleBackend'
    __ooo_type_name__: str = 'service'


__all__ = ['SingleBackend']

