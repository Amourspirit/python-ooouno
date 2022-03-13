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
    from ...dyn.util.alias_programmatic_pair import AliasProgrammaticPair as AliasProgrammaticPair
except ImportError:
    pass
try:
    from ...dyn.util.atom_class_request import AtomClassRequest as AtomClassRequest
except ImportError:
    pass
try:
    from ...dyn.util.atom_description import AtomDescription as AtomDescription
except ImportError:
    pass
try:
    from ...dyn.util.bootstrap_macro_expander import BootstrapMacroExpander as BootstrapMacroExpander
except ImportError:
    pass
try:
    from ...dyn.util.cell_protection import CellProtection as CellProtection
except ImportError:
    pass
try:
    from ...dyn.util.changes_event import ChangesEvent as ChangesEvent
except ImportError:
    pass
try:
    from ...dyn.util.changes_set import ChangesSet as ChangesSet
except ImportError:
    pass
try:
    from ...dyn.util.close_veto_exception import CloseVetoException as CloseVetoException
except ImportError:
    pass
try:
    from ...dyn.util.color import Color as Color
except ImportError:
    pass
try:
    from ...dyn.util.data_editor_event import DataEditorEvent as DataEditorEvent
except ImportError:
    pass
try:
    from ...dyn.util.data_editor_event_type import DataEditorEventType as DataEditorEventType
except ImportError:
    pass
try:
    from ...dyn.util.date import Date as Date
except ImportError:
    pass
try:
    from ...dyn.util.date_time import DateTime as DateTime
except ImportError:
    pass
try:
    from ...dyn.util.date_time_range import DateTimeRange as DateTimeRange
except ImportError:
    pass
try:
    from ...dyn.util.date_time_with_timezone import DateTimeWithTimezone as DateTimeWithTimezone
except ImportError:
    pass
try:
    from ...dyn.util.date_with_timezone import DateWithTimezone as DateWithTimezone
except ImportError:
    pass
try:
    from ...dyn.util.duration import Duration as Duration
except ImportError:
    pass
try:
    from ...dyn.util.element_change import ElementChange as ElementChange
except ImportError:
    pass
try:
    from ...dyn.util.endianness import Endianness as Endianness
except ImportError:
    pass
try:
    from ...dyn.util.endianness import EndiannessEnum as EndiannessEnum
except ImportError:
    pass
try:
    from ...dyn.util.invalid_state_exception import InvalidStateException as InvalidStateException
except ImportError:
    pass
try:
    from ...dyn.util.job_manager import JobManager as JobManager
except ImportError:
    pass
try:
    from ...dyn.util.language import Language as Language
except ImportError:
    pass
try:
    from ...dyn.util.macro_expander import MacroExpander as MacroExpander
except ImportError:
    pass
try:
    from ...dyn.util.malformed_number_format_exception import MalformedNumberFormatException as MalformedNumberFormatException
except ImportError:
    pass
try:
    from ...dyn.util.measure_unit import MeasureUnit as MeasureUnit
except ImportError:
    pass
try:
    from ...dyn.util.measure_unit import MeasureUnitEnum as MeasureUnitEnum
except ImportError:
    pass
try:
    from ...dyn.util.mode_change_event import ModeChangeEvent as ModeChangeEvent
except ImportError:
    pass
try:
    from ...dyn.util.not_locked_exception import NotLockedException as NotLockedException
except ImportError:
    pass
try:
    from ...dyn.util.not_numeric_exception import NotNumericException as NotNumericException
except ImportError:
    pass
try:
    from ...dyn.util.number_format import NumberFormat as NumberFormat
except ImportError:
    pass
try:
    from ...dyn.util.number_format import NumberFormatEnum as NumberFormatEnum
except ImportError:
    pass
try:
    from ...dyn.util.number_format_properties import NumberFormatProperties as NumberFormatProperties
except ImportError:
    pass
try:
    from ...dyn.util.number_format_settings import NumberFormatSettings as NumberFormatSettings
except ImportError:
    pass
try:
    from ...dyn.util.number_formats import NumberFormats as NumberFormats
except ImportError:
    pass
try:
    from ...dyn.util.number_formats_supplier import NumberFormatsSupplier as NumberFormatsSupplier
except ImportError:
    pass
try:
    from ...dyn.util.number_formatter import NumberFormatter as NumberFormatter
except ImportError:
    pass
try:
    from ...dyn.util.office_installation_directories import OfficeInstallationDirectories as OfficeInstallationDirectories
except ImportError:
    pass
try:
    from ...dyn.util.path_settings import PathSettings as PathSettings
except ImportError:
    pass
try:
    from ...dyn.util.path_substitution import PathSubstitution as PathSubstitution
except ImportError:
    pass
try:
    from ...dyn.util.replace_descriptor import ReplaceDescriptor as ReplaceDescriptor
except ImportError:
    pass
try:
    from ...dyn.util.revision_tag import RevisionTag as RevisionTag
except ImportError:
    pass
try:
    from ...dyn.util.search_algorithms import SearchAlgorithms as SearchAlgorithms
except ImportError:
    pass
try:
    from ...dyn.util.search_algorithms2 import SearchAlgorithms2 as SearchAlgorithms2
except ImportError:
    pass
try:
    from ...dyn.util.search_algorithms2 import SearchAlgorithms2Enum as SearchAlgorithms2Enum
except ImportError:
    pass
try:
    from ...dyn.util.search_descriptor import SearchDescriptor as SearchDescriptor
except ImportError:
    pass
try:
    from ...dyn.util.search_flags import SearchFlags as SearchFlags
except ImportError:
    pass
try:
    from ...dyn.util.search_flags import SearchFlagsEnum as SearchFlagsEnum
except ImportError:
    pass
try:
    from ...dyn.util.search_options import SearchOptions as SearchOptions
except ImportError:
    pass
try:
    from ...dyn.util.search_options2 import SearchOptions2 as SearchOptions2
except ImportError:
    pass
try:
    from ...dyn.util.search_result import SearchResult as SearchResult
except ImportError:
    pass
try:
    from ...dyn.util.sort_descriptor import SortDescriptor as SortDescriptor
except ImportError:
    pass
try:
    from ...dyn.util.sort_descriptor2 import SortDescriptor2 as SortDescriptor2
except ImportError:
    pass
try:
    from ...dyn.util.sort_field import SortField as SortField
except ImportError:
    pass
try:
    from ...dyn.util.sort_field_type import SortFieldType as SortFieldType
except ImportError:
    pass
try:
    from ...dyn.util.sortable import Sortable as Sortable
except ImportError:
    pass
try:
    from ...dyn.util.text_search import TextSearch as TextSearch
except ImportError:
    pass
try:
    from ...dyn.util.text_search2 import TextSearch2 as TextSearch2
except ImportError:
    pass
try:
    from ...dyn.util.time import Time as Time
except ImportError:
    pass
try:
    from ...dyn.util.time_with_timezone import TimeWithTimezone as TimeWithTimezone
except ImportError:
    pass
try:
    from ...dyn.util.tri_state import TriState as TriState
except ImportError:
    pass
try:
    from ...dyn.util.url import URL as URL
except ImportError:
    pass
try:
    from ...dyn.util.url_transformer import URLTransformer as URLTransformer
except ImportError:
    pass
try:
    from ...dyn.util.uri_abbreviation import UriAbbreviation as UriAbbreviation
except ImportError:
    pass
try:
    from ...dyn.util.veto_exception import VetoException as VetoException
except ImportError:
    pass
try:
    from ...dyn.util.x_accounting import XAccounting as XAccounting
except ImportError:
    pass
try:
    from ...dyn.util.x_atom_server import XAtomServer as XAtomServer
except ImportError:
    pass
try:
    from ...dyn.util.x_binary_data_container import XBinaryDataContainer as XBinaryDataContainer
except ImportError:
    pass
try:
    from ...dyn.util.x_broadcaster import XBroadcaster as XBroadcaster
except ImportError:
    pass
try:
    from ...dyn.util.x_cancellable import XCancellable as XCancellable
except ImportError:
    pass
try:
    from ...dyn.util.x_chainable import XChainable as XChainable
except ImportError:
    pass
try:
    from ...dyn.util.x_changes_batch import XChangesBatch as XChangesBatch
except ImportError:
    pass
try:
    from ...dyn.util.x_changes_listener import XChangesListener as XChangesListener
except ImportError:
    pass
try:
    from ...dyn.util.x_changes_notifier import XChangesNotifier as XChangesNotifier
except ImportError:
    pass
try:
    from ...dyn.util.x_changes_set import XChangesSet as XChangesSet
except ImportError:
    pass
try:
    from ...dyn.util.x_cloneable import XCloneable as XCloneable
except ImportError:
    pass
try:
    from ...dyn.util.x_close_broadcaster import XCloseBroadcaster as XCloseBroadcaster
except ImportError:
    pass
try:
    from ...dyn.util.x_close_listener import XCloseListener as XCloseListener
except ImportError:
    pass
try:
    from ...dyn.util.x_closeable import XCloseable as XCloseable
except ImportError:
    pass
try:
    from ...dyn.util.x_data_editor import XDataEditor as XDataEditor
except ImportError:
    pass
try:
    from ...dyn.util.x_data_editor_listener import XDataEditorListener as XDataEditorListener
except ImportError:
    pass
try:
    from ...dyn.util.x_flush_listener import XFlushListener as XFlushListener
except ImportError:
    pass
try:
    from ...dyn.util.x_flushable import XFlushable as XFlushable
except ImportError:
    pass
try:
    from ...dyn.util.x_importable import XImportable as XImportable
except ImportError:
    pass
try:
    from ...dyn.util.x_indent import XIndent as XIndent
except ImportError:
    pass
try:
    from ...dyn.util.x_job_manager import XJobManager as XJobManager
except ImportError:
    pass
try:
    from ...dyn.util.x_link_update import XLinkUpdate as XLinkUpdate
except ImportError:
    pass
try:
    from ...dyn.util.x_localized_aliases import XLocalizedAliases as XLocalizedAliases
except ImportError:
    pass
try:
    from ...dyn.util.x_lockable import XLockable as XLockable
except ImportError:
    pass
try:
    from ...dyn.util.x_macro_expander import XMacroExpander as XMacroExpander
except ImportError:
    pass
try:
    from ...dyn.util.x_mergeable import XMergeable as XMergeable
except ImportError:
    pass
try:
    from ...dyn.util.x_mode_change_approve_listener import XModeChangeApproveListener as XModeChangeApproveListener
except ImportError:
    pass
try:
    from ...dyn.util.x_mode_change_broadcaster import XModeChangeBroadcaster as XModeChangeBroadcaster
except ImportError:
    pass
try:
    from ...dyn.util.x_mode_change_listener import XModeChangeListener as XModeChangeListener
except ImportError:
    pass
try:
    from ...dyn.util.x_mode_selector import XModeSelector as XModeSelector
except ImportError:
    pass
try:
    from ...dyn.util.x_modifiable import XModifiable as XModifiable
except ImportError:
    pass
try:
    from ...dyn.util.x_modifiable2 import XModifiable2 as XModifiable2
except ImportError:
    pass
try:
    from ...dyn.util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster
except ImportError:
    pass
try:
    from ...dyn.util.x_modify_listener import XModifyListener as XModifyListener
except ImportError:
    pass
try:
    from ...dyn.util.x_number_format_previewer import XNumberFormatPreviewer as XNumberFormatPreviewer
except ImportError:
    pass
try:
    from ...dyn.util.x_number_format_types import XNumberFormatTypes as XNumberFormatTypes
except ImportError:
    pass
try:
    from ...dyn.util.x_number_formats import XNumberFormats as XNumberFormats
except ImportError:
    pass
try:
    from ...dyn.util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier
except ImportError:
    pass
try:
    from ...dyn.util.x_number_formatter import XNumberFormatter as XNumberFormatter
except ImportError:
    pass
try:
    from ...dyn.util.x_number_formatter2 import XNumberFormatter2 as XNumberFormatter2
except ImportError:
    pass
try:
    from ...dyn.util.x_office_installation_directories import XOfficeInstallationDirectories as XOfficeInstallationDirectories
except ImportError:
    pass
try:
    from ...dyn.util.x_path_settings import XPathSettings as XPathSettings
except ImportError:
    pass
try:
    from ...dyn.util.x_property_replace import XPropertyReplace as XPropertyReplace
except ImportError:
    pass
try:
    from ...dyn.util.x_protectable import XProtectable as XProtectable
except ImportError:
    pass
try:
    from ...dyn.util.x_refresh_listener import XRefreshListener as XRefreshListener
except ImportError:
    pass
try:
    from ...dyn.util.x_refreshable import XRefreshable as XRefreshable
except ImportError:
    pass
try:
    from ...dyn.util.x_replace_descriptor import XReplaceDescriptor as XReplaceDescriptor
except ImportError:
    pass
try:
    from ...dyn.util.x_replaceable import XReplaceable as XReplaceable
except ImportError:
    pass
try:
    from ...dyn.util.x_search_descriptor import XSearchDescriptor as XSearchDescriptor
except ImportError:
    pass
try:
    from ...dyn.util.x_searchable import XSearchable as XSearchable
except ImportError:
    pass
try:
    from ...dyn.util.x_sortable import XSortable as XSortable
except ImportError:
    pass
try:
    from ...dyn.util.x_string_abbreviation import XStringAbbreviation as XStringAbbreviation
except ImportError:
    pass
try:
    from ...dyn.util.x_string_escape import XStringEscape as XStringEscape
except ImportError:
    pass
try:
    from ...dyn.util.x_string_mapping import XStringMapping as XStringMapping
except ImportError:
    pass
try:
    from ...dyn.util.x_string_substitution import XStringSubstitution as XStringSubstitution
except ImportError:
    pass
try:
    from ...dyn.util.x_string_width import XStringWidth as XStringWidth
except ImportError:
    pass
try:
    from ...dyn.util.x_text_search import XTextSearch as XTextSearch
except ImportError:
    pass
try:
    from ...dyn.util.x_text_search2 import XTextSearch2 as XTextSearch2
except ImportError:
    pass
try:
    from ...dyn.util.x_time_stamped import XTimeStamped as XTimeStamped
except ImportError:
    pass
try:
    from ...dyn.util.xurl_transformer import XURLTransformer as XURLTransformer
except ImportError:
    pass
try:
    from ...dyn.util.x_unique_id_factory import XUniqueIDFactory as XUniqueIDFactory
except ImportError:
    pass
try:
    from ...dyn.util.x_updatable import XUpdatable as XUpdatable
except ImportError:
    pass
try:
    from ...dyn.util.x_updatable2 import XUpdatable2 as XUpdatable2
except ImportError:
    pass
try:
    from ...dyn.util.x_veto import XVeto as XVeto
except ImportError:
    pass
try:
    from ...dyn.util.the_macro_expander import theMacroExpander as theMacroExpander
except ImportError:
    pass
try:
    from ...dyn.util.the_office_installation_directories import theOfficeInstallationDirectories as theOfficeInstallationDirectories
except ImportError:
    pass
try:
    from ...dyn.util.the_path_settings import thePathSettings as thePathSettings
except ImportError:
    pass
