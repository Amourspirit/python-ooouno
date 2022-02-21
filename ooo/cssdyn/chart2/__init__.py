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
    from ...dyn.chart2.axis import Axis as Axis
except ImportError:
    pass
try:
    from ...dyn.chart2.axis_orientation import AxisOrientation as AxisOrientation
except ImportError:
    pass
try:
    from ...dyn.chart2.axis_type import AxisType as AxisType
except ImportError:
    pass
try:
    from ...dyn.chart2.axis_type import AxisTypeEnum as AxisTypeEnum
except ImportError:
    pass
try:
    from ...dyn.chart2.candle_stick_chart_type import CandleStickChartType as CandleStickChartType
except ImportError:
    pass
try:
    from ...dyn.chart2.cartesian_coordinate_system2d import CartesianCoordinateSystem2d as CartesianCoordinateSystem2d
except ImportError:
    pass
try:
    from ...dyn.chart2.cartesian_coordinate_system3d import CartesianCoordinateSystem3d as CartesianCoordinateSystem3d
except ImportError:
    pass
try:
    from ...dyn.chart2.chart_document import ChartDocument as ChartDocument
except ImportError:
    pass
try:
    from ...dyn.chart2.chart_document_wrapper import ChartDocumentWrapper as ChartDocumentWrapper
except ImportError:
    pass
try:
    from ...dyn.chart2.chart_type import ChartType as ChartType
except ImportError:
    pass
try:
    from ...dyn.chart2.chart_type_manager import ChartTypeManager as ChartTypeManager
except ImportError:
    pass
try:
    from ...dyn.chart2.chart_type_template import ChartTypeTemplate as ChartTypeTemplate
except ImportError:
    pass
try:
    from ...dyn.chart2.coordinate_system import CoordinateSystem as CoordinateSystem
except ImportError:
    pass
try:
    from ...dyn.chart2.coordinate_system_type import CoordinateSystemType as CoordinateSystemType
except ImportError:
    pass
try:
    from ...dyn.chart2.coordinate_system_type_id import CoordinateSystemTypeID as CoordinateSystemTypeID
except ImportError:
    pass
try:
    from ...dyn.chart2.curve_style import CurveStyle as CurveStyle
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point import DataPoint as DataPoint
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_custom_label_field import DataPointCustomLabelField as DataPointCustomLabelField
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_custom_label_field_type import DataPointCustomLabelFieldType as DataPointCustomLabelFieldType
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_geometry3_d import DataPointGeometry3D as DataPointGeometry3D
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_geometry3_d import DataPointGeometry3DEnum as DataPointGeometry3DEnum
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_label import DataPointLabel as DataPointLabel
except ImportError:
    pass
try:
    from ...dyn.chart2.data_point_properties import DataPointProperties as DataPointProperties
except ImportError:
    pass
try:
    from ...dyn.chart2.data_series import DataSeries as DataSeries
except ImportError:
    pass
try:
    from ...dyn.chart2.diagram import Diagram as Diagram
except ImportError:
    pass
try:
    from ...dyn.chart2.error_bar import ErrorBar as ErrorBar
except ImportError:
    pass
try:
    from ...dyn.chart2.exponential_regression_curve import ExponentialRegressionCurve as ExponentialRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.exponential_scaling import ExponentialScaling as ExponentialScaling
except ImportError:
    pass
try:
    from ...dyn.chart2.fill_bitmap import FillBitmap as FillBitmap
except ImportError:
    pass
try:
    from ...dyn.chart2.formatted_string import FormattedString as FormattedString
except ImportError:
    pass
try:
    from ...dyn.chart2.grid_properties import GridProperties as GridProperties
except ImportError:
    pass
try:
    from ...dyn.chart2.increment_data import IncrementData as IncrementData
except ImportError:
    pass
try:
    from ...dyn.chart2.interpreted_data import InterpretedData as InterpretedData
except ImportError:
    pass
try:
    from ...dyn.chart2.legend import Legend as Legend
except ImportError:
    pass
try:
    from ...dyn.chart2.legend_position import LegendPosition as LegendPosition
except ImportError:
    pass
try:
    from ...dyn.chart2.light_source import LightSource as LightSource
except ImportError:
    pass
try:
    from ...dyn.chart2.linear_regression_curve import LinearRegressionCurve as LinearRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.linear_scaling import LinearScaling as LinearScaling
except ImportError:
    pass
try:
    from ...dyn.chart2.logarithmic_regression_curve import LogarithmicRegressionCurve as LogarithmicRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.logarithmic_scaling import LogarithmicScaling as LogarithmicScaling
except ImportError:
    pass
try:
    from ...dyn.chart2.logic_target_model import LogicTargetModel as LogicTargetModel
except ImportError:
    pass
try:
    from ...dyn.chart2.moving_average_regression_curve import MovingAverageRegressionCurve as MovingAverageRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.moving_average_type import MovingAverageType as MovingAverageType
except ImportError:
    pass
try:
    from ...dyn.chart2.moving_average_type import MovingAverageTypeEnum as MovingAverageTypeEnum
except ImportError:
    pass
try:
    from ...dyn.chart2.pie_chart_offset_mode import PieChartOffsetMode as PieChartOffsetMode
except ImportError:
    pass
try:
    from ...dyn.chart2.polar_coordinate_system2d import PolarCoordinateSystem2d as PolarCoordinateSystem2d
except ImportError:
    pass
try:
    from ...dyn.chart2.polar_coordinate_system3d import PolarCoordinateSystem3d as PolarCoordinateSystem3d
except ImportError:
    pass
try:
    from ...dyn.chart2.polynomial_regression_curve import PolynomialRegressionCurve as PolynomialRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.potential_regression_curve import PotentialRegressionCurve as PotentialRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.power_scaling import PowerScaling as PowerScaling
except ImportError:
    pass
try:
    from ...dyn.chart2.property_pool import PropertyPool as PropertyPool
except ImportError:
    pass
try:
    from ...dyn.chart2.regression_curve import RegressionCurve as RegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.regression_curve_equation import RegressionCurveEquation as RegressionCurveEquation
except ImportError:
    pass
try:
    from ...dyn.chart2.regression_equation import RegressionEquation as RegressionEquation
except ImportError:
    pass
try:
    from ...dyn.chart2.relative_position import RelativePosition as RelativePosition
except ImportError:
    pass
try:
    from ...dyn.chart2.relative_size import RelativeSize as RelativeSize
except ImportError:
    pass
try:
    from ...dyn.chart2.scale_data import ScaleData as ScaleData
except ImportError:
    pass
try:
    from ...dyn.chart2.scaling import Scaling as Scaling
except ImportError:
    pass
try:
    from ...dyn.chart2.stacking_direction import StackingDirection as StackingDirection
except ImportError:
    pass
try:
    from ...dyn.chart2.standard_diagram_creation_parameters import StandardDiagramCreationParameters as StandardDiagramCreationParameters
except ImportError:
    pass
try:
    from ...dyn.chart2.sub_increment import SubIncrement as SubIncrement
except ImportError:
    pass
try:
    from ...dyn.chart2.symbol import Symbol as Symbol
except ImportError:
    pass
try:
    from ...dyn.chart2.symbol_style import SymbolStyle as SymbolStyle
except ImportError:
    pass
try:
    from ...dyn.chart2.tickmark_style import TickmarkStyle as TickmarkStyle
except ImportError:
    pass
try:
    from ...dyn.chart2.tickmark_style import TickmarkStyleEnum as TickmarkStyleEnum
except ImportError:
    pass
try:
    from ...dyn.chart2.title import Title as Title
except ImportError:
    pass
try:
    from ...dyn.chart2.transparency_style import TransparencyStyle as TransparencyStyle
except ImportError:
    pass
try:
    from ...dyn.chart2.x_any_description_access import XAnyDescriptionAccess as XAnyDescriptionAccess
except ImportError:
    pass
try:
    from ...dyn.chart2.x_axis import XAxis as XAxis
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_document import XChartDocument as XChartDocument
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_shape import XChartShape as XChartShape
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_shape_container import XChartShapeContainer as XChartShapeContainer
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_type import XChartType as XChartType
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_type_container import XChartTypeContainer as XChartTypeContainer
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_type_manager import XChartTypeManager as XChartTypeManager
except ImportError:
    pass
try:
    from ...dyn.chart2.x_chart_type_template import XChartTypeTemplate as XChartTypeTemplate
except ImportError:
    pass
try:
    from ...dyn.chart2.x_color_scheme import XColorScheme as XColorScheme
except ImportError:
    pass
try:
    from ...dyn.chart2.x_coordinate_system import XCoordinateSystem as XCoordinateSystem
except ImportError:
    pass
try:
    from ...dyn.chart2.x_coordinate_system_container import XCoordinateSystemContainer as XCoordinateSystemContainer
except ImportError:
    pass
try:
    from ...dyn.chart2.x_data_interpreter import XDataInterpreter as XDataInterpreter
except ImportError:
    pass
try:
    from ...dyn.chart2.x_data_point_custom_label_field import XDataPointCustomLabelField as XDataPointCustomLabelField
except ImportError:
    pass
try:
    from ...dyn.chart2.x_data_provider_access import XDataProviderAccess as XDataProviderAccess
except ImportError:
    pass
try:
    from ...dyn.chart2.x_data_series import XDataSeries as XDataSeries
except ImportError:
    pass
try:
    from ...dyn.chart2.x_data_series_container import XDataSeriesContainer as XDataSeriesContainer
except ImportError:
    pass
try:
    from ...dyn.chart2.x_default_size_transmitter import XDefaultSizeTransmitter as XDefaultSizeTransmitter
except ImportError:
    pass
try:
    from ...dyn.chart2.x_diagram import XDiagram as XDiagram
except ImportError:
    pass
try:
    from ...dyn.chart2.x_diagram_provider import XDiagramProvider as XDiagramProvider
except ImportError:
    pass
try:
    from ...dyn.chart2.x_formatted_string import XFormattedString as XFormattedString
except ImportError:
    pass
try:
    from ...dyn.chart2.x_formatted_string2 import XFormattedString2 as XFormattedString2
except ImportError:
    pass
try:
    from ...dyn.chart2.x_internal_data_provider import XInternalDataProvider as XInternalDataProvider
except ImportError:
    pass
try:
    from ...dyn.chart2.x_labeled import XLabeled as XLabeled
except ImportError:
    pass
try:
    from ...dyn.chart2.x_legend import XLegend as XLegend
except ImportError:
    pass
try:
    from ...dyn.chart2.x_regression_curve import XRegressionCurve as XRegressionCurve
except ImportError:
    pass
try:
    from ...dyn.chart2.x_regression_curve_calculator import XRegressionCurveCalculator as XRegressionCurveCalculator
except ImportError:
    pass
try:
    from ...dyn.chart2.x_regression_curve_container import XRegressionCurveContainer as XRegressionCurveContainer
except ImportError:
    pass
try:
    from ...dyn.chart2.x_scaling import XScaling as XScaling
except ImportError:
    pass
try:
    from ...dyn.chart2.x_target import XTarget as XTarget
except ImportError:
    pass
try:
    from ...dyn.chart2.x_time_based import XTimeBased as XTimeBased
except ImportError:
    pass
try:
    from ...dyn.chart2.x_title import XTitle as XTitle
except ImportError:
    pass
try:
    from ...dyn.chart2.x_titled import XTitled as XTitled
except ImportError:
    pass
try:
    from ...dyn.chart2.x_transformation import XTransformation as XTransformation
except ImportError:
    pass
