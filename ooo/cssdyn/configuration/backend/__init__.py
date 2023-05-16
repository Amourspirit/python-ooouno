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
    from ....dyn.configuration.backend.authentication_failed_exception import AuthenticationFailedException as AuthenticationFailedException
with suppress(ImportError):
    from ....dyn.configuration.backend.backend import Backend as Backend
with suppress(ImportError):
    from ....dyn.configuration.backend.backend_access_exception import BackendAccessException as BackendAccessException
with suppress(ImportError):
    from ....dyn.configuration.backend.backend_adapter import BackendAdapter as BackendAdapter
with suppress(ImportError):
    from ....dyn.configuration.backend.backend_setup_exception import BackendSetupException as BackendSetupException
with suppress(ImportError):
    from ....dyn.configuration.backend.cannot_connect_exception import CannotConnectException as CannotConnectException
with suppress(ImportError):
    from ....dyn.configuration.backend.component_change_event import ComponentChangeEvent as ComponentChangeEvent
with suppress(ImportError):
    from ....dyn.configuration.backend.connection_lost_exception import ConnectionLostException as ConnectionLostException
with suppress(ImportError):
    from ....dyn.configuration.backend.copy_importer import CopyImporter as CopyImporter
with suppress(ImportError):
    from ....dyn.configuration.backend.data_importer import DataImporter as DataImporter
with suppress(ImportError):
    from ....dyn.configuration.backend.default_backend import DefaultBackend as DefaultBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.hierarchy_browser import HierarchyBrowser as HierarchyBrowser
with suppress(ImportError):
    from ....dyn.configuration.backend.importer import Importer as Importer
with suppress(ImportError):
    from ....dyn.configuration.backend.insufficient_access_rights_exception import InsufficientAccessRightsException as InsufficientAccessRightsException
with suppress(ImportError):
    from ....dyn.configuration.backend.interaction_handler import InteractionHandler as InteractionHandler
with suppress(ImportError):
    from ....dyn.configuration.backend.invalid_authentication_mechanism_exception import InvalidAuthenticationMechanismException as InvalidAuthenticationMechanismException
with suppress(ImportError):
    from ....dyn.configuration.backend.layer import Layer as Layer
with suppress(ImportError):
    from ....dyn.configuration.backend.layer_describer import LayerDescriber as LayerDescriber
with suppress(ImportError):
    from ....dyn.configuration.backend.layer_filter import LayerFilter as LayerFilter
with suppress(ImportError):
    from ....dyn.configuration.backend.layer_update_merger import LayerUpdateMerger as LayerUpdateMerger
with suppress(ImportError):
    from ....dyn.configuration.backend.ldap_multi_layer_stratum import LdapMultiLayerStratum as LdapMultiLayerStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.ldap_single_backend import LdapSingleBackend as LdapSingleBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.ldap_single_stratum import LdapSingleStratum as LdapSingleStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.local_data_importer import LocalDataImporter as LocalDataImporter
with suppress(ImportError):
    from ....dyn.configuration.backend.local_hierarchy_browser import LocalHierarchyBrowser as LocalHierarchyBrowser
with suppress(ImportError):
    from ....dyn.configuration.backend.local_schema_supplier import LocalSchemaSupplier as LocalSchemaSupplier
with suppress(ImportError):
    from ....dyn.configuration.backend.local_single_backend import LocalSingleBackend as LocalSingleBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.local_single_stratum import LocalSingleStratum as LocalSingleStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.malformed_data_exception import MalformedDataException as MalformedDataException
with suppress(ImportError):
    from ....dyn.configuration.backend.merge_importer import MergeImporter as MergeImporter
with suppress(ImportError):
    from ....dyn.configuration.backend.merge_recovery_request import MergeRecoveryRequest as MergeRecoveryRequest
with suppress(ImportError):
    from ....dyn.configuration.backend.multi_layer_stratum import MultiLayerStratum as MultiLayerStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.multi_stratum_backend import MultiStratumBackend as MultiStratumBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.node_attribute import NodeAttribute as NodeAttribute
with suppress(ImportError):
    from ....dyn.configuration.backend.node_attribute import NodeAttributeEnum as NodeAttributeEnum
with suppress(ImportError):
    from ....dyn.configuration.backend.offline_backend import OfflineBackend as OfflineBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.online_backend import OnlineBackend as OnlineBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.platform_backend import PlatformBackend as PlatformBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.property_info import PropertyInfo as PropertyInfo
with suppress(ImportError):
    from ....dyn.configuration.backend.schema import Schema as Schema
with suppress(ImportError):
    from ....dyn.configuration.backend.schema_attribute import SchemaAttribute as SchemaAttribute
with suppress(ImportError):
    from ....dyn.configuration.backend.schema_attribute import SchemaAttributeEnum as SchemaAttributeEnum
with suppress(ImportError):
    from ....dyn.configuration.backend.schema_supplier import SchemaSupplier as SchemaSupplier
with suppress(ImportError):
    from ....dyn.configuration.backend.single_backend import SingleBackend as SingleBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.single_backend_adapter import SingleBackendAdapter as SingleBackendAdapter
with suppress(ImportError):
    from ....dyn.configuration.backend.single_layer_stratum import SingleLayerStratum as SingleLayerStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.stratum_creation_exception import StratumCreationException as StratumCreationException
with suppress(ImportError):
    from ....dyn.configuration.backend.system_integration import SystemIntegration as SystemIntegration
with suppress(ImportError):
    from ....dyn.configuration.backend.template_identifier import TemplateIdentifier as TemplateIdentifier
with suppress(ImportError):
    from ....dyn.configuration.backend.updatable_layer import UpdatableLayer as UpdatableLayer
with suppress(ImportError):
    from ....dyn.configuration.backend.x_backend import XBackend as XBackend
with suppress(ImportError):
    from ....dyn.configuration.backend.x_backend_changes_listener import XBackendChangesListener as XBackendChangesListener
with suppress(ImportError):
    from ....dyn.configuration.backend.x_backend_changes_notifier import XBackendChangesNotifier as XBackendChangesNotifier
with suppress(ImportError):
    from ....dyn.configuration.backend.x_backend_entities import XBackendEntities as XBackendEntities
with suppress(ImportError):
    from ....dyn.configuration.backend.x_composite_layer import XCompositeLayer as XCompositeLayer
with suppress(ImportError):
    from ....dyn.configuration.backend.x_layer import XLayer as XLayer
with suppress(ImportError):
    from ....dyn.configuration.backend.x_layer_content_describer import XLayerContentDescriber as XLayerContentDescriber
with suppress(ImportError):
    from ....dyn.configuration.backend.x_layer_handler import XLayerHandler as XLayerHandler
with suppress(ImportError):
    from ....dyn.configuration.backend.x_layer_importer import XLayerImporter as XLayerImporter
with suppress(ImportError):
    from ....dyn.configuration.backend.x_multi_layer_stratum import XMultiLayerStratum as XMultiLayerStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.x_schema import XSchema as XSchema
with suppress(ImportError):
    from ....dyn.configuration.backend.x_schema_handler import XSchemaHandler as XSchemaHandler
with suppress(ImportError):
    from ....dyn.configuration.backend.x_schema_supplier import XSchemaSupplier as XSchemaSupplier
with suppress(ImportError):
    from ....dyn.configuration.backend.x_single_layer_stratum import XSingleLayerStratum as XSingleLayerStratum
with suppress(ImportError):
    from ....dyn.configuration.backend.x_updatable_layer import XUpdatableLayer as XUpdatableLayer
with suppress(ImportError):
    from ....dyn.configuration.backend.x_update_handler import XUpdateHandler as XUpdateHandler
with suppress(ImportError):
    from ....dyn.configuration.backend.x_versioned_schema_supplier import XVersionedSchemaSupplier as XVersionedSchemaSupplier
