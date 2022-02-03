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
from ...uno_obj.embed.actions import Actions as Actions
from ...uno_obj.embed.actions import ActionsEnum as ActionsEnum
from ...uno_obj.embed.aspects import Aspects as Aspects
from ...uno_obj.embed.aspects import AspectsEnum as AspectsEnum
from ...uno_obj.embed.base_storage import BaseStorage as BaseStorage
from ...uno_obj.embed.document_closer import DocumentCloser as DocumentCloser
from ...uno_obj.embed.element_modes import ElementModes as ElementModes
from ...uno_obj.embed.element_modes import ElementModesEnum as ElementModesEnum
from ...uno_obj.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits
from ...uno_obj.embed.embed_map_units import EmbedMapUnitsEnum as EmbedMapUnitsEnum
from ...uno_obj.embed.embed_misc import EmbedMisc as EmbedMisc
from ...uno_obj.embed.embed_misc import EmbedMiscEnum as EmbedMiscEnum
from ...uno_obj.embed.embed_states import EmbedStates as EmbedStates
from ...uno_obj.embed.embed_states import EmbedStatesEnum as EmbedStatesEnum
from ...uno_obj.embed.embed_update_modes import EmbedUpdateModes as EmbedUpdateModes
from ...uno_obj.embed.embed_update_modes import EmbedUpdateModesEnum as EmbedUpdateModesEnum
from ...uno_obj.embed.embed_verbs import EmbedVerbs as EmbedVerbs
from ...uno_obj.embed.embed_verbs import EmbedVerbsEnum as EmbedVerbsEnum
from ...uno_obj.embed.embedded_object_creator import EmbeddedObjectCreator as EmbeddedObjectCreator
from ...uno_obj.embed.embedded_object_descriptor import EmbeddedObjectDescriptor as EmbeddedObjectDescriptor
from ...uno_obj.embed.entry_init_modes import EntryInitModes as EntryInitModes
from ...uno_obj.embed.entry_init_modes import EntryInitModesEnum as EntryInitModesEnum
from ...uno_obj.embed.file_system_storage import FileSystemStorage as FileSystemStorage
from ...uno_obj.embed.file_system_storage_factory import FileSystemStorageFactory as FileSystemStorageFactory
from ...uno_obj.embed.hatch_window_factory import HatchWindowFactory as HatchWindowFactory
from ...uno_obj.embed.inserted_object_info import InsertedObjectInfo as InsertedObjectInfo
from ...uno_obj.embed.instance_locker import InstanceLocker as InstanceLocker
from ...uno_obj.embed.invalid_storage_exception import InvalidStorageException as InvalidStorageException
from ...uno_obj.embed.linkage_misuse_exception import LinkageMisuseException as LinkageMisuseException
from ...uno_obj.embed.msole_object_system_creator import MSOLEObjectSystemCreator as MSOLEObjectSystemCreator
from ...uno_obj.embed.needs_running_state_exception import NeedsRunningStateException as NeedsRunningStateException
from ...uno_obj.embed.no_visual_area_size_exception import NoVisualAreaSizeException as NoVisualAreaSizeException
from ...uno_obj.embed.ole_embedded_object_factory import OLEEmbeddedObjectFactory as OLEEmbeddedObjectFactory
from ...uno_obj.embed.ole_simple_storage import OLESimpleStorage as OLESimpleStorage
from ...uno_obj.embed.o_oo_embedded_object_factory import OOoEmbeddedObjectFactory as OOoEmbeddedObjectFactory
from ...uno_obj.embed.object_save_veto_exception import ObjectSaveVetoException as ObjectSaveVetoException
from ...uno_obj.embed.state_change_in_progress_exception import StateChangeInProgressException as StateChangeInProgressException
from ...uno_obj.embed.storage import Storage as Storage
from ...uno_obj.embed.storage_factory import StorageFactory as StorageFactory
from ...uno_obj.embed.storage_formats import StorageFormats as StorageFormats
from ...uno_obj.embed.storage_formats import StorageFormatsEnum as StorageFormatsEnum
from ...uno_obj.embed.storage_stream import StorageStream as StorageStream
from ...uno_obj.embed.storage_wrapped_target_exception import StorageWrappedTargetException as StorageWrappedTargetException
from ...uno_obj.embed.unreachable_state_exception import UnreachableStateException as UnreachableStateException
from ...uno_obj.embed.use_backup_exception import UseBackupException as UseBackupException
from ...uno_obj.embed.verb_attributes import VerbAttributes as VerbAttributes
from ...uno_obj.embed.verb_attributes import VerbAttributesEnum as VerbAttributesEnum
from ...uno_obj.embed.verb_descriptor import VerbDescriptor as VerbDescriptor
from ...uno_obj.embed.visual_representation import VisualRepresentation as VisualRepresentation
from ...uno_obj.embed.wrong_state_exception import WrongStateException as WrongStateException
from ...uno_obj.embed.x_actions_approval import XActionsApproval as XActionsApproval
from ...uno_obj.embed.x_classified_object import XClassifiedObject as XClassifiedObject
from ...uno_obj.embed.x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist
from ...uno_obj.embed.x_component_supplier import XComponentSupplier as XComponentSupplier
from ...uno_obj.embed.x_embed_object_clipboard_creator import XEmbedObjectClipboardCreator as XEmbedObjectClipboardCreator
from ...uno_obj.embed.x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator
from ...uno_obj.embed.x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory
from ...uno_obj.embed.x_embed_persist import XEmbedPersist as XEmbedPersist
from ...uno_obj.embed.x_embed_persist2 import XEmbedPersist2 as XEmbedPersist2
from ...uno_obj.embed.x_embedded_client import XEmbeddedClient as XEmbeddedClient
from ...uno_obj.embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject
from ...uno_obj.embed.x_embedded_object_creator import XEmbeddedObjectCreator as XEmbeddedObjectCreator
from ...uno_obj.embed.x_embedded_ole_object import XEmbeddedOleObject as XEmbeddedOleObject
from ...uno_obj.embed.x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource
from ...uno_obj.embed.x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2
from ...uno_obj.embed.x_encryption_protected_storage import XEncryptionProtectedStorage as XEncryptionProtectedStorage
from ...uno_obj.embed.x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream
from ...uno_obj.embed.x_hatch_window import XHatchWindow as XHatchWindow
from ...uno_obj.embed.x_hatch_window_controller import XHatchWindowController as XHatchWindowController
from ...uno_obj.embed.x_hatch_window_factory import XHatchWindowFactory as XHatchWindowFactory
from ...uno_obj.embed.x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess
from ...uno_obj.embed.x_hierarchical_storage_access2 import XHierarchicalStorageAccess2 as XHierarchicalStorageAccess2
from ...uno_obj.embed.x_inplace_client import XInplaceClient as XInplaceClient
from ...uno_obj.embed.x_inplace_object import XInplaceObject as XInplaceObject
from ...uno_obj.embed.x_insert_object_dialog import XInsertObjectDialog as XInsertObjectDialog
from ...uno_obj.embed.x_link_creator import XLinkCreator as XLinkCreator
from ...uno_obj.embed.x_link_factory import XLinkFactory as XLinkFactory
from ...uno_obj.embed.x_linkage_support import XLinkageSupport as XLinkageSupport
from ...uno_obj.embed.xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage
from ...uno_obj.embed.x_optimized_storage import XOptimizedStorage as XOptimizedStorage
from ...uno_obj.embed.x_package_structure_creator import XPackageStructureCreator as XPackageStructureCreator
from ...uno_obj.embed.x_persistance_holder import XPersistanceHolder as XPersistanceHolder
from ...uno_obj.embed.x_relationship_access import XRelationshipAccess as XRelationshipAccess
from ...uno_obj.embed.x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster
from ...uno_obj.embed.x_state_change_listener import XStateChangeListener as XStateChangeListener
from ...uno_obj.embed.x_storage import XStorage as XStorage
from ...uno_obj.embed.x_storage2 import XStorage2 as XStorage2
from ...uno_obj.embed.x_storage_raw_access import XStorageRawAccess as XStorageRawAccess
from ...uno_obj.embed.x_transacted_object import XTransactedObject as XTransactedObject
from ...uno_obj.embed.x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster
from ...uno_obj.embed.x_transaction_listener import XTransactionListener as XTransactionListener
from ...uno_obj.embed.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
from ...uno_obj.embed.x_visual_object import XVisualObject as XVisualObject
from ...uno_obj.embed.x_window_supplier import XWindowSupplier as XWindowSupplier
