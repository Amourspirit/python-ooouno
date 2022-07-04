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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XPrintAreas(XInterface_8f010a43):
    """
    represents a sheet which has print areas.

    See Also:
        `API XPrintAreas <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XPrintAreas.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XPrintAreas'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XPrintAreas'

    @abstractmethod
    def getPrintAreas(self) -> 'typing.Tuple[CellRangeAddress_ec450d43, ...]':
        """
        returns a sequence containing all print areas of the sheet.
        """
        ...
    @abstractmethod
    def getPrintTitleColumns(self) -> bool:
        """
        returns, whether the title columns are repeated on all subsequent print pages to the right.
        """
        ...
    @abstractmethod
    def getPrintTitleRows(self) -> bool:
        """
        returns, whether the title rows are repeated on all subsequent print pages to the bottom.
        """
        ...
    @abstractmethod
    def getTitleColumns(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the range that is specified as title columns range.
        
        Title columns can be automatically repeated on all subsequent print pages to the right, using XPrintAreas.setPrintTitleColumns().
        """
        ...
    @abstractmethod
    def getTitleRows(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the range that is specified as title rows range.
        
        Title rows can be automatically repeated on all subsequent print pages to the bottom, using XPrintAreas.setPrintTitleRows().
        """
        ...
    @abstractmethod
    def setPrintAreas(self, aPrintAreas: 'typing.Tuple[CellRangeAddress_ec450d43, ...]') -> None:
        """
        sets the print areas of the sheet.
        
        If none of the sheets in a document have print areas, the whole sheets are printed. If any sheet contains print areas, other sheets without print areas are not printed.
        """
        ...
    @abstractmethod
    def setPrintTitleColumns(self, bPrintTitleColumns: bool) -> None:
        """
        specifies whether the title columns are repeated on all subsequent print pages to the right.
        """
        ...
    @abstractmethod
    def setPrintTitleRows(self, bPrintTitleRows: bool) -> None:
        """
        specifies whether the title rows are repeated on all subsequent print pages to the bottom.
        """
        ...
    @abstractmethod
    def setTitleColumns(self, aTitleColumns: 'CellRangeAddress_ec450d43') -> None:
        """
        specifies a range of columns as title columns range.
        
        The rows of the passed range are ignored.
        
        Title columns can be automatically repeated on all subsequent print pages to the right, using XPrintAreas.setPrintTitleColumns().
        """
        ...
    @abstractmethod
    def setTitleRows(self, aTitleRows: 'CellRangeAddress_ec450d43') -> None:
        """
        specifies a range of rows as title rows range.
        
        The columns of the passed range are ignored.
        
        Title rows can be automatically repeated on all subsequent print pages to the bottom, using XPrintAreas.setPrintTitleRows().
        """
        ...

__all__ = ['XPrintAreas']

