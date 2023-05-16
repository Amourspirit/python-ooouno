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
    from ...dyn.chart2.axis import Axis as Axis
with suppress(ImportError):
    from ...dyn.chart2.axis_orientation import AxisOrientation as AxisOrientation
with suppress(ImportError):
    from ...dyn.chart2.axis_type import AxisType as AxisType
with suppress(ImportError):
    from ...dyn.chart2.axis_type import AxisTypeEnum as AxisTypeEnum
with suppress(ImportError):
    from ...dyn.chart2.candle_stick_chart_type import CandleStickChartType as CandleStickChartType
with suppress(ImportError):
    from ...dyn.chart2.cartesian_coordinate_system2d import CartesianCoordinateSystem2d as CartesianCoordinateSystem2d
with suppress(ImportError):
    from ...dyn.chart2.cartesian_coordinate_system3d import CartesianCoordinateSystem3d as CartesianCoordinateSystem3d
with suppress(ImportError):
    from ...dyn.chart2.chart_document import ChartDocument as ChartDocument
with suppress(ImportError):
    from ...dyn.chart2.chart_document_wrapper import ChartDocumentWrapper as ChartDocumentWrapper
with suppress(ImportError):
    from ...dyn.chart2.chart_type import ChartType as ChartType
with suppress(ImportError):
    from ...dyn.chart2.chart_type_manager import ChartTypeManager as ChartTypeManager
with suppress(ImportError):
    from ...dyn.chart2.chart_type_template import ChartTypeTemplate as ChartTypeTemplate
with suppress(ImportError):
    from ...dyn.chart2.coordinate_system import CoordinateSystem as CoordinateSystem
with suppress(ImportError):
    from ...dyn.chart2.coordinate_system_type import CoordinateSystemType as CoordinateSystemType
with suppress(ImportError):
    from ...dyn.chart2.coordinate_system_type_id import CoordinateSystemTypeID as CoordinateSystemTypeID
with suppress(ImportError):
    from ...dyn.chart2.curve_style import CurveStyle as CurveStyle
with suppress(ImportError):
    from ...dyn.chart2.data_point import DataPoint as DataPoint
with suppress(ImportError):
    from ...dyn.chart2.data_point_custom_label_field import DataPointCustomLabelField as DataPointCustomLabelField
with suppress(ImportError):
    from ...dyn.chart2.data_point_custom_label_field_type import DataPointCustomLabelFieldType as DataPointCustomLabelFieldType
with suppress(ImportError):
    from ...dyn.chart2.data_point_geometry3_d import DataPointGeometry3D as DataPointGeometry3D
with suppress(ImportError):
    from ...dyn.chart2.data_point_geometry3_d import DataPointGeometry3DEnum as DataPointGeometry3DEnum
with suppress(ImportError):
    from ...dyn.chart2.data_point_label import DataPointLabel as DataPointLabel
with suppress(ImportError):
    from ...dyn.chart2.data_point_properties import DataPointProperties as DataPointProperties
with suppress(ImportError):
    from ...dyn.chart2.data_series import DataSeries as DataSeries
with suppress(ImportError):
    from ...dyn.chart2.diagram import Diagram as Diagram
with suppress(ImportError):
    from ...dyn.chart2.error_bar import ErrorBar as ErrorBar
with suppress(ImportError):
    from ...dyn.chart2.exponential_regression_curve import ExponentialRegressionCurve as ExponentialRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.exponential_scaling import ExponentialScaling as ExponentialScaling
with suppress(ImportError):
    from ...dyn.chart2.fill_bitmap import FillBitmap as FillBitmap
with suppress(ImportError):
    from ...dyn.chart2.formatted_string import FormattedString as FormattedString
with suppress(ImportError):
    from ...dyn.chart2.grid_properties import GridProperties as GridProperties
with suppress(ImportError):
    from ...dyn.chart2.increment_data import IncrementData as IncrementData
with suppress(ImportError):
    from ...dyn.chart2.legend import Legend as Legend
with suppress(ImportError):
    from ...dyn.chart2.legend_position import LegendPosition as LegendPosition
with suppress(ImportError):
    from ...dyn.chart2.light_source import LightSource as LightSource
with suppress(ImportError):
    from ...dyn.chart2.linear_regression_curve import LinearRegressionCurve as LinearRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.linear_scaling import LinearScaling as LinearScaling
with suppress(ImportError):
    from ...dyn.chart2.logarithmic_regression_curve import LogarithmicRegressionCurve as LogarithmicRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.logarithmic_scaling import LogarithmicScaling as LogarithmicScaling
with suppress(ImportError):
    from ...dyn.chart2.logic_target_model import LogicTargetModel as LogicTargetModel
with suppress(ImportError):
    from ...dyn.chart2.moving_average_regression_curve import MovingAverageRegressionCurve as MovingAverageRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.moving_average_type import MovingAverageType as MovingAverageType
with suppress(ImportError):
    from ...dyn.chart2.moving_average_type import MovingAverageTypeEnum as MovingAverageTypeEnum
with suppress(ImportError):
    from ...dyn.chart2.pie_chart_offset_mode import PieChartOffsetMode as PieChartOffsetMode
with suppress(ImportError):
    from ...dyn.chart2.polar_coordinate_system2d import PolarCoordinateSystem2d as PolarCoordinateSystem2d
with suppress(ImportError):
    from ...dyn.chart2.polar_coordinate_system3d import PolarCoordinateSystem3d as PolarCoordinateSystem3d
with suppress(ImportError):
    from ...dyn.chart2.polynomial_regression_curve import PolynomialRegressionCurve as PolynomialRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.potential_regression_curve import PotentialRegressionCurve as PotentialRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.power_scaling import PowerScaling as PowerScaling
with suppress(ImportError):
    from ...dyn.chart2.property_pool import PropertyPool as PropertyPool
with suppress(ImportError):
    from ...dyn.chart2.regression_curve import RegressionCurve as RegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.regression_curve_equation import RegressionCurveEquation as RegressionCurveEquation
with suppress(ImportError):
    from ...dyn.chart2.regression_equation import RegressionEquation as RegressionEquation
with suppress(ImportError):
    from ...dyn.chart2.relative_position import RelativePosition as RelativePosition
with suppress(ImportError):
    from ...dyn.chart2.relative_size import RelativeSize as RelativeSize
with suppress(ImportError):
    from ...dyn.chart2.scale_data import ScaleData as ScaleData
with suppress(ImportError):
    from ...dyn.chart2.scaling import Scaling as Scaling
with suppress(ImportError):
    from ...dyn.chart2.stacking_direction import StackingDirection as StackingDirection
with suppress(ImportError):
    from ...dyn.chart2.standard_diagram_creation_parameters import StandardDiagramCreationParameters as StandardDiagramCreationParameters
with suppress(ImportError):
    from ...dyn.chart2.sub_increment import SubIncrement as SubIncrement
with suppress(ImportError):
    from ...dyn.chart2.symbol import Symbol as Symbol
with suppress(ImportError):
    from ...dyn.chart2.symbol_style import SymbolStyle as SymbolStyle
with suppress(ImportError):
    from ...dyn.chart2.tickmark_style import TickmarkStyle as TickmarkStyle
with suppress(ImportError):
    from ...dyn.chart2.tickmark_style import TickmarkStyleEnum as TickmarkStyleEnum
with suppress(ImportError):
    from ...dyn.chart2.title import Title as Title
with suppress(ImportError):
    from ...dyn.chart2.transparency_style import TransparencyStyle as TransparencyStyle
with suppress(ImportError):
    from ...dyn.chart2.x_any_description_access import XAnyDescriptionAccess as XAnyDescriptionAccess
with suppress(ImportError):
    from ...dyn.chart2.x_axis import XAxis as XAxis
with suppress(ImportError):
    from ...dyn.chart2.x_chart_document import XChartDocument as XChartDocument
with suppress(ImportError):
    from ...dyn.chart2.x_chart_shape import XChartShape as XChartShape
with suppress(ImportError):
    from ...dyn.chart2.x_chart_shape_container import XChartShapeContainer as XChartShapeContainer
with suppress(ImportError):
    from ...dyn.chart2.x_chart_type import XChartType as XChartType
with suppress(ImportError):
    from ...dyn.chart2.x_chart_type_container import XChartTypeContainer as XChartTypeContainer
with suppress(ImportError):
    from ...dyn.chart2.x_chart_type_manager import XChartTypeManager as XChartTypeManager
with suppress(ImportError):
    from ...dyn.chart2.x_chart_type_template import XChartTypeTemplate as XChartTypeTemplate
with suppress(ImportError):
    from ...dyn.chart2.x_color_scheme import XColorScheme as XColorScheme
with suppress(ImportError):
    from ...dyn.chart2.x_coordinate_system import XCoordinateSystem as XCoordinateSystem
with suppress(ImportError):
    from ...dyn.chart2.x_coordinate_system_container import XCoordinateSystemContainer as XCoordinateSystemContainer
with suppress(ImportError):
    from ...dyn.chart2.x_data_point_custom_label_field import XDataPointCustomLabelField as XDataPointCustomLabelField
with suppress(ImportError):
    from ...dyn.chart2.x_data_provider_access import XDataProviderAccess as XDataProviderAccess
with suppress(ImportError):
    from ...dyn.chart2.x_data_series import XDataSeries as XDataSeries
with suppress(ImportError):
    from ...dyn.chart2.x_data_series_container import XDataSeriesContainer as XDataSeriesContainer
with suppress(ImportError):
    from ...dyn.chart2.x_default_size_transmitter import XDefaultSizeTransmitter as XDefaultSizeTransmitter
with suppress(ImportError):
    from ...dyn.chart2.x_diagram import XDiagram as XDiagram
with suppress(ImportError):
    from ...dyn.chart2.x_diagram_provider import XDiagramProvider as XDiagramProvider
with suppress(ImportError):
    from ...dyn.chart2.x_formatted_string import XFormattedString as XFormattedString
with suppress(ImportError):
    from ...dyn.chart2.x_formatted_string2 import XFormattedString2 as XFormattedString2
with suppress(ImportError):
    from ...dyn.chart2.x_internal_data_provider import XInternalDataProvider as XInternalDataProvider
with suppress(ImportError):
    from ...dyn.chart2.x_labeled import XLabeled as XLabeled
with suppress(ImportError):
    from ...dyn.chart2.x_legend import XLegend as XLegend
with suppress(ImportError):
    from ...dyn.chart2.x_regression_curve import XRegressionCurve as XRegressionCurve
with suppress(ImportError):
    from ...dyn.chart2.x_regression_curve_calculator import XRegressionCurveCalculator as XRegressionCurveCalculator
with suppress(ImportError):
    from ...dyn.chart2.x_regression_curve_container import XRegressionCurveContainer as XRegressionCurveContainer
with suppress(ImportError):
    from ...dyn.chart2.x_scaling import XScaling as XScaling
with suppress(ImportError):
    from ...dyn.chart2.x_target import XTarget as XTarget
with suppress(ImportError):
    from ...dyn.chart2.x_time_based import XTimeBased as XTimeBased
with suppress(ImportError):
    from ...dyn.chart2.x_title import XTitle as XTitle
with suppress(ImportError):
    from ...dyn.chart2.x_titled import XTitled as XTitled
