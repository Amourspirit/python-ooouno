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
    from ...dyn.drawing.accessible_draw_document_view import AccessibleDrawDocumentView as AccessibleDrawDocumentView
with suppress(ImportError):
    from ...dyn.drawing.accessible_graph_control import AccessibleGraphControl as AccessibleGraphControl
with suppress(ImportError):
    from ...dyn.drawing.accessible_graphic_shape import AccessibleGraphicShape as AccessibleGraphicShape
with suppress(ImportError):
    from ...dyn.drawing.accessible_image_bullet import AccessibleImageBullet as AccessibleImageBullet
with suppress(ImportError):
    from ...dyn.drawing.accessible_ole_shape import AccessibleOLEShape as AccessibleOLEShape
with suppress(ImportError):
    from ...dyn.drawing.accessible_shape import AccessibleShape as AccessibleShape
with suppress(ImportError):
    from ...dyn.drawing.accessible_slide_view import AccessibleSlideView as AccessibleSlideView
with suppress(ImportError):
    from ...dyn.drawing.accessible_slide_view_object import AccessibleSlideViewObject as AccessibleSlideViewObject
with suppress(ImportError):
    from ...dyn.drawing.alignment import Alignment as Alignment
with suppress(ImportError):
    from ...dyn.drawing.applet_shape import AppletShape as AppletShape
with suppress(ImportError):
    from ...dyn.drawing.arrangement import Arrangement as Arrangement
with suppress(ImportError):
    from ...dyn.drawing.background import Background as Background
with suppress(ImportError):
    from ...dyn.drawing.bar_code import BarCode as BarCode
with suppress(ImportError):
    from ...dyn.drawing.bar_code_error_correction import BarCodeErrorCorrection as BarCodeErrorCorrection
with suppress(ImportError):
    from ...dyn.drawing.bar_code_error_correction import BarCodeErrorCorrectionEnum as BarCodeErrorCorrectionEnum
with suppress(ImportError):
    from ...dyn.drawing.bezier_point import BezierPoint as BezierPoint
with suppress(ImportError):
    from ...dyn.drawing.bitmap_mode import BitmapMode as BitmapMode
with suppress(ImportError):
    from ...dyn.drawing.bitmap_table import BitmapTable as BitmapTable
with suppress(ImportError):
    from ...dyn.drawing.bound_volume import BoundVolume as BoundVolume
with suppress(ImportError):
    from ...dyn.drawing.camera_geometry import CameraGeometry as CameraGeometry
with suppress(ImportError):
    from ...dyn.drawing.caption_escape_direction import CaptionEscapeDirection as CaptionEscapeDirection
with suppress(ImportError):
    from ...dyn.drawing.caption_escape_direction import CaptionEscapeDirectionEnum as CaptionEscapeDirectionEnum
with suppress(ImportError):
    from ...dyn.drawing.caption_shape import CaptionShape as CaptionShape
with suppress(ImportError):
    from ...dyn.drawing.caption_type import CaptionType as CaptionType
with suppress(ImportError):
    from ...dyn.drawing.caption_type import CaptionTypeEnum as CaptionTypeEnum
with suppress(ImportError):
    from ...dyn.drawing.circle_kind import CircleKind as CircleKind
with suppress(ImportError):
    from ...dyn.drawing.closed_bezier_shape import ClosedBezierShape as ClosedBezierShape
with suppress(ImportError):
    from ...dyn.drawing.color_mode import ColorMode as ColorMode
with suppress(ImportError):
    from ...dyn.drawing.color_table import ColorTable as ColorTable
with suppress(ImportError):
    from ...dyn.drawing.connection_type import ConnectionType as ConnectionType
with suppress(ImportError):
    from ...dyn.drawing.connector_properties import ConnectorProperties as ConnectorProperties
with suppress(ImportError):
    from ...dyn.drawing.connector_shape import ConnectorShape as ConnectorShape
with suppress(ImportError):
    from ...dyn.drawing.connector_type import ConnectorType as ConnectorType
with suppress(ImportError):
    from ...dyn.drawing.control_shape import ControlShape as ControlShape
with suppress(ImportError):
    from ...dyn.drawing.coordinate_sequence import CoordinateSequence as CoordinateSequence
with suppress(ImportError):
    from ...dyn.drawing.coordinate_sequence_sequence import CoordinateSequenceSequence as CoordinateSequenceSequence
with suppress(ImportError):
    from ...dyn.drawing.custom_shape import CustomShape as CustomShape
with suppress(ImportError):
    from ...dyn.drawing.custom_shape_engine import CustomShapeEngine as CustomShapeEngine
with suppress(ImportError):
    from ...dyn.drawing.dash_style import DashStyle as DashStyle
with suppress(ImportError):
    from ...dyn.drawing.dash_table import DashTable as DashTable
with suppress(ImportError):
    from ...dyn.drawing.defaults import Defaults as Defaults
with suppress(ImportError):
    from ...dyn.drawing.direction3_d import Direction3D as Direction3D
with suppress(ImportError):
    from ...dyn.drawing.document_settings import DocumentSettings as DocumentSettings
with suppress(ImportError):
    from ...dyn.drawing.double_sequence import DoubleSequence as DoubleSequence
with suppress(ImportError):
    from ...dyn.drawing.double_sequence_sequence import DoubleSequenceSequence as DoubleSequenceSequence
with suppress(ImportError):
    from ...dyn.drawing.draw_page import DrawPage as DrawPage
with suppress(ImportError):
    from ...dyn.drawing.draw_pages import DrawPages as DrawPages
with suppress(ImportError):
    from ...dyn.drawing.draw_view_mode import DrawViewMode as DrawViewMode
with suppress(ImportError):
    from ...dyn.drawing.drawing_document import DrawingDocument as DrawingDocument
with suppress(ImportError):
    from ...dyn.drawing.drawing_document_draw_view import DrawingDocumentDrawView as DrawingDocumentDrawView
with suppress(ImportError):
    from ...dyn.drawing.drawing_document_factory import DrawingDocumentFactory as DrawingDocumentFactory
with suppress(ImportError):
    from ...dyn.drawing.ellipse_shape import EllipseShape as EllipseShape
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_adjustment_value import EnhancedCustomShapeAdjustmentValue as EnhancedCustomShapeAdjustmentValue
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_extrusion import EnhancedCustomShapeExtrusion as EnhancedCustomShapeExtrusion
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_geometry import EnhancedCustomShapeGeometry as EnhancedCustomShapeGeometry
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_glue_point_type import EnhancedCustomShapeGluePointType as EnhancedCustomShapeGluePointType
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_glue_point_type import EnhancedCustomShapeGluePointTypeEnum as EnhancedCustomShapeGluePointTypeEnum
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_handle import EnhancedCustomShapeHandle as EnhancedCustomShapeHandle
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_metal_type import EnhancedCustomShapeMetalType as EnhancedCustomShapeMetalType
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_metal_type import EnhancedCustomShapeMetalTypeEnum as EnhancedCustomShapeMetalTypeEnum
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_parameter_pair import EnhancedCustomShapeParameterPair as EnhancedCustomShapeParameterPair
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_parameter_type import EnhancedCustomShapeParameterType as EnhancedCustomShapeParameterType
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_parameter_type import EnhancedCustomShapeParameterTypeEnum as EnhancedCustomShapeParameterTypeEnum
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_path import EnhancedCustomShapePath as EnhancedCustomShapePath
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_segment import EnhancedCustomShapeSegment as EnhancedCustomShapeSegment
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_segment_command import EnhancedCustomShapeSegmentCommand as EnhancedCustomShapeSegmentCommand
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_segment_command import EnhancedCustomShapeSegmentCommandEnum as EnhancedCustomShapeSegmentCommandEnum
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_text_frame import EnhancedCustomShapeTextFrame as EnhancedCustomShapeTextFrame
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_text_path import EnhancedCustomShapeTextPath as EnhancedCustomShapeTextPath
with suppress(ImportError):
    from ...dyn.drawing.enhanced_custom_shape_text_path_mode import EnhancedCustomShapeTextPathMode as EnhancedCustomShapeTextPathMode
with suppress(ImportError):
    from ...dyn.drawing.escape_direction import EscapeDirection as EscapeDirection
with suppress(ImportError):
    from ...dyn.drawing.fill_properties import FillProperties as FillProperties
with suppress(ImportError):
    from ...dyn.drawing.fill_style import FillStyle as FillStyle
with suppress(ImportError):
    from ...dyn.drawing.flag_sequence import FlagSequence as FlagSequence
with suppress(ImportError):
    from ...dyn.drawing.flag_sequence_sequence import FlagSequenceSequence as FlagSequenceSequence
with suppress(ImportError):
    from ...dyn.drawing.generic_draw_page import GenericDrawPage as GenericDrawPage
with suppress(ImportError):
    from ...dyn.drawing.generic_drawing_document import GenericDrawingDocument as GenericDrawingDocument
with suppress(ImportError):
    from ...dyn.drawing.glue_point import GluePoint as GluePoint
with suppress(ImportError):
    from ...dyn.drawing.glue_point2 import GluePoint2 as GluePoint2
with suppress(ImportError):
    from ...dyn.drawing.gradient_table import GradientTable as GradientTable
with suppress(ImportError):
    from ...dyn.drawing.graphic_export_filter import GraphicExportFilter as GraphicExportFilter
with suppress(ImportError):
    from ...dyn.drawing.graphic_filter_request import GraphicFilterRequest as GraphicFilterRequest
with suppress(ImportError):
    from ...dyn.drawing.graphic_object_shape import GraphicObjectShape as GraphicObjectShape
with suppress(ImportError):
    from ...dyn.drawing.group_shape import GroupShape as GroupShape
with suppress(ImportError):
    from ...dyn.drawing.hatch import Hatch as Hatch
with suppress(ImportError):
    from ...dyn.drawing.hatch_style import HatchStyle as HatchStyle
with suppress(ImportError):
    from ...dyn.drawing.hatch_table import HatchTable as HatchTable
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix import HomogenMatrix as HomogenMatrix
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix3 import HomogenMatrix3 as HomogenMatrix3
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix4 import HomogenMatrix4 as HomogenMatrix4
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix_line import HomogenMatrixLine as HomogenMatrixLine
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix_line3 import HomogenMatrixLine3 as HomogenMatrixLine3
with suppress(ImportError):
    from ...dyn.drawing.homogen_matrix_line4 import HomogenMatrixLine4 as HomogenMatrixLine4
with suppress(ImportError):
    from ...dyn.drawing.horizontal_dimensioning import HorizontalDimensioning as HorizontalDimensioning
with suppress(ImportError):
    from ...dyn.drawing.layer import Layer as Layer
with suppress(ImportError):
    from ...dyn.drawing.layer_manager import LayerManager as LayerManager
with suppress(ImportError):
    from ...dyn.drawing.layer_type import LayerType as LayerType
with suppress(ImportError):
    from ...dyn.drawing.line_cap import LineCap as LineCap
with suppress(ImportError):
    from ...dyn.drawing.line_dash import LineDash as LineDash
with suppress(ImportError):
    from ...dyn.drawing.line_end_type import LineEndType as LineEndType
with suppress(ImportError):
    from ...dyn.drawing.line_joint import LineJoint as LineJoint
with suppress(ImportError):
    from ...dyn.drawing.line_properties import LineProperties as LineProperties
with suppress(ImportError):
    from ...dyn.drawing.line_shape import LineShape as LineShape
with suppress(ImportError):
    from ...dyn.drawing.line_style import LineStyle as LineStyle
with suppress(ImportError):
    from ...dyn.drawing.marker_table import MarkerTable as MarkerTable
with suppress(ImportError):
    from ...dyn.drawing.master_page import MasterPage as MasterPage
with suppress(ImportError):
    from ...dyn.drawing.master_pages import MasterPages as MasterPages
with suppress(ImportError):
    from ...dyn.drawing.measure_kind import MeasureKind as MeasureKind
with suppress(ImportError):
    from ...dyn.drawing.measure_properties import MeasureProperties as MeasureProperties
with suppress(ImportError):
    from ...dyn.drawing.measure_shape import MeasureShape as MeasureShape
with suppress(ImportError):
    from ...dyn.drawing.measure_text_horz_pos import MeasureTextHorzPos as MeasureTextHorzPos
with suppress(ImportError):
    from ...dyn.drawing.measure_text_vert_pos import MeasureTextVertPos as MeasureTextVertPos
with suppress(ImportError):
    from ...dyn.drawing.mirror_axis import MirrorAxis as MirrorAxis
with suppress(ImportError):
    from ...dyn.drawing.module_dispatcher import ModuleDispatcher as ModuleDispatcher
with suppress(ImportError):
    from ...dyn.drawing.normals_kind import NormalsKind as NormalsKind
with suppress(ImportError):
    from ...dyn.drawing.ole2_shape import OLE2Shape as OLE2Shape
with suppress(ImportError):
    from ...dyn.drawing.open_bezier_shape import OpenBezierShape as OpenBezierShape
with suppress(ImportError):
    from ...dyn.drawing.page_shape import PageShape as PageShape
with suppress(ImportError):
    from ...dyn.drawing.plugin_shape import PluginShape as PluginShape
with suppress(ImportError):
    from ...dyn.drawing.point_sequence import PointSequence as PointSequence
with suppress(ImportError):
    from ...dyn.drawing.point_sequence_sequence import PointSequenceSequence as PointSequenceSequence
with suppress(ImportError):
    from ...dyn.drawing.poly_line_shape import PolyLineShape as PolyLineShape
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_bezier_coords import PolyPolygonBezierCoords as PolyPolygonBezierCoords
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_bezier_descriptor import PolyPolygonBezierDescriptor as PolyPolygonBezierDescriptor
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_bezier_shape import PolyPolygonBezierShape as PolyPolygonBezierShape
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_descriptor import PolyPolygonDescriptor as PolyPolygonDescriptor
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_shape import PolyPolygonShape as PolyPolygonShape
with suppress(ImportError):
    from ...dyn.drawing.poly_polygon_shape3_d import PolyPolygonShape3D as PolyPolygonShape3D
with suppress(ImportError):
    from ...dyn.drawing.polygon_flags import PolygonFlags as PolygonFlags
with suppress(ImportError):
    from ...dyn.drawing.polygon_kind import PolygonKind as PolygonKind
with suppress(ImportError):
    from ...dyn.drawing.position3_d import Position3D as Position3D
with suppress(ImportError):
    from ...dyn.drawing.projection_mode import ProjectionMode as ProjectionMode
with suppress(ImportError):
    from ...dyn.drawing.rectangle_point import RectanglePoint as RectanglePoint
with suppress(ImportError):
    from ...dyn.drawing.rectangle_shape import RectangleShape as RectangleShape
with suppress(ImportError):
    from ...dyn.drawing.rotation_descriptor import RotationDescriptor as RotationDescriptor
with suppress(ImportError):
    from ...dyn.drawing.shade_mode import ShadeMode as ShadeMode
with suppress(ImportError):
    from ...dyn.drawing.shading_pattern import ShadingPattern as ShadingPattern
with suppress(ImportError):
    from ...dyn.drawing.shading_pattern import ShadingPatternEnum as ShadingPatternEnum
with suppress(ImportError):
    from ...dyn.drawing.shadow_properties import ShadowProperties as ShadowProperties
with suppress(ImportError):
    from ...dyn.drawing.shape import Shape as Shape
with suppress(ImportError):
    from ...dyn.drawing.shape_collection import ShapeCollection as ShapeCollection
with suppress(ImportError):
    from ...dyn.drawing.shapes import Shapes as Shapes
with suppress(ImportError):
    from ...dyn.drawing.slide_renderer import SlideRenderer as SlideRenderer
with suppress(ImportError):
    from ...dyn.drawing.slide_sorter import SlideSorter as SlideSorter
with suppress(ImportError):
    from ...dyn.drawing.snap_object_type import SnapObjectType as SnapObjectType
with suppress(ImportError):
    from ...dyn.drawing.text import Text as Text
with suppress(ImportError):
    from ...dyn.drawing.text_adjust import TextAdjust as TextAdjust
with suppress(ImportError):
    from ...dyn.drawing.text_animation_direction import TextAnimationDirection as TextAnimationDirection
with suppress(ImportError):
    from ...dyn.drawing.text_animation_kind import TextAnimationKind as TextAnimationKind
with suppress(ImportError):
    from ...dyn.drawing.text_fit_to_size_type import TextFitToSizeType as TextFitToSizeType
with suppress(ImportError):
    from ...dyn.drawing.text_horizontal_adjust import TextHorizontalAdjust as TextHorizontalAdjust
with suppress(ImportError):
    from ...dyn.drawing.text_properties import TextProperties as TextProperties
with suppress(ImportError):
    from ...dyn.drawing.text_shape import TextShape as TextShape
with suppress(ImportError):
    from ...dyn.drawing.text_vertical_adjust import TextVerticalAdjust as TextVerticalAdjust
with suppress(ImportError):
    from ...dyn.drawing.texture_kind import TextureKind as TextureKind
with suppress(ImportError):
    from ...dyn.drawing.texture_kind2 import TextureKind2 as TextureKind2
with suppress(ImportError):
    from ...dyn.drawing.texture_mode import TextureMode as TextureMode
with suppress(ImportError):
    from ...dyn.drawing.texture_projection_mode import TextureProjectionMode as TextureProjectionMode
with suppress(ImportError):
    from ...dyn.drawing.transparency_gradient_table import TransparencyGradientTable as TransparencyGradientTable
with suppress(ImportError):
    from ...dyn.drawing.vertical_dimensioning import VerticalDimensioning as VerticalDimensioning
with suppress(ImportError):
    from ...dyn.drawing.x_connectable_shape import XConnectableShape as XConnectableShape
with suppress(ImportError):
    from ...dyn.drawing.x_connector_shape import XConnectorShape as XConnectorShape
with suppress(ImportError):
    from ...dyn.drawing.x_control_shape import XControlShape as XControlShape
with suppress(ImportError):
    from ...dyn.drawing.x_custom_shape_engine import XCustomShapeEngine as XCustomShapeEngine
with suppress(ImportError):
    from ...dyn.drawing.x_custom_shape_handle import XCustomShapeHandle as XCustomShapeHandle
with suppress(ImportError):
    from ...dyn.drawing.x_draw_page import XDrawPage as XDrawPage
with suppress(ImportError):
    from ...dyn.drawing.x_draw_page_duplicator import XDrawPageDuplicator as XDrawPageDuplicator
with suppress(ImportError):
    from ...dyn.drawing.x_draw_page_expander import XDrawPageExpander as XDrawPageExpander
with suppress(ImportError):
    from ...dyn.drawing.x_draw_page_summarizer import XDrawPageSummarizer as XDrawPageSummarizer
with suppress(ImportError):
    from ...dyn.drawing.x_draw_page_supplier import XDrawPageSupplier as XDrawPageSupplier
with suppress(ImportError):
    from ...dyn.drawing.x_draw_pages import XDrawPages as XDrawPages
with suppress(ImportError):
    from ...dyn.drawing.x_draw_pages_supplier import XDrawPagesSupplier as XDrawPagesSupplier
with suppress(ImportError):
    from ...dyn.drawing.x_draw_sub_controller import XDrawSubController as XDrawSubController
with suppress(ImportError):
    from ...dyn.drawing.x_draw_view import XDrawView as XDrawView
with suppress(ImportError):
    from ...dyn.drawing.x_enhanced_custom_shape_defaulter import XEnhancedCustomShapeDefaulter as XEnhancedCustomShapeDefaulter
with suppress(ImportError):
    from ...dyn.drawing.x_glue_points_supplier import XGluePointsSupplier as XGluePointsSupplier
with suppress(ImportError):
    from ...dyn.drawing.x_graphic_export_filter import XGraphicExportFilter as XGraphicExportFilter
with suppress(ImportError):
    from ...dyn.drawing.x_layer import XLayer as XLayer
with suppress(ImportError):
    from ...dyn.drawing.x_layer_manager import XLayerManager as XLayerManager
with suppress(ImportError):
    from ...dyn.drawing.x_layer_supplier import XLayerSupplier as XLayerSupplier
with suppress(ImportError):
    from ...dyn.drawing.x_master_page_target import XMasterPageTarget as XMasterPageTarget
with suppress(ImportError):
    from ...dyn.drawing.x_master_pages_supplier import XMasterPagesSupplier as XMasterPagesSupplier
with suppress(ImportError):
    from ...dyn.drawing.x_presenter_helper import XPresenterHelper as XPresenterHelper
with suppress(ImportError):
    from ...dyn.drawing.x_selection_function import XSelectionFunction as XSelectionFunction
with suppress(ImportError):
    from ...dyn.drawing.x_shape import XShape as XShape
with suppress(ImportError):
    from ...dyn.drawing.x_shape_aligner import XShapeAligner as XShapeAligner
with suppress(ImportError):
    from ...dyn.drawing.x_shape_arranger import XShapeArranger as XShapeArranger
with suppress(ImportError):
    from ...dyn.drawing.x_shape_binder import XShapeBinder as XShapeBinder
with suppress(ImportError):
    from ...dyn.drawing.x_shape_combiner import XShapeCombiner as XShapeCombiner
with suppress(ImportError):
    from ...dyn.drawing.x_shape_descriptor import XShapeDescriptor as XShapeDescriptor
with suppress(ImportError):
    from ...dyn.drawing.x_shape_group import XShapeGroup as XShapeGroup
with suppress(ImportError):
    from ...dyn.drawing.x_shape_grouper import XShapeGrouper as XShapeGrouper
with suppress(ImportError):
    from ...dyn.drawing.x_shape_mirror import XShapeMirror as XShapeMirror
with suppress(ImportError):
    from ...dyn.drawing.x_shapes import XShapes as XShapes
with suppress(ImportError):
    from ...dyn.drawing.x_shapes2 import XShapes2 as XShapes2
with suppress(ImportError):
    from ...dyn.drawing.x_shapes3 import XShapes3 as XShapes3
with suppress(ImportError):
    from ...dyn.drawing.x_slide_preview_cache import XSlidePreviewCache as XSlidePreviewCache
with suppress(ImportError):
    from ...dyn.drawing.x_slide_preview_cache_listener import XSlidePreviewCacheListener as XSlidePreviewCacheListener
with suppress(ImportError):
    from ...dyn.drawing.x_slide_renderer import XSlideRenderer as XSlideRenderer
with suppress(ImportError):
    from ...dyn.drawing.x_slide_sorter_base import XSlideSorterBase as XSlideSorterBase
with suppress(ImportError):
    from ...dyn.drawing.x_universal_shape_descriptor import XUniversalShapeDescriptor as XUniversalShapeDescriptor
