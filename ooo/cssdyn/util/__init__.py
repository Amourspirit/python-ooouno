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
    from ...dyn.util.alias_programmatic_pair import AliasProgrammaticPair as AliasProgrammaticPair
with suppress(ImportError):
    from ...dyn.util.atom_class_request import AtomClassRequest as AtomClassRequest
with suppress(ImportError):
    from ...dyn.util.atom_description import AtomDescription as AtomDescription
with suppress(ImportError):
    from ...dyn.util.bootstrap_macro_expander import BootstrapMacroExpander as BootstrapMacroExpander
with suppress(ImportError):
    from ...dyn.util.cell_protection import CellProtection as CellProtection
with suppress(ImportError):
    from ...dyn.util.changes_event import ChangesEvent as ChangesEvent
with suppress(ImportError):
    from ...dyn.util.changes_set import ChangesSet as ChangesSet
with suppress(ImportError):
    from ...dyn.util.close_veto_exception import CloseVetoException as CloseVetoException
with suppress(ImportError):
    from ...dyn.util.color import Color as Color
with suppress(ImportError):
    from ...dyn.util.data_editor_event import DataEditorEvent as DataEditorEvent
with suppress(ImportError):
    from ...dyn.util.data_editor_event_type import DataEditorEventType as DataEditorEventType
with suppress(ImportError):
    from ...dyn.util.date import Date as Date
with suppress(ImportError):
    from ...dyn.util.date_time import DateTime as DateTime
with suppress(ImportError):
    from ...dyn.util.date_time_range import DateTimeRange as DateTimeRange
with suppress(ImportError):
    from ...dyn.util.date_time_with_timezone import DateTimeWithTimezone as DateTimeWithTimezone
with suppress(ImportError):
    from ...dyn.util.date_with_timezone import DateWithTimezone as DateWithTimezone
with suppress(ImportError):
    from ...dyn.util.duration import Duration as Duration
with suppress(ImportError):
    from ...dyn.util.element_change import ElementChange as ElementChange
with suppress(ImportError):
    from ...dyn.util.endianness import Endianness as Endianness
with suppress(ImportError):
    from ...dyn.util.endianness import EndiannessEnum as EndiannessEnum
with suppress(ImportError):
    from ...dyn.util.invalid_state_exception import InvalidStateException as InvalidStateException
with suppress(ImportError):
    from ...dyn.util.job_manager import JobManager as JobManager
with suppress(ImportError):
    from ...dyn.util.language import Language as Language
with suppress(ImportError):
    from ...dyn.util.macro_expander import MacroExpander as MacroExpander
with suppress(ImportError):
    from ...dyn.util.malformed_number_format_exception import MalformedNumberFormatException as MalformedNumberFormatException
with suppress(ImportError):
    from ...dyn.util.measure_unit import MeasureUnit as MeasureUnit
with suppress(ImportError):
    from ...dyn.util.measure_unit import MeasureUnitEnum as MeasureUnitEnum
with suppress(ImportError):
    from ...dyn.util.mode_change_event import ModeChangeEvent as ModeChangeEvent
with suppress(ImportError):
    from ...dyn.util.not_locked_exception import NotLockedException as NotLockedException
with suppress(ImportError):
    from ...dyn.util.not_numeric_exception import NotNumericException as NotNumericException
with suppress(ImportError):
    from ...dyn.util.number_format import NumberFormat as NumberFormat
with suppress(ImportError):
    from ...dyn.util.number_format import NumberFormatEnum as NumberFormatEnum
with suppress(ImportError):
    from ...dyn.util.number_format_properties import NumberFormatProperties as NumberFormatProperties
with suppress(ImportError):
    from ...dyn.util.number_format_settings import NumberFormatSettings as NumberFormatSettings
with suppress(ImportError):
    from ...dyn.util.number_formats import NumberFormats as NumberFormats
with suppress(ImportError):
    from ...dyn.util.number_formats_supplier import NumberFormatsSupplier as NumberFormatsSupplier
with suppress(ImportError):
    from ...dyn.util.number_formatter import NumberFormatter as NumberFormatter
with suppress(ImportError):
    from ...dyn.util.office_installation_directories import OfficeInstallationDirectories as OfficeInstallationDirectories
with suppress(ImportError):
    from ...dyn.util.path_settings import PathSettings as PathSettings
with suppress(ImportError):
    from ...dyn.util.path_substitution import PathSubstitution as PathSubstitution
with suppress(ImportError):
    from ...dyn.util.replace_descriptor import ReplaceDescriptor as ReplaceDescriptor
with suppress(ImportError):
    from ...dyn.util.revision_tag import RevisionTag as RevisionTag
with suppress(ImportError):
    from ...dyn.util.search_algorithms import SearchAlgorithms as SearchAlgorithms
with suppress(ImportError):
    from ...dyn.util.search_algorithms2 import SearchAlgorithms2 as SearchAlgorithms2
with suppress(ImportError):
    from ...dyn.util.search_algorithms2 import SearchAlgorithms2Enum as SearchAlgorithms2Enum
with suppress(ImportError):
    from ...dyn.util.search_descriptor import SearchDescriptor as SearchDescriptor
with suppress(ImportError):
    from ...dyn.util.search_flags import SearchFlags as SearchFlags
with suppress(ImportError):
    from ...dyn.util.search_flags import SearchFlagsEnum as SearchFlagsEnum
with suppress(ImportError):
    from ...dyn.util.search_options import SearchOptions as SearchOptions
with suppress(ImportError):
    from ...dyn.util.search_options2 import SearchOptions2 as SearchOptions2
with suppress(ImportError):
    from ...dyn.util.search_result import SearchResult as SearchResult
with suppress(ImportError):
    from ...dyn.util.sort_descriptor import SortDescriptor as SortDescriptor
with suppress(ImportError):
    from ...dyn.util.sort_descriptor2 import SortDescriptor2 as SortDescriptor2
with suppress(ImportError):
    from ...dyn.util.sort_field import SortField as SortField
with suppress(ImportError):
    from ...dyn.util.sort_field_type import SortFieldType as SortFieldType
with suppress(ImportError):
    from ...dyn.util.sortable import Sortable as Sortable
with suppress(ImportError):
    from ...dyn.util.text_search import TextSearch as TextSearch
with suppress(ImportError):
    from ...dyn.util.text_search2 import TextSearch2 as TextSearch2
with suppress(ImportError):
    from ...dyn.util.time import Time as Time
with suppress(ImportError):
    from ...dyn.util.time_with_timezone import TimeWithTimezone as TimeWithTimezone
with suppress(ImportError):
    from ...dyn.util.tri_state import TriState as TriState
with suppress(ImportError):
    from ...dyn.util.url import URL as URL
with suppress(ImportError):
    from ...dyn.util.url_transformer import URLTransformer as URLTransformer
with suppress(ImportError):
    from ...dyn.util.uri_abbreviation import UriAbbreviation as UriAbbreviation
with suppress(ImportError):
    from ...dyn.util.veto_exception import VetoException as VetoException
with suppress(ImportError):
    from ...dyn.util.x_accounting import XAccounting as XAccounting
with suppress(ImportError):
    from ...dyn.util.x_atom_server import XAtomServer as XAtomServer
with suppress(ImportError):
    from ...dyn.util.x_binary_data_container import XBinaryDataContainer as XBinaryDataContainer
with suppress(ImportError):
    from ...dyn.util.x_broadcaster import XBroadcaster as XBroadcaster
with suppress(ImportError):
    from ...dyn.util.x_cache_info import XCacheInfo as XCacheInfo
with suppress(ImportError):
    from ...dyn.util.x_cancellable import XCancellable as XCancellable
with suppress(ImportError):
    from ...dyn.util.x_chainable import XChainable as XChainable
with suppress(ImportError):
    from ...dyn.util.x_changes_batch import XChangesBatch as XChangesBatch
with suppress(ImportError):
    from ...dyn.util.x_changes_listener import XChangesListener as XChangesListener
with suppress(ImportError):
    from ...dyn.util.x_changes_notifier import XChangesNotifier as XChangesNotifier
with suppress(ImportError):
    from ...dyn.util.x_changes_set import XChangesSet as XChangesSet
with suppress(ImportError):
    from ...dyn.util.x_cloneable import XCloneable as XCloneable
with suppress(ImportError):
    from ...dyn.util.x_close_broadcaster import XCloseBroadcaster as XCloseBroadcaster
with suppress(ImportError):
    from ...dyn.util.x_close_listener import XCloseListener as XCloseListener
with suppress(ImportError):
    from ...dyn.util.x_closeable import XCloseable as XCloseable
with suppress(ImportError):
    from ...dyn.util.x_data_editor import XDataEditor as XDataEditor
with suppress(ImportError):
    from ...dyn.util.x_data_editor_listener import XDataEditorListener as XDataEditorListener
with suppress(ImportError):
    from ...dyn.util.x_flush_listener import XFlushListener as XFlushListener
with suppress(ImportError):
    from ...dyn.util.x_flushable import XFlushable as XFlushable
with suppress(ImportError):
    from ...dyn.util.x_importable import XImportable as XImportable
with suppress(ImportError):
    from ...dyn.util.x_indent import XIndent as XIndent
with suppress(ImportError):
    from ...dyn.util.x_job_manager import XJobManager as XJobManager
with suppress(ImportError):
    from ...dyn.util.x_link_update import XLinkUpdate as XLinkUpdate
with suppress(ImportError):
    from ...dyn.util.x_localized_aliases import XLocalizedAliases as XLocalizedAliases
with suppress(ImportError):
    from ...dyn.util.x_lockable import XLockable as XLockable
with suppress(ImportError):
    from ...dyn.util.x_macro_expander import XMacroExpander as XMacroExpander
with suppress(ImportError):
    from ...dyn.util.x_mergeable import XMergeable as XMergeable
with suppress(ImportError):
    from ...dyn.util.x_mode_change_approve_listener import XModeChangeApproveListener as XModeChangeApproveListener
with suppress(ImportError):
    from ...dyn.util.x_mode_change_broadcaster import XModeChangeBroadcaster as XModeChangeBroadcaster
with suppress(ImportError):
    from ...dyn.util.x_mode_change_listener import XModeChangeListener as XModeChangeListener
with suppress(ImportError):
    from ...dyn.util.x_mode_selector import XModeSelector as XModeSelector
with suppress(ImportError):
    from ...dyn.util.x_modifiable import XModifiable as XModifiable
with suppress(ImportError):
    from ...dyn.util.x_modifiable2 import XModifiable2 as XModifiable2
with suppress(ImportError):
    from ...dyn.util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster
with suppress(ImportError):
    from ...dyn.util.x_modify_listener import XModifyListener as XModifyListener
with suppress(ImportError):
    from ...dyn.util.x_number_format_previewer import XNumberFormatPreviewer as XNumberFormatPreviewer
with suppress(ImportError):
    from ...dyn.util.x_number_format_types import XNumberFormatTypes as XNumberFormatTypes
with suppress(ImportError):
    from ...dyn.util.x_number_formats import XNumberFormats as XNumberFormats
with suppress(ImportError):
    from ...dyn.util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier
with suppress(ImportError):
    from ...dyn.util.x_number_formatter import XNumberFormatter as XNumberFormatter
with suppress(ImportError):
    from ...dyn.util.x_number_formatter2 import XNumberFormatter2 as XNumberFormatter2
with suppress(ImportError):
    from ...dyn.util.x_office_installation_directories import XOfficeInstallationDirectories as XOfficeInstallationDirectories
with suppress(ImportError):
    from ...dyn.util.x_path_settings import XPathSettings as XPathSettings
with suppress(ImportError):
    from ...dyn.util.x_property_replace import XPropertyReplace as XPropertyReplace
with suppress(ImportError):
    from ...dyn.util.x_protectable import XProtectable as XProtectable
with suppress(ImportError):
    from ...dyn.util.x_refresh_listener import XRefreshListener as XRefreshListener
with suppress(ImportError):
    from ...dyn.util.x_refreshable import XRefreshable as XRefreshable
with suppress(ImportError):
    from ...dyn.util.x_replace_descriptor import XReplaceDescriptor as XReplaceDescriptor
with suppress(ImportError):
    from ...dyn.util.x_replaceable import XReplaceable as XReplaceable
with suppress(ImportError):
    from ...dyn.util.x_search_descriptor import XSearchDescriptor as XSearchDescriptor
with suppress(ImportError):
    from ...dyn.util.x_searchable import XSearchable as XSearchable
with suppress(ImportError):
    from ...dyn.util.x_sortable import XSortable as XSortable
with suppress(ImportError):
    from ...dyn.util.x_string_abbreviation import XStringAbbreviation as XStringAbbreviation
with suppress(ImportError):
    from ...dyn.util.x_string_escape import XStringEscape as XStringEscape
with suppress(ImportError):
    from ...dyn.util.x_string_mapping import XStringMapping as XStringMapping
with suppress(ImportError):
    from ...dyn.util.x_string_substitution import XStringSubstitution as XStringSubstitution
with suppress(ImportError):
    from ...dyn.util.x_string_width import XStringWidth as XStringWidth
with suppress(ImportError):
    from ...dyn.util.x_text_search import XTextSearch as XTextSearch
with suppress(ImportError):
    from ...dyn.util.x_text_search2 import XTextSearch2 as XTextSearch2
with suppress(ImportError):
    from ...dyn.util.x_time_stamped import XTimeStamped as XTimeStamped
with suppress(ImportError):
    from ...dyn.util.xurl_transformer import XURLTransformer as XURLTransformer
with suppress(ImportError):
    from ...dyn.util.x_unique_id_factory import XUniqueIDFactory as XUniqueIDFactory
with suppress(ImportError):
    from ...dyn.util.x_updatable import XUpdatable as XUpdatable
with suppress(ImportError):
    from ...dyn.util.x_updatable2 import XUpdatable2 as XUpdatable2
with suppress(ImportError):
    from ...dyn.util.x_veto import XVeto as XVeto
with suppress(ImportError):
    from ...dyn.util.the_macro_expander import theMacroExpander as theMacroExpander
with suppress(ImportError):
    from ...dyn.util.the_office_installation_directories import theOfficeInstallationDirectories as theOfficeInstallationDirectories
with suppress(ImportError):
    from ...dyn.util.the_path_settings import thePathSettings as thePathSettings
