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
    from ...dyn.rendering.argb_color import ARGBColor as ARGBColor
except ImportError:
    pass
try:
    from ...dyn.rendering.animation_attributes import AnimationAttributes as AnimationAttributes
except ImportError:
    pass
try:
    from ...dyn.rendering.animation_repeat import AnimationRepeat as AnimationRepeat
except ImportError:
    pass
try:
    from ...dyn.rendering.animation_repeat import AnimationRepeatEnum as AnimationRepeatEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.bitmap_canvas import BitmapCanvas as BitmapCanvas
except ImportError:
    pass
try:
    from ...dyn.rendering.blend_mode import BlendMode as BlendMode
except ImportError:
    pass
try:
    from ...dyn.rendering.blend_mode import BlendModeEnum as BlendModeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.canvas import Canvas as Canvas
except ImportError:
    pass
try:
    from ...dyn.rendering.canvas_factory import CanvasFactory as CanvasFactory
except ImportError:
    pass
try:
    from ...dyn.rendering.caret import Caret as Caret
except ImportError:
    pass
try:
    from ...dyn.rendering.color import Color as Color
except ImportError:
    pass
try:
    from ...dyn.rendering.color_component import ColorComponent as ColorComponent
except ImportError:
    pass
try:
    from ...dyn.rendering.color_component_tag import ColorComponentTag as ColorComponentTag
except ImportError:
    pass
try:
    from ...dyn.rendering.color_component_tag import ColorComponentTagEnum as ColorComponentTagEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.color_profile import ColorProfile as ColorProfile
except ImportError:
    pass
try:
    from ...dyn.rendering.color_space_type import ColorSpaceType as ColorSpaceType
except ImportError:
    pass
try:
    from ...dyn.rendering.color_space_type import ColorSpaceTypeEnum as ColorSpaceTypeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.composite_operation import CompositeOperation as CompositeOperation
except ImportError:
    pass
try:
    from ...dyn.rendering.composite_operation import CompositeOperationEnum as CompositeOperationEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.emphasis_mark import EmphasisMark as EmphasisMark
except ImportError:
    pass
try:
    from ...dyn.rendering.emphasis_mark import EmphasisMarkEnum as EmphasisMarkEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.fill_rule import FillRule as FillRule
except ImportError:
    pass
try:
    from ...dyn.rendering.floating_point_bitmap_format import FloatingPointBitmapFormat as FloatingPointBitmapFormat
except ImportError:
    pass
try:
    from ...dyn.rendering.floating_point_bitmap_format import FloatingPointBitmapFormatEnum as FloatingPointBitmapFormatEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.floating_point_bitmap_layout import FloatingPointBitmapLayout as FloatingPointBitmapLayout
except ImportError:
    pass
try:
    from ...dyn.rendering.font_info import FontInfo as FontInfo
except ImportError:
    pass
try:
    from ...dyn.rendering.font_metrics import FontMetrics as FontMetrics
except ImportError:
    pass
try:
    from ...dyn.rendering.font_request import FontRequest as FontRequest
except ImportError:
    pass
try:
    from ...dyn.rendering.integer_bitmap_layout import IntegerBitmapLayout as IntegerBitmapLayout
except ImportError:
    pass
try:
    from ...dyn.rendering.interpolation_mode import InterpolationMode as InterpolationMode
except ImportError:
    pass
try:
    from ...dyn.rendering.interpolation_mode import InterpolationModeEnum as InterpolationModeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.mtf_renderer import MtfRenderer as MtfRenderer
except ImportError:
    pass
try:
    from ...dyn.rendering.panose import Panose as Panose
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_arm_style import PanoseArmStyle as PanoseArmStyle
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_arm_style import PanoseArmStyleEnum as PanoseArmStyleEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_contrast import PanoseContrast as PanoseContrast
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_contrast import PanoseContrastEnum as PanoseContrastEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_family_types import PanoseFamilyTypes as PanoseFamilyTypes
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_family_types import PanoseFamilyTypesEnum as PanoseFamilyTypesEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_letter_form import PanoseLetterForm as PanoseLetterForm
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_letter_form import PanoseLetterFormEnum as PanoseLetterFormEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_midline import PanoseMidline as PanoseMidline
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_midline import PanoseMidlineEnum as PanoseMidlineEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_proportion import PanoseProportion as PanoseProportion
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_proportion import PanoseProportionEnum as PanoseProportionEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_serif_style import PanoseSerifStyle as PanoseSerifStyle
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_serif_style import PanoseSerifStyleEnum as PanoseSerifStyleEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_stroke_variation import PanoseStrokeVariation as PanoseStrokeVariation
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_stroke_variation import PanoseStrokeVariationEnum as PanoseStrokeVariationEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_weight import PanoseWeight as PanoseWeight
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_weight import PanoseWeightEnum as PanoseWeightEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_x_height import PanoseXHeight as PanoseXHeight
except ImportError:
    pass
try:
    from ...dyn.rendering.panose_x_height import PanoseXHeightEnum as PanoseXHeightEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.path_cap_type import PathCapType as PathCapType
except ImportError:
    pass
try:
    from ...dyn.rendering.path_cap_type import PathCapTypeEnum as PathCapTypeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.path_join_type import PathJoinType as PathJoinType
except ImportError:
    pass
try:
    from ...dyn.rendering.path_join_type import PathJoinTypeEnum as PathJoinTypeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.rgb_color import RGBColor as RGBColor
except ImportError:
    pass
try:
    from ...dyn.rendering.render_state import RenderState as RenderState
except ImportError:
    pass
try:
    from ...dyn.rendering.rendering_intent import RenderingIntent as RenderingIntent
except ImportError:
    pass
try:
    from ...dyn.rendering.rendering_intent import RenderingIntentEnum as RenderingIntentEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.repaint_result import RepaintResult as RepaintResult
except ImportError:
    pass
try:
    from ...dyn.rendering.repaint_result import RepaintResultEnum as RepaintResultEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.string_context import StringContext as StringContext
except ImportError:
    pass
try:
    from ...dyn.rendering.stroke_attributes import StrokeAttributes as StrokeAttributes
except ImportError:
    pass
try:
    from ...dyn.rendering.text_direction import TextDirection as TextDirection
except ImportError:
    pass
try:
    from ...dyn.rendering.text_direction import TextDirectionEnum as TextDirectionEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.text_hit import TextHit as TextHit
except ImportError:
    pass
try:
    from ...dyn.rendering.texture import Texture as Texture
except ImportError:
    pass
try:
    from ...dyn.rendering.texturing_mode import TexturingMode as TexturingMode
except ImportError:
    pass
try:
    from ...dyn.rendering.texturing_mode import TexturingModeEnum as TexturingModeEnum
except ImportError:
    pass
try:
    from ...dyn.rendering.view_state import ViewState as ViewState
except ImportError:
    pass
try:
    from ...dyn.rendering.volatile_content_destroyed_exception import VolatileContentDestroyedException as VolatileContentDestroyedException
except ImportError:
    pass
try:
    from ...dyn.rendering.x_animated_sprite import XAnimatedSprite as XAnimatedSprite
except ImportError:
    pass
try:
    from ...dyn.rendering.x_animation import XAnimation as XAnimation
except ImportError:
    pass
try:
    from ...dyn.rendering.x_bezier_poly_polygon2_d import XBezierPolyPolygon2D as XBezierPolyPolygon2D
except ImportError:
    pass
try:
    from ...dyn.rendering.x_bitmap import XBitmap as XBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_bitmap_canvas import XBitmapCanvas as XBitmapCanvas
except ImportError:
    pass
try:
    from ...dyn.rendering.x_bitmap_palette import XBitmapPalette as XBitmapPalette
except ImportError:
    pass
try:
    from ...dyn.rendering.x_buffer_controller import XBufferController as XBufferController
except ImportError:
    pass
try:
    from ...dyn.rendering.x_cached_primitive import XCachedPrimitive as XCachedPrimitive
except ImportError:
    pass
try:
    from ...dyn.rendering.x_canvas import XCanvas as XCanvas
except ImportError:
    pass
try:
    from ...dyn.rendering.x_canvas_font import XCanvasFont as XCanvasFont
except ImportError:
    pass
try:
    from ...dyn.rendering.x_color_space import XColorSpace as XColorSpace
except ImportError:
    pass
try:
    from ...dyn.rendering.x_custom_sprite import XCustomSprite as XCustomSprite
except ImportError:
    pass
try:
    from ...dyn.rendering.x_graphic_device import XGraphicDevice as XGraphicDevice
except ImportError:
    pass
try:
    from ...dyn.rendering.x_half_float_bitmap import XHalfFloatBitmap as XHalfFloatBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_half_float_read_only_bitmap import XHalfFloatReadOnlyBitmap as XHalfFloatReadOnlyBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_ieee_double_bitmap import XIeeeDoubleBitmap as XIeeeDoubleBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_ieee_double_read_only_bitmap import XIeeeDoubleReadOnlyBitmap as XIeeeDoubleReadOnlyBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_ieee_float_bitmap import XIeeeFloatBitmap as XIeeeFloatBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_ieee_float_read_only_bitmap import XIeeeFloatReadOnlyBitmap as XIeeeFloatReadOnlyBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_integer_bitmap import XIntegerBitmap as XIntegerBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_integer_bitmap_color_space import XIntegerBitmapColorSpace as XIntegerBitmapColorSpace
except ImportError:
    pass
try:
    from ...dyn.rendering.x_integer_read_only_bitmap import XIntegerReadOnlyBitmap as XIntegerReadOnlyBitmap
except ImportError:
    pass
try:
    from ...dyn.rendering.x_line_poly_polygon2_d import XLinePolyPolygon2D as XLinePolyPolygon2D
except ImportError:
    pass
try:
    from ...dyn.rendering.x_mtf_renderer import XMtfRenderer as XMtfRenderer
except ImportError:
    pass
try:
    from ...dyn.rendering.x_parametric_poly_polygon2_d import XParametricPolyPolygon2D as XParametricPolyPolygon2D
except ImportError:
    pass
try:
    from ...dyn.rendering.x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D
except ImportError:
    pass
try:
    from ...dyn.rendering.x_simple_canvas import XSimpleCanvas as XSimpleCanvas
except ImportError:
    pass
try:
    from ...dyn.rendering.x_sprite import XSprite as XSprite
except ImportError:
    pass
try:
    from ...dyn.rendering.x_sprite_canvas import XSpriteCanvas as XSpriteCanvas
except ImportError:
    pass
try:
    from ...dyn.rendering.x_text_layout import XTextLayout as XTextLayout
except ImportError:
    pass
try:
    from ...dyn.rendering.x_volatile_bitmap import XVolatileBitmap as XVolatileBitmap
except ImportError:
    pass
