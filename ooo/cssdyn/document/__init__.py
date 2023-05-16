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
    from ...dyn.document.ambigous_filter_request import AmbigousFilterRequest as AmbigousFilterRequest
with suppress(ImportError):
    from ...dyn.document.broken_package_request import BrokenPackageRequest as BrokenPackageRequest
with suppress(ImportError):
    from ...dyn.document.changed_by_others_request import ChangedByOthersRequest as ChangedByOthersRequest
with suppress(ImportError):
    from ...dyn.document.cmis_property import CmisProperty as CmisProperty
with suppress(ImportError):
    from ...dyn.document.cmis_version import CmisVersion as CmisVersion
with suppress(ImportError):
    from ...dyn.document.corrupted_filter_configuration_exception import CorruptedFilterConfigurationException as CorruptedFilterConfigurationException
with suppress(ImportError):
    from ...dyn.document.document_event import DocumentEvent as DocumentEvent
with suppress(ImportError):
    from ...dyn.document.document_properties import DocumentProperties as DocumentProperties
with suppress(ImportError):
    from ...dyn.document.document_revision_list_persistence import DocumentRevisionListPersistence as DocumentRevisionListPersistence
with suppress(ImportError):
    from ...dyn.document.empty_undo_stack_exception import EmptyUndoStackException as EmptyUndoStackException
with suppress(ImportError):
    from ...dyn.document.event_descriptor import EventDescriptor as EventDescriptor
with suppress(ImportError):
    from ...dyn.document.event_object import EventObject as EventObject
with suppress(ImportError):
    from ...dyn.document.events import Events as Events
with suppress(ImportError):
    from ...dyn.document.exotic_file_load_exception import ExoticFileLoadException as ExoticFileLoadException
with suppress(ImportError):
    from ...dyn.document.export_filter import ExportFilter as ExportFilter
with suppress(ImportError):
    from ...dyn.document.extended_type_detection import ExtendedTypeDetection as ExtendedTypeDetection
with suppress(ImportError):
    from ...dyn.document.extended_type_detection_factory import ExtendedTypeDetectionFactory as ExtendedTypeDetectionFactory
with suppress(ImportError):
    from ...dyn.document.filter_adapter import FilterAdapter as FilterAdapter
with suppress(ImportError):
    from ...dyn.document.filter_config_refresh import FilterConfigRefresh as FilterConfigRefresh
with suppress(ImportError):
    from ...dyn.document.filter_factory import FilterFactory as FilterFactory
with suppress(ImportError):
    from ...dyn.document.filter_options_request import FilterOptionsRequest as FilterOptionsRequest
with suppress(ImportError):
    from ...dyn.document.graphic_storage_handler import GraphicStorageHandler as GraphicStorageHandler
with suppress(ImportError):
    from ...dyn.document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings
with suppress(ImportError):
    from ...dyn.document.import_filter import ImportFilter as ImportFilter
with suppress(ImportError):
    from ...dyn.document.indexed_property_values import IndexedPropertyValues as IndexedPropertyValues
with suppress(ImportError):
    from ...dyn.document.link_target import LinkTarget as LinkTarget
with suppress(ImportError):
    from ...dyn.document.link_targets import LinkTargets as LinkTargets
with suppress(ImportError):
    from ...dyn.document.link_update_modes import LinkUpdateModes as LinkUpdateModes
with suppress(ImportError):
    from ...dyn.document.link_update_modes import LinkUpdateModesEnum as LinkUpdateModesEnum
with suppress(ImportError):
    from ...dyn.document.lock_file_corrupt_request import LockFileCorruptRequest as LockFileCorruptRequest
with suppress(ImportError):
    from ...dyn.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest
with suppress(ImportError):
    from ...dyn.document.locked_document_request import LockedDocumentRequest as LockedDocumentRequest
with suppress(ImportError):
    from ...dyn.document.locked_on_saving_request import LockedOnSavingRequest as LockedOnSavingRequest
with suppress(ImportError):
    from ...dyn.document.macro_exec_mode import MacroExecMode as MacroExecMode
with suppress(ImportError):
    from ...dyn.document.macro_exec_mode import MacroExecModeEnum as MacroExecModeEnum
with suppress(ImportError):
    from ...dyn.document.media_descriptor import MediaDescriptor as MediaDescriptor
with suppress(ImportError):
    from ...dyn.document.named_property_values import NamedPropertyValues as NamedPropertyValues
with suppress(ImportError):
    from ...dyn.document.no_such_filter_request import NoSuchFilterRequest as NoSuchFilterRequest
with suppress(ImportError):
    from ...dyn.document.ooxml_document_properties_importer import OOXMLDocumentPropertiesImporter as OOXMLDocumentPropertiesImporter
with suppress(ImportError):
    from ...dyn.document.office_document import OfficeDocument as OfficeDocument
with suppress(ImportError):
    from ...dyn.document.ole_embedded_server_registration import OleEmbeddedServerRegistration as OleEmbeddedServerRegistration
with suppress(ImportError):
    from ...dyn.document.own_lock_on_document_request import OwnLockOnDocumentRequest as OwnLockOnDocumentRequest
with suppress(ImportError):
    from ...dyn.document.pdf_dialog import PDFDialog as PDFDialog
with suppress(ImportError):
    from ...dyn.document.printer_independent_layout import PrinterIndependentLayout as PrinterIndependentLayout
with suppress(ImportError):
    from ...dyn.document.printer_independent_layout import PrinterIndependentLayoutEnum as PrinterIndependentLayoutEnum
with suppress(ImportError):
    from ...dyn.document.redline_display_type import RedlineDisplayType as RedlineDisplayType
with suppress(ImportError):
    from ...dyn.document.redline_display_type import RedlineDisplayTypeEnum as RedlineDisplayTypeEnum
with suppress(ImportError):
    from ...dyn.document.reload_editable_request import ReloadEditableRequest as ReloadEditableRequest
with suppress(ImportError):
    from ...dyn.document.settings import Settings as Settings
with suppress(ImportError):
    from ...dyn.document.type_detection import TypeDetection as TypeDetection
with suppress(ImportError):
    from ...dyn.document.undo_context_not_closed_exception import UndoContextNotClosedException as UndoContextNotClosedException
with suppress(ImportError):
    from ...dyn.document.undo_failed_exception import UndoFailedException as UndoFailedException
with suppress(ImportError):
    from ...dyn.document.undo_manager_event import UndoManagerEvent as UndoManagerEvent
with suppress(ImportError):
    from ...dyn.document.update_doc_mode import UpdateDocMode as UpdateDocMode
with suppress(ImportError):
    from ...dyn.document.update_doc_mode import UpdateDocModeEnum as UpdateDocModeEnum
with suppress(ImportError):
    from ...dyn.document.x_action_lockable import XActionLockable as XActionLockable
with suppress(ImportError):
    from ...dyn.document.x_binary_stream_resolver import XBinaryStreamResolver as XBinaryStreamResolver
with suppress(ImportError):
    from ...dyn.document.x_cmis_document import XCmisDocument as XCmisDocument
with suppress(ImportError):
    from ...dyn.document.x_code_name_query import XCodeNameQuery as XCodeNameQuery
with suppress(ImportError):
    from ...dyn.document.x_compat_writer_doc_properties import XCompatWriterDocProperties as XCompatWriterDocProperties
with suppress(ImportError):
    from ...dyn.document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster
with suppress(ImportError):
    from ...dyn.document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener
with suppress(ImportError):
    from ...dyn.document.x_document_insertable import XDocumentInsertable as XDocumentInsertable
with suppress(ImportError):
    from ...dyn.document.x_document_languages import XDocumentLanguages as XDocumentLanguages
with suppress(ImportError):
    from ...dyn.document.x_document_properties import XDocumentProperties as XDocumentProperties
with suppress(ImportError):
    from ...dyn.document.x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier
with suppress(ImportError):
    from ...dyn.document.x_document_recovery import XDocumentRecovery as XDocumentRecovery
with suppress(ImportError):
    from ...dyn.document.x_document_revision_list_persistence import XDocumentRevisionListPersistence as XDocumentRevisionListPersistence
with suppress(ImportError):
    from ...dyn.document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier
with suppress(ImportError):
    from ...dyn.document.x_embedded_object_resolver import XEmbeddedObjectResolver as XEmbeddedObjectResolver
with suppress(ImportError):
    from ...dyn.document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier
with suppress(ImportError):
    from ...dyn.document.x_embedded_object_supplier2 import XEmbeddedObjectSupplier2 as XEmbeddedObjectSupplier2
with suppress(ImportError):
    from ...dyn.document.x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts
with suppress(ImportError):
    from ...dyn.document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster
with suppress(ImportError):
    from ...dyn.document.x_event_listener import XEventListener as XEventListener
with suppress(ImportError):
    from ...dyn.document.x_events_supplier import XEventsSupplier as XEventsSupplier
with suppress(ImportError):
    from ...dyn.document.x_exporter import XExporter as XExporter
with suppress(ImportError):
    from ...dyn.document.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
with suppress(ImportError):
    from ...dyn.document.x_filter import XFilter as XFilter
with suppress(ImportError):
    from ...dyn.document.x_filter_adapter import XFilterAdapter as XFilterAdapter
with suppress(ImportError):
    from ...dyn.document.x_graphic_object_resolver import XGraphicObjectResolver as XGraphicObjectResolver
with suppress(ImportError):
    from ...dyn.document.x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler
with suppress(ImportError):
    from ...dyn.document.x_importer import XImporter as XImporter
with suppress(ImportError):
    from ...dyn.document.x_interaction_filter_options import XInteractionFilterOptions as XInteractionFilterOptions
with suppress(ImportError):
    from ...dyn.document.x_interaction_filter_select import XInteractionFilterSelect as XInteractionFilterSelect
with suppress(ImportError):
    from ...dyn.document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier
with suppress(ImportError):
    from ...dyn.document.xml_basic_exporter import XMLBasicExporter as XMLBasicExporter
with suppress(ImportError):
    from ...dyn.document.xml_oasis_basic_exporter import XMLOasisBasicExporter as XMLOasisBasicExporter
with suppress(ImportError):
    from ...dyn.document.x_mime_type_info import XMimeTypeInfo as XMimeTypeInfo
with suppress(ImportError):
    from ...dyn.document.xooxml_document_properties_importer import XOOXMLDocumentPropertiesImporter as XOOXMLDocumentPropertiesImporter
with suppress(ImportError):
    from ...dyn.document.x_redlines_supplier import XRedlinesSupplier as XRedlinesSupplier
with suppress(ImportError):
    from ...dyn.document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext
with suppress(ImportError):
    from ...dyn.document.x_shape_event_broadcaster import XShapeEventBroadcaster as XShapeEventBroadcaster
with suppress(ImportError):
    from ...dyn.document.x_shape_event_listener import XShapeEventListener as XShapeEventListener
with suppress(ImportError):
    from ...dyn.document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument
with suppress(ImportError):
    from ...dyn.document.x_storage_change_listener import XStorageChangeListener as XStorageChangeListener
with suppress(ImportError):
    from ...dyn.document.x_type_detection import XTypeDetection as XTypeDetection
with suppress(ImportError):
    from ...dyn.document.x_undo_action import XUndoAction as XUndoAction
with suppress(ImportError):
    from ...dyn.document.x_undo_manager import XUndoManager as XUndoManager
with suppress(ImportError):
    from ...dyn.document.x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener
with suppress(ImportError):
    from ...dyn.document.x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier
with suppress(ImportError):
    from ...dyn.document.x_vba_method_parameter import XVbaMethodParameter as XVbaMethodParameter
with suppress(ImportError):
    from ...dyn.document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier
with suppress(ImportError):
    from ...dyn.document.xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter
