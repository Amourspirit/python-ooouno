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
from ...dyn.embed.actions import Actions as Actions
from ...dyn.embed.actions import ActionsEnum as ActionsEnum
from ...dyn.embed.aspects import Aspects as Aspects
from ...dyn.embed.aspects import AspectsEnum as AspectsEnum
from ...dyn.embed.base_storage import BaseStorage as BaseStorage
from ...dyn.embed.document_closer import DocumentCloser as DocumentCloser
from ...dyn.embed.element_modes import ElementModes as ElementModes
from ...dyn.embed.element_modes import ElementModesEnum as ElementModesEnum
from ...dyn.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits
from ...dyn.embed.embed_map_units import EmbedMapUnitsEnum as EmbedMapUnitsEnum
from ...dyn.embed.embed_misc import EmbedMisc as EmbedMisc
from ...dyn.embed.embed_misc import EmbedMiscEnum as EmbedMiscEnum
from ...dyn.embed.embed_states import EmbedStates as EmbedStates
from ...dyn.embed.embed_states import EmbedStatesEnum as EmbedStatesEnum
from ...dyn.embed.embed_update_modes import EmbedUpdateModes as EmbedUpdateModes
from ...dyn.embed.embed_update_modes import EmbedUpdateModesEnum as EmbedUpdateModesEnum
from ...dyn.embed.embed_verbs import EmbedVerbs as EmbedVerbs
from ...dyn.embed.embed_verbs import EmbedVerbsEnum as EmbedVerbsEnum
from ...dyn.embed.embedded_object_creator import EmbeddedObjectCreator as EmbeddedObjectCreator
from ...dyn.embed.embedded_object_descriptor import EmbeddedObjectDescriptor as EmbeddedObjectDescriptor
from ...dyn.embed.entry_init_modes import EntryInitModes as EntryInitModes
from ...dyn.embed.entry_init_modes import EntryInitModesEnum as EntryInitModesEnum
from ...dyn.embed.file_system_storage import FileSystemStorage as FileSystemStorage
from ...dyn.embed.file_system_storage_factory import FileSystemStorageFactory as FileSystemStorageFactory
from ...dyn.embed.hatch_window_factory import HatchWindowFactory as HatchWindowFactory
from ...dyn.embed.inserted_object_info import InsertedObjectInfo as InsertedObjectInfo
from ...dyn.embed.instance_locker import InstanceLocker as InstanceLocker
from ...dyn.embed.invalid_storage_exception import InvalidStorageException as InvalidStorageException
from ...dyn.embed.linkage_misuse_exception import LinkageMisuseException as LinkageMisuseException
from ...dyn.embed.msole_object_system_creator import MSOLEObjectSystemCreator as MSOLEObjectSystemCreator
from ...dyn.embed.needs_running_state_exception import NeedsRunningStateException as NeedsRunningStateException
from ...dyn.embed.no_visual_area_size_exception import NoVisualAreaSizeException as NoVisualAreaSizeException
from ...dyn.embed.ole_embedded_object_factory import OLEEmbeddedObjectFactory as OLEEmbeddedObjectFactory
from ...dyn.embed.ole_simple_storage import OLESimpleStorage as OLESimpleStorage
from ...dyn.embed.o_oo_embedded_object_factory import OOoEmbeddedObjectFactory as OOoEmbeddedObjectFactory
from ...dyn.embed.object_save_veto_exception import ObjectSaveVetoException as ObjectSaveVetoException
from ...dyn.embed.state_change_in_progress_exception import StateChangeInProgressException as StateChangeInProgressException
from ...dyn.embed.storage import Storage as Storage
from ...dyn.embed.storage_factory import StorageFactory as StorageFactory
from ...dyn.embed.storage_formats import StorageFormats as StorageFormats
from ...dyn.embed.storage_formats import StorageFormatsEnum as StorageFormatsEnum
from ...dyn.embed.storage_stream import StorageStream as StorageStream
from ...dyn.embed.storage_wrapped_target_exception import StorageWrappedTargetException as StorageWrappedTargetException
from ...dyn.embed.unreachable_state_exception import UnreachableStateException as UnreachableStateException
from ...dyn.embed.use_backup_exception import UseBackupException as UseBackupException
from ...dyn.embed.verb_attributes import VerbAttributes as VerbAttributes
from ...dyn.embed.verb_attributes import VerbAttributesEnum as VerbAttributesEnum
from ...dyn.embed.verb_descriptor import VerbDescriptor as VerbDescriptor
from ...dyn.embed.visual_representation import VisualRepresentation as VisualRepresentation
from ...dyn.embed.wrong_state_exception import WrongStateException as WrongStateException
from ...dyn.embed.x_actions_approval import XActionsApproval as XActionsApproval
from ...dyn.embed.x_classified_object import XClassifiedObject as XClassifiedObject
from ...dyn.embed.x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist
from ...dyn.embed.x_component_supplier import XComponentSupplier as XComponentSupplier
from ...dyn.embed.x_embed_object_clipboard_creator import XEmbedObjectClipboardCreator as XEmbedObjectClipboardCreator
from ...dyn.embed.x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator
from ...dyn.embed.x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory
from ...dyn.embed.x_embed_persist import XEmbedPersist as XEmbedPersist
from ...dyn.embed.x_embed_persist2 import XEmbedPersist2 as XEmbedPersist2
from ...dyn.embed.x_embedded_client import XEmbeddedClient as XEmbeddedClient
from ...dyn.embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject
from ...dyn.embed.x_embedded_object_creator import XEmbeddedObjectCreator as XEmbeddedObjectCreator
from ...dyn.embed.x_embedded_ole_object import XEmbeddedOleObject as XEmbeddedOleObject
from ...dyn.embed.x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource
from ...dyn.embed.x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2
from ...dyn.embed.x_encryption_protected_storage import XEncryptionProtectedStorage as XEncryptionProtectedStorage
from ...dyn.embed.x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream
from ...dyn.embed.x_hatch_window import XHatchWindow as XHatchWindow
from ...dyn.embed.x_hatch_window_controller import XHatchWindowController as XHatchWindowController
from ...dyn.embed.x_hatch_window_factory import XHatchWindowFactory as XHatchWindowFactory
from ...dyn.embed.x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess
from ...dyn.embed.x_hierarchical_storage_access2 import XHierarchicalStorageAccess2 as XHierarchicalStorageAccess2
from ...dyn.embed.x_inplace_client import XInplaceClient as XInplaceClient
from ...dyn.embed.x_inplace_object import XInplaceObject as XInplaceObject
from ...dyn.embed.x_insert_object_dialog import XInsertObjectDialog as XInsertObjectDialog
from ...dyn.embed.x_link_creator import XLinkCreator as XLinkCreator
from ...dyn.embed.x_link_factory import XLinkFactory as XLinkFactory
from ...dyn.embed.x_linkage_support import XLinkageSupport as XLinkageSupport
from ...dyn.embed.xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage
from ...dyn.embed.x_optimized_storage import XOptimizedStorage as XOptimizedStorage
from ...dyn.embed.x_package_structure_creator import XPackageStructureCreator as XPackageStructureCreator
from ...dyn.embed.x_persistance_holder import XPersistanceHolder as XPersistanceHolder
from ...dyn.embed.x_relationship_access import XRelationshipAccess as XRelationshipAccess
from ...dyn.embed.x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster
from ...dyn.embed.x_state_change_listener import XStateChangeListener as XStateChangeListener
from ...dyn.embed.x_storage import XStorage as XStorage
from ...dyn.embed.x_storage2 import XStorage2 as XStorage2
from ...dyn.embed.x_storage_raw_access import XStorageRawAccess as XStorageRawAccess
from ...dyn.embed.x_transacted_object import XTransactedObject as XTransactedObject
from ...dyn.embed.x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster
from ...dyn.embed.x_transaction_listener import XTransactionListener as XTransactionListener
from ...dyn.embed.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
from ...dyn.embed.x_visual_object import XVisualObject as XVisualObject
from ...dyn.embed.x_window_supplier import XWindowSupplier as XWindowSupplier
