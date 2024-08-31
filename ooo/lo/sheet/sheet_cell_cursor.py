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
from .sheet_cell_range import SheetCellRange as SheetCellRange_d4540c87
from .x_sheet_cell_cursor import XSheetCellCursor as XSheetCellCursor_ee400d70
from .x_used_area_cursor import XUsedAreaCursor as XUsedAreaCursor_e0c20d01
from ..table.cell_cursor import CellCursor as CellCursor_a3b80b0e

class SheetCellCursor(SheetCellRange_d4540c87, CellCursor_a3b80b0e, XSheetCellCursor_ee400d70, XUsedAreaCursor_e0c20d01):
    """
    Service Class

    represents a cursor in a spreadsheet.
    
    A cursor is a cell range which provides additional methods to move through the table (i.e. to find specific cell ranges).

    See Also:
        `API SheetCellCursor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetCellCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SheetCellCursor'
    __ooo_type_name__: str = 'service'


__all__ = ['SheetCellCursor']

