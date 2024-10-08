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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..document.settings import Settings as Settings_b2bc0bb8
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class DocumentSettings(Settings_b2bc0bb8):
    """
    Service Class

    describes properties that apply to the whole spreadsheet document.
    
    For settings that affect view properties, these settings apply to subsequently created views and are saved with the document, while SpreadsheetViewSettings can be used to alter a specific view that is already open.

    See Also:
        `API DocumentSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DocumentSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DocumentSettings'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def GridColor(self) -> Color_68e908c5:
        """
        specifies the color in which the cell grid is displayed.
        """
        ...

    @property
    @abstractmethod
    def HasColumnRowHeaders(self) -> bool:
        """
        enables the column and row headers of the view.
        """
        ...

    @property
    @abstractmethod
    def HasSheetTabs(self) -> bool:
        """
        enables the sheet tabs of the view.
        """
        ...

    @property
    @abstractmethod
    def IsDocumentShared(self) -> bool:
        """
        enables the document sharing feature (Tools->Share Spreadsheet)
        """
        ...

    @property
    @abstractmethod
    def IsOutlineSymbolsSet(self) -> bool:
        """
        enables the display of outline symbols.
        """
        ...

    @property
    @abstractmethod
    def IsRasterAxisSynchronized(self) -> bool:
        """
        enables the synchronization of horizontal and vertical grid settings in the user interface.
        """
        ...

    @property
    @abstractmethod
    def IsSnapToRaster(self) -> bool:
        """
        enables the restriction of object movement and resizing of drawing objects to the raster.
        """
        ...

    @property
    @abstractmethod
    def RasterIsVisible(self) -> bool:
        """
        enables the display of the drawing object raster.
        """
        ...

    @property
    @abstractmethod
    def RasterResolutionX(self) -> int:
        """
        specifies the distance between horizontal grid elements in 1/100 mm.
        """
        ...

    @property
    @abstractmethod
    def RasterResolutionY(self) -> int:
        """
        specifies the distance between vertical grid elements in 1/100 mm.
        """
        ...

    @property
    @abstractmethod
    def RasterSubdivisionX(self) -> int:
        """
        specifies the number of subdivisions between two horizontal grid elements.
        """
        ...

    @property
    @abstractmethod
    def RasterSubdivisionY(self) -> int:
        """
        specifies the number of subdivisions between two vertical grid elements.
        """
        ...

    @property
    @abstractmethod
    def ShowGrid(self) -> bool:
        """
        enables the display of the cell grid.
        """
        ...

    @property
    @abstractmethod
    def ShowNotes(self) -> bool:
        """
        controls whether a marker is shown for notes in cells.
        """
        ...

    @property
    @abstractmethod
    def ShowPageBreaks(self) -> bool:
        """
        enables display of page breaks.
        """
        ...

    @property
    @abstractmethod
    def ShowZeroValues(self) -> bool:
        """
        enables display of zero-values.
        """
        ...


__all__ = ['DocumentSettings']

