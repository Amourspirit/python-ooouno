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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .fill_date_mode import FillDateMode as FillDateMode_bb000bab
    from .fill_direction import FillDirection as FillDirection_c7f00c49
    from .fill_mode import FillMode as FillMode_8ee80a2d

class XCellSeries(XInterface_8f010a43):
    """
    provides methods to fill out a cell range automatically with values based on a start value, step count and fill mode.

    See Also:
        `API XCellSeries <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XCellSeries.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XCellSeries'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XCellSeries'

    @abstractmethod
    def fillAuto(self, nFillDirection: 'FillDirection_c7f00c49', nSourceCount: int) -> None:
        """
        fills all cells in the range in a way that is specified by the first cell(s) in the range.
        """
    @abstractmethod
    def fillSeries(self, nFillDirection: 'FillDirection_c7f00c49', nFillMode: 'FillMode_8ee80a2d', nFillDateMode: 'FillDateMode_bb000bab', fStep: float, fEndValue: float) -> None:
        """
        fills all cells in the range based on the specified settings.
        """

__all__ = ['XCellSeries']

