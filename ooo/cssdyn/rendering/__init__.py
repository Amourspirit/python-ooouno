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
    from ...dyn.rendering.argb_color import ARGBColor as ARGBColor
with suppress(ImportError):
    from ...dyn.rendering.animation_attributes import AnimationAttributes as AnimationAttributes
with suppress(ImportError):
    from ...dyn.rendering.animation_repeat import AnimationRepeat as AnimationRepeat
with suppress(ImportError):
    from ...dyn.rendering.animation_repeat import AnimationRepeatEnum as AnimationRepeatEnum
with suppress(ImportError):
    from ...dyn.rendering.bitmap_canvas import BitmapCanvas as BitmapCanvas
with suppress(ImportError):
    from ...dyn.rendering.blend_mode import BlendMode as BlendMode
with suppress(ImportError):
    from ...dyn.rendering.blend_mode import BlendModeEnum as BlendModeEnum
with suppress(ImportError):
    from ...dyn.rendering.canvas import Canvas as Canvas
with suppress(ImportError):
    from ...dyn.rendering.canvas_factory import CanvasFactory as CanvasFactory
with suppress(ImportError):
    from ...dyn.rendering.caret import Caret as Caret
with suppress(ImportError):
    from ...dyn.rendering.color import Color as Color
with suppress(ImportError):
    from ...dyn.rendering.color_component import ColorComponent as ColorComponent
with suppress(ImportError):
    from ...dyn.rendering.color_component_tag import ColorComponentTag as ColorComponentTag
with suppress(ImportError):
    from ...dyn.rendering.color_component_tag import ColorComponentTagEnum as ColorComponentTagEnum
with suppress(ImportError):
    from ...dyn.rendering.color_profile import ColorProfile as ColorProfile
with suppress(ImportError):
    from ...dyn.rendering.color_space_type import ColorSpaceType as ColorSpaceType
with suppress(ImportError):
    from ...dyn.rendering.color_space_type import ColorSpaceTypeEnum as ColorSpaceTypeEnum
with suppress(ImportError):
    from ...dyn.rendering.composite_operation import CompositeOperation as CompositeOperation
with suppress(ImportError):
    from ...dyn.rendering.composite_operation import CompositeOperationEnum as CompositeOperationEnum
with suppress(ImportError):
    from ...dyn.rendering.emphasis_mark import EmphasisMark as EmphasisMark
with suppress(ImportError):
    from ...dyn.rendering.emphasis_mark import EmphasisMarkEnum as EmphasisMarkEnum
with suppress(ImportError):
    from ...dyn.rendering.fill_rule import FillRule as FillRule
with suppress(ImportError):
    from ...dyn.rendering.floating_point_bitmap_format import FloatingPointBitmapFormat as FloatingPointBitmapFormat
with suppress(ImportError):
    from ...dyn.rendering.floating_point_bitmap_format import FloatingPointBitmapFormatEnum as FloatingPointBitmapFormatEnum
with suppress(ImportError):
    from ...dyn.rendering.floating_point_bitmap_layout import FloatingPointBitmapLayout as FloatingPointBitmapLayout
with suppress(ImportError):
    from ...dyn.rendering.font_info import FontInfo as FontInfo
with suppress(ImportError):
    from ...dyn.rendering.font_metrics import FontMetrics as FontMetrics
with suppress(ImportError):
    from ...dyn.rendering.font_request import FontRequest as FontRequest
with suppress(ImportError):
    from ...dyn.rendering.integer_bitmap_layout import IntegerBitmapLayout as IntegerBitmapLayout
with suppress(ImportError):
    from ...dyn.rendering.interpolation_mode import InterpolationMode as InterpolationMode
with suppress(ImportError):
    from ...dyn.rendering.interpolation_mode import InterpolationModeEnum as InterpolationModeEnum
with suppress(ImportError):
    from ...dyn.rendering.mtf_renderer import MtfRenderer as MtfRenderer
with suppress(ImportError):
    from ...dyn.rendering.panose import Panose as Panose
with suppress(ImportError):
    from ...dyn.rendering.panose_arm_style import PanoseArmStyle as PanoseArmStyle
with suppress(ImportError):
    from ...dyn.rendering.panose_arm_style import PanoseArmStyleEnum as PanoseArmStyleEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_contrast import PanoseContrast as PanoseContrast
with suppress(ImportError):
    from ...dyn.rendering.panose_contrast import PanoseContrastEnum as PanoseContrastEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_family_types import PanoseFamilyTypes as PanoseFamilyTypes
with suppress(ImportError):
    from ...dyn.rendering.panose_family_types import PanoseFamilyTypesEnum as PanoseFamilyTypesEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_letter_form import PanoseLetterForm as PanoseLetterForm
with suppress(ImportError):
    from ...dyn.rendering.panose_letter_form import PanoseLetterFormEnum as PanoseLetterFormEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_midline import PanoseMidline as PanoseMidline
with suppress(ImportError):
    from ...dyn.rendering.panose_midline import PanoseMidlineEnum as PanoseMidlineEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_proportion import PanoseProportion as PanoseProportion
with suppress(ImportError):
    from ...dyn.rendering.panose_proportion import PanoseProportionEnum as PanoseProportionEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_serif_style import PanoseSerifStyle as PanoseSerifStyle
with suppress(ImportError):
    from ...dyn.rendering.panose_serif_style import PanoseSerifStyleEnum as PanoseSerifStyleEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_stroke_variation import PanoseStrokeVariation as PanoseStrokeVariation
with suppress(ImportError):
    from ...dyn.rendering.panose_stroke_variation import PanoseStrokeVariationEnum as PanoseStrokeVariationEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_weight import PanoseWeight as PanoseWeight
with suppress(ImportError):
    from ...dyn.rendering.panose_weight import PanoseWeightEnum as PanoseWeightEnum
with suppress(ImportError):
    from ...dyn.rendering.panose_x_height import PanoseXHeight as PanoseXHeight
with suppress(ImportError):
    from ...dyn.rendering.panose_x_height import PanoseXHeightEnum as PanoseXHeightEnum
with suppress(ImportError):
    from ...dyn.rendering.path_cap_type import PathCapType as PathCapType
with suppress(ImportError):
    from ...dyn.rendering.path_cap_type import PathCapTypeEnum as PathCapTypeEnum
with suppress(ImportError):
    from ...dyn.rendering.path_join_type import PathJoinType as PathJoinType
with suppress(ImportError):
    from ...dyn.rendering.path_join_type import PathJoinTypeEnum as PathJoinTypeEnum
with suppress(ImportError):
    from ...dyn.rendering.rgb_color import RGBColor as RGBColor
with suppress(ImportError):
    from ...dyn.rendering.render_state import RenderState as RenderState
with suppress(ImportError):
    from ...dyn.rendering.rendering_intent import RenderingIntent as RenderingIntent
with suppress(ImportError):
    from ...dyn.rendering.rendering_intent import RenderingIntentEnum as RenderingIntentEnum
with suppress(ImportError):
    from ...dyn.rendering.repaint_result import RepaintResult as RepaintResult
with suppress(ImportError):
    from ...dyn.rendering.repaint_result import RepaintResultEnum as RepaintResultEnum
with suppress(ImportError):
    from ...dyn.rendering.string_context import StringContext as StringContext
with suppress(ImportError):
    from ...dyn.rendering.stroke_attributes import StrokeAttributes as StrokeAttributes
with suppress(ImportError):
    from ...dyn.rendering.text_direction import TextDirection as TextDirection
with suppress(ImportError):
    from ...dyn.rendering.text_direction import TextDirectionEnum as TextDirectionEnum
with suppress(ImportError):
    from ...dyn.rendering.text_hit import TextHit as TextHit
with suppress(ImportError):
    from ...dyn.rendering.texture import Texture as Texture
with suppress(ImportError):
    from ...dyn.rendering.texturing_mode import TexturingMode as TexturingMode
with suppress(ImportError):
    from ...dyn.rendering.texturing_mode import TexturingModeEnum as TexturingModeEnum
with suppress(ImportError):
    from ...dyn.rendering.view_state import ViewState as ViewState
with suppress(ImportError):
    from ...dyn.rendering.volatile_content_destroyed_exception import VolatileContentDestroyedException as VolatileContentDestroyedException
with suppress(ImportError):
    from ...dyn.rendering.x_animated_sprite import XAnimatedSprite as XAnimatedSprite
with suppress(ImportError):
    from ...dyn.rendering.x_animation import XAnimation as XAnimation
with suppress(ImportError):
    from ...dyn.rendering.x_bezier_poly_polygon2_d import XBezierPolyPolygon2D as XBezierPolyPolygon2D
with suppress(ImportError):
    from ...dyn.rendering.x_bitmap import XBitmap as XBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_bitmap_canvas import XBitmapCanvas as XBitmapCanvas
with suppress(ImportError):
    from ...dyn.rendering.x_bitmap_palette import XBitmapPalette as XBitmapPalette
with suppress(ImportError):
    from ...dyn.rendering.x_buffer_controller import XBufferController as XBufferController
with suppress(ImportError):
    from ...dyn.rendering.x_cached_primitive import XCachedPrimitive as XCachedPrimitive
with suppress(ImportError):
    from ...dyn.rendering.x_canvas import XCanvas as XCanvas
with suppress(ImportError):
    from ...dyn.rendering.x_canvas_font import XCanvasFont as XCanvasFont
with suppress(ImportError):
    from ...dyn.rendering.x_color_space import XColorSpace as XColorSpace
with suppress(ImportError):
    from ...dyn.rendering.x_custom_sprite import XCustomSprite as XCustomSprite
with suppress(ImportError):
    from ...dyn.rendering.x_graphic_device import XGraphicDevice as XGraphicDevice
with suppress(ImportError):
    from ...dyn.rendering.x_half_float_bitmap import XHalfFloatBitmap as XHalfFloatBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_half_float_read_only_bitmap import XHalfFloatReadOnlyBitmap as XHalfFloatReadOnlyBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_ieee_double_bitmap import XIeeeDoubleBitmap as XIeeeDoubleBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_ieee_double_read_only_bitmap import XIeeeDoubleReadOnlyBitmap as XIeeeDoubleReadOnlyBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_ieee_float_bitmap import XIeeeFloatBitmap as XIeeeFloatBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_ieee_float_read_only_bitmap import XIeeeFloatReadOnlyBitmap as XIeeeFloatReadOnlyBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_integer_bitmap import XIntegerBitmap as XIntegerBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_integer_bitmap_color_space import XIntegerBitmapColorSpace as XIntegerBitmapColorSpace
with suppress(ImportError):
    from ...dyn.rendering.x_integer_read_only_bitmap import XIntegerReadOnlyBitmap as XIntegerReadOnlyBitmap
with suppress(ImportError):
    from ...dyn.rendering.x_line_poly_polygon2_d import XLinePolyPolygon2D as XLinePolyPolygon2D
with suppress(ImportError):
    from ...dyn.rendering.x_mtf_renderer import XMtfRenderer as XMtfRenderer
with suppress(ImportError):
    from ...dyn.rendering.x_parametric_poly_polygon2_d import XParametricPolyPolygon2D as XParametricPolyPolygon2D
with suppress(ImportError):
    from ...dyn.rendering.x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D
with suppress(ImportError):
    from ...dyn.rendering.x_simple_canvas import XSimpleCanvas as XSimpleCanvas
with suppress(ImportError):
    from ...dyn.rendering.x_sprite import XSprite as XSprite
with suppress(ImportError):
    from ...dyn.rendering.x_sprite_canvas import XSpriteCanvas as XSpriteCanvas
with suppress(ImportError):
    from ...dyn.rendering.x_text_layout import XTextLayout as XTextLayout
with suppress(ImportError):
    from ...dyn.rendering.x_volatile_bitmap import XVolatileBitmap as XVolatileBitmap
