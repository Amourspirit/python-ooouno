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
# Namespace: com.sun.star.awt.grid
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
import typing


class GridDataEvent(EventObject_a3d70b03):
    """
    Struct Class

    used to notify changes in the data represented by an XMutableGridDataModel.
    
    Effectively, a GridDataEvent denotes a continuous two-dimensional cell range within a grid's data model, which is affected by a certain change.
    
    **since**
    
        OOo 3.3

    See Also:
        `API GridDataEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridDataEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.GridDataEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.grid.GridDataEvent'
    """Literal Constant ``com.sun.star.awt.grid.GridDataEvent``"""

    def __init__(self, FirstColumn: int = 0, LastColumn: int = 0, FirstRow: int = 0, LastRow: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``FirstColumn`` can be another ``GridDataEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            FirstColumn (int, optional): FirstColumn value
            LastColumn (int, optional): LastColumn value
            FirstRow (int, optional): FirstRow value
            LastRow (int, optional): LastRow value
        """
        super().__init__(**kwargs)
        if isinstance(FirstColumn, GridDataEvent):
            oth: GridDataEvent = FirstColumn
            self._first_column = oth.FirstColumn
            self._last_column = oth.LastColumn
            self._first_row = oth.FirstRow
            self._last_row = oth.LastRow
            return
        else:
            self._first_column = FirstColumn
            self._last_column = LastColumn
            self._first_row = FirstRow
            self._last_row = LastRow



    @property
    def FirstColumn(self) -> int:
        """
        denotes the first column affected by a change.
        
        If FirstColumn is -1, the listener should assume that all rows of a grid's data model are affected.
        """
        return self._first_column
    
    @FirstColumn.setter
    def FirstColumn(self, value: int) -> None:
        self._first_column = value

    @property
    def LastColumn(self) -> int:
        """
        denotes the last column affected by a change
        """
        return self._last_column
    
    @LastColumn.setter
    def LastColumn(self, value: int) -> None:
        self._last_column = value

    @property
    def FirstRow(self) -> int:
        """
        denotes the first row affected by a change.
        
        If FirstRow is -1, the listener should assume that all rows of a grid's data model are affected.
        """
        return self._first_row
    
    @FirstRow.setter
    def FirstRow(self, value: int) -> None:
        self._first_row = value

    @property
    def LastRow(self) -> int:
        """
        denotes the last row affected by a change
        """
        return self._last_row
    
    @LastRow.setter
    def LastRow(self, value: int) -> None:
        self._last_row = value


__all__ = ['GridDataEvent']