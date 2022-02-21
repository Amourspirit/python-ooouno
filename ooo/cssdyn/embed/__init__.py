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
    from ...dyn.embed.actions import Actions as Actions
except ImportError:
    pass
try:
    from ...dyn.embed.actions import ActionsEnum as ActionsEnum
except ImportError:
    pass
try:
    from ...dyn.embed.aspects import Aspects as Aspects
except ImportError:
    pass
try:
    from ...dyn.embed.aspects import AspectsEnum as AspectsEnum
except ImportError:
    pass
try:
    from ...dyn.embed.base_storage import BaseStorage as BaseStorage
except ImportError:
    pass
try:
    from ...dyn.embed.document_closer import DocumentCloser as DocumentCloser
except ImportError:
    pass
try:
    from ...dyn.embed.element_modes import ElementModes as ElementModes
except ImportError:
    pass
try:
    from ...dyn.embed.element_modes import ElementModesEnum as ElementModesEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits
except ImportError:
    pass
try:
    from ...dyn.embed.embed_map_units import EmbedMapUnitsEnum as EmbedMapUnitsEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embed_misc import EmbedMisc as EmbedMisc
except ImportError:
    pass
try:
    from ...dyn.embed.embed_misc import EmbedMiscEnum as EmbedMiscEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embed_states import EmbedStates as EmbedStates
except ImportError:
    pass
try:
    from ...dyn.embed.embed_states import EmbedStatesEnum as EmbedStatesEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embed_update_modes import EmbedUpdateModes as EmbedUpdateModes
except ImportError:
    pass
try:
    from ...dyn.embed.embed_update_modes import EmbedUpdateModesEnum as EmbedUpdateModesEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embed_verbs import EmbedVerbs as EmbedVerbs
except ImportError:
    pass
try:
    from ...dyn.embed.embed_verbs import EmbedVerbsEnum as EmbedVerbsEnum
except ImportError:
    pass
try:
    from ...dyn.embed.embedded_object_creator import EmbeddedObjectCreator as EmbeddedObjectCreator
except ImportError:
    pass
try:
    from ...dyn.embed.embedded_object_descriptor import EmbeddedObjectDescriptor as EmbeddedObjectDescriptor
except ImportError:
    pass
try:
    from ...dyn.embed.entry_init_modes import EntryInitModes as EntryInitModes
except ImportError:
    pass
try:
    from ...dyn.embed.entry_init_modes import EntryInitModesEnum as EntryInitModesEnum
except ImportError:
    pass
try:
    from ...dyn.embed.file_system_storage import FileSystemStorage as FileSystemStorage
except ImportError:
    pass
try:
    from ...dyn.embed.file_system_storage_factory import FileSystemStorageFactory as FileSystemStorageFactory
except ImportError:
    pass
try:
    from ...dyn.embed.hatch_window_factory import HatchWindowFactory as HatchWindowFactory
except ImportError:
    pass
try:
    from ...dyn.embed.inserted_object_info import InsertedObjectInfo as InsertedObjectInfo
except ImportError:
    pass
try:
    from ...dyn.embed.instance_locker import InstanceLocker as InstanceLocker
except ImportError:
    pass
try:
    from ...dyn.embed.invalid_storage_exception import InvalidStorageException as InvalidStorageException
except ImportError:
    pass
try:
    from ...dyn.embed.linkage_misuse_exception import LinkageMisuseException as LinkageMisuseException
except ImportError:
    pass
try:
    from ...dyn.embed.msole_object_system_creator import MSOLEObjectSystemCreator as MSOLEObjectSystemCreator
except ImportError:
    pass
try:
    from ...dyn.embed.needs_running_state_exception import NeedsRunningStateException as NeedsRunningStateException
except ImportError:
    pass
try:
    from ...dyn.embed.no_visual_area_size_exception import NoVisualAreaSizeException as NoVisualAreaSizeException
except ImportError:
    pass
try:
    from ...dyn.embed.ole_embedded_object_factory import OLEEmbeddedObjectFactory as OLEEmbeddedObjectFactory
except ImportError:
    pass
try:
    from ...dyn.embed.ole_simple_storage import OLESimpleStorage as OLESimpleStorage
except ImportError:
    pass
try:
    from ...dyn.embed.o_oo_embedded_object_factory import OOoEmbeddedObjectFactory as OOoEmbeddedObjectFactory
except ImportError:
    pass
try:
    from ...dyn.embed.object_save_veto_exception import ObjectSaveVetoException as ObjectSaveVetoException
except ImportError:
    pass
try:
    from ...dyn.embed.state_change_in_progress_exception import StateChangeInProgressException as StateChangeInProgressException
except ImportError:
    pass
try:
    from ...dyn.embed.storage import Storage as Storage
except ImportError:
    pass
try:
    from ...dyn.embed.storage_factory import StorageFactory as StorageFactory
except ImportError:
    pass
try:
    from ...dyn.embed.storage_formats import StorageFormats as StorageFormats
except ImportError:
    pass
try:
    from ...dyn.embed.storage_formats import StorageFormatsEnum as StorageFormatsEnum
except ImportError:
    pass
try:
    from ...dyn.embed.storage_stream import StorageStream as StorageStream
except ImportError:
    pass
try:
    from ...dyn.embed.storage_wrapped_target_exception import StorageWrappedTargetException as StorageWrappedTargetException
except ImportError:
    pass
try:
    from ...dyn.embed.unreachable_state_exception import UnreachableStateException as UnreachableStateException
except ImportError:
    pass
try:
    from ...dyn.embed.use_backup_exception import UseBackupException as UseBackupException
except ImportError:
    pass
try:
    from ...dyn.embed.verb_attributes import VerbAttributes as VerbAttributes
except ImportError:
    pass
try:
    from ...dyn.embed.verb_attributes import VerbAttributesEnum as VerbAttributesEnum
except ImportError:
    pass
try:
    from ...dyn.embed.verb_descriptor import VerbDescriptor as VerbDescriptor
except ImportError:
    pass
try:
    from ...dyn.embed.visual_representation import VisualRepresentation as VisualRepresentation
except ImportError:
    pass
try:
    from ...dyn.embed.wrong_state_exception import WrongStateException as WrongStateException
except ImportError:
    pass
try:
    from ...dyn.embed.x_actions_approval import XActionsApproval as XActionsApproval
except ImportError:
    pass
try:
    from ...dyn.embed.x_classified_object import XClassifiedObject as XClassifiedObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist
except ImportError:
    pass
try:
    from ...dyn.embed.x_component_supplier import XComponentSupplier as XComponentSupplier
except ImportError:
    pass
try:
    from ...dyn.embed.x_embed_object_clipboard_creator import XEmbedObjectClipboardCreator as XEmbedObjectClipboardCreator
except ImportError:
    pass
try:
    from ...dyn.embed.x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator
except ImportError:
    pass
try:
    from ...dyn.embed.x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory
except ImportError:
    pass
try:
    from ...dyn.embed.x_embed_persist import XEmbedPersist as XEmbedPersist
except ImportError:
    pass
try:
    from ...dyn.embed.x_embed_persist2 import XEmbedPersist2 as XEmbedPersist2
except ImportError:
    pass
try:
    from ...dyn.embed.x_embedded_client import XEmbeddedClient as XEmbeddedClient
except ImportError:
    pass
try:
    from ...dyn.embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_embedded_object_creator import XEmbeddedObjectCreator as XEmbeddedObjectCreator
except ImportError:
    pass
try:
    from ...dyn.embed.x_embedded_ole_object import XEmbeddedOleObject as XEmbeddedOleObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource
except ImportError:
    pass
try:
    from ...dyn.embed.x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2
except ImportError:
    pass
try:
    from ...dyn.embed.x_encryption_protected_storage import XEncryptionProtectedStorage as XEncryptionProtectedStorage
except ImportError:
    pass
try:
    from ...dyn.embed.x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream
except ImportError:
    pass
try:
    from ...dyn.embed.x_hatch_window import XHatchWindow as XHatchWindow
except ImportError:
    pass
try:
    from ...dyn.embed.x_hatch_window_controller import XHatchWindowController as XHatchWindowController
except ImportError:
    pass
try:
    from ...dyn.embed.x_hatch_window_factory import XHatchWindowFactory as XHatchWindowFactory
except ImportError:
    pass
try:
    from ...dyn.embed.x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess
except ImportError:
    pass
try:
    from ...dyn.embed.x_hierarchical_storage_access2 import XHierarchicalStorageAccess2 as XHierarchicalStorageAccess2
except ImportError:
    pass
try:
    from ...dyn.embed.x_inplace_client import XInplaceClient as XInplaceClient
except ImportError:
    pass
try:
    from ...dyn.embed.x_inplace_object import XInplaceObject as XInplaceObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_insert_object_dialog import XInsertObjectDialog as XInsertObjectDialog
except ImportError:
    pass
try:
    from ...dyn.embed.x_link_creator import XLinkCreator as XLinkCreator
except ImportError:
    pass
try:
    from ...dyn.embed.x_link_factory import XLinkFactory as XLinkFactory
except ImportError:
    pass
try:
    from ...dyn.embed.x_linkage_support import XLinkageSupport as XLinkageSupport
except ImportError:
    pass
try:
    from ...dyn.embed.xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage
except ImportError:
    pass
try:
    from ...dyn.embed.x_optimized_storage import XOptimizedStorage as XOptimizedStorage
except ImportError:
    pass
try:
    from ...dyn.embed.x_package_structure_creator import XPackageStructureCreator as XPackageStructureCreator
except ImportError:
    pass
try:
    from ...dyn.embed.x_persistance_holder import XPersistanceHolder as XPersistanceHolder
except ImportError:
    pass
try:
    from ...dyn.embed.x_relationship_access import XRelationshipAccess as XRelationshipAccess
except ImportError:
    pass
try:
    from ...dyn.embed.x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster
except ImportError:
    pass
try:
    from ...dyn.embed.x_state_change_listener import XStateChangeListener as XStateChangeListener
except ImportError:
    pass
try:
    from ...dyn.embed.x_storage import XStorage as XStorage
except ImportError:
    pass
try:
    from ...dyn.embed.x_storage2 import XStorage2 as XStorage2
except ImportError:
    pass
try:
    from ...dyn.embed.x_storage_raw_access import XStorageRawAccess as XStorageRawAccess
except ImportError:
    pass
try:
    from ...dyn.embed.x_transacted_object import XTransactedObject as XTransactedObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster
except ImportError:
    pass
try:
    from ...dyn.embed.x_transaction_listener import XTransactionListener as XTransactionListener
except ImportError:
    pass
try:
    from ...dyn.embed.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
except ImportError:
    pass
try:
    from ...dyn.embed.x_visual_object import XVisualObject as XVisualObject
except ImportError:
    pass
try:
    from ...dyn.embed.x_window_supplier import XWindowSupplier as XWindowSupplier
except ImportError:
    pass
