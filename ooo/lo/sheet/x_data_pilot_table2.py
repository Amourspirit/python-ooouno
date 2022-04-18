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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from .x_data_pilot_table import XDataPilotTable as XDataPilotTable_e0530ce3
if typing.TYPE_CHECKING:
    from .data_pilot_table_position_data import DataPilotTablePositionData as DataPilotTablePositionData_8a0c115a
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XDataPilotTable2(XDataPilotTable_e0530ce3):
    """
    additional methods to extend com.sun.star.sheet.XDataPilotTable.
    
    com.sun.star.sheet.XDataPilotTable2 extends the old com.sun.star.sheet.XDataPilotTable interface with additional methods.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XDataPilotTable2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDataPilotTable2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XDataPilotTable2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XDataPilotTable2'

    @abstractmethod
    def getDrillDownData(self, aAddr: 'CellAddress_ae5f0b56') -> 'typing.Tuple[typing.Tuple[object, ...], ...]':
        """
        When the address of a cell within the result area is given, XDataPilotTable2.getDrillDownData() returns its drill-down output table that includes only those rows that contribute to the value of that cell.
        """
    @abstractmethod
    def getOutputRangeByType(self, nType: int) -> 'CellRangeAddress_ec450d43':
        """
        This method returns a different output range of a DataPilot table per specified output range type.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getPositionData(self, aAddr: 'CellAddress_ae5f0b56') -> 'DataPilotTablePositionData_8a0c115a':
        """
        Given a cell address, it returns the information about that cell.
        
        The type of information returned depends upon whether the cell is within the result area or column/row header area.
        """
    @abstractmethod
    def insertDrillDownSheet(self, aAddr: 'CellAddress_ae5f0b56') -> None:
        """
        This method inserts a new sheet to display the drill-down data for a specified result cell. A drill-down data for a result cell consists of a subset of rows from the original data source that contribute to the value displayed in that cell.
        
        The new sheet is always inserted to the immediate left of the current sheet where the DataPilot table is. Note that when the drill-down data is empty, no new sheet is inserted.
        """

__all__ = ['XDataPilotTable2']

