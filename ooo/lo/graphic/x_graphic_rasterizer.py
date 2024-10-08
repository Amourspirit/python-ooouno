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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.graphic
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_graphic import XGraphic as XGraphic_a4da0afc
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XGraphicRasterizer(XInterface_8f010a43):
    """
    This interfaces exposes the initialize and a rasterize method to rasterize a given data stream to a pixel graphic.

    See Also:
        `API XGraphicRasterizer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicRasterizer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XGraphicRasterizer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XGraphicRasterizer'

    @abstractmethod
    def initializeData(self, DataStream: XInputStream_98d40ab4, DPIX: int, DPIY: int, DefaultSizePixel: Size_576707ef) -> bool:
        """
        Initializing the rasterizer.
        
        This method could also be used to determine, if the provided data is able to be rasterized by the implementation. The implementation should take care of this feature as well as setting the default image size in pixel within the given output parameter.
        
        0
        
        is given, a horizontal default resolution of 72 DPI is used.
        
        0
        
        is given, a vertical default resolution of 72 DPI is used.
        
        In case no default size can be determined during initialization, a default pixel size of 0,0 is returned. In this case, the caller needs to assume a default pixel size, appropriate for the calling context.

        * ``DefaultSizePixel`` is an out direction argument.
        """
        ...
    @abstractmethod
    def rasterize(self, Width: int, Height: int, RotateAngle: float, ShearAngleX: float, ShearAngleY: float, RasterizeProperties: PropertyValues_d6470ce6) -> XGraphic_a4da0afc:
        """
        Rasterizing the initialized data into a XGraphic container.
        
        The XGraphic container will contain a pixel type graphic after a successful rasterization process
        
        In case of any fault during the rasterization process, the XGraphic container will be empty afterwards and the method will return false
        """
        ...

__all__ = ['XGraphicRasterizer']

