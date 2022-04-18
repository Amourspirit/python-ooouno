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
from ...dyn.document.ambigous_filter_request import AmbigousFilterRequest as AmbigousFilterRequest
from ...dyn.document.broken_package_request import BrokenPackageRequest as BrokenPackageRequest
from ...dyn.document.changed_by_others_request import ChangedByOthersRequest as ChangedByOthersRequest
from ...dyn.document.cmis_property import CmisProperty as CmisProperty
from ...dyn.document.cmis_version import CmisVersion as CmisVersion
from ...dyn.document.corrupted_filter_configuration_exception import CorruptedFilterConfigurationException as CorruptedFilterConfigurationException
from ...dyn.document.document_event import DocumentEvent as DocumentEvent
from ...dyn.document.document_properties import DocumentProperties as DocumentProperties
from ...dyn.document.document_revision_list_persistence import DocumentRevisionListPersistence as DocumentRevisionListPersistence
from ...dyn.document.empty_undo_stack_exception import EmptyUndoStackException as EmptyUndoStackException
from ...dyn.document.event_descriptor import EventDescriptor as EventDescriptor
from ...dyn.document.event_object import EventObject as EventObject
from ...dyn.document.events import Events as Events
from ...dyn.document.exotic_file_load_exception import ExoticFileLoadException as ExoticFileLoadException
from ...dyn.document.export_filter import ExportFilter as ExportFilter
from ...dyn.document.extended_type_detection import ExtendedTypeDetection as ExtendedTypeDetection
from ...dyn.document.extended_type_detection_factory import ExtendedTypeDetectionFactory as ExtendedTypeDetectionFactory
from ...dyn.document.filter_adapter import FilterAdapter as FilterAdapter
from ...dyn.document.filter_config_refresh import FilterConfigRefresh as FilterConfigRefresh
from ...dyn.document.filter_factory import FilterFactory as FilterFactory
from ...dyn.document.filter_options_request import FilterOptionsRequest as FilterOptionsRequest
from ...dyn.document.graphic_storage_handler import GraphicStorageHandler as GraphicStorageHandler
from ...dyn.document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings
from ...dyn.document.import_filter import ImportFilter as ImportFilter
from ...dyn.document.indexed_property_values import IndexedPropertyValues as IndexedPropertyValues
from ...dyn.document.link_target import LinkTarget as LinkTarget
from ...dyn.document.link_targets import LinkTargets as LinkTargets
from ...dyn.document.link_update_modes import LinkUpdateModes as LinkUpdateModes
from ...dyn.document.link_update_modes import LinkUpdateModesEnum as LinkUpdateModesEnum
from ...dyn.document.lock_file_corrupt_request import LockFileCorruptRequest as LockFileCorruptRequest
from ...dyn.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest
from ...dyn.document.locked_document_request import LockedDocumentRequest as LockedDocumentRequest
from ...dyn.document.locked_on_saving_request import LockedOnSavingRequest as LockedOnSavingRequest
from ...dyn.document.macro_exec_mode import MacroExecMode as MacroExecMode
from ...dyn.document.macro_exec_mode import MacroExecModeEnum as MacroExecModeEnum
from ...dyn.document.media_descriptor import MediaDescriptor as MediaDescriptor
from ...dyn.document.named_property_values import NamedPropertyValues as NamedPropertyValues
from ...dyn.document.no_such_filter_request import NoSuchFilterRequest as NoSuchFilterRequest
from ...dyn.document.ooxml_document_properties_importer import OOXMLDocumentPropertiesImporter as OOXMLDocumentPropertiesImporter
from ...dyn.document.office_document import OfficeDocument as OfficeDocument
from ...dyn.document.ole_embedded_server_registration import OleEmbeddedServerRegistration as OleEmbeddedServerRegistration
from ...dyn.document.own_lock_on_document_request import OwnLockOnDocumentRequest as OwnLockOnDocumentRequest
from ...dyn.document.pdf_dialog import PDFDialog as PDFDialog
from ...dyn.document.printer_independent_layout import PrinterIndependentLayout as PrinterIndependentLayout
from ...dyn.document.printer_independent_layout import PrinterIndependentLayoutEnum as PrinterIndependentLayoutEnum
from ...dyn.document.redline_display_type import RedlineDisplayType as RedlineDisplayType
from ...dyn.document.redline_display_type import RedlineDisplayTypeEnum as RedlineDisplayTypeEnum
from ...dyn.document.reload_editable_request import ReloadEditableRequest as ReloadEditableRequest
from ...dyn.document.settings import Settings as Settings
from ...dyn.document.type_detection import TypeDetection as TypeDetection
from ...dyn.document.undo_context_not_closed_exception import UndoContextNotClosedException as UndoContextNotClosedException
from ...dyn.document.undo_failed_exception import UndoFailedException as UndoFailedException
from ...dyn.document.undo_manager_event import UndoManagerEvent as UndoManagerEvent
from ...dyn.document.update_doc_mode import UpdateDocMode as UpdateDocMode
from ...dyn.document.update_doc_mode import UpdateDocModeEnum as UpdateDocModeEnum
from ...dyn.document.x_action_lockable import XActionLockable as XActionLockable
from ...dyn.document.x_binary_stream_resolver import XBinaryStreamResolver as XBinaryStreamResolver
from ...dyn.document.x_cmis_document import XCmisDocument as XCmisDocument
from ...dyn.document.x_code_name_query import XCodeNameQuery as XCodeNameQuery
from ...dyn.document.x_compat_writer_doc_properties import XCompatWriterDocProperties as XCompatWriterDocProperties
from ...dyn.document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster
from ...dyn.document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener
from ...dyn.document.x_document_insertable import XDocumentInsertable as XDocumentInsertable
from ...dyn.document.x_document_languages import XDocumentLanguages as XDocumentLanguages
from ...dyn.document.x_document_properties import XDocumentProperties as XDocumentProperties
from ...dyn.document.x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier
from ...dyn.document.x_document_recovery import XDocumentRecovery as XDocumentRecovery
from ...dyn.document.x_document_revision_list_persistence import XDocumentRevisionListPersistence as XDocumentRevisionListPersistence
from ...dyn.document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier
from ...dyn.document.x_embedded_object_resolver import XEmbeddedObjectResolver as XEmbeddedObjectResolver
from ...dyn.document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier
from ...dyn.document.x_embedded_object_supplier2 import XEmbeddedObjectSupplier2 as XEmbeddedObjectSupplier2
from ...dyn.document.x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts
from ...dyn.document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster
from ...dyn.document.x_event_listener import XEventListener as XEventListener
from ...dyn.document.x_events_supplier import XEventsSupplier as XEventsSupplier
from ...dyn.document.x_exporter import XExporter as XExporter
from ...dyn.document.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
from ...dyn.document.x_filter import XFilter as XFilter
from ...dyn.document.x_filter_adapter import XFilterAdapter as XFilterAdapter
from ...dyn.document.x_graphic_object_resolver import XGraphicObjectResolver as XGraphicObjectResolver
from ...dyn.document.x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler
from ...dyn.document.x_importer import XImporter as XImporter
from ...dyn.document.x_interaction_filter_options import XInteractionFilterOptions as XInteractionFilterOptions
from ...dyn.document.x_interaction_filter_select import XInteractionFilterSelect as XInteractionFilterSelect
from ...dyn.document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier
from ...dyn.document.xml_basic_exporter import XMLBasicExporter as XMLBasicExporter
from ...dyn.document.xml_oasis_basic_exporter import XMLOasisBasicExporter as XMLOasisBasicExporter
from ...dyn.document.x_mime_type_info import XMimeTypeInfo as XMimeTypeInfo
from ...dyn.document.xooxml_document_properties_importer import XOOXMLDocumentPropertiesImporter as XOOXMLDocumentPropertiesImporter
from ...dyn.document.x_redlines_supplier import XRedlinesSupplier as XRedlinesSupplier
from ...dyn.document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext
from ...dyn.document.x_shape_event_broadcaster import XShapeEventBroadcaster as XShapeEventBroadcaster
from ...dyn.document.x_shape_event_listener import XShapeEventListener as XShapeEventListener
from ...dyn.document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument
from ...dyn.document.x_storage_change_listener import XStorageChangeListener as XStorageChangeListener
from ...dyn.document.x_type_detection import XTypeDetection as XTypeDetection
from ...dyn.document.x_undo_action import XUndoAction as XUndoAction
from ...dyn.document.x_undo_manager import XUndoManager as XUndoManager
from ...dyn.document.x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener
from ...dyn.document.x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier
from ...dyn.document.x_vba_method_parameter import XVbaMethodParameter as XVbaMethodParameter
from ...dyn.document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier
from ...dyn.document.xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter
