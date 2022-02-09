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
# Namespace: com.sun.star.table
# Libre Office Version: 7.2


class CellRangeAddress(object):
    """
    Struct Class

    contains a cell range address within a spreadsheet document.

    See Also:
        `API CellRangeAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1CellRangeAddress.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.CellRangeAddress'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.CellRangeAddress'
    """Literal Constant ``com.sun.star.table.CellRangeAddress``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``CellRangeAddress`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``CellRangeAddress``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Sheet (int, optional): Sheet value
            StartColumn (int, optional): StartColumn value
            StartRow (int, optional): StartRow value
            EndColumn (int, optional): EndColumn value
            EndRow (int, optional): EndRow value
        """
        self._sheet = None
        self._start_column = None
        self._start_row = None
        self._end_column = None
        self._end_row = None

        key_order = ('Sheet', 'StartColumn', 'StartRow', 'EndColumn', 'EndRow')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], CellRangeAddress):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("CellRangeAddress.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Sheet(self) -> int:
        """
        is the index of the sheet that contains the cell range.
        """
        return self._sheet
    
    @Sheet.setter
    def Sheet(self, value: int) -> None:
        self._sheet = value

    @property
    def StartColumn(self) -> int:
        """
        is the index of the column of the left edge of the range.
        """
        return self._start_column
    
    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def StartRow(self) -> int:
        """
        is the index of the row of the top edge of the range.
        """
        return self._start_row
    
    @StartRow.setter
    def StartRow(self, value: int) -> None:
        self._start_row = value

    @property
    def EndColumn(self) -> int:
        """
        is the index of the column of the right edge of the range.
        """
        return self._end_column
    
    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def EndRow(self) -> int:
        """
        is the index of the row of the bottom edge of the range.
        """
        return self._end_row
    
    @EndRow.setter
    def EndRow(self, value: int) -> None:
        self._end_row = value


__all__ = ['CellRangeAddress']
