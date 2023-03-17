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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..geometry.matrix2_d import Matrix2D as Matrix2D_b26c0b5f
    from ..geometry.real_bezier_segment2_d import RealBezierSegment2D as RealBezierSegment2D_4a970fa2
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..geometry.x_mapping2_d import XMapping2D as XMapping2D_ca1e0c0e
    from .font_info import FontInfo as FontInfo_bded0be9
    from .font_request import FontRequest as FontRequest_e4890d46
    from .render_state import RenderState as RenderState_e4490d27
    from .string_context import StringContext as StringContext_d50e22
    from .stroke_attributes import StrokeAttributes as StrokeAttributes_2dd10f65
    from .texture import Texture as Texture_b2e70bb7
    from .view_state import ViewState as ViewState_cab30c62
    from .x_bitmap import XBitmap as XBitmap_b1b70b7b
    from .x_cached_primitive import XCachedPrimitive as XCachedPrimitive_29890f0f
    from .x_canvas_font import XCanvasFont as XCanvasFont_e3380d11
    from .x_graphic_device import XGraphicDevice as XGraphicDevice_ca80e2c
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20
    from .x_text_layout import XTextLayout as XTextLayout_e44a0d41

class XCanvas(XInterface_8f010a43):
    """
    Central interface for rendering.
    
    This is the central interface for graphical output production, and the place where all draw methods are located.
    
    Some notes are in order to explain the concepts used here. The XCanvas interface is free of client-modifiable state, i.e. it can be used safely and without external synchronization in a multi-threaded environment. On the other hand, this implies that for nearly every canvas operation, external state is required. This is provided by ViewState and RenderState in a unified fashion, supplemented by a few extra state parameters for some methods (e.g. textured polygons or text rendering).
    
    When used careless, this scheme can be inefficient to some extend, because internally, view, render and other states have to be combined before rendering. This is especially expensive for complex clip polygons, i.e. when both ViewState and RenderState have a complex clip polygon set, which have to be intersected before rendering. It is therefore recommended to combine ViewState and RenderState already at the client side, when objects are organized in a hierarchical way: the classic example are grouped draw shapes, whose parent group object imposes a common clipping and a common transformation on its siblings. The group object would therefore merge the ViewState and the RenderState it is called with into a new ViewState, and call its siblings with a RenderState containing only the local offset (and no extra clipping).
    
    Further on, this stateless nature provides easy ways for caching. Every non-trivial operation on XCanvas can return a cache object, which, when called to redraw, renders the primitive usually much more quickly than the original method. Note that such caching is a lot more complicated, should the actual rendering a method yields depend on internal state (which is the case e.g. for the com.sun.star.awt.XGraphics interface). Please note, though, that deciding whether to return an XCachedPrimitive is completely up to the implementation - don't rely on the methods returning something (this is because there might be cases when returning such a cache object will actually be a pessimization, since it involves memory allocation and comparisons).
    
    Things that need more than a small, fixed amount of data are encapsulated in own interfaces, e.g. polygons and bitmaps. You can, in principle, roll your own implementations of these interfaces, wrap it around your internal representation of polygons and bitmaps, and render them. It might just not be overly fast, because the XCanvas would need to convert for each render call. It is therefore recommended to create such objects via the XGraphicDevice factory (to be retrieved from every canvas object via the getDevice() call) - they will then internally optimize to the underlying graphics subsystem.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XCanvas <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XCanvas.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XCanvas'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XCanvas'

    @abstractmethod
    def clear(self) -> None:
        """
        Clear the whole canvas area.
        
        This method clears the whole canvas area to the device default color (e.g. white for a printer, transparent for an XCustomSprite).
        """
        ...
    @abstractmethod
    def createFont(self, aFontRequest: 'FontRequest_e4890d46', aExtraFontProperties: 'typing.Tuple[PropertyValue_c9610c73, ...]', aFontMatrix: 'Matrix2D_b26c0b5f') -> 'XCanvasFont_e3380d11':
        """
        Create a suitable font for the specified font description.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawBezier(self, aBezierSegment: 'RealBezierSegment2D_4a970fa2', aEndPoint: 'RealPoint2D_d6e70c78', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> None:
        """
        Draw a cubic Bezier curve in device resolution width (i.e.
        
        one device pixel wide).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawBitmap(self, xBitmap: 'XBitmap_b1b70b7b', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> 'XCachedPrimitive_29890f0f':
        """
        Render the given bitmap.
        
        This method renders the bitmap, at a position and shape as specified by the combined view and render transformations. For fast render speed, the bitmap should be created by the corresponding XGraphicDevice's XGraphicDevice.createCompatibleBitmap() method.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def drawBitmapModulated(self, xBitmap: 'XBitmap_b1b70b7b', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> 'XCachedPrimitive_29890f0f':
        """
        Render the given bitmap, with a global color modulation.
        
        This method renders the bitmap, at a position and shape as specified by the combined view and render transformations. For fast render speed, the bitmap should be created by the corresponding XGraphicDevice's XGraphicDevice.createCompatibleBitmap() method. The bitmap's color channel values are multiplied with the device color values as specified in the render state.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def drawLine(self, aStartPoint: 'RealPoint2D_d6e70c78', aEndPoint: 'RealPoint2D_d6e70c78', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> None:
        """
        Draw a line in device resolution width (i.e.
        
        one device pixel wide).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawPoint(self, aPoint: 'RealPoint2D_d6e70c78', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> None:
        """
        Draw a point in device resolution on the device.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> 'XCachedPrimitive_29890f0f':
        """
        Draw a poly-polygon in device resolution line width (i.e.
        
        the lines are one device pixel wide).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawText(self, aText: 'StringContext_d50e22', xFont: 'XCanvasFont_e3380d11', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', nTextDirection: int) -> 'XCachedPrimitive_29890f0f':
        """
        Draw the text given by the substring of the specified string with the given font.
        
        The local origin of this output operation is either the left end of the text baseline, for textDirection equal LEFT_TO_RIGHT, or the right end of the baseline, for textDirection equal to RIGHT_TO_LEFT, respectively.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def drawTextLayout(self, xLayoutetText: 'XTextLayout_e44a0d41', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> 'XCachedPrimitive_29890f0f':
        """
        Draw the formatted text given by the text layout.
        
        The glyphs as represented by the text layout are always output with the reference position being the leftmost edge of the layout object's baseline. If the layout contains more than one baseline, the baseline of the first strong character in logical order is used here (strong in this context means that the character can be unambiguously assigned to a Unicode script).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def fillPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> 'XCachedPrimitive_29890f0f':
        """
        Fill the given poly-polygon.
        
        This method fills the given poly-polygon according to the RenderState's color and the poly-polygon's fill rule.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def fillTextureMappedPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', xTextures: 'typing.Tuple[Texture_b2e70bb7, ...]', xMapping: 'XMapping2D_ca1e0c0e') -> 'XCachedPrimitive_29890f0f':
        """
        Fill the given poly-polygon with a mapped texture.
        
        This method fills the given poly-polygon according to the RenderState's color, the given textures and poly-polygon's fill rule. The texture is mapped to the poly-polygon's interior via the given texture mapping.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def fillTexturedPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', xTextures: 'typing.Tuple[Texture_b2e70bb7, ...]') -> 'XCachedPrimitive_29890f0f':
        """
        Fill the given poly-polygon with a texture.
        
        This method fills the given poly-polygon according to the RenderState's color, the given textures and poly-polygon's fill rule.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def getDevice(self) -> 'XGraphicDevice_ca80e2c':
        """
        Request the associated graphic device for this canvas.
        
        A graphic device provides methods specific to the underlying output device capabilities, which are common for all canvases rendering to such a device. This includes device resolution, color space, or bitmap formats.
        """
        ...
    @abstractmethod
    def queryAvailableFonts(self, aFilter: 'FontInfo_bded0be9', aFontProperties: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[FontInfo_bded0be9, ...]':
        """
        Query font information, specific to this canvas.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def queryStrokeShapes(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', aStrokeAttributes: 'StrokeAttributes_2dd10f65') -> 'XPolyPolygon2D_e1b0e20':
        """
        Query the polygonal representation of the stroke outlines, as it would be generated by the strokePolyPolygon methods.
        
        This method can be used to e.g. set a clipping which covers the same area as a stroke.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def strokePolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', aStrokeAttributes: 'StrokeAttributes_2dd10f65') -> 'XCachedPrimitive_29890f0f':
        """
        Stroke each polygon of the provided poly-polygon with the specified stroke attributes.
        
        This method considers the stroking of all polygons as an atomic operation in relation to the RenderState's CompositeOperationy operation. That means, overlapping strokes from distinct polygons will look exactly as overlapping segments of the same polygon, even with transparency.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def strokeTextureMappedPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', aTextures: 'typing.Tuple[Texture_b2e70bb7, ...]', xMapping: 'XMapping2D_ca1e0c0e', aStrokeAttributes: 'StrokeAttributes_2dd10f65') -> 'XCachedPrimitive_29890f0f':
        """
        Stroke each polygon of the provided poly-polygon with the specified stroke attributes, fill the stroked outline with the specified texture graphics, map the texture to the outline via the specified texture mapping.
        
        This method considers the stroking of all polygons as an atomic operation in relation to the RenderState's CompositeOp operation. That means, overlapping strokes from distinct polygons will look exactly as overlapping segments of the same polygon, even with transparency.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def strokeTexturedPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27', aTextures: 'typing.Tuple[Texture_b2e70bb7, ...]', aStrokeAttributes: 'StrokeAttributes_2dd10f65') -> 'XCachedPrimitive_29890f0f':
        """
        Stroke each polygon of the provided poly-polygon with the specified stroke attributes, fill the stroked outline with the specified texture graphics.
        
        This method considers the stroking of all polygons as an atomic operation in relation to the RenderState's CompositeOp operation. That means, overlapping strokes from distinct polygons will look exactly as overlapping segments of the same polygon, even with transparency.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...

__all__ = ['XCanvas']

