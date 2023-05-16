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
    from ...dyn.chart.accessible_chart_document_view import AccessibleChartDocumentView as AccessibleChartDocumentView
with suppress(ImportError):
    from ...dyn.chart.accessible_chart_element import AccessibleChartElement as AccessibleChartElement
with suppress(ImportError):
    from ...dyn.chart.area_diagram import AreaDiagram as AreaDiagram
with suppress(ImportError):
    from ...dyn.chart.bar_diagram import BarDiagram as BarDiagram
with suppress(ImportError):
    from ...dyn.chart.bubble_diagram import BubbleDiagram as BubbleDiagram
with suppress(ImportError):
    from ...dyn.chart.chart3_d_bar_properties import Chart3DBarProperties as Chart3DBarProperties
with suppress(ImportError):
    from ...dyn.chart.chart_area import ChartArea as ChartArea
with suppress(ImportError):
    from ...dyn.chart.chart_axis import ChartAxis as ChartAxis
with suppress(ImportError):
    from ...dyn.chart.chart_axis_arrange_order_type import ChartAxisArrangeOrderType as ChartAxisArrangeOrderType
with suppress(ImportError):
    from ...dyn.chart.chart_axis_assign import ChartAxisAssign as ChartAxisAssign
with suppress(ImportError):
    from ...dyn.chart.chart_axis_assign import ChartAxisAssignEnum as ChartAxisAssignEnum
with suppress(ImportError):
    from ...dyn.chart.chart_axis_label_position import ChartAxisLabelPosition as ChartAxisLabelPosition
with suppress(ImportError):
    from ...dyn.chart.chart_axis_mark_position import ChartAxisMarkPosition as ChartAxisMarkPosition
with suppress(ImportError):
    from ...dyn.chart.chart_axis_marks import ChartAxisMarks as ChartAxisMarks
with suppress(ImportError):
    from ...dyn.chart.chart_axis_marks import ChartAxisMarksEnum as ChartAxisMarksEnum
with suppress(ImportError):
    from ...dyn.chart.chart_axis_position import ChartAxisPosition as ChartAxisPosition
with suppress(ImportError):
    from ...dyn.chart.chart_axis_type import ChartAxisType as ChartAxisType
with suppress(ImportError):
    from ...dyn.chart.chart_axis_type import ChartAxisTypeEnum as ChartAxisTypeEnum
with suppress(ImportError):
    from ...dyn.chart.chart_axis_x_supplier import ChartAxisXSupplier as ChartAxisXSupplier
with suppress(ImportError):
    from ...dyn.chart.chart_axis_y_supplier import ChartAxisYSupplier as ChartAxisYSupplier
with suppress(ImportError):
    from ...dyn.chart.chart_axis_z_supplier import ChartAxisZSupplier as ChartAxisZSupplier
with suppress(ImportError):
    from ...dyn.chart.chart_data import ChartData as ChartData
with suppress(ImportError):
    from ...dyn.chart.chart_data_array import ChartDataArray as ChartDataArray
with suppress(ImportError):
    from ...dyn.chart.chart_data_caption import ChartDataCaption as ChartDataCaption
with suppress(ImportError):
    from ...dyn.chart.chart_data_caption import ChartDataCaptionEnum as ChartDataCaptionEnum
with suppress(ImportError):
    from ...dyn.chart.chart_data_change_event import ChartDataChangeEvent as ChartDataChangeEvent
with suppress(ImportError):
    from ...dyn.chart.chart_data_change_type import ChartDataChangeType as ChartDataChangeType
with suppress(ImportError):
    from ...dyn.chart.chart_data_point import ChartDataPoint as ChartDataPoint
with suppress(ImportError):
    from ...dyn.chart.chart_data_point_properties import ChartDataPointProperties as ChartDataPointProperties
with suppress(ImportError):
    from ...dyn.chart.chart_data_row import ChartDataRow as ChartDataRow
with suppress(ImportError):
    from ...dyn.chart.chart_data_row_properties import ChartDataRowProperties as ChartDataRowProperties
with suppress(ImportError):
    from ...dyn.chart.chart_data_row_source import ChartDataRowSource as ChartDataRowSource
with suppress(ImportError):
    from ...dyn.chart.chart_data_value import ChartDataValue as ChartDataValue
with suppress(ImportError):
    from ...dyn.chart.chart_document import ChartDocument as ChartDocument
with suppress(ImportError):
    from ...dyn.chart.chart_error_category import ChartErrorCategory as ChartErrorCategory
with suppress(ImportError):
    from ...dyn.chart.chart_error_indicator_type import ChartErrorIndicatorType as ChartErrorIndicatorType
with suppress(ImportError):
    from ...dyn.chart.chart_grid import ChartGrid as ChartGrid
with suppress(ImportError):
    from ...dyn.chart.chart_legend import ChartLegend as ChartLegend
with suppress(ImportError):
    from ...dyn.chart.chart_legend_expansion import ChartLegendExpansion as ChartLegendExpansion
with suppress(ImportError):
    from ...dyn.chart.chart_legend_position import ChartLegendPosition as ChartLegendPosition
with suppress(ImportError):
    from ...dyn.chart.chart_line import ChartLine as ChartLine
with suppress(ImportError):
    from ...dyn.chart.chart_pie_segment_properties import ChartPieSegmentProperties as ChartPieSegmentProperties
with suppress(ImportError):
    from ...dyn.chart.chart_regression_curve_type import ChartRegressionCurveType as ChartRegressionCurveType
with suppress(ImportError):
    from ...dyn.chart.chart_series_address import ChartSeriesAddress as ChartSeriesAddress
with suppress(ImportError):
    from ...dyn.chart.chart_solid_type import ChartSolidType as ChartSolidType
with suppress(ImportError):
    from ...dyn.chart.chart_solid_type import ChartSolidTypeEnum as ChartSolidTypeEnum
with suppress(ImportError):
    from ...dyn.chart.chart_statistics import ChartStatistics as ChartStatistics
with suppress(ImportError):
    from ...dyn.chart.chart_symbol_type import ChartSymbolType as ChartSymbolType
with suppress(ImportError):
    from ...dyn.chart.chart_symbol_type import ChartSymbolTypeEnum as ChartSymbolTypeEnum
with suppress(ImportError):
    from ...dyn.chart.chart_table_address_supplier import ChartTableAddressSupplier as ChartTableAddressSupplier
with suppress(ImportError):
    from ...dyn.chart.chart_title import ChartTitle as ChartTitle
with suppress(ImportError):
    from ...dyn.chart.chart_two_axis_x_supplier import ChartTwoAxisXSupplier as ChartTwoAxisXSupplier
with suppress(ImportError):
    from ...dyn.chart.chart_two_axis_y_supplier import ChartTwoAxisYSupplier as ChartTwoAxisYSupplier
with suppress(ImportError):
    from ...dyn.chart.data_label_placement import DataLabelPlacement as DataLabelPlacement
with suppress(ImportError):
    from ...dyn.chart.data_label_placement import DataLabelPlacementEnum as DataLabelPlacementEnum
with suppress(ImportError):
    from ...dyn.chart.diagram import Diagram as Diagram
with suppress(ImportError):
    from ...dyn.chart.dim3_d_diagram import Dim3DDiagram as Dim3DDiagram
with suppress(ImportError):
    from ...dyn.chart.donut_diagram import DonutDiagram as DonutDiagram
with suppress(ImportError):
    from ...dyn.chart.error_bar_style import ErrorBarStyle as ErrorBarStyle
with suppress(ImportError):
    from ...dyn.chart.error_bar_style import ErrorBarStyleEnum as ErrorBarStyleEnum
with suppress(ImportError):
    from ...dyn.chart.filled_net_diagram import FilledNetDiagram as FilledNetDiagram
with suppress(ImportError):
    from ...dyn.chart.line_diagram import LineDiagram as LineDiagram
with suppress(ImportError):
    from ...dyn.chart.missing_value_treatment import MissingValueTreatment as MissingValueTreatment
with suppress(ImportError):
    from ...dyn.chart.missing_value_treatment import MissingValueTreatmentEnum as MissingValueTreatmentEnum
with suppress(ImportError):
    from ...dyn.chart.net_diagram import NetDiagram as NetDiagram
with suppress(ImportError):
    from ...dyn.chart.pie_diagram import PieDiagram as PieDiagram
with suppress(ImportError):
    from ...dyn.chart.stackable_diagram import StackableDiagram as StackableDiagram
with suppress(ImportError):
    from ...dyn.chart.stock_diagram import StockDiagram as StockDiagram
with suppress(ImportError):
    from ...dyn.chart.time_increment import TimeIncrement as TimeIncrement
with suppress(ImportError):
    from ...dyn.chart.time_interval import TimeInterval as TimeInterval
with suppress(ImportError):
    from ...dyn.chart.time_unit import TimeUnit as TimeUnit
with suppress(ImportError):
    from ...dyn.chart.time_unit import TimeUnitEnum as TimeUnitEnum
with suppress(ImportError):
    from ...dyn.chart.x3_d_default_setter import X3DDefaultSetter as X3DDefaultSetter
with suppress(ImportError):
    from ...dyn.chart.x3_d_display import X3DDisplay as X3DDisplay
with suppress(ImportError):
    from ...dyn.chart.x_axis import XAxis as XAxis
with suppress(ImportError):
    from ...dyn.chart.x_axis_supplier import XAxisSupplier as XAxisSupplier
with suppress(ImportError):
    from ...dyn.chart.x_axis_x_supplier import XAxisXSupplier as XAxisXSupplier
with suppress(ImportError):
    from ...dyn.chart.x_axis_y_supplier import XAxisYSupplier as XAxisYSupplier
with suppress(ImportError):
    from ...dyn.chart.x_axis_z_supplier import XAxisZSupplier as XAxisZSupplier
with suppress(ImportError):
    from ...dyn.chart.x_chart_data import XChartData as XChartData
with suppress(ImportError):
    from ...dyn.chart.x_chart_data_array import XChartDataArray as XChartDataArray
with suppress(ImportError):
    from ...dyn.chart.x_chart_data_change_event_listener import XChartDataChangeEventListener as XChartDataChangeEventListener
with suppress(ImportError):
    from ...dyn.chart.x_chart_document import XChartDocument as XChartDocument
with suppress(ImportError):
    from ...dyn.chart.x_complex_description_access import XComplexDescriptionAccess as XComplexDescriptionAccess
with suppress(ImportError):
    from ...dyn.chart.x_date_categories import XDateCategories as XDateCategories
with suppress(ImportError):
    from ...dyn.chart.x_diagram import XDiagram as XDiagram
with suppress(ImportError):
    from ...dyn.chart.x_diagram_positioning import XDiagramPositioning as XDiagramPositioning
with suppress(ImportError):
    from ...dyn.chart.x_second_axis_title_supplier import XSecondAxisTitleSupplier as XSecondAxisTitleSupplier
with suppress(ImportError):
    from ...dyn.chart.x_statistic_display import XStatisticDisplay as XStatisticDisplay
with suppress(ImportError):
    from ...dyn.chart.x_two_axis_x_supplier import XTwoAxisXSupplier as XTwoAxisXSupplier
with suppress(ImportError):
    from ...dyn.chart.x_two_axis_y_supplier import XTwoAxisYSupplier as XTwoAxisYSupplier
with suppress(ImportError):
    from ...dyn.chart.xy_diagram import XYDiagram as XYDiagram
