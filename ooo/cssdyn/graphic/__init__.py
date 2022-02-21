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
    from ...dyn.graphic.emf_tools import EmfTools as EmfTools
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic import Graphic as Graphic
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_color_mode import GraphicColorMode as GraphicColorMode
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_color_mode import GraphicColorModeEnum as GraphicColorModeEnum
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_descriptor import GraphicDescriptor as GraphicDescriptor
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_mapper import GraphicMapper as GraphicMapper
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_object import GraphicObject as GraphicObject
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_provider import GraphicProvider as GraphicProvider
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_rasterizer import GraphicRasterizer as GraphicRasterizer
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_renderer_vcl import GraphicRendererVCL as GraphicRendererVCL
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_type import GraphicType as GraphicType
except ImportError:
    pass
try:
    from ...dyn.graphic.graphic_type import GraphicTypeEnum as GraphicTypeEnum
except ImportError:
    pass
try:
    from ...dyn.graphic.media_properties import MediaProperties as MediaProperties
except ImportError:
    pass
try:
    from ...dyn.graphic.pdf_tools import PdfTools as PdfTools
except ImportError:
    pass
try:
    from ...dyn.graphic.primitive2_d_tools import Primitive2DTools as Primitive2DTools
except ImportError:
    pass
try:
    from ...dyn.graphic.primitive_factory2_d import PrimitiveFactory2D as PrimitiveFactory2D
except ImportError:
    pass
try:
    from ...dyn.graphic.svg_tools import SvgTools as SvgTools
except ImportError:
    pass
try:
    from ...dyn.graphic.x_emf_parser import XEmfParser as XEmfParser
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic import XGraphic as XGraphic
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_mapper import XGraphicMapper as XGraphicMapper
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_object import XGraphicObject as XGraphicObject
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_provider import XGraphicProvider as XGraphicProvider
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_provider2 import XGraphicProvider2 as XGraphicProvider2
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_rasterizer import XGraphicRasterizer as XGraphicRasterizer
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_renderer import XGraphicRenderer as XGraphicRenderer
except ImportError:
    pass
try:
    from ...dyn.graphic.x_graphic_transformer import XGraphicTransformer as XGraphicTransformer
except ImportError:
    pass
try:
    from ...dyn.graphic.x_pdf_decomposer import XPdfDecomposer as XPdfDecomposer
except ImportError:
    pass
try:
    from ...dyn.graphic.x_primitive2_d import XPrimitive2D as XPrimitive2D
except ImportError:
    pass
try:
    from ...dyn.graphic.x_primitive2_d_renderer import XPrimitive2DRenderer as XPrimitive2DRenderer
except ImportError:
    pass
try:
    from ...dyn.graphic.x_primitive3_d import XPrimitive3D as XPrimitive3D
except ImportError:
    pass
try:
    from ...dyn.graphic.x_primitive_factory2_d import XPrimitiveFactory2D as XPrimitiveFactory2D
except ImportError:
    pass
try:
    from ...dyn.graphic.x_svg_parser import XSvgParser as XSvgParser
except ImportError:
    pass
