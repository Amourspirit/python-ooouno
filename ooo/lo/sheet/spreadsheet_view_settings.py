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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class SpreadsheetViewSettings(XPropertySet_bc180bfa):
    """
    Service Class

    contains settings which are specific to each view of a spreadsheet

    See Also:
        `API SpreadsheetViewSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SpreadsheetViewSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SpreadsheetViewSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def GridColor(self) -> 'Color_68e908c5':
        """
        specifies the color in which the cell grid is displayed.
        """

    @abstractproperty
    def HasColumnRowHeaders(self) -> bool:
        """
        enables the column and row headers of the view.
        """

    @abstractproperty
    def HasHorizontalScrollBar(self) -> bool:
        """
        enables the horizontal scroll bar of the view.
        """

    @abstractproperty
    def HasSheetTabs(self) -> bool:
        """
        enables the sheet tabs of the view.
        """

    @abstractproperty
    def HasVerticalScrollBar(self) -> bool:
        """
        enables the vertical scroll bar of the view.
        """

    @abstractproperty
    def HideSpellMarks(self) -> bool:
        """
        disables the display of marks from online spelling.
        """

    @abstractproperty
    def IsOutlineSymbolsSet(self) -> bool:
        """
        enables the display of outline symbols.
        """

    @abstractproperty
    def IsValueHighlightingEnabled(self) -> bool:
        """
        controls whether strings, values, and formulas are displayed in different colors.
        """

    @abstractproperty
    def ShowAnchor(self) -> bool:
        """
        enables display of anchor symbols when drawing objects are selected.
        """

    @abstractproperty
    def ShowCharts(self) -> int:
        """
        enables the display of charts in the view.
        """

    @abstractproperty
    def ShowDrawing(self) -> int:
        """
        enables the display of drawing objects in the view.
        """

    @abstractproperty
    def ShowFormulas(self) -> bool:
        """
        controls whether formulas are displayed instead of their results.
        """

    @abstractproperty
    def ShowGrid(self) -> bool:
        """
        enables the display of the cell grid.
        """

    @abstractproperty
    def ShowHelpLines(self) -> bool:
        """
        enables display of help lines when moving drawing objects.
        """

    @abstractproperty
    def ShowNotes(self) -> bool:
        """
        controls whether a marker is shown for notes in cells.
        """

    @abstractproperty
    def ShowObjects(self) -> int:
        """
        enables display of embedded objects in the view.
        """

    @abstractproperty
    def ShowPageBreaks(self) -> bool:
        """
        enables display of page breaks.
        """

    @abstractproperty
    def ShowZeroValues(self) -> bool:
        """
        enables display of zero-values.
        """

    @abstractproperty
    def ZoomType(self) -> int:
        """
        This property defines the zoom type for the document.
        """

    @abstractproperty
    def ZoomValue(self) -> int:
        """
        Defines the zoom value to use.
        
        Valid only if the ZoomType is set to com.sun.star.view.DocumentZoomType.BY_VALUE.
        """



__all__ = ['SpreadsheetViewSettings']
