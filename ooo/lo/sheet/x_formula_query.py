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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_sheet_cell_ranges import XSheetCellRanges as XSheetCellRanges_edef0d52

class XFormulaQuery(XInterface_8f010a43):
    """
    provides methods to query cells for dependencies in formulas.
    
    All methods return a collection of cell ranges.

    See Also:
        `API XFormulaQuery <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XFormulaQuery.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XFormulaQuery'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XFormulaQuery'

    @abstractmethod
    def queryDependents(self, bRecursive: bool) -> XSheetCellRanges_edef0d52:
        """
        queries all dependent formula cells.
        
        Dependent cells are cells containing formulas with references to the original cell.
        """
        ...
    @abstractmethod
    def queryPrecedents(self, bRecursive: bool) -> XSheetCellRanges_edef0d52:
        """
        queries all precedent cells.
        
        Precedent cells are cells which are referenced from a formula cell.
        """
        ...

__all__ = ['XFormulaQuery']

