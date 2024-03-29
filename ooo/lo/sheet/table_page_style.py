# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractproperty
from ..style.page_style import PageStyle as PageStyle_9b210ac7
if typing.TYPE_CHECKING:
    from .x_header_footer_content import XHeaderFooterContent as XHeaderFooterContent_275c0f0c

class TablePageStyle(PageStyle_9b210ac7):
    """
    Service Class

    represents a page style for a spreadsheet.
    
    This service extends the service com.sun.star.style.PageStyle with spreadsheet specific properties.
    
    **since**
    
        OOo 2.0

    See Also:
        `API TablePageStyle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1TablePageStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TablePageStyle'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CenterHorizontally(self) -> bool:
        """
        determines whether the table is centered horizontally on the page.
        """
        ...

    @abstractproperty
    def CenterVertically(self) -> bool:
        """
        determines whether the table is centered vertically on the page.
        """
        ...

    @abstractproperty
    def FirstPageNumber(self) -> int:
        """
        contains the page number applied to the first page for this sheet.
        
        The value 0 indicates that the page numbers are continued from the previous sheet.
        """
        ...

    @abstractproperty
    def LeftPageFooterContent(self) -> XHeaderFooterContent_275c0f0c:
        """
        contains the content of the footer for left pages.
        
        After changing the footer text contents, this property has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def LeftPageHeaderContent(self) -> XHeaderFooterContent_275c0f0c:
        """
        contains the content of the header for left pages.
        
        After changing the header text contents, this property has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def PageScale(self) -> int:
        """
        contains the scaling factor (in percent) for printing the sheet.
        """
        ...

    @abstractproperty
    def PrintAnnotations(self) -> bool:
        """
        enables printing of cell annotations.
        """
        ...

    @abstractproperty
    def PrintCharts(self) -> bool:
        """
        enables printing of charts.
        """
        ...

    @abstractproperty
    def PrintDownFirst(self) -> bool:
        """
        specifies the print order for the pages within each sheet.
        
        If TRUE, the order for printing pages begins with top-to-bottom, then continues with the next set of cell columns to the right. If FALSE, the order for printing pages begins with left-to-right, then continues with the next set of cell rows to the bottom.
        """
        ...

    @abstractproperty
    def PrintDrawing(self) -> bool:
        """
        enables printing of drawing objects.
        """
        ...

    @abstractproperty
    def PrintFormulas(self) -> bool:
        """
        enables printing of formulas instead of their results.
        """
        ...

    @abstractproperty
    def PrintGrid(self) -> bool:
        """
        enables printing of the cell grid.
        """
        ...

    @abstractproperty
    def PrintHeaders(self) -> bool:
        """
        enables printing of column and row headers.
        """
        ...

    @abstractproperty
    def PrintObjects(self) -> bool:
        """
        enables printing of embedded objects.
        """
        ...

    @abstractproperty
    def PrintZeroValues(self) -> bool:
        """
        enables printing of zero-values.
        """
        ...

    @abstractproperty
    def RightPageFooterContent(self) -> XHeaderFooterContent_275c0f0c:
        """
        contains the content of the footer for right pages.
        
        After changing the footer text contents, this property has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def RightPageHeaderContent(self) -> XHeaderFooterContent_275c0f0c:
        """
        contains the content of the header for right pages.
        
        After changing the header text contents, this property has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def ScaleToPages(self) -> int:
        """
        contains the number of pages the sheet will printed.
        """
        ...

    @abstractproperty
    def ScaleToPagesX(self) -> int:
        """
        contains the number of horizontal pages the sheet will printed on.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def ScaleToPagesY(self) -> int:
        """
        contains the number of vertical pages the sheet will printed on.
        
        **since**
        
            OOo 2.0
        """
        ...


__all__ = ['TablePageStyle']

