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
    from ....dyn.chart2.data.data_filter import DataFilter as DataFilter
with suppress(ImportError):
    from ....dyn.chart2.data.data_provider import DataProvider as DataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.data_sequence import DataSequence as DataSequence
with suppress(ImportError):
    from ....dyn.chart2.data.data_sequence_role import DataSequenceRole as DataSequenceRole
with suppress(ImportError):
    from ....dyn.chart2.data.data_sink import DataSink as DataSink
with suppress(ImportError):
    from ....dyn.chart2.data.data_source import DataSource as DataSource
with suppress(ImportError):
    from ....dyn.chart2.data.database_data_provider import DatabaseDataProvider as DatabaseDataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.highlighted_range import HighlightedRange as HighlightedRange
with suppress(ImportError):
    from ....dyn.chart2.data.label_origin import LabelOrigin as LabelOrigin
with suppress(ImportError):
    from ....dyn.chart2.data.labeled_data_sequence import LabeledDataSequence as LabeledDataSequence
with suppress(ImportError):
    from ....dyn.chart2.data.pivot_table_field_entry import PivotTableFieldEntry as PivotTableFieldEntry
with suppress(ImportError):
    from ....dyn.chart2.data.range_highlight_listener import RangeHighlightListener as RangeHighlightListener
with suppress(ImportError):
    from ....dyn.chart2.data.range_highlighter import RangeHighlighter as RangeHighlighter
with suppress(ImportError):
    from ....dyn.chart2.data.tabular_data_provider_arguments import TabularDataProviderArguments as TabularDataProviderArguments
with suppress(ImportError):
    from ....dyn.chart2.data.x_data_provider import XDataProvider as XDataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.x_data_receiver import XDataReceiver as XDataReceiver
with suppress(ImportError):
    from ....dyn.chart2.data.x_data_sequence import XDataSequence as XDataSequence
with suppress(ImportError):
    from ....dyn.chart2.data.x_data_sink import XDataSink as XDataSink
with suppress(ImportError):
    from ....dyn.chart2.data.x_data_source import XDataSource as XDataSource
with suppress(ImportError):
    from ....dyn.chart2.data.x_database_data_provider import XDatabaseDataProvider as XDatabaseDataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence
with suppress(ImportError):
    from ....dyn.chart2.data.x_labeled_data_sequence2 import XLabeledDataSequence2 as XLabeledDataSequence2
with suppress(ImportError):
    from ....dyn.chart2.data.x_numerical_data_sequence import XNumericalDataSequence as XNumericalDataSequence
with suppress(ImportError):
    from ....dyn.chart2.data.x_pivot_table_data_provider import XPivotTableDataProvider as XPivotTableDataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.x_range_highlighter import XRangeHighlighter as XRangeHighlighter
with suppress(ImportError):
    from ....dyn.chart2.data.x_range_xml_conversion import XRangeXMLConversion as XRangeXMLConversion
with suppress(ImportError):
    from ....dyn.chart2.data.x_sheet_data_provider import XSheetDataProvider as XSheetDataProvider
with suppress(ImportError):
    from ....dyn.chart2.data.x_textual_data_sequence import XTextualDataSequence as XTextualDataSequence
