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
    from ...dyn.document.ambigous_filter_request import AmbigousFilterRequest as AmbigousFilterRequest
except ImportError:
    pass
try:
    from ...dyn.document.broken_package_request import BrokenPackageRequest as BrokenPackageRequest
except ImportError:
    pass
try:
    from ...dyn.document.changed_by_others_request import ChangedByOthersRequest as ChangedByOthersRequest
except ImportError:
    pass
try:
    from ...dyn.document.cmis_property import CmisProperty as CmisProperty
except ImportError:
    pass
try:
    from ...dyn.document.cmis_version import CmisVersion as CmisVersion
except ImportError:
    pass
try:
    from ...dyn.document.corrupted_filter_configuration_exception import CorruptedFilterConfigurationException as CorruptedFilterConfigurationException
except ImportError:
    pass
try:
    from ...dyn.document.document_event import DocumentEvent as DocumentEvent
except ImportError:
    pass
try:
    from ...dyn.document.document_properties import DocumentProperties as DocumentProperties
except ImportError:
    pass
try:
    from ...dyn.document.document_revision_list_persistence import DocumentRevisionListPersistence as DocumentRevisionListPersistence
except ImportError:
    pass
try:
    from ...dyn.document.empty_undo_stack_exception import EmptyUndoStackException as EmptyUndoStackException
except ImportError:
    pass
try:
    from ...dyn.document.event_descriptor import EventDescriptor as EventDescriptor
except ImportError:
    pass
try:
    from ...dyn.document.event_object import EventObject as EventObject
except ImportError:
    pass
try:
    from ...dyn.document.events import Events as Events
except ImportError:
    pass
try:
    from ...dyn.document.exotic_file_load_exception import ExoticFileLoadException as ExoticFileLoadException
except ImportError:
    pass
try:
    from ...dyn.document.export_filter import ExportFilter as ExportFilter
except ImportError:
    pass
try:
    from ...dyn.document.extended_type_detection import ExtendedTypeDetection as ExtendedTypeDetection
except ImportError:
    pass
try:
    from ...dyn.document.extended_type_detection_factory import ExtendedTypeDetectionFactory as ExtendedTypeDetectionFactory
except ImportError:
    pass
try:
    from ...dyn.document.filter_adapter import FilterAdapter as FilterAdapter
except ImportError:
    pass
try:
    from ...dyn.document.filter_config_refresh import FilterConfigRefresh as FilterConfigRefresh
except ImportError:
    pass
try:
    from ...dyn.document.filter_factory import FilterFactory as FilterFactory
except ImportError:
    pass
try:
    from ...dyn.document.filter_options_request import FilterOptionsRequest as FilterOptionsRequest
except ImportError:
    pass
try:
    from ...dyn.document.graphic_storage_handler import GraphicStorageHandler as GraphicStorageHandler
except ImportError:
    pass
try:
    from ...dyn.document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings
except ImportError:
    pass
try:
    from ...dyn.document.import_filter import ImportFilter as ImportFilter
except ImportError:
    pass
try:
    from ...dyn.document.indexed_property_values import IndexedPropertyValues as IndexedPropertyValues
except ImportError:
    pass
try:
    from ...dyn.document.link_target import LinkTarget as LinkTarget
except ImportError:
    pass
try:
    from ...dyn.document.link_targets import LinkTargets as LinkTargets
except ImportError:
    pass
try:
    from ...dyn.document.link_update_modes import LinkUpdateModes as LinkUpdateModes
except ImportError:
    pass
try:
    from ...dyn.document.link_update_modes import LinkUpdateModesEnum as LinkUpdateModesEnum
except ImportError:
    pass
try:
    from ...dyn.document.lock_file_corrupt_request import LockFileCorruptRequest as LockFileCorruptRequest
except ImportError:
    pass
try:
    from ...dyn.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest
except ImportError:
    pass
try:
    from ...dyn.document.locked_document_request import LockedDocumentRequest as LockedDocumentRequest
except ImportError:
    pass
try:
    from ...dyn.document.locked_on_saving_request import LockedOnSavingRequest as LockedOnSavingRequest
except ImportError:
    pass
try:
    from ...dyn.document.macro_exec_mode import MacroExecMode as MacroExecMode
except ImportError:
    pass
try:
    from ...dyn.document.macro_exec_mode import MacroExecModeEnum as MacroExecModeEnum
except ImportError:
    pass
try:
    from ...dyn.document.media_descriptor import MediaDescriptor as MediaDescriptor
except ImportError:
    pass
try:
    from ...dyn.document.named_property_values import NamedPropertyValues as NamedPropertyValues
except ImportError:
    pass
try:
    from ...dyn.document.no_such_filter_request import NoSuchFilterRequest as NoSuchFilterRequest
except ImportError:
    pass
try:
    from ...dyn.document.ooxml_document_properties_importer import OOXMLDocumentPropertiesImporter as OOXMLDocumentPropertiesImporter
except ImportError:
    pass
try:
    from ...dyn.document.office_document import OfficeDocument as OfficeDocument
except ImportError:
    pass
try:
    from ...dyn.document.ole_embedded_server_registration import OleEmbeddedServerRegistration as OleEmbeddedServerRegistration
except ImportError:
    pass
try:
    from ...dyn.document.own_lock_on_document_request import OwnLockOnDocumentRequest as OwnLockOnDocumentRequest
except ImportError:
    pass
try:
    from ...dyn.document.pdf_dialog import PDFDialog as PDFDialog
except ImportError:
    pass
try:
    from ...dyn.document.printer_independent_layout import PrinterIndependentLayout as PrinterIndependentLayout
except ImportError:
    pass
try:
    from ...dyn.document.printer_independent_layout import PrinterIndependentLayoutEnum as PrinterIndependentLayoutEnum
except ImportError:
    pass
try:
    from ...dyn.document.read_only_open_request import ReadOnlyOpenRequest as ReadOnlyOpenRequest
except ImportError:
    pass
try:
    from ...dyn.document.redline_display_type import RedlineDisplayType as RedlineDisplayType
except ImportError:
    pass
try:
    from ...dyn.document.redline_display_type import RedlineDisplayTypeEnum as RedlineDisplayTypeEnum
except ImportError:
    pass
try:
    from ...dyn.document.reload_editable_request import ReloadEditableRequest as ReloadEditableRequest
except ImportError:
    pass
try:
    from ...dyn.document.settings import Settings as Settings
except ImportError:
    pass
try:
    from ...dyn.document.type_detection import TypeDetection as TypeDetection
except ImportError:
    pass
try:
    from ...dyn.document.undo_context_not_closed_exception import UndoContextNotClosedException as UndoContextNotClosedException
except ImportError:
    pass
try:
    from ...dyn.document.undo_failed_exception import UndoFailedException as UndoFailedException
except ImportError:
    pass
try:
    from ...dyn.document.undo_manager_event import UndoManagerEvent as UndoManagerEvent
except ImportError:
    pass
try:
    from ...dyn.document.update_doc_mode import UpdateDocMode as UpdateDocMode
except ImportError:
    pass
try:
    from ...dyn.document.update_doc_mode import UpdateDocModeEnum as UpdateDocModeEnum
except ImportError:
    pass
try:
    from ...dyn.document.x_action_lockable import XActionLockable as XActionLockable
except ImportError:
    pass
try:
    from ...dyn.document.x_binary_stream_resolver import XBinaryStreamResolver as XBinaryStreamResolver
except ImportError:
    pass
try:
    from ...dyn.document.x_cmis_document import XCmisDocument as XCmisDocument
except ImportError:
    pass
try:
    from ...dyn.document.x_code_name_query import XCodeNameQuery as XCodeNameQuery
except ImportError:
    pass
try:
    from ...dyn.document.x_compat_writer_doc_properties import XCompatWriterDocProperties as XCompatWriterDocProperties
except ImportError:
    pass
try:
    from ...dyn.document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener
except ImportError:
    pass
try:
    from ...dyn.document.x_document_insertable import XDocumentInsertable as XDocumentInsertable
except ImportError:
    pass
try:
    from ...dyn.document.x_document_languages import XDocumentLanguages as XDocumentLanguages
except ImportError:
    pass
try:
    from ...dyn.document.x_document_properties import XDocumentProperties as XDocumentProperties
except ImportError:
    pass
try:
    from ...dyn.document.x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_document_recovery import XDocumentRecovery as XDocumentRecovery
except ImportError:
    pass
try:
    from ...dyn.document.x_document_revision_list_persistence import XDocumentRevisionListPersistence as XDocumentRevisionListPersistence
except ImportError:
    pass
try:
    from ...dyn.document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_embedded_object_resolver import XEmbeddedObjectResolver as XEmbeddedObjectResolver
except ImportError:
    pass
try:
    from ...dyn.document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_embedded_object_supplier2 import XEmbeddedObjectSupplier2 as XEmbeddedObjectSupplier2
except ImportError:
    pass
try:
    from ...dyn.document.x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts
except ImportError:
    pass
try:
    from ...dyn.document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.document.x_event_listener import XEventListener as XEventListener
except ImportError:
    pass
try:
    from ...dyn.document.x_events_supplier import XEventsSupplier as XEventsSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_exporter import XExporter as XExporter
except ImportError:
    pass
try:
    from ...dyn.document.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
except ImportError:
    pass
try:
    from ...dyn.document.x_filter import XFilter as XFilter
except ImportError:
    pass
try:
    from ...dyn.document.x_filter_adapter import XFilterAdapter as XFilterAdapter
except ImportError:
    pass
try:
    from ...dyn.document.x_graphic_object_resolver import XGraphicObjectResolver as XGraphicObjectResolver
except ImportError:
    pass
try:
    from ...dyn.document.x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler
except ImportError:
    pass
try:
    from ...dyn.document.x_importer import XImporter as XImporter
except ImportError:
    pass
try:
    from ...dyn.document.x_interaction_filter_options import XInteractionFilterOptions as XInteractionFilterOptions
except ImportError:
    pass
try:
    from ...dyn.document.x_interaction_filter_select import XInteractionFilterSelect as XInteractionFilterSelect
except ImportError:
    pass
try:
    from ...dyn.document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier
except ImportError:
    pass
try:
    from ...dyn.document.xml_basic_exporter import XMLBasicExporter as XMLBasicExporter
except ImportError:
    pass
try:
    from ...dyn.document.xml_oasis_basic_exporter import XMLOasisBasicExporter as XMLOasisBasicExporter
except ImportError:
    pass
try:
    from ...dyn.document.x_mime_type_info import XMimeTypeInfo as XMimeTypeInfo
except ImportError:
    pass
try:
    from ...dyn.document.xooxml_document_properties_importer import XOOXMLDocumentPropertiesImporter as XOOXMLDocumentPropertiesImporter
except ImportError:
    pass
try:
    from ...dyn.document.x_redlines_supplier import XRedlinesSupplier as XRedlinesSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext
except ImportError:
    pass
try:
    from ...dyn.document.x_shape_event_broadcaster import XShapeEventBroadcaster as XShapeEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.document.x_shape_event_listener import XShapeEventListener as XShapeEventListener
except ImportError:
    pass
try:
    from ...dyn.document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument
except ImportError:
    pass
try:
    from ...dyn.document.x_storage_change_listener import XStorageChangeListener as XStorageChangeListener
except ImportError:
    pass
try:
    from ...dyn.document.x_type_detection import XTypeDetection as XTypeDetection
except ImportError:
    pass
try:
    from ...dyn.document.x_undo_action import XUndoAction as XUndoAction
except ImportError:
    pass
try:
    from ...dyn.document.x_undo_manager import XUndoManager as XUndoManager
except ImportError:
    pass
try:
    from ...dyn.document.x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener
except ImportError:
    pass
try:
    from ...dyn.document.x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier
except ImportError:
    pass
try:
    from ...dyn.document.x_vba_method_parameter import XVbaMethodParameter as XVbaMethodParameter
except ImportError:
    pass
try:
    from ...dyn.document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier
except ImportError:
    pass
try:
    from ...dyn.document.xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter
except ImportError:
    pass
