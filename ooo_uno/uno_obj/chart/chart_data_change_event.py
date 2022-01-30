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
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
if typing.TYPE_CHECKING:
    from .chart_data_change_type import ChartDataChangeType as ChartDataChangeType_16cc0e6e
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class ChartDataChangeEvent(EventObject_a3d70b03):
        """
        Struct Class

        describes a change that was applied to the data.

        See Also:
            `API ChartDataChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataChangeEvent.html>`_


        Note:
            | At runtime ChartDataChangeEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | ChartDataChangeEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, EndColumn: typing.Optional[int] = None, EndRow: typing.Optional[int] = None, StartColumn: typing.Optional[int] = None, StartRow: typing.Optional[int] = None, Type: 'typing.Optional[ChartDataChangeType_16cc0e6e]' = None):
            self._end_column = EndColumn
            self._end_row = EndRow
            self._start_column = StartColumn
            self._start_row = StartRow
            self._type = Type

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
        def EndRow(self) -> int:
            """
            specifies the row number in which the changes end.
            """
            return self._end_row
        
        @EndRow.setter
        def EndRow(self, value: int) -> None:
            self._end_row = value

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
        def StartRow(self) -> int:
            """
            specifies the row number in which the changes begin.
            """
            return self._start_row
        
        @StartRow.setter
        def StartRow(self, value: int) -> None:
            self._start_row = value

        @property
        def Type(self) -> 'ChartDataChangeType_16cc0e6e':
            """
            specifies the type of change to the data.
            """
            return self._type
        
        @Type.setter
        def Type(self, value: 'ChartDataChangeType_16cc0e6e') -> None:
            self._type = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global ChartDataChangeEvent
        order = ('EndColumn', 'EndRow', 'StartColumn', 'StartRow', 'Type')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.chart.ChartDataChangeEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ChartDataChangeEvent = _struct_init

    _dynamic_struct()

__all__ = ['ChartDataChangeEvent']
