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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.gradient import Gradient as Gradient_7a8a0982
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909
    from .bitmap_mode import BitmapMode as BitmapMode_bced0bd6
    from .fill_style import FillStyle as FillStyle_b1460b8c
    from .hatch import Hatch as Hatch_859b09dc
    from .rectangle_point import RectanglePoint as RectanglePoint_f0ff0d93
    from ..text.graphic_crop import GraphicCrop as GraphicCrop_a58e0b1f
    from ..util.color import Color as Color_68e908c5

class FillProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style for rendering an area.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API FillProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1FillProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.FillProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def FillBackground(self) -> bool:
        """
        if this is TRUE, the transparent background of a hatch filled area is drawn in the current background color.
        """

    @abstractproperty
    def FillBitmap(self) -> 'XBitmap_70cd0909':
        """
        If the property FillStyle is set to FillStyle.BITMAP, this is the bitmap used.
        """

    @abstractproperty
    def FillBitmapLogicalSize(self) -> bool:
        """
        specifies if the size is given in percentage or as an absolute value.
        
        If this is TRUE, the properties FillBitmapSizeX and FillBitmapSizeY contain the size of the tile in percent of the size of the original bitmap. If this is FALSE, the size of the tile is specified with 1/100th mm.
        """

    @abstractproperty
    def FillBitmapMode(self) -> 'BitmapMode_bced0bd6':
        """
        this enum selects how an area is filled with a single bitmap.
        
        This property corresponds to the properties FillBitmapStretch and FillBitmapTile.
        
        If set to BitmapMode.REPEAT, the property FillBitmapStretch is set to FALSE, and the property FillBitmapTile is set to TRUE.
        
        If set to BitmapMode.STRETCH, the property FillBitmapStretch is set to TRUE, and the property FillBitmapTile is set to FALSE.
        
        If set to BitmapMode.NO_REPEAT, both properties FillBitmapStretch and FillBitmapTile are set to FALSE.
        """

    @abstractproperty
    def FillBitmapName(self) -> str:
        """
        If the property FillStyle is set to FillStyle.BITMAP, this is the name of the used fill bitmap style.
        """

    @abstractproperty
    def FillBitmapOffsetX(self) -> int:
        """
        Every second line of tiles is moved the given percent of the width of the bitmap.
        """

    @abstractproperty
    def FillBitmapOffsetY(self) -> int:
        """
        Every second row of tiles is moved the given percent of the height of the bitmap.
        """

    @abstractproperty
    def FillBitmapPositionOffsetX(self) -> int:
        """
        This is the horizontal offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """

    @abstractproperty
    def FillBitmapPositionOffsetY(self) -> int:
        """
        This is the vertical offset where the tile starts.
        
        It is given in percent in relation to the height of the bitmap.
        """

    @abstractproperty
    def FillBitmapRectanglePoint(self) -> 'RectanglePoint_f0ff0d93':
        """
        The RectanglePoint specifies the position inside of the bitmap to use as the top left position for rendering.
        """

    @abstractproperty
    def FillBitmapSizeX(self) -> int:
        """
        This is the width of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """

    @abstractproperty
    def FillBitmapSizeY(self) -> int:
        """
        This is the height of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """

    @abstractproperty
    def FillBitmapStretch(self) -> bool:
        """
        if set, the fill bitmap is stretched to fill the area of the shape.
        
        This property should not be used anymore and is included here for completeness. The FillBitmapMode property can be used instead to set all supported bitmap modes.
        
        If set to TRUE, the value of the FillBitmapMode property changes to BitmapMode.STRETCH. BUT: behavior is undefined, if the property FillBitmapTile is TRUE too.
        
        If set to FALSE, the value of the FillBitmapMode property changes to BitmapMode.REPEAT or BitmapMode.NO_REPEAT, depending on the current value of the FillBitmapTile property.
        """

    @abstractproperty
    def FillBitmapTile(self) -> bool:
        """
        if set, the fill bitmap is repeated to fill the area of the shape.
        
        This property should not be used anymore and is included here for completeness. The FillBitmapMode property can be used instead to set all supported bitmap modes.
        
        If set to TRUE, the value of the FillBitmapMode property changes to BitmapMode.REPEAT. BUT: behavior is undefined, if the property FillBitmapStretch is TRUE too.
        
        If set to FALSE, the value of the FillBitmapMode property changes to BitmapMode.STRETCH or BitmapMode.NO_REPEAT, depending on the current value of the FillBitmapStretch property.
        """

    @abstractproperty
    def FillBitmapURL(self) -> str:
        """
        If the property FillStyle is set to FillStyle.BITMAP, this is a URL to the bitmap used.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When a URL is set, then it will load the bitmap and set the FillBitmap property.
        """

    @abstractproperty
    def FillColor(self) -> 'Color_68e908c5':
        """
        If the property FillStyle is set to FillStyle.SOLID, this is the color used.
        """

    @abstractproperty
    def FillGradient(self) -> 'Gradient_7a8a0982':
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this describes the gradient used.
        """

    @abstractproperty
    def FillGradientName(self) -> str:
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this is the name of the used fill gradient style.
        """

    @abstractproperty
    def FillHatch(self) -> 'Hatch_859b09dc':
        """
        If the property FillStyle is set to FillStyle.HATCH, this describes the hatch used.
        """

    @abstractproperty
    def FillHatchName(self) -> str:
        """
        If the property FillStyle is set to FillStyle.HATCH, this is the name of the used fill hatch style.
        """

    @abstractproperty
    def FillStyle(self) -> 'FillStyle_b1460b8c':
        """
        This enumeration selects the style the area will be filled with.
        """

    @abstractproperty
    def FillTransparence(self) -> int:
        """
        This is the transparence of the filled area.
        
        This property is only valid if the property FillStyle is set to FillStyle.SOLID.
        """

    @abstractproperty
    def FillTransparenceGradient(self) -> 'Gradient_7a8a0982':
        """
        This describes the transparency of the fill area as a gradient.
        """

    @abstractproperty
    def FillTransparenceGradientName(self) -> str:
        """
        If a gradient is used for transparency, this is the name of the used transparence gradient style or it is empty.
        
        If you set the name of a transparence gradient style contained in the document, this style used.
        """

    @abstractproperty
    def GraphicCrop(self) -> 'GraphicCrop_a58e0b1f':
        """
        contains the cropping of the object.
        
        If the property FillBitmapMode is set to BitmapMode.STRETCH, this is the cropping, otherwise it is empty.
        
        **since**
        
            LibreOffice 4.3
        """



__all__ = ['FillProperties']
