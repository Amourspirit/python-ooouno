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
    from ...dyn.graphic.emf_tools import EmfTools as EmfTools
with suppress(ImportError):
    from ...dyn.graphic.graphic import Graphic as Graphic
with suppress(ImportError):
    from ...dyn.graphic.graphic_color_mode import GraphicColorMode as GraphicColorMode
with suppress(ImportError):
    from ...dyn.graphic.graphic_color_mode import GraphicColorModeEnum as GraphicColorModeEnum
with suppress(ImportError):
    from ...dyn.graphic.graphic_descriptor import GraphicDescriptor as GraphicDescriptor
with suppress(ImportError):
    from ...dyn.graphic.graphic_mapper import GraphicMapper as GraphicMapper
with suppress(ImportError):
    from ...dyn.graphic.graphic_object import GraphicObject as GraphicObject
with suppress(ImportError):
    from ...dyn.graphic.graphic_provider import GraphicProvider as GraphicProvider
with suppress(ImportError):
    from ...dyn.graphic.graphic_rasterizer import GraphicRasterizer as GraphicRasterizer
with suppress(ImportError):
    from ...dyn.graphic.graphic_renderer_vcl import GraphicRendererVCL as GraphicRendererVCL
with suppress(ImportError):
    from ...dyn.graphic.graphic_type import GraphicType as GraphicType
with suppress(ImportError):
    from ...dyn.graphic.graphic_type import GraphicTypeEnum as GraphicTypeEnum
with suppress(ImportError):
    from ...dyn.graphic.media_properties import MediaProperties as MediaProperties
with suppress(ImportError):
    from ...dyn.graphic.pdf_tools import PdfTools as PdfTools
with suppress(ImportError):
    from ...dyn.graphic.primitive2_d_tools import Primitive2DTools as Primitive2DTools
with suppress(ImportError):
    from ...dyn.graphic.primitive_factory2_d import PrimitiveFactory2D as PrimitiveFactory2D
with suppress(ImportError):
    from ...dyn.graphic.svg_tools import SvgTools as SvgTools
with suppress(ImportError):
    from ...dyn.graphic.x_emf_parser import XEmfParser as XEmfParser
with suppress(ImportError):
    from ...dyn.graphic.x_graphic import XGraphic as XGraphic
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_mapper import XGraphicMapper as XGraphicMapper
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_object import XGraphicObject as XGraphicObject
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_provider import XGraphicProvider as XGraphicProvider
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_provider2 import XGraphicProvider2 as XGraphicProvider2
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_rasterizer import XGraphicRasterizer as XGraphicRasterizer
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_renderer import XGraphicRenderer as XGraphicRenderer
with suppress(ImportError):
    from ...dyn.graphic.x_graphic_transformer import XGraphicTransformer as XGraphicTransformer
with suppress(ImportError):
    from ...dyn.graphic.x_pdf_decomposer import XPdfDecomposer as XPdfDecomposer
with suppress(ImportError):
    from ...dyn.graphic.x_primitive2_d import XPrimitive2D as XPrimitive2D
with suppress(ImportError):
    from ...dyn.graphic.x_primitive2_d_renderer import XPrimitive2DRenderer as XPrimitive2DRenderer
with suppress(ImportError):
    from ...dyn.graphic.x_primitive3_d import XPrimitive3D as XPrimitive3D
with suppress(ImportError):
    from ...dyn.graphic.x_primitive_factory2_d import XPrimitiveFactory2D as XPrimitiveFactory2D
with suppress(ImportError):
    from ...dyn.graphic.x_svg_parser import XSvgParser as XSvgParser
