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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.embed.actions import Actions as Actions
with suppress(ImportError):
    from ...dyn.embed.actions import ActionsEnum as ActionsEnum
with suppress(ImportError):
    from ...dyn.embed.aspects import Aspects as Aspects
with suppress(ImportError):
    from ...dyn.embed.aspects import AspectsEnum as AspectsEnum
with suppress(ImportError):
    from ...dyn.embed.base_storage import BaseStorage as BaseStorage
with suppress(ImportError):
    from ...dyn.embed.document_closer import DocumentCloser as DocumentCloser
with suppress(ImportError):
    from ...dyn.embed.element_modes import ElementModes as ElementModes
with suppress(ImportError):
    from ...dyn.embed.element_modes import ElementModesEnum as ElementModesEnum
with suppress(ImportError):
    from ...dyn.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits
with suppress(ImportError):
    from ...dyn.embed.embed_map_units import EmbedMapUnitsEnum as EmbedMapUnitsEnum
with suppress(ImportError):
    from ...dyn.embed.embed_misc import EmbedMisc as EmbedMisc
with suppress(ImportError):
    from ...dyn.embed.embed_misc import EmbedMiscEnum as EmbedMiscEnum
with suppress(ImportError):
    from ...dyn.embed.embed_states import EmbedStates as EmbedStates
with suppress(ImportError):
    from ...dyn.embed.embed_states import EmbedStatesEnum as EmbedStatesEnum
with suppress(ImportError):
    from ...dyn.embed.embed_update_modes import EmbedUpdateModes as EmbedUpdateModes
with suppress(ImportError):
    from ...dyn.embed.embed_update_modes import EmbedUpdateModesEnum as EmbedUpdateModesEnum
with suppress(ImportError):
    from ...dyn.embed.embed_verbs import EmbedVerbs as EmbedVerbs
with suppress(ImportError):
    from ...dyn.embed.embed_verbs import EmbedVerbsEnum as EmbedVerbsEnum
with suppress(ImportError):
    from ...dyn.embed.embedded_object_creator import EmbeddedObjectCreator as EmbeddedObjectCreator
with suppress(ImportError):
    from ...dyn.embed.embedded_object_descriptor import EmbeddedObjectDescriptor as EmbeddedObjectDescriptor
with suppress(ImportError):
    from ...dyn.embed.entry_init_modes import EntryInitModes as EntryInitModes
with suppress(ImportError):
    from ...dyn.embed.entry_init_modes import EntryInitModesEnum as EntryInitModesEnum
with suppress(ImportError):
    from ...dyn.embed.file_system_storage import FileSystemStorage as FileSystemStorage
with suppress(ImportError):
    from ...dyn.embed.file_system_storage_factory import FileSystemStorageFactory as FileSystemStorageFactory
with suppress(ImportError):
    from ...dyn.embed.hatch_window_factory import HatchWindowFactory as HatchWindowFactory
with suppress(ImportError):
    from ...dyn.embed.inserted_object_info import InsertedObjectInfo as InsertedObjectInfo
with suppress(ImportError):
    from ...dyn.embed.instance_locker import InstanceLocker as InstanceLocker
with suppress(ImportError):
    from ...dyn.embed.invalid_storage_exception import InvalidStorageException as InvalidStorageException
with suppress(ImportError):
    from ...dyn.embed.linkage_misuse_exception import LinkageMisuseException as LinkageMisuseException
with suppress(ImportError):
    from ...dyn.embed.msole_object_system_creator import MSOLEObjectSystemCreator as MSOLEObjectSystemCreator
with suppress(ImportError):
    from ...dyn.embed.needs_running_state_exception import NeedsRunningStateException as NeedsRunningStateException
with suppress(ImportError):
    from ...dyn.embed.no_visual_area_size_exception import NoVisualAreaSizeException as NoVisualAreaSizeException
with suppress(ImportError):
    from ...dyn.embed.ole_embedded_object_factory import OLEEmbeddedObjectFactory as OLEEmbeddedObjectFactory
with suppress(ImportError):
    from ...dyn.embed.ole_simple_storage import OLESimpleStorage as OLESimpleStorage
with suppress(ImportError):
    from ...dyn.embed.o_oo_embedded_object_factory import OOoEmbeddedObjectFactory as OOoEmbeddedObjectFactory
with suppress(ImportError):
    from ...dyn.embed.object_save_veto_exception import ObjectSaveVetoException as ObjectSaveVetoException
with suppress(ImportError):
    from ...dyn.embed.state_change_in_progress_exception import StateChangeInProgressException as StateChangeInProgressException
with suppress(ImportError):
    from ...dyn.embed.storage import Storage as Storage
with suppress(ImportError):
    from ...dyn.embed.storage_factory import StorageFactory as StorageFactory
with suppress(ImportError):
    from ...dyn.embed.storage_formats import StorageFormats as StorageFormats
with suppress(ImportError):
    from ...dyn.embed.storage_formats import StorageFormatsEnum as StorageFormatsEnum
with suppress(ImportError):
    from ...dyn.embed.storage_stream import StorageStream as StorageStream
with suppress(ImportError):
    from ...dyn.embed.storage_wrapped_target_exception import StorageWrappedTargetException as StorageWrappedTargetException
with suppress(ImportError):
    from ...dyn.embed.unreachable_state_exception import UnreachableStateException as UnreachableStateException
with suppress(ImportError):
    from ...dyn.embed.use_backup_exception import UseBackupException as UseBackupException
with suppress(ImportError):
    from ...dyn.embed.verb_attributes import VerbAttributes as VerbAttributes
with suppress(ImportError):
    from ...dyn.embed.verb_attributes import VerbAttributesEnum as VerbAttributesEnum
with suppress(ImportError):
    from ...dyn.embed.verb_descriptor import VerbDescriptor as VerbDescriptor
with suppress(ImportError):
    from ...dyn.embed.visual_representation import VisualRepresentation as VisualRepresentation
with suppress(ImportError):
    from ...dyn.embed.wrong_state_exception import WrongStateException as WrongStateException
with suppress(ImportError):
    from ...dyn.embed.x_actions_approval import XActionsApproval as XActionsApproval
with suppress(ImportError):
    from ...dyn.embed.x_classified_object import XClassifiedObject as XClassifiedObject
with suppress(ImportError):
    from ...dyn.embed.x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist
with suppress(ImportError):
    from ...dyn.embed.x_component_supplier import XComponentSupplier as XComponentSupplier
with suppress(ImportError):
    from ...dyn.embed.x_embed_object_clipboard_creator import XEmbedObjectClipboardCreator as XEmbedObjectClipboardCreator
with suppress(ImportError):
    from ...dyn.embed.x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator
with suppress(ImportError):
    from ...dyn.embed.x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory
with suppress(ImportError):
    from ...dyn.embed.x_embed_persist import XEmbedPersist as XEmbedPersist
with suppress(ImportError):
    from ...dyn.embed.x_embed_persist2 import XEmbedPersist2 as XEmbedPersist2
with suppress(ImportError):
    from ...dyn.embed.x_embedded_client import XEmbeddedClient as XEmbeddedClient
with suppress(ImportError):
    from ...dyn.embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject
with suppress(ImportError):
    from ...dyn.embed.x_embedded_object_creator import XEmbeddedObjectCreator as XEmbeddedObjectCreator
with suppress(ImportError):
    from ...dyn.embed.x_embedded_ole_object import XEmbeddedOleObject as XEmbeddedOleObject
with suppress(ImportError):
    from ...dyn.embed.x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource
with suppress(ImportError):
    from ...dyn.embed.x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2
with suppress(ImportError):
    from ...dyn.embed.x_encryption_protected_storage import XEncryptionProtectedStorage as XEncryptionProtectedStorage
with suppress(ImportError):
    from ...dyn.embed.x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream
with suppress(ImportError):
    from ...dyn.embed.x_hatch_window import XHatchWindow as XHatchWindow
with suppress(ImportError):
    from ...dyn.embed.x_hatch_window_controller import XHatchWindowController as XHatchWindowController
with suppress(ImportError):
    from ...dyn.embed.x_hatch_window_factory import XHatchWindowFactory as XHatchWindowFactory
with suppress(ImportError):
    from ...dyn.embed.x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess
with suppress(ImportError):
    from ...dyn.embed.x_hierarchical_storage_access2 import XHierarchicalStorageAccess2 as XHierarchicalStorageAccess2
with suppress(ImportError):
    from ...dyn.embed.x_inplace_client import XInplaceClient as XInplaceClient
with suppress(ImportError):
    from ...dyn.embed.x_inplace_object import XInplaceObject as XInplaceObject
with suppress(ImportError):
    from ...dyn.embed.x_insert_object_dialog import XInsertObjectDialog as XInsertObjectDialog
with suppress(ImportError):
    from ...dyn.embed.x_link_creator import XLinkCreator as XLinkCreator
with suppress(ImportError):
    from ...dyn.embed.x_link_factory import XLinkFactory as XLinkFactory
with suppress(ImportError):
    from ...dyn.embed.x_linkage_support import XLinkageSupport as XLinkageSupport
with suppress(ImportError):
    from ...dyn.embed.xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage
with suppress(ImportError):
    from ...dyn.embed.x_optimized_storage import XOptimizedStorage as XOptimizedStorage
with suppress(ImportError):
    from ...dyn.embed.x_package_structure_creator import XPackageStructureCreator as XPackageStructureCreator
with suppress(ImportError):
    from ...dyn.embed.x_persistance_holder import XPersistanceHolder as XPersistanceHolder
with suppress(ImportError):
    from ...dyn.embed.x_relationship_access import XRelationshipAccess as XRelationshipAccess
with suppress(ImportError):
    from ...dyn.embed.x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster
with suppress(ImportError):
    from ...dyn.embed.x_state_change_listener import XStateChangeListener as XStateChangeListener
with suppress(ImportError):
    from ...dyn.embed.x_storage import XStorage as XStorage
with suppress(ImportError):
    from ...dyn.embed.x_storage2 import XStorage2 as XStorage2
with suppress(ImportError):
    from ...dyn.embed.x_storage_raw_access import XStorageRawAccess as XStorageRawAccess
with suppress(ImportError):
    from ...dyn.embed.x_transacted_object import XTransactedObject as XTransactedObject
with suppress(ImportError):
    from ...dyn.embed.x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster
with suppress(ImportError):
    from ...dyn.embed.x_transaction_listener import XTransactionListener as XTransactionListener
with suppress(ImportError):
    from ...dyn.embed.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
with suppress(ImportError):
    from ...dyn.embed.x_visual_object import XVisualObject as XVisualObject
with suppress(ImportError):
    from ...dyn.embed.x_window_supplier import XWindowSupplier as XWindowSupplier
