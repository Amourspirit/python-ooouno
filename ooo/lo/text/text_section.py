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
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from ..container.x_named import XNamed as XNamed_a6520b08
from .text_content import TextContent as TextContent_a6810b4d
from .x_text_section import XTextSection as XTextSection_b1730b9f
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..style.graphic_location import GraphicLocation as GraphicLocation_e3ef0d30
    from .section_file_link import SectionFileLink as SectionFileLink_d63e0cb0
    from .x_text_columns import XTextColumns as XTextColumns_b17f0bab

class TextSection(TextContent_a6810b4d, UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa, XPropertyState_d55c0ccf, XNamed_a6520b08, XTextSection_b1730b9f):
    """
    Service Class

    A TextSection is a range of complete paragraphs within a text.
    
    The content of the section may be the content of a link into another document, a link from the same document, or the result of a DDE operation.
    
    TextSection instances can be linked from and to other texts.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API TextSection <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextSection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextSection'
    __ooo_type_name__: str = 'service'

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
        contains the name of the file filter for the background graphic.
        """
    @abstractproperty
    def BackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the position of the background graphic.
        """
    @abstractproperty
    def BackGraphicURL(self) -> str:
        """
        contains the URL for the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
    @abstractproperty
    def Condition(self) -> str:
        """
        This property contains a conditional expression.
        
        If the result of the conditional expression is TRUE and the property TextSection.IsVisible is FALSE, then the section is hidden.
        """
    @abstractproperty
    def DDECommandElement(self) -> str:
        """
        specifies the source element of the command string for a DDE operation.
        
        The element can be i.e. a name of a cell in a sheet or a bookmark.
        """
    @abstractproperty
    def DDECommandFile(self) -> str:
        """
        specifies the source file name of the command string for a DDE operation.
        """
    @abstractproperty
    def DDECommandType(self) -> str:
        """
        specifies the type of the command string for a DDE operation.
        
        The type can be the name of the application that provides a DDE source.
        """
    @abstractproperty
    def EndnoteIsCollectAtTextEnd(self) -> bool:
        """
        determines whether endnotes inside the section are displayed at the end of the section text.
        """
    @abstractproperty
    def EndnoteIsOwnNumbering(self) -> bool:
        """
        determines whether the endnotes within the section use an own numbering format.
        
        This is only valid if EndnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def EndnoteIsRestartNumbering(self) -> bool:
        """
        determines whether the endnotes numbering restarts within the section.
        
        This is only valid if EndnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def EndnoteNumberingPrefix(self) -> str:
        """
        determines the prefix that is display before the endnote number.
        
        This is only valid if EndnoteIsOwnNumbering is set.
        """
    @abstractproperty
    def EndnoteNumberingSuffix(self) -> str:
        """
        determines the suffix that is display after the endnote number.
        
        This is only valid if EndnoteIsOwnNumbering is set.
        """
    @abstractproperty
    def EndnoteNumberingType(self) -> int:
        """
        determines the numbering type of the endnote numbering as a value of com.sun.star.style.NumberingType.
        
        This is only valid if EndoteIsOwnNumbering is set.
        """
    @abstractproperty
    def EndnoteRestartNumberingAt(self) -> int:
        """
        determines at which number the endnote numbering inside of the section starts.
        
        This is only valid if EndnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def FileLink(self) -> 'SectionFileLink_d63e0cb0':
        """
        If this property is set, then the content of the section is read from the specified document.
        """
    @abstractproperty
    def FootnoteIsCollectAtTextEnd(self) -> bool:
        """
        determines whether footnotes inside the section are displayed at the end of the section text.
        """
    @abstractproperty
    def FootnoteIsOwnNumbering(self) -> bool:
        """
        determines whether the footnotes within the section use an own numbering format.
        
        This is only valid if FootnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def FootnoteIsRestartNumbering(self) -> bool:
        """
        determines whether the footnotes numbering restarts within the section.
        
        This is only valid if FootnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def FootnoteNumberingPrefix(self) -> str:
        """
        determines the prefix that is display before the footnote number.
        
        This is only valid if FootnoteIsOwnNumbering is set.
        """
    @abstractproperty
    def FootnoteNumberingSuffix(self) -> str:
        """
        determines the suffix that is display after of the footnote number.
        
        This is only valid if FootnoteIsOwnNumbering is set.
        """
    @abstractproperty
    def FootnoteNumberingType(self) -> int:
        """
        determines the numbering type of the footnote numbering as a value of com.sun.star.style.NumberingType.
        
        This is only valid if FootnoteIsOwnNumbering is set.
        """
    @abstractproperty
    def FootnoteRestartNumberingAt(self) -> int:
        """
        determines at which number the footnote numbering inside of the section starts.
        
        This is only valid if FootnoteIsRestartNumbering is set.
        """
    @abstractproperty
    def IsAutomaticUpdate(self) -> bool:
        """
        determines if a DDE link is updated automatically.
        """
    @abstractproperty
    def IsProtected(self) -> bool:
        """
        If this property is TRUE, the text section is protected and cannot be modified from the user interface.
        """
    @abstractproperty
    def IsVisible(self) -> bool:
        """
        If this property is FALSE, the text section is hidden.
        """
    @abstractproperty
    def LinkRegion(self) -> str:
        """
        specifies the source of a file link in the document that is specified in TextSection.FileLink.
        
        The source may be a text section or a bookmark. If TextSection.FileLink is empty, then the current document is searched for the source. If this property is empty and TextSection.FileLink is set, then the complete document content is linked into this section.
        """
    @abstractproperty
    def SectionLeftMargin(self) -> int:
        """
        determines the left margin of the section
        """
    @abstractproperty
    def SectionRightMargin(self) -> int:
        """
        determines the left margin of the section
        """
    @abstractproperty
    def TextColumns(self) -> 'XTextColumns_b17f0bab':
        """
        allows columns to be set into the text section
        """

__all__ = ['TextSection']

