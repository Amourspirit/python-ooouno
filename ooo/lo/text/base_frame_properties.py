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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..awt.gradient import Gradient as Gradient_7a8a0982
    from ..awt.size import Size as Size_576707ef
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..drawing.fill_style import FillStyle as FillStyle_b1460b8c
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..style.graphic_location import GraphicLocation as GraphicLocation_e3ef0d30
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from .wrap_text_mode import WrapTextMode as WrapTextMode_b1dd0b91
    from .x_text_frame import XTextFrame as XTextFrame_9a7e0ab5
    from ..util.color import Color as Color_68e908c5

class BaseFrameProperties(UserDefinedAttributesSupplier_9fbe1222):
    """
    Service Class

    specifies the properties that are provided by all text frames, graphic objects, embedded objects and frame styles.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API BaseFrameProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1BaseFrameProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.BaseFrameProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def FrameInteropGrabBag(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Grab bag of frame properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @abstractproperty
    def AllowOverlap(self) -> bool:
        """
        This defines if the frame is allowed to overlap with other anchored objects.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @abstractproperty
    def AnchorFrame(self) -> 'XTextFrame_9a7e0ab5':
        """
        contains the text frame the current frame is anchored to.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_FRAME.
        """
        ...

    @abstractproperty
    def AnchorPageNo(self) -> int:
        """
        contains the number of the page where the objects are anchored.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_PAGE.
        """
        ...

    @abstractproperty
    def BackColor(self) -> 'Color_68e908c5':
        """
        contains the color of the background of the object.
        """
        ...

    @abstractproperty
    def BackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic for the background.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @abstractproperty
    def BackGraphicFilter(self) -> str:
        """
        contains the name of the file filter for the background graphic.
        """
        ...

    @abstractproperty
    def BackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the position of the background graphic.
        """
        ...

    @abstractproperty
    def BackGraphicURL(self) -> str:
        """
        contains the URL for the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...

    @abstractproperty
    def BackTransparent(self) -> bool:
        """
        If TRUE, the \"BackColor\" is ignored.
        """
        ...

    @abstractproperty
    def BorderDistance(self) -> int:
        """
        contains the distance from the border to the object.
        """
        ...

    @abstractproperty
    def BottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the bottom border of the object.
        """
        ...

    @abstractproperty
    def BottomBorderDistance(self) -> int:
        """
        contains the distance from the bottom border to the object.
        """
        ...

    @abstractproperty
    def BottomMargin(self) -> int:
        """
        contains the bottom margin of the object.
        """
        ...

    @abstractproperty
    def ContentProtected(self) -> bool:
        """
        determines if the content is protected.
        """
        ...

    @abstractproperty
    def Description(self) -> str:
        """
        contains description for the object
        
        The long description text can be entered to describe an object in more detail to users with screen reader software. The description is visible as an alternative tag for accessibility tools.
        
        **since**
        
            OOo 3.2
        """
        ...

    @abstractproperty
    def FillGradient(self) -> 'Gradient_7a8a0982':
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this describes the gradient used.
        
        **since**
        
            LibreOffice 4.1
        """
        ...

    @abstractproperty
    def FillGradientName(self) -> str:
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this is the name of the gradient used.
        
        **since**
        
            LibreOffice 4.1
        """
        ...

    @abstractproperty
    def FillStyle(self) -> 'FillStyle_b1460b8c':
        """
        This enumeration selects the style the area will be filled with.
        
        Currently only set for gradients.
        
        **since**
        
            LibreOffice 4.1
        """
        ...

    @abstractproperty
    def Height(self) -> int:
        """
        contains the height of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.RelativeHeight is zero.
        """
        ...

    @abstractproperty
    def HoriOrient(self) -> int:
        """
        determines the horizontal orientation of the object.
        """
        ...

    @abstractproperty
    def HoriOrientPosition(self) -> int:
        """
        contains the horizontal position of the object (1/100 mm).
        
        It is only valid if \"HoriOrient\" is HoriOrientation_NONE.
        """
        ...

    @abstractproperty
    def HoriOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...

    @abstractproperty
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink that is set at the object.
        """
        ...

    @abstractproperty
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink that is set at the object.
        """
        ...

    @abstractproperty
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink that is set at the object.
        """
        ...

    @abstractproperty
    def IsSyncHeightToWidth(self) -> bool:
        """
        determines whether the height follows the width.
        """
        ...

    @abstractproperty
    def IsSyncWidthToHeight(self) -> bool:
        """
        determines whether the width follows the height.
        """
        ...

    @abstractproperty
    def LayoutSize(self) -> 'Size_576707ef':
        """
        returns the actual size of the object.
        
        Since to obtain the correct actual size of the object not only the layouting for the frame needs to be finished but the whole document needs to be formatted as well. Thus if that was not done previously it may take some while to retrieve this value.
        
        **since**
        
            OOo 2.0.4
        """
        ...

    @abstractproperty
    def LeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the left border of the object.
        """
        ...

    @abstractproperty
    def LeftBorderDistance(self) -> int:
        """
        contains the distance from the left border to the object.
        """
        ...

    @abstractproperty
    def LeftMargin(self) -> int:
        """
        contains the left margin of the object.
        """
        ...

    @abstractproperty
    def Opaque(self) -> bool:
        """
        determines if the object is opaque or transparent for text.
        """
        ...

    @abstractproperty
    def PageToggle(self) -> bool:
        """
        determines if the object is mirrored on even pages.
        """
        ...

    @abstractproperty
    def PositionProtected(self) -> bool:
        """
        determines if the position is protected.
        """
        ...

    @abstractproperty
    def Print(self) -> bool:
        """
        determines if the object is included in printing.
        """
        ...

    @abstractproperty
    def RelativeHeight(self) -> int:
        """
        contains the relative height of the object.
        
        It is only valid if it is greater than zero.
        """
        ...

    @abstractproperty
    def RelativeHeightRelation(self) -> int:
        """
        contains the relation of the relative height of the object.
        
        It is only valid if RelativeHeight is greater than zero.
        
        **since**
        
            LibreOffice 4.3
        """
        ...

    @abstractproperty
    def RelativeWidth(self) -> int:
        """
        contains the relative width of the object.
        
        It is only valid if it is greater than zero.
        """
        ...

    @abstractproperty
    def RelativeWidthRelation(self) -> int:
        """
        contains the relation of the relative width of the object.
        
        It is only valid if RelativeWidth is greater than zero.
        
        **since**
        
            LibreOffice 4.3
        """
        ...

    @abstractproperty
    def RightBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the right border of the object.
        """
        ...

    @abstractproperty
    def RightBorderDistance(self) -> int:
        """
        contains the distance from the right border to the object.
        """
        ...

    @abstractproperty
    def RightMargin(self) -> int:
        """
        contains the right margin of the object.
        """
        ...

    @abstractproperty
    def ServerMap(self) -> bool:
        """
        determines if the object gets an image map from a server.
        """
        ...

    @abstractproperty
    def ShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        contains the type of the shadow of the object.
        """
        ...

    @abstractproperty
    def ShadowTransparence(self) -> int:
        """
        This defines the degree of transparence of the shadow in percent.
        
        This is the same as setting the Color member of the ShadowFormat property to an ARGB color.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @abstractproperty
    def Size(self) -> 'Size_576707ef':
        """
        contains the size of the object.
        """
        ...

    @abstractproperty
    def SizeProtected(self) -> bool:
        """
        determines if the size is protected.
        """
        ...

    @abstractproperty
    def Surround(self) -> 'WrapTextMode_b1dd0b91':
        """
        determines the type of the surrounding text.
        """
        ...

    @abstractproperty
    def SurroundAnchorOnly(self) -> bool:
        """
        determines if the text of the paragraph in which the object is anchored, wraps around the object.
        """
        ...

    @abstractproperty
    def Title(self) -> str:
        """
        contains short title for the object
        
        This short title is visible as an alternative tag in HTML format. Accessibility tools can read this text.
        
        **since**
        
            OOo 3.2
        """
        ...

    @abstractproperty
    def TopBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the top border of the object.
        """
        ...

    @abstractproperty
    def TopBorderDistance(self) -> int:
        """
        contains the distance from the top border to the object.
        """
        ...

    @abstractproperty
    def TopMargin(self) -> int:
        """
        contains the top margin of the object.
        """
        ...

    @abstractproperty
    def VertOrient(self) -> int:
        """
        determines the vertical orientation of the object.
        """
        ...

    @abstractproperty
    def VertOrientPosition(self) -> int:
        """
        contains the vertical position of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.VertOrient is VertOrientation.NONE.
        """
        ...

    @abstractproperty
    def VertOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...

    @abstractproperty
    def Width(self) -> int:
        """
        contains the width of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.RelativeWidth is zero.
        """
        ...

    @abstractproperty
    def WrapInfluenceOnPosition(self) -> int:
        """
        determines the influence of the text wrap on the positioning of the shape
        
        The value of this property is only evaluated for the positioning of the shape, if the text document setting ConsiderTextWrapOnObjPos is TRUE. Valid values are given by WrapInfluenceOnPosition
        
        **since**
        
            OOo 2.0
        """
        ...



__all__ = ['BaseFrameProperties']

