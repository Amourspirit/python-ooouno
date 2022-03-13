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
from ...lo.embed.actions import Actions as Actions
from ...lo.embed.aspects import Aspects as Aspects
from ...lo.embed.base_storage import BaseStorage as BaseStorage
from ...lo.embed.document_closer import DocumentCloser as DocumentCloser
from ...lo.embed.element_modes import ElementModes as ElementModes
from ...lo.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits
from ...lo.embed.embed_misc import EmbedMisc as EmbedMisc
from ...lo.embed.embed_states import EmbedStates as EmbedStates
from ...lo.embed.embed_update_modes import EmbedUpdateModes as EmbedUpdateModes
from ...lo.embed.embed_verbs import EmbedVerbs as EmbedVerbs
from ...lo.embed.embedded_object_creator import EmbeddedObjectCreator as EmbeddedObjectCreator
from ...lo.embed.embedded_object_descriptor import EmbeddedObjectDescriptor as EmbeddedObjectDescriptor
from ...lo.embed.entry_init_modes import EntryInitModes as EntryInitModes
from ...lo.embed.file_system_storage import FileSystemStorage as FileSystemStorage
from ...lo.embed.file_system_storage_factory import FileSystemStorageFactory as FileSystemStorageFactory
from ...lo.embed.hatch_window_factory import HatchWindowFactory as HatchWindowFactory
from ...lo.embed.inserted_object_info import InsertedObjectInfo as InsertedObjectInfo
from ...lo.embed.instance_locker import InstanceLocker as InstanceLocker
from ...lo.embed.invalid_storage_exception import InvalidStorageException as InvalidStorageException
from ...lo.embed.linkage_misuse_exception import LinkageMisuseException as LinkageMisuseException
from ...lo.embed.msole_object_system_creator import MSOLEObjectSystemCreator as MSOLEObjectSystemCreator
from ...lo.embed.needs_running_state_exception import NeedsRunningStateException as NeedsRunningStateException
from ...lo.embed.no_visual_area_size_exception import NoVisualAreaSizeException as NoVisualAreaSizeException
from ...lo.embed.ole_embedded_object_factory import OLEEmbeddedObjectFactory as OLEEmbeddedObjectFactory
from ...lo.embed.ole_simple_storage import OLESimpleStorage as OLESimpleStorage
from ...lo.embed.o_oo_embedded_object_factory import OOoEmbeddedObjectFactory as OOoEmbeddedObjectFactory
from ...lo.embed.object_save_veto_exception import ObjectSaveVetoException as ObjectSaveVetoException
from ...lo.embed.state_change_in_progress_exception import StateChangeInProgressException as StateChangeInProgressException
from ...lo.embed.storage import Storage as Storage
from ...lo.embed.storage_factory import StorageFactory as StorageFactory
from ...lo.embed.storage_formats import StorageFormats as StorageFormats
from ...lo.embed.storage_stream import StorageStream as StorageStream
from ...lo.embed.storage_wrapped_target_exception import StorageWrappedTargetException as StorageWrappedTargetException
from ...lo.embed.unreachable_state_exception import UnreachableStateException as UnreachableStateException
from ...lo.embed.use_backup_exception import UseBackupException as UseBackupException
from ...lo.embed.verb_attributes import VerbAttributes as VerbAttributes
from ...lo.embed.verb_descriptor import VerbDescriptor as VerbDescriptor
from ...lo.embed.visual_representation import VisualRepresentation as VisualRepresentation
from ...lo.embed.wrong_state_exception import WrongStateException as WrongStateException
from ...lo.embed.x_actions_approval import XActionsApproval as XActionsApproval
from ...lo.embed.x_classified_object import XClassifiedObject as XClassifiedObject
from ...lo.embed.x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist
from ...lo.embed.x_component_supplier import XComponentSupplier as XComponentSupplier
from ...lo.embed.x_embed_object_clipboard_creator import XEmbedObjectClipboardCreator as XEmbedObjectClipboardCreator
from ...lo.embed.x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator
from ...lo.embed.x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory
from ...lo.embed.x_embed_persist import XEmbedPersist as XEmbedPersist
from ...lo.embed.x_embed_persist2 import XEmbedPersist2 as XEmbedPersist2
from ...lo.embed.x_embedded_client import XEmbeddedClient as XEmbeddedClient
from ...lo.embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject
from ...lo.embed.x_embedded_object_creator import XEmbeddedObjectCreator as XEmbeddedObjectCreator
from ...lo.embed.x_embedded_ole_object import XEmbeddedOleObject as XEmbeddedOleObject
from ...lo.embed.x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource
from ...lo.embed.x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2
from ...lo.embed.x_encryption_protected_storage import XEncryptionProtectedStorage as XEncryptionProtectedStorage
from ...lo.embed.x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream
from ...lo.embed.x_hatch_window import XHatchWindow as XHatchWindow
from ...lo.embed.x_hatch_window_controller import XHatchWindowController as XHatchWindowController
from ...lo.embed.x_hatch_window_factory import XHatchWindowFactory as XHatchWindowFactory
from ...lo.embed.x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess
from ...lo.embed.x_hierarchical_storage_access2 import XHierarchicalStorageAccess2 as XHierarchicalStorageAccess2
from ...lo.embed.x_inplace_client import XInplaceClient as XInplaceClient
from ...lo.embed.x_inplace_object import XInplaceObject as XInplaceObject
from ...lo.embed.x_insert_object_dialog import XInsertObjectDialog as XInsertObjectDialog
from ...lo.embed.x_link_creator import XLinkCreator as XLinkCreator
from ...lo.embed.x_link_factory import XLinkFactory as XLinkFactory
from ...lo.embed.x_linkage_support import XLinkageSupport as XLinkageSupport
from ...lo.embed.xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage
from ...lo.embed.x_optimized_storage import XOptimizedStorage as XOptimizedStorage
from ...lo.embed.x_package_structure_creator import XPackageStructureCreator as XPackageStructureCreator
from ...lo.embed.x_persistance_holder import XPersistanceHolder as XPersistanceHolder
from ...lo.embed.x_relationship_access import XRelationshipAccess as XRelationshipAccess
from ...lo.embed.x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster
from ...lo.embed.x_state_change_listener import XStateChangeListener as XStateChangeListener
from ...lo.embed.x_storage import XStorage as XStorage
from ...lo.embed.x_storage2 import XStorage2 as XStorage2
from ...lo.embed.x_storage_raw_access import XStorageRawAccess as XStorageRawAccess
from ...lo.embed.x_transacted_object import XTransactedObject as XTransactedObject
from ...lo.embed.x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster
from ...lo.embed.x_transaction_listener import XTransactionListener as XTransactionListener
from ...lo.embed.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
from ...lo.embed.x_visual_object import XVisualObject as XVisualObject
from ...lo.embed.x_window_supplier import XWindowSupplier as XWindowSupplier
