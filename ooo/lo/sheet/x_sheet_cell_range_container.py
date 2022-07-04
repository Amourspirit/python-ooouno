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
from .x_sheet_cell_ranges import XSheetCellRanges as XSheetCellRanges_edef0d52
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XSheetCellRangeContainer(XSheetCellRanges_edef0d52):
    """
    provides methods to access cell ranges in a collection via index and to add and remove cell ranges.

    See Also:
        `API XSheetCellRangeContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetCellRangeContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetCellRangeContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetCellRangeContainer'

    @abstractmethod
    def addRangeAddress(self, aCellRangeAddress: 'CellRangeAddress_ec450d43', bMergeRanges: bool) -> None:
        """
        adds the given range to the collection of cell ranges.
        """
        ...
    @abstractmethod
    def addRangeAddresses(self, aCellRangeAddresses: 'typing.Tuple[CellRangeAddress_ec450d43, ...]', bMergeRanges: bool) -> None:
        """
        adds the given ranges to the collection of cell ranges.
        """
        ...
    @abstractmethod
    def removeRangeAddress(self, aCellRangeAddress: 'CellRangeAddress_ec450d43') -> None:
        """
        removes the given range from the collection of cell ranges.
        
        The specified range must fit exactly to an element of the collection. The method does not try to shorten a range.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def removeRangeAddresses(self, aCellRangeAddresses: 'typing.Tuple[CellRangeAddress_ec450d43, ...]') -> None:
        """
        removes the given ranges from the collection of cell ranges.
        
        All specified ranges must fit exactly to elements of the collection. The method does not try to shorten ranges.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XSheetCellRangeContainer']

