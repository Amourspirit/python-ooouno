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
# Namespace: com.sun.star.style
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from .graphic_location import GraphicLocation as GraphicLocation_e3ef0d30
    from .page_style_layout import PageStyleLayout as PageStyleLayout_e4070d45
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..text.x_text import XText as XText_690408ca
    from ..text.x_text_columns import XTextColumns as XTextColumns_b17f0bab
    from ..util.color import Color as Color_68e908c5

class PageProperties(ABC):
    """
    Service Class

    describes the style of pages.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API PageProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1PageProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.PageProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BackColor(self) -> 'Color_68e908c5':
        """
        contains the background color of the page.
        """
    @abstractproperty
    def BackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background.
        
        **since**
        
            LibreOffice 6.1
        """
    @abstractproperty
    def BackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic.
        """
    @abstractproperty
    def BackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic.
        """
    @abstractproperty
    def BackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
    @abstractproperty
    def BackTransparent(self) -> bool:
        """
        determines if the background color is transparent.
        
        If this property is set to TRUE, PageStyle.BackColor will not be used.
        """
    @abstractproperty
    def BackgroundFullSize(self) -> bool:
        """
        does the background cover the full page or only inside the margins?
        
        **since**
        
            LibreOffice 7.2
        """
    @abstractproperty
    def BorderDistance(self) -> int:
        """
        determines the distance of all borders of the page.
        """
    @abstractproperty
    def BottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the bottom border line of the page.
        """
    @abstractproperty
    def BottomBorderDistance(self) -> int:
        """
        determines the bottom border distance of the page.
        """
    @abstractproperty
    def BottomMargin(self) -> int:
        """
        determines the bottom margin of the page.
        """
    @abstractproperty
    def FirstIsShared(self) -> bool:
        """
        determines if the header/footer content on the first page and remaining pages is the same.
        
        **since**
        
            LibreOffice 4.0
        """
    @abstractproperty
    def FooterBackColor(self) -> 'Color_68e908c5':
        """
        contains the color of the background of the footer.
        """
    @abstractproperty
    def FooterBackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background of the footer.
        
        **since**
        
            LibreOffice 6.1
        """
    @abstractproperty
    def FooterBackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic in the footer.
        """
    @abstractproperty
    def FooterBackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic in the footer.
        """
    @abstractproperty
    def FooterBackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic in the footer.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the FooterBackGraphic property.
        """
    @abstractproperty
    def FooterBackTransparent(self) -> bool:
        """
        determines if the background of the footer is transparent.
        """
    @abstractproperty
    def FooterBodyDistance(self) -> int:
        """
        determines the distance between the footer and the body text area.
        """
    @abstractproperty
    def FooterBorderDistance(self) -> int:
        """
        contains the distance of all borders of the footer.
        """
    @abstractproperty
    def FooterBottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the bottom border line of the footer.
        """
    @abstractproperty
    def FooterBottomBorderDistance(self) -> int:
        """
        contains the bottom border distance of the footer.
        """
    @abstractproperty
    def FooterDynamicSpacing(self) -> bool:
        """
        determines whether to use dynamic spacing in footer or not.
        """
    @abstractproperty
    def FooterHeight(self) -> int:
        """
        determines the height of the footer.
        """
    @abstractproperty
    def FooterIsDynamicHeight(self) -> bool:
        """
        determines if the height of the footer depends on the content.
        """
    @abstractproperty
    def FooterIsOn(self) -> bool:
        """
        determines if a footer is used on the page.
        """
    @abstractproperty
    def FooterIsShared(self) -> bool:
        """
        determines if the footer content on left and right pages is the same.
        """
    @abstractproperty
    def FooterLeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the left border line of the footer.
        """
    @abstractproperty
    def FooterLeftBorderDistance(self) -> int:
        """
        contains the left border distance of the footer.
        """
    @abstractproperty
    def FooterLeftMargin(self) -> int:
        """
        determines the left margin of the footer.
        """
    @abstractproperty
    def FooterRightBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the right border line of the footer.
        """
    @abstractproperty
    def FooterRightBorderDistance(self) -> int:
        """
        contains the right border distance of the footer.
        """
    @abstractproperty
    def FooterRightMargin(self) -> int:
        """
        determines the right margin of the footer.
        """
    @abstractproperty
    def FooterShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the footer.
        """
    @abstractproperty
    def FooterText(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer.
        """
    @abstractproperty
    def FooterTextLeft(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer of a left page.
        """
    @abstractproperty
    def FooterTextRight(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer of a right page.
        """
    @abstractproperty
    def FooterTopBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the top border line of the footer.
        """
    @abstractproperty
    def FooterTopBorderDistance(self) -> int:
        """
        contains the top border distance of the footer.
        """
    @abstractproperty
    def FootnoteHeight(self) -> int:
        """
        contains the maximum height of the footnote area.
        
        If set to zero then the height of the current page is used as limit.
        """
    @abstractproperty
    def FootnoteLineAdjust(self) -> int:
        """
        contains the adjustment of the separator line between the text and the footnote area.
        
        com.sun.star.text.HorizontalAdjusts.
        """
    @abstractproperty
    def FootnoteLineColor(self) -> 'Color_68e908c5':
        """
        contains the color of the separator line between the text and the footnote area.
        """
    @abstractproperty
    def FootnoteLineDistance(self) -> int:
        """
        contains the distance between the footnote area and the separator line between the text and the footnote area.
        """
    @abstractproperty
    def FootnoteLineRelativeWidth(self) -> int:
        """
        contains the relative width of the separator line between the text and the footnote area.
        """
    @abstractproperty
    def FootnoteLineStyle(self) -> int:
        """
        contains the style of the separator line between the text and the footnote area.
        """
    @abstractproperty
    def FootnoteLineTextDistance(self) -> int:
        """
        contains the distance between the text and the separator line between the text and the footnote area.
        """
    @abstractproperty
    def FootnoteLineWeight(self) -> int:
        """
        contains the weight of the separator line between the text and the footnote area.
        """
    @abstractproperty
    def GridBaseHeight(self) -> int:
        """
        contains the height of the base text line inside the text grid
        """
    @abstractproperty
    def GridColor(self) -> 'Color_68e908c5':
        """
        contains the display color of the text grid
        """
    @abstractproperty
    def GridDisplay(self) -> bool:
        """
        determines whether the text grid lines are visible or not
        """
    @abstractproperty
    def GridLines(self) -> int:
        """
        contains the number of lines in the text grid
        """
    @abstractproperty
    def GridMode(self) -> int:
        """
        contains the mode of the text grid (none, lines, ...), as represented by com.sun.star.text.TextGridMode constants
        """
    @abstractproperty
    def GridPrint(self) -> bool:
        """
        determines whether the text grid lines are printed
        """
    @abstractproperty
    def GridRubyBelow(self) -> bool:
        """
        determines whether the text grid's ruby line is located below or above the base line
        """
    @abstractproperty
    def GridRubyHeight(self) -> int:
        """
        contains the height of the ruby text line inside the text grid
        """
    @abstractproperty
    def GutterMargin(self) -> int:
        """
        determines the gutter margin of the page.
        
        **since**
        
            LibreOffice 7.2
        """
    @abstractproperty
    def HeaderBackColor(self) -> 'Color_68e908c5':
        """
        contains the color of the background of the header.
        """
    @abstractproperty
    def HeaderBackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background of the header.
        
        **since**
        
            LibreOffice 6.1
        """
    @abstractproperty
    def HeaderBackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic of the header.
        """
    @abstractproperty
    def HeaderBackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic of the header.
        """
    @abstractproperty
    def HeaderBackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic of the header.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the HeaderBackGraphic property.
        """
    @abstractproperty
    def HeaderBackTransparent(self) -> bool:
        """
        determines if the background color of the header is transparent.
        
        If this property is set to TRUE, PageStyle.HeaderBackColor will not be used.
        """
    @abstractproperty
    def HeaderBodyDistance(self) -> int:
        """
        determines the distance between the header and the body text area.
        """
    @abstractproperty
    def HeaderBorderDistance(self) -> int:
        """
        determines the distance of all borders of the header.
        """
    @abstractproperty
    def HeaderBottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the bottom border line of the header.
        """
    @abstractproperty
    def HeaderBottomBorderDistance(self) -> int:
        """
        determines the bottom border distance of the header.
        """
    @abstractproperty
    def HeaderDynamicSpacing(self) -> bool:
        """
        determines whether to use dynamic spacing in header or not.
        """
    @abstractproperty
    def HeaderHeight(self) -> int:
        """
        contains the height of the header.
        """
    @abstractproperty
    def HeaderIsDynamicHeight(self) -> bool:
        """
        determines if the height of the header depends on the content.
        """
    @abstractproperty
    def HeaderIsOn(self) -> bool:
        """
        determines if a header is used on the page.
        """
    @abstractproperty
    def HeaderIsShared(self) -> bool:
        """
        determines if the header content on left and right pages is the same.
        """
    @abstractproperty
    def HeaderLeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the left border line of the header.
        """
    @abstractproperty
    def HeaderLeftBorderDistance(self) -> int:
        """
        determines the left border distance of the header.
        """
    @abstractproperty
    def HeaderLeftMargin(self) -> int:
        """
        contains the left margin of the header.
        """
    @abstractproperty
    def HeaderRightBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the right border line of the header.
        """
    @abstractproperty
    def HeaderRightBorderDistance(self) -> int:
        """
        determines the right border distance of the header.
        """
    @abstractproperty
    def HeaderRightMargin(self) -> int:
        """
        contains the right margin of the header.
        """
    @abstractproperty
    def HeaderShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the header.
        """
    @abstractproperty
    def HeaderText(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header.
        """
    @abstractproperty
    def HeaderTextLeft(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header of left pages.
        """
    @abstractproperty
    def HeaderTextRight(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header of right pages.
        """
    @abstractproperty
    def HeaderTopBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the top border line of the header.
        """
    @abstractproperty
    def HeaderTopBorderDistance(self) -> int:
        """
        determines the top border distance of the header.
        """
    @abstractproperty
    def Height(self) -> int:
        """
        contains the height of the page.
        """
    @abstractproperty
    def IsLandscape(self) -> bool:
        """
        determines if the page format is landscape.
        """
    @abstractproperty
    def LeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the left border line of the page.
        """
    @abstractproperty
    def LeftBorderDistance(self) -> int:
        """
        determines the left border distance of the page.
        """
    @abstractproperty
    def LeftMargin(self) -> int:
        """
        determines the left margin of the page.
        """
    @abstractproperty
    def NumberingType(self) -> int:
        """
        determines the default numbering type for this page.
        """
    @abstractproperty
    def PageStyleLayout(self) -> 'PageStyleLayout_e4070d45':
        """
        determines the layout of the page.
        """
    @abstractproperty
    def PrinterPaperTray(self) -> str:
        """
        contains the name of a paper tray of the selected printer.
        """
    @abstractproperty
    def RegisterModeActive(self) -> bool:
        """
        determines if the register mode is active on that page.
        """
    @abstractproperty
    def RegisterParagraphStyle(self) -> str:
        """
        contains the name of the paragraph style that is used as reference of the register mode.
        """
    @abstractproperty
    def RightBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the right border line of the page.
        """
    @abstractproperty
    def RightBorderDistance(self) -> int:
        """
        determines the right border distance of the page.
        """
    @abstractproperty
    def RightMargin(self) -> int:
        """
        determines the right margin of the page.
        """
    @abstractproperty
    def RtlGutter(self) -> bool:
        """
        specifies that the page gutter shall be placed on the right side of the page.
        
        **since**
        
            LibreOffice 7.2
        """
    @abstractproperty
    def ShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the page.
        """
    @abstractproperty
    def Size(self) -> 'Size_576707ef':
        """
        contains the paper size of the page.
        """
    @abstractproperty
    def TextColumns(self) -> 'XTextColumns_b17f0bab':
        """
        contains the column settings of the page.
        """
    @abstractproperty
    def TopBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the top border line of the page.
        """
    @abstractproperty
    def TopBorderDistance(self) -> int:
        """
        determines the top border distance of the page.
        """
    @abstractproperty
    def TopMargin(self) -> int:
        """
        determines the top margin of the page.
        """
    @abstractproperty
    def UserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        contains user defined attributes.
        
        This com.sun.star.container.XNameContainer supports the service com.sun.star.xml.AttributeContainer.
        """
    @abstractproperty
    def Width(self) -> int:
        """
        contains the width of the page.
        """
    @abstractproperty
    def WritingMode(self) -> int:
        """
        contains the writing direction, as represented by the com.sun.star.text.WritingMode2 constants
        """

__all__ = ['PageProperties']

