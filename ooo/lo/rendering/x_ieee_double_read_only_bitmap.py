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
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_bitmap import XBitmap as XBitmap_b1b70b7b
if typing.TYPE_CHECKING:
    from ..geometry.integer_point2_d import IntegerPoint2D as IntegerPoint2D_8f0dc2
    from ..geometry.integer_rectangle2_d import IntegerRectangle2D as IntegerRectangle2D_3c5c0f4d
    from .floating_point_bitmap_layout import FloatingPointBitmapLayout as FloatingPointBitmapLayout_c66812df

class XIeeeDoubleReadOnlyBitmap(XBitmap_b1b70b7b):
    """
    This is a specialized interface for bitmaps containing IEEE doubles for their color components.
    
    In contrast to XIeeeDoubleBitmap, this interface only permits read-only access.
    
    Use this interface for e.g. bitmaps that are calculated on-the-fly, or that are pure functional, and thus cannot be modified.
    
    If you get passed an instance of XHalfFloatReadOnlyBitmap that also supports the XVolatileBitmap interface, things become a bit more complicated. When reading data, one has to check for both VolatileContentDestroyedException and mismatching FloatingPointBitmapLayout return values. If either of them occurs, the whole bitmap read operation should be repeated.

    See Also:
        `API XIeeeDoubleReadOnlyBitmap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XIeeeDoubleReadOnlyBitmap.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XIeeeDoubleReadOnlyBitmap'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XIeeeDoubleReadOnlyBitmap'

    @abstractmethod
    def getData(self, bitmapLayout: FloatingPointBitmapLayout_c66812df, rect: IntegerRectangle2D_3c5c0f4d) -> typing.Tuple[float, ...]:
        """
        Query the raw data of this bitmap.
        
        Query the raw data of this bitmap, in the format as defined by getMemoryLayout(). With the given rectangle, a subset of the whole bitmap can be queried. When querying subsets of the bitmap, the same scanline padding takes place as when the whole bitmap is requested.
        
        Note that the bitmap memory layout might change for volatile bitmaps.

        * ``bitmapLayout`` is an out direction argument.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    @abstractmethod
    def getMemoryLayout(self) -> FloatingPointBitmapLayout_c66812df:
        """
        Query the memory layout for this bitmap.
        
        Please note that for volatile bitmaps, the memory layout might change between subsequent calls.
        """
        ...
    @abstractmethod
    def getPixel(self, bitmapLayout: FloatingPointBitmapLayout_c66812df, pos: IntegerPoint2D_8f0dc2) -> typing.Tuple[float, ...]:
        """
        Get a single pixel of the bitmap, returning its color value.
        
        Note that the bitmap memory layout might change for volatile bitmaps.

        * ``bitmapLayout`` is an out direction argument.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...

__all__ = ['XIeeeDoubleReadOnlyBitmap']

