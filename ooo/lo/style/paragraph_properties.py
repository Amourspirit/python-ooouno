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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.style
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from .drop_cap_format import DropCapFormat as DropCapFormat_c95f0c4b
    from .line_spacing import LineSpacing as LineSpacing_b1ad0b86
    from .tab_stop import TabStop as TabStop_860309f6
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.BreakType import BreakTypeProto  # type: ignore
    from com.sun.star.style.ParagraphAdjust import ParagraphAdjustProto  # type: ignore
    from com.sun.star.style.GraphicLocation import GraphicLocationProto  # type: ignore

class ParagraphProperties(ABC):
    """
    Service Class

    describes the style of paragraphs.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API ParagraphProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1ParagraphProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.ParagraphProperties'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BorderDistance(self) -> int:
        """
        contains the distance from the border to the object.
        """
        ...

    @property
    @abstractmethod
    def BottomBorder(self) -> BorderLine_a3f80af6:
        """
        contains the bottom border of the object.
        """
        ...

    @property
    @abstractmethod
    def BottomBorderDistance(self) -> int:
        """
        contains the distance from the bottom border to the object.
        """
        ...

    @property
    @abstractmethod
    def BreakType(self) -> BreakTypeProto:
        """
        determines the type of break that is applied at the beginning of the table.
        """
        ...

    @property
    @abstractmethod
    def ContinueingPreviousSubTree(self) -> bool:
        """
        specifies that a child node of a parent node that is not counted is continuing the numbering of parent's previous node's sub tree.
        
        **since**
        
            OOo 3.0.1
        """
        ...

    @property
    @abstractmethod
    def DropCapCharStyleName(self) -> str:
        """
        specifies the character style name for drop caps.
        """
        ...

    @property
    @abstractmethod
    def DropCapFormat(self) -> DropCapFormat_c95f0c4b:
        """
        specifies whether the first characters of the paragraph are displayed in capital letters and how they are formatted.
        """
        ...

    @property
    @abstractmethod
    def DropCapWholeWord(self) -> bool:
        """
        specifies if the property DropCapFormat is applied to the whole first word.
        """
        ...

    @property
    @abstractmethod
    def LeftBorder(self) -> BorderLine_a3f80af6:
        """
        contains the left border of the object.
        """
        ...

    @property
    @abstractmethod
    def LeftBorderDistance(self) -> int:
        """
        contains the distance from the left border to the object.
        """
        ...

    @property
    @abstractmethod
    def ListId(self) -> str:
        """
        specifies the id of the list to which the paragraph belongs
        """
        ...

    @property
    @abstractmethod
    def ListLabelString(self) -> str:
        """
        allows reading the generated numbering list label.
        
        **since**
        
            OOo 3.0.1
        """
        ...

    @property
    @abstractmethod
    def NumberingIsNumber(self) -> bool:
        """
        returns FALSE if the paragraph is part of a numbering, but has no numbering label.
        
        A paragraph is part of a numbering, if a style for a numbering is set - see NumberingStyleName.
        
        If the paragraph is not part of a numbering the property is void.
        """
        ...

    @property
    @abstractmethod
    def NumberingLevel(self) -> int:
        """
        specifies the numbering level of the paragraph.
        """
        ...

    @property
    @abstractmethod
    def NumberingRules(self) -> XIndexReplace_feed0dd7:
        """
        contains the numbering rules applied to this paragraph.
        """
        ...

    @property
    @abstractmethod
    def NumberingStartValue(self) -> int:
        """
        specifies the start value for numbering if a new numbering starts at this paragraph.
        """
        ...

    @property
    @abstractmethod
    def NumberingStyleName(self) -> str:
        """
        specifies the name of the style for the numbering.
        
        The name must be one of the names which are available via XStyleFamiliesSupplier.
        """
        ...

    @property
    @abstractmethod
    def OutlineLevel(self) -> int:
        """
        specifies the outline level to which the paragraph belongs
        
        Value 0 indicates that the paragraph belongs to the body text.
        
        Values [1..10] indicates that the paragraph belongs to the corresponding outline level.
        
        **since**
        
            OOo 3.1
        """
        ...

    @property
    @abstractmethod
    def PageDescName(self) -> str:
        """
        If this property is set, it creates a page break before the paragraph it belongs to and assigns the value as the name of the new page style sheet to use.
        """
        ...

    @property
    @abstractmethod
    def PageNumberOffset(self) -> int:
        """
        If a page break property is set at a paragraph, this property contains the new value for the page number.
        """
        ...

    @property
    @abstractmethod
    def PageStyleName(self) -> str:
        """
        contains the name of the current page style.
        """
        ...

    @property
    @abstractmethod
    def ParaAdjust(self) -> ParagraphAdjustProto:
        """
        determines the adjustment of a paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaBackColor(self) -> Color_68e908c5:
        """
        contains the paragraph background color.
        """
        ...

    @property
    @abstractmethod
    def ParaBackGraphic(self) -> XGraphic_a4da0afc:
        """
        contains the graphic for the background of a paragraph.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @property
    @abstractmethod
    def ParaBackGraphicFilter(self) -> str:
        """
        contains the name of the graphic filter for the background graphic of a paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaBackGraphicLocation(self) -> GraphicLocationProto:
        """
        contains the value for the position of a background graphic.
        """
        ...

    @property
    @abstractmethod
    def ParaBackGraphicURL(self) -> str:
        """
        contains the value of a link for the background graphic of a paragraph.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the ParaBackGraphic property.
        """
        ...

    @property
    @abstractmethod
    def ParaBackTransparent(self) -> bool:
        """
        This value is TRUE if the paragraph background color is set to transparent.
        """
        ...

    @property
    @abstractmethod
    def ParaBottomMargin(self) -> int:
        """
        determines the bottom margin of the paragraph in 100th mm.
        
        The distance between two paragraphs is specified by:
        
        The greater one is chosen.
        """
        ...

    @property
    @abstractmethod
    def ParaContextMargin(self) -> bool:
        """
        determines if contextual spacing is used.
        
        If true, the top and bottom margins of the paragraph should not be applied when the previous and next paragraphs have the same style.
        
        **since**
        
            LibreOffice 3.6
        """
        ...

    @property
    @abstractmethod
    def ParaExpandSingleWord(self) -> bool:
        """
        determines if single words are stretched.
        
        It is only valid if ParagraphProperties.ParaAdjust and ParagraphProperties.ParaLastLineAdjust are also valid.
        """
        ...

    @property
    @abstractmethod
    def ParaFirstLineIndent(self) -> int:
        """
        specifies the indent for the first line.
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationMaxHyphens(self) -> int:
        """
        specifies the maximum number of consecutive hyphens.
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationMaxLeadingChars(self) -> int:
        """
        specifies the minimum number of characters to remain before the hyphen character (when hyphenation is applied).
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationMaxTrailingChars(self) -> int:
        """
        specifies the minimum number of characters to remain after the hyphen character (when hyphenation is applied).
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationMinWordLength(self) -> int:
        """
        specifies the minimum word length in characters, when hyphenation is applied.
        
        **since**
        
            LibreOffice 7.4
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationNoCaps(self) -> bool:
        """
        Specifies whether words written in CAPS will be hyphenated.
        
        Setting to true will disable hyphenation of words written in CAPS for this paragraph.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationNoLastWord(self) -> bool:
        """
        Specifies whether last word of paragraph will be hyphenated.
        
        Setting to true will disable hyphenation of last word for this paragraph.
        
        **since**
        
            LibreOffice 7.4
        """
        ...

    @property
    @abstractmethod
    def ParaHyphenationZone(self) -> int:
        """
        specifies the hyphenation zone, i.e.
        
        allowed extra white space in the line before applying hyphenation.
        
        **since**
        
            LibreOffice 7.4
        """
        ...

    @property
    @abstractmethod
    def ParaInteropGrabBag(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Grab bag of paragraph properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def ParaIsAutoFirstLineIndent(self) -> bool:
        """
        determines if the first line should be indented automatically.
        """
        ...

    @property
    @abstractmethod
    def ParaIsConnectBorder(self) -> bool:
        """
        the property determines if borders set at a paragraph are merged with the next paragraph.
        
        Borders are only merged if they are identical.
        """
        ...

    @property
    @abstractmethod
    def ParaIsHyphenation(self) -> bool:
        """
        specifies if automatic hyphenation is applied.
        """
        ...

    @property
    @abstractmethod
    def ParaIsNumberingRestart(self) -> bool:
        """
        determines if the numbering rules restart, counting at the current paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaKeepTogether(self) -> bool:
        """
        Setting this property to TRUE prevents page or column breaks between this and the following paragraph.
        
        This feature is useful for preventing title paragraphs to be the last line on a page or column.
        """
        ...

    @property
    @abstractmethod
    def ParaLastLineAdjust(self) -> int:
        """
        determines the adjustment of the last line.
        
        It is only valid if ParagraphProperties.ParaAdjust is set to ParagraphAdjust.BLOCK.
        """
        ...

    @property
    @abstractmethod
    def ParaLeftMargin(self) -> int:
        """
        determines the left margin of the paragraph in 100th mm.
        """
        ...

    @property
    @abstractmethod
    def ParaLineNumberCount(self) -> bool:
        """
        determines if the paragraph is included in the line numbering.
        """
        ...

    @property
    @abstractmethod
    def ParaLineNumberStartValue(self) -> int:
        """
        contains the start value for the line numbering.
        """
        ...

    @property
    @abstractmethod
    def ParaLineSpacing(self) -> LineSpacing_b1ad0b86:
        """
        contains the type of the line spacing of a paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaOrphans(self) -> int:
        """
        specifies the minimum number of lines of the paragraph that have to be at bottom of a page if the paragraph is spread over more than one page.
        """
        ...

    @property
    @abstractmethod
    def ParaRegisterModeActive(self) -> bool:
        """
        determines if the register mode is applied to a paragraph.
        
        Remark: Register mode is only used if the register mode property of the page style is switched on.
        """
        ...

    @property
    @abstractmethod
    def ParaRightMargin(self) -> int:
        """
        determines the right margin of the paragraph in 100th mm.
        """
        ...

    @property
    @abstractmethod
    def ParaShadowFormat(self) -> ShadowFormat_bb840bdf:
        """
        determines the type, color, and size of the shadow.
        """
        ...

    @property
    @abstractmethod
    def ParaSplit(self) -> bool:
        """
        Setting this property to FALSE prevents the paragraph from getting split into two pages or columns.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleName(self) -> str:
        """
        contains the name of the current paragraph style.
        """
        ...

    @property
    @abstractmethod
    def ParaTabStops(self) -> typing.Tuple[TabStop_860309f6, ...]:
        """
        specifies the positions and kinds of the tab stops within this paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaTopMargin(self) -> int:
        """
        determines the top margin of the paragraph in 100th mm.
        
        The distance between two paragraphs is specified by:
        
        The greater one is chosen.
        """
        ...

    @property
    @abstractmethod
    def ParaUserDefinedAttributes(self) -> XNameContainer_cb90e47:
        """
        this property stores xml attributes.
        
        They will be saved to and restored from automatic styles inside xml files.
        """
        ...

    @property
    @abstractmethod
    def ParaVertAlignment(self) -> int:
        """
        specifies the vertical alignment of a paragraph.
        """
        ...

    @property
    @abstractmethod
    def ParaWidows(self) -> int:
        """
        specifies the minimum number of lines of the paragraph that have to be at top of a page if the paragraph is spread over more than one page.
        """
        ...

    @property
    @abstractmethod
    def RightBorder(self) -> BorderLine_a3f80af6:
        """
        contains the right border of the object.
        """
        ...

    @property
    @abstractmethod
    def RightBorderDistance(self) -> int:
        """
        contains the distance from the right border to the object.
        """
        ...

    @property
    @abstractmethod
    def SortedTextId(self) -> int:
        """
        contains a paragraph identifier within the actual text, which also shows the position of the paragraph relative to the other paragraphs of the same text, i.e.
        
        a paragraph with lower identifier is there before the other ones with greater values. This property depends on implementation details and is considered experimental.
        
        **since**
        
            LibreOffice 7.6
        """
        ...

    @property
    @abstractmethod
    def TopBorder(self) -> BorderLine_a3f80af6:
        """
        contains the top border of the object.
        """
        ...

    @property
    @abstractmethod
    def TopBorderDistance(self) -> int:
        """
        contains the distance from the top border to the object.
        """
        ...


__all__ = ['ParagraphProperties']