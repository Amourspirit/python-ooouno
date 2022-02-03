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
from ...uno_obj.document.ambigous_filter_request import AmbigousFilterRequest as AmbigousFilterRequest
from ...uno_obj.document.broken_package_request import BrokenPackageRequest as BrokenPackageRequest
from ...uno_obj.document.changed_by_others_request import ChangedByOthersRequest as ChangedByOthersRequest
from ...uno_obj.document.cmis_property import CmisProperty as CmisProperty
from ...uno_obj.document.cmis_version import CmisVersion as CmisVersion
from ...uno_obj.document.corrupted_filter_configuration_exception import CorruptedFilterConfigurationException as CorruptedFilterConfigurationException
from ...uno_obj.document.document_event import DocumentEvent as DocumentEvent
from ...uno_obj.document.document_properties import DocumentProperties as DocumentProperties
from ...uno_obj.document.document_revision_list_persistence import DocumentRevisionListPersistence as DocumentRevisionListPersistence
from ...uno_obj.document.empty_undo_stack_exception import EmptyUndoStackException as EmptyUndoStackException
from ...uno_obj.document.event_descriptor import EventDescriptor as EventDescriptor
from ...uno_obj.document.event_object import EventObject as EventObject
from ...uno_obj.document.events import Events as Events
from ...uno_obj.document.exotic_file_load_exception import ExoticFileLoadException as ExoticFileLoadException
from ...uno_obj.document.export_filter import ExportFilter as ExportFilter
from ...uno_obj.document.extended_type_detection import ExtendedTypeDetection as ExtendedTypeDetection
from ...uno_obj.document.extended_type_detection_factory import ExtendedTypeDetectionFactory as ExtendedTypeDetectionFactory
from ...uno_obj.document.filter_adapter import FilterAdapter as FilterAdapter
from ...uno_obj.document.filter_config_refresh import FilterConfigRefresh as FilterConfigRefresh
from ...uno_obj.document.filter_factory import FilterFactory as FilterFactory
from ...uno_obj.document.filter_options_request import FilterOptionsRequest as FilterOptionsRequest
from ...uno_obj.document.graphic_storage_handler import GraphicStorageHandler as GraphicStorageHandler
from ...uno_obj.document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings
from ...uno_obj.document.import_filter import ImportFilter as ImportFilter
from ...uno_obj.document.indexed_property_values import IndexedPropertyValues as IndexedPropertyValues
from ...uno_obj.document.link_target import LinkTarget as LinkTarget
from ...uno_obj.document.link_targets import LinkTargets as LinkTargets
from ...uno_obj.document.link_update_modes import LinkUpdateModes as LinkUpdateModes
from ...uno_obj.document.link_update_modes import LinkUpdateModesEnum as LinkUpdateModesEnum
from ...uno_obj.document.lock_file_corrupt_request import LockFileCorruptRequest as LockFileCorruptRequest
from ...uno_obj.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest
from ...uno_obj.document.locked_document_request import LockedDocumentRequest as LockedDocumentRequest
from ...uno_obj.document.locked_on_saving_request import LockedOnSavingRequest as LockedOnSavingRequest
from ...uno_obj.document.macro_exec_mode import MacroExecMode as MacroExecMode
from ...uno_obj.document.macro_exec_mode import MacroExecModeEnum as MacroExecModeEnum
from ...uno_obj.document.media_descriptor import MediaDescriptor as MediaDescriptor
from ...uno_obj.document.named_property_values import NamedPropertyValues as NamedPropertyValues
from ...uno_obj.document.no_such_filter_request import NoSuchFilterRequest as NoSuchFilterRequest
from ...uno_obj.document.ooxml_document_properties_importer import OOXMLDocumentPropertiesImporter as OOXMLDocumentPropertiesImporter
from ...uno_obj.document.office_document import OfficeDocument as OfficeDocument
from ...uno_obj.document.ole_embedded_server_registration import OleEmbeddedServerRegistration as OleEmbeddedServerRegistration
from ...uno_obj.document.own_lock_on_document_request import OwnLockOnDocumentRequest as OwnLockOnDocumentRequest
from ...uno_obj.document.pdf_dialog import PDFDialog as PDFDialog
from ...uno_obj.document.printer_independent_layout import PrinterIndependentLayout as PrinterIndependentLayout
from ...uno_obj.document.printer_independent_layout import PrinterIndependentLayoutEnum as PrinterIndependentLayoutEnum
from ...uno_obj.document.read_only_open_request import ReadOnlyOpenRequest as ReadOnlyOpenRequest
from ...uno_obj.document.redline_display_type import RedlineDisplayType as RedlineDisplayType
from ...uno_obj.document.redline_display_type import RedlineDisplayTypeEnum as RedlineDisplayTypeEnum
from ...uno_obj.document.reload_editable_request import ReloadEditableRequest as ReloadEditableRequest
from ...uno_obj.document.settings import Settings as Settings
from ...uno_obj.document.type_detection import TypeDetection as TypeDetection
from ...uno_obj.document.undo_context_not_closed_exception import UndoContextNotClosedException as UndoContextNotClosedException
from ...uno_obj.document.undo_failed_exception import UndoFailedException as UndoFailedException
from ...uno_obj.document.undo_manager_event import UndoManagerEvent as UndoManagerEvent
from ...uno_obj.document.update_doc_mode import UpdateDocMode as UpdateDocMode
from ...uno_obj.document.update_doc_mode import UpdateDocModeEnum as UpdateDocModeEnum
from ...uno_obj.document.x_action_lockable import XActionLockable as XActionLockable
from ...uno_obj.document.x_binary_stream_resolver import XBinaryStreamResolver as XBinaryStreamResolver
from ...uno_obj.document.x_cmis_document import XCmisDocument as XCmisDocument
from ...uno_obj.document.x_code_name_query import XCodeNameQuery as XCodeNameQuery
from ...uno_obj.document.x_compat_writer_doc_properties import XCompatWriterDocProperties as XCompatWriterDocProperties
from ...uno_obj.document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster
from ...uno_obj.document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener
from ...uno_obj.document.x_document_insertable import XDocumentInsertable as XDocumentInsertable
from ...uno_obj.document.x_document_languages import XDocumentLanguages as XDocumentLanguages
from ...uno_obj.document.x_document_properties import XDocumentProperties as XDocumentProperties
from ...uno_obj.document.x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier
from ...uno_obj.document.x_document_recovery import XDocumentRecovery as XDocumentRecovery
from ...uno_obj.document.x_document_revision_list_persistence import XDocumentRevisionListPersistence as XDocumentRevisionListPersistence
from ...uno_obj.document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier
from ...uno_obj.document.x_embedded_object_resolver import XEmbeddedObjectResolver as XEmbeddedObjectResolver
from ...uno_obj.document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier
from ...uno_obj.document.x_embedded_object_supplier2 import XEmbeddedObjectSupplier2 as XEmbeddedObjectSupplier2
from ...uno_obj.document.x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts
from ...uno_obj.document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster
from ...uno_obj.document.x_event_listener import XEventListener as XEventListener
from ...uno_obj.document.x_events_supplier import XEventsSupplier as XEventsSupplier
from ...uno_obj.document.x_exporter import XExporter as XExporter
from ...uno_obj.document.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
from ...uno_obj.document.x_filter import XFilter as XFilter
from ...uno_obj.document.x_filter_adapter import XFilterAdapter as XFilterAdapter
from ...uno_obj.document.x_graphic_object_resolver import XGraphicObjectResolver as XGraphicObjectResolver
from ...uno_obj.document.x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler
from ...uno_obj.document.x_importer import XImporter as XImporter
from ...uno_obj.document.x_interaction_filter_options import XInteractionFilterOptions as XInteractionFilterOptions
from ...uno_obj.document.x_interaction_filter_select import XInteractionFilterSelect as XInteractionFilterSelect
from ...uno_obj.document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier
from ...uno_obj.document.xml_basic_exporter import XMLBasicExporter as XMLBasicExporter
from ...uno_obj.document.xml_oasis_basic_exporter import XMLOasisBasicExporter as XMLOasisBasicExporter
from ...uno_obj.document.x_mime_type_info import XMimeTypeInfo as XMimeTypeInfo
from ...uno_obj.document.xooxml_document_properties_importer import XOOXMLDocumentPropertiesImporter as XOOXMLDocumentPropertiesImporter
from ...uno_obj.document.x_redlines_supplier import XRedlinesSupplier as XRedlinesSupplier
from ...uno_obj.document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext
from ...uno_obj.document.x_shape_event_broadcaster import XShapeEventBroadcaster as XShapeEventBroadcaster
from ...uno_obj.document.x_shape_event_listener import XShapeEventListener as XShapeEventListener
from ...uno_obj.document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument
from ...uno_obj.document.x_storage_change_listener import XStorageChangeListener as XStorageChangeListener
from ...uno_obj.document.x_type_detection import XTypeDetection as XTypeDetection
from ...uno_obj.document.x_undo_action import XUndoAction as XUndoAction
from ...uno_obj.document.x_undo_manager import XUndoManager as XUndoManager
from ...uno_obj.document.x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener
from ...uno_obj.document.x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier
from ...uno_obj.document.x_vba_method_parameter import XVbaMethodParameter as XVbaMethodParameter
from ...uno_obj.document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier
from ...uno_obj.document.xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter
