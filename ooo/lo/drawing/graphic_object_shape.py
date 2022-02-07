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
from abc import abstractproperty
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
    from .color_mode import ColorMode as ColorMode_b13e0b78
    from .qr_code import QRCode as QRCode_8f1f0a12
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc

class GraphicObjectShape(RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for a graphic shape.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API GraphicObjectShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1GraphicObjectShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.GraphicObjectShape'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AdjustBlue(self) -> int:
        """
        If this property is set, the blue channel of this graphic shape is adjusted by the given signed percent value.
        """
    @abstractproperty
    def AdjustContrast(self) -> int:
        """
        If this property is set, the contrast of this graphic shape is adjusted by the given signed percent value.
        """
    @abstractproperty
    def AdjustGreen(self) -> int:
        """
        If this property is set, the green channel of this graphic shape is adjusted by the given signed percent value.
        """
    @abstractproperty
    def AdjustLuminance(self) -> int:
        """
        If this property is set, the luminance of this graphic shape is adjusted by the given signed percent value.
        """
    @abstractproperty
    def AdjustRed(self) -> int:
        """
        If this property is set, the red channel of this graphic shape is adjusted by the given signed percent value.
        """
    @abstractproperty
    def Gamma(self) -> float:
        """
        If this property is set, the gamma value of this graphic shape is adjusted by the given value.
        """
    @abstractproperty
    def Graphic(self) -> 'XGraphic_a4da0afc':
        """
        This is the graphic that represents this graphic shape.
        """
    @abstractproperty
    def GraphicColorMode(self) -> 'ColorMode_b13e0b78':
        """
        This property selects the color mode that is used for rendering.
        """
    @abstractproperty
    def GraphicObjectFillBitmap(self) -> 'XBitmap_70cd0909':
        """
        This is the bitmap that represents this graphic shape.
        """
    @abstractproperty
    def GraphicStreamURL(self) -> str:
        """
        This is a url to the stream (\"in document\" or linked graphic) for this graphic shape.
        """
    @abstractproperty
    def GraphicURL(self) -> str:
        """
        This is a url to the source bitmap for this graphic shape.
        
        Note the new behaviour since it was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When a URL is set, then it will load the image and set the Graphic property.
        """
    @abstractproperty
    def ImageMap(self) -> 'XIndexContainer_1c040ebe':
        """
        This property contains an image map for this graphic.
        """
    @abstractproperty
    def IsSignatureLine(self) -> bool:
        """
        Whether this shape is actually a signature line.
        """
    @abstractproperty
    def QRCodeProperties(self) -> 'QRCode_8f1f0a12':
        """
        Shape as a QR Code.
        
        **since**
        
            LibreOffice 6.4
        """
    @abstractproperty
    def SignatureLineCanAddComment(self) -> bool:
        """
        Whether the user can attach a comment at signing time.
        """
    @abstractproperty
    def SignatureLineId(self) -> str:
        """
        The ID of the signature line, used to connect to a signature.
        """
    @abstractproperty
    def SignatureLineIsSigned(self) -> bool:
        """
        Whether the signature line is signed using a digital signature.
        """
    @abstractproperty
    def SignatureLineShowSignDate(self) -> bool:
        """
        Whether the signing date should be shown in the shape.
        """
    @abstractproperty
    def SignatureLineSigningInstructions(self) -> str:
        """
        Signing instructions, to be shown at signing time.
        """
    @abstractproperty
    def SignatureLineSuggestedSignerEmail(self) -> str:
        """
        Suggested Signer Email.
        """
    @abstractproperty
    def SignatureLineSuggestedSignerName(self) -> str:
        """
        Suggested Signer, Name of the Signer.
        """
    @abstractproperty
    def SignatureLineSuggestedSignerTitle(self) -> str:
        """
        Suggested Signer, Line 2 (Title or additional information)
        """
    @abstractproperty
    def SignatureLineUnsignedImage(self) -> 'XGraphic_a4da0afc':
        """
        Image to be displayed when the signature line is unsigned.
        
        Images for signed signature lines (valid and invalid) are to be retrieved via com.sun.star.security.DocumentSignatureInformation (you can get the matching signature with the SignatureLineId property).
        """
    @abstractproperty
    def Transparency(self) -> int:
        """
        If this property is set, the transparency value of this graphic shape is adjusted by the given unsigned percent value.
        
        100% is fully transparent, 0% is fully opaque.
        """

__all__ = ['GraphicObjectShape']

