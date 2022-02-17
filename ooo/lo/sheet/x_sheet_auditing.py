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
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XSheetAuditing(XInterface_8f010a43):
    """
    provides methods to access auditing (detective) features in a spreadsheet.

    See Also:
        `API XSheetAuditing <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetAuditing.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetAuditing'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetAuditing'

    @abstractmethod
    def clearArrows(self) -> None:
        """
        removes all auditing arrows from the spreadsheet.
        """
    @abstractmethod
    def hideDependents(self, aPosition: 'CellAddress_ae5f0b56') -> bool:
        """
        removes arrows for one level of dependents of a formula cell.
        
        If the method is executed again for the same cell, the previous level of dependent cells is removed.
        """
    @abstractmethod
    def hidePrecedents(self, aPosition: 'CellAddress_ae5f0b56') -> bool:
        """
        removes arrows for one level of precedents of a formula cell.
        
        If the method is executed again for the same cell, the previous level of dependent cells is removed.
        """
    @abstractmethod
    def showDependents(self, aPosition: 'CellAddress_ae5f0b56') -> bool:
        """
        draws arrows between a formula cell and its dependents.
        
        If the method is executed again for the same cell, the next level of dependent cells is marked.
        """
    @abstractmethod
    def showErrors(self, aPosition: 'CellAddress_ae5f0b56') -> bool:
        """
        draws arrows between a formula cell containing an error and the cells causing the error.
        """
    @abstractmethod
    def showInvalid(self) -> bool:
        """
        marks all cells containing invalid values.
        """
    @abstractmethod
    def showPrecedents(self, aPosition: 'CellAddress_ae5f0b56') -> bool:
        """
        draws arrows between a formula cell and its precedents.
        
        If the method is executed again for the same cell, the next level of dependent cells is marked.
        """

__all__ = ['XSheetAuditing']
