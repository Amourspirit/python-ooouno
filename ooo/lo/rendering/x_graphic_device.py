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
    from ..geometry.integer_size2_d import IntegerSize2D as IntegerSize2D_f2690d53
    from ..geometry.real_bezier_segment2_d import RealBezierSegment2D as RealBezierSegment2D_4a970fa2
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..geometry.real_size2_d import RealSize2D as RealSize2D_ca1a0c09
    from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
    from .x_bezier_poly_polygon2_d import XBezierPolyPolygon2D as XBezierPolyPolygon2D_6ba01081
    from .x_bitmap import XBitmap as XBitmap_b1b70b7b
    from .x_buffer_controller import XBufferController as XBufferController_3a970f9c
    from .x_color_space import XColorSpace as XColorSpace_e3940d09
    from .x_line_poly_polygon2_d import XLinePolyPolygon2D as XLinePolyPolygon2D_4a270fa8
    from .x_volatile_bitmap import XVolatileBitmap as XVolatileBitmap_1ca40ebb

class XGraphicDevice(XInterface_8f010a43):
    """
    This interface provides access to a graphic device, such as a printer, or a screen device.
    
    Every canvas (
    
    For a typical windowing system, the graphic device is equivalent to a distinct OS window, with its own clipped output area, fullscreen and double-buffering attributes. That is, even if one can have multiple canvases per system window, they all share the same graphic device and thus e.g. fullscreen state. If the OS restrictions are in such a way that fullscreen or double-buffering is screen-exclusive, i.e. that per screen, only one object can have this state, it might even be that all windows on the screen share a common graphic device.

    See Also:
        `API XGraphicDevice <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XGraphicDevice.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XGraphicDevice'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XGraphicDevice'

    @abstractmethod
    def createCompatibleAlphaBitmap(self, size: 'IntegerSize2D_f2690d53') -> 'XBitmap_b1b70b7b':
        """
        Create a bitmap with alpha channel whose memory layout and sample model is compatible to the graphic device.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createCompatibleBezierPolyPolygon(self, points: 'typing.Tuple[typing.Tuple[RealBezierSegment2D_4a970fa2, ...], ...]') -> 'XBezierPolyPolygon2D_6ba01081':
        """
        Create a Bezier poly-polygon which can internally use device-optimized representations already.
        """
        ...
    @abstractmethod
    def createCompatibleBitmap(self, size: 'IntegerSize2D_f2690d53') -> 'XBitmap_b1b70b7b':
        """
        Create a bitmap whose memory layout and sample model is compatible to the graphic device.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createCompatibleLinePolyPolygon(self, points: 'typing.Tuple[typing.Tuple[RealPoint2D_d6e70c78, ...], ...]') -> 'XLinePolyPolygon2D_4a270fa8':
        """
        Create a line poly-polygon which can internally use device-optimized representations already.
        """
        ...
    @abstractmethod
    def createVolatileAlphaBitmap(self, size: 'IntegerSize2D_f2690d53') -> 'XVolatileBitmap_1ca40ebb':
        """
        Create a volatile bitmap with alpha channel that is usable with this graphic device.
        
        A volatile bitmap's difference in comparison to a plain bitmap (e.g. generated via createCompatibleBitmap()) is the fact that its content might vanish at any point in time (making any operation with them produce a VolatileContentDestroyedException). The benefit, on the other hand, is that they might be easy to hardware-accelerate on certain platforms, without the need to keep a safety copy of the content internally.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createVolatileBitmap(self, size: 'IntegerSize2D_f2690d53') -> 'XVolatileBitmap_1ca40ebb':
        """
        Create a volatile bitmap that is usable with this graphic device.
        
        A volatile bitmap's difference in comparison to a plain bitmap (e.g. generated via createCompatibleBitmap()) is the fact that its content might vanish at any point in time (making any operation with them produce a VolatileContentDestroyedException). The benefit, on the other hand, is that they might be easy to hardware-accelerate on certain platforms, without the need to keep a safety copy of the content internally.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def enterFullScreenMode(self, bEnter: bool) -> bool:
        """
        Enter or leave the fullscreen mode, if possible.
        
        The return value denotes the success of the operation.
        """
        ...
    @abstractmethod
    def getBufferController(self) -> 'XBufferController_3a970f9c':
        """
        Query the controller for multi buffering functionality on this graphic device.
        
        If there is no such functionality available, the NULL reference is returned.
        """
        ...
    @abstractmethod
    def getDeviceColorSpace(self) -> 'XColorSpace_e3940d09':
        """
        Query the color space interface for this graphic device.
        
        This is to be used when interpreting or setting device color values.
        """
        ...
    @abstractmethod
    def getParametricPolyPolygonFactory(self) -> 'XMultiServiceFactory_191e0eb6':
        """
        Get a reference to this device's parametric polygon factory.
        
        Available services (all canvas implementations should provide this minimal set, though are free to add more; just check the getAvailableServiceNames() on the returned interface):
        """
        ...
    @abstractmethod
    def getPhysicalResolution(self) -> 'RealSize2D_ca1a0c09':
        """
        Query the physical resolution of the device in pixel per millimeter.
        
        A special floating point value of +infinity here indicates \"unknown\", i.e. at the time of rendering undetermined or possibly infinite resolution along the corresponding direction.
        """
        ...
    @abstractmethod
    def getPhysicalSize(self) -> 'RealSize2D_ca1a0c09':
        """
        Query the physical dimensions of the device in millimeter.
        
        A special floating point value of +infinity here indicates \"unknown\", i.e. at the time of rendering undetermined or possibly infinite resolution along the corresponding direction.
        """
        ...
    @abstractmethod
    def hasFullScreenMode(self) -> bool:
        """
        Tells whether this graphic device has a full screen mode, i.e.
        
        whether a window can cover the whole screen exclusively.
        """
        ...

__all__ = ['XGraphicDevice']

