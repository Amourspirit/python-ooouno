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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from .chart_data_change_type import ChartDataChangeType as ChartDataChangeType_16cc0e6e


class ChartDataChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes a change that was applied to the data.

    See Also:
        `API ChartDataChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart.ChartDataChangeEvent'
    """Literal Constant ``com.sun.star.chart.ChartDataChangeEvent``"""

    def __init__(self, Type: ChartDataChangeType_16cc0e6e = ChartDataChangeType_16cc0e6e.ALL, StartColumn: int = 0, EndColumn: int = 0, StartRow: int = 0, EndRow: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Type`` can be another ``ChartDataChangeEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Type (ChartDataChangeType, optional): Type value
            StartColumn (int, optional): StartColumn value
            EndColumn (int, optional): EndColumn value
            StartRow (int, optional): StartRow value
            EndRow (int, optional): EndRow value
        """
        super().__init__(**kwargs)
        if isinstance(Type, ChartDataChangeEvent):
            oth: ChartDataChangeEvent = Type
            self._type = oth.Type
            self._start_column = oth.StartColumn
            self._end_column = oth.EndColumn
            self._start_row = oth.StartRow
            self._end_row = oth.EndRow
            return
        else:
            self._type = Type
            self._start_column = StartColumn
            self._end_column = EndColumn
            self._start_row = StartRow
            self._end_row = EndRow



    @property
    def Type(self) -> ChartDataChangeType_16cc0e6e:
        """
        specifies the type of change to the data.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: ChartDataChangeType_16cc0e6e) -> None:
        self._type = value

    @property
    def StartColumn(self) -> int:
        """
        specifies the column number in which the changes begin.
        """
        return self._start_column
    
    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def EndColumn(self) -> int:
        """
        specifies the column number in which the changes end.
        """
        return self._end_column
    
    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def StartRow(self) -> int:
        """
        specifies the row number in which the changes begin.
        """
        return self._start_row
    
    @StartRow.setter
    def StartRow(self, value: int) -> None:
        self._start_row = value

    @property
    def EndRow(self) -> int:
        """
        specifies the row number in which the changes end.
        """
        return self._end_row
    
    @EndRow.setter
    def EndRow(self, value: int) -> None:
        self._end_row = value


__all__ = ['ChartDataChangeEvent']
