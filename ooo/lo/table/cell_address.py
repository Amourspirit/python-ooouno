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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.table
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class CellAddress(object):
    """
    Struct Class

    contains a cell address within a spreadsheet document.

    See Also:
        `API CellAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1CellAddress.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.CellAddress'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.CellAddress'
    """Literal Constant ``com.sun.star.table.CellAddress``"""

    def __init__(self, Sheet: typing.Optional[int] = 0, Column: typing.Optional[int] = 0, Row: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Sheet (int, optional): Sheet value.
            Column (int, optional): Column value.
            Row (int, optional): Row value.
        """
        super().__init__()

        if isinstance(Sheet, CellAddress):
            oth: CellAddress = Sheet
            self.Sheet = oth.Sheet
            self.Column = oth.Column
            self.Row = oth.Row
            return

        kargs = {
            "Sheet": Sheet,
            "Column": Column,
            "Row": Row,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._sheet = kwargs["Sheet"]
        self._column = kwargs["Column"]
        self._row = kwargs["Row"]


    @property
    def Sheet(self) -> int:
        """
        is the index of the sheet that contains the cell.
        """
        return self._sheet

    @Sheet.setter
    def Sheet(self, value: int) -> None:
        self._sheet = value

    @property
    def Column(self) -> int:
        """
        is the index of the column where the cell is located.
        """
        return self._column

    @Column.setter
    def Column(self, value: int) -> None:
        self._column = value

    @property
    def Row(self) -> int:
        """
        is the index of the row where the cell is located.
        """
        return self._row

    @Row.setter
    def Row(self, value: int) -> None:
        self._row = value


__all__ = ['CellAddress']
