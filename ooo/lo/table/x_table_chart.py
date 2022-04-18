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
# Namespace: com.sun.star.table
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XTableChart(XInterface_8f010a43):
    """
    provides access to the settings of a chart object in a table or spreadsheet.

    See Also:
        `API XTableChart <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XTableChart.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.XTableChart'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.table.XTableChart'

    @abstractmethod
    def getHasColumnHeaders(self) -> bool:
        """
        returns, whether the cells of the topmost row of the source data are interpreted as column headers.
        """
    @abstractmethod
    def getHasRowHeaders(self) -> bool:
        """
        returns, whether the cells of the leftmost column of the source data are interpreted as row headers.
        """
    @abstractmethod
    def getRanges(self) -> 'typing.Tuple[CellRangeAddress_ec450d43, ...]':
        """
        returns the cell ranges that contain the data for the chart.
        """
    @abstractmethod
    def setHasColumnHeaders(self, bHasColumnHeaders: bool) -> None:
        """
        specifies whether the cells of the topmost row of the source data are interpreted as column headers.
        """
    @abstractmethod
    def setHasRowHeaders(self, bHasRowHeaders: bool) -> None:
        """
        specifies whether the cells of the leftmost column of the source data are interpreted as row headers.
        """
    @abstractmethod
    def setRanges(self, aRanges: 'typing.Tuple[CellRangeAddress_ec450d43, ...]') -> None:
        """
        sets the cell ranges that contain the data for the chart.
        """

__all__ = ['XTableChart']

