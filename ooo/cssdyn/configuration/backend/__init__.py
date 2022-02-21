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
    from ....dyn.configuration.backend.authentication_failed_exception import AuthenticationFailedException as AuthenticationFailedException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.backend import Backend as Backend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.backend_access_exception import BackendAccessException as BackendAccessException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.backend_adapter import BackendAdapter as BackendAdapter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.backend_setup_exception import BackendSetupException as BackendSetupException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.cannot_connect_exception import CannotConnectException as CannotConnectException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.component_change_event import ComponentChangeEvent as ComponentChangeEvent
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.connection_lost_exception import ConnectionLostException as ConnectionLostException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.copy_importer import CopyImporter as CopyImporter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.data_importer import DataImporter as DataImporter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.default_backend import DefaultBackend as DefaultBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.hierarchy_browser import HierarchyBrowser as HierarchyBrowser
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.importer import Importer as Importer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.insufficient_access_rights_exception import InsufficientAccessRightsException as InsufficientAccessRightsException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.interaction_handler import InteractionHandler as InteractionHandler
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.invalid_authentication_mechanism_exception import InvalidAuthenticationMechanismException as InvalidAuthenticationMechanismException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.layer import Layer as Layer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.layer_describer import LayerDescriber as LayerDescriber
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.layer_filter import LayerFilter as LayerFilter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.layer_update_merger import LayerUpdateMerger as LayerUpdateMerger
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.ldap_multi_layer_stratum import LdapMultiLayerStratum as LdapMultiLayerStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.ldap_single_backend import LdapSingleBackend as LdapSingleBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.ldap_single_stratum import LdapSingleStratum as LdapSingleStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.local_data_importer import LocalDataImporter as LocalDataImporter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.local_hierarchy_browser import LocalHierarchyBrowser as LocalHierarchyBrowser
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.local_schema_supplier import LocalSchemaSupplier as LocalSchemaSupplier
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.local_single_backend import LocalSingleBackend as LocalSingleBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.local_single_stratum import LocalSingleStratum as LocalSingleStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.malformed_data_exception import MalformedDataException as MalformedDataException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.merge_importer import MergeImporter as MergeImporter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.merge_recovery_request import MergeRecoveryRequest as MergeRecoveryRequest
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.multi_layer_stratum import MultiLayerStratum as MultiLayerStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.multi_stratum_backend import MultiStratumBackend as MultiStratumBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.node_attribute import NodeAttribute as NodeAttribute
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.node_attribute import NodeAttributeEnum as NodeAttributeEnum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.offline_backend import OfflineBackend as OfflineBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.online_backend import OnlineBackend as OnlineBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.platform_backend import PlatformBackend as PlatformBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.property_info import PropertyInfo as PropertyInfo
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.schema import Schema as Schema
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.schema_attribute import SchemaAttribute as SchemaAttribute
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.schema_attribute import SchemaAttributeEnum as SchemaAttributeEnum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.schema_supplier import SchemaSupplier as SchemaSupplier
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.single_backend import SingleBackend as SingleBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.single_backend_adapter import SingleBackendAdapter as SingleBackendAdapter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.single_layer_stratum import SingleLayerStratum as SingleLayerStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.stratum_creation_exception import StratumCreationException as StratumCreationException
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.system_integration import SystemIntegration as SystemIntegration
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.template_identifier import TemplateIdentifier as TemplateIdentifier
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.updatable_layer import UpdatableLayer as UpdatableLayer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_backend import XBackend as XBackend
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_backend_changes_listener import XBackendChangesListener as XBackendChangesListener
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_backend_changes_notifier import XBackendChangesNotifier as XBackendChangesNotifier
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_backend_entities import XBackendEntities as XBackendEntities
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_composite_layer import XCompositeLayer as XCompositeLayer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_layer import XLayer as XLayer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_layer_content_describer import XLayerContentDescriber as XLayerContentDescriber
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_layer_handler import XLayerHandler as XLayerHandler
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_layer_importer import XLayerImporter as XLayerImporter
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_multi_layer_stratum import XMultiLayerStratum as XMultiLayerStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_schema import XSchema as XSchema
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_schema_handler import XSchemaHandler as XSchemaHandler
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_schema_supplier import XSchemaSupplier as XSchemaSupplier
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_single_layer_stratum import XSingleLayerStratum as XSingleLayerStratum
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_updatable_layer import XUpdatableLayer as XUpdatableLayer
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_update_handler import XUpdateHandler as XUpdateHandler
except ImportError:
    pass
try:
    from ....dyn.configuration.backend.x_versioned_schema_supplier import XVersionedSchemaSupplier as XVersionedSchemaSupplier
except ImportError:
    pass
