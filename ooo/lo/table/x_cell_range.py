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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.table
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_cell import XCell as XCell_70d408e8

class XCellRange(XInterface_8f010a43):
    """
    provides access to the cells or to sub-ranges of a cell range.

    See Also:
        `API XCellRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XCellRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.XCellRange'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.table.XCellRange'

    @abstractmethod
    def getCellByPosition(self, nColumn: int, nRow: int) -> XCell_70d408e8:
        """
        Returns a single cell within the range.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getCellRangeByName(self, aRange: str) -> XCellRange:
        """
        Returns a sub-range of cells within the range.
        
        The sub-range is specified by its name. The format of the range name is dependent of the context of the table. In spreadsheets valid names may be \"A1:C5\" or \"$B$2\" or even defined names for cell ranges such as \"MySpecialCell\".
        """
        ...
    @abstractmethod
    def getCellRangeByPosition(self, nLeft: int, nTop: int, nRight: int, nBottom: int) -> XCellRange:
        """
        Returns a sub-range of cells within the range.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...

__all__ = ['XCellRange']

