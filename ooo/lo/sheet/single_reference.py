# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class SingleReference(object):
    """
    Struct Class

    contains a reference to a single cell.

    See Also:
        `API SingleReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1SingleReference.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SingleReference'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.SingleReference'
    """Literal Constant ``com.sun.star.sheet.SingleReference``"""

    def __init__(self, Column: typing.Optional[int] = 0, RelativeColumn: typing.Optional[int] = 0, Row: typing.Optional[int] = 0, RelativeRow: typing.Optional[int] = 0, Sheet: typing.Optional[int] = 0, RelativeSheet: typing.Optional[int] = 0, Flags: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Column (int, optional): Column value.
            RelativeColumn (int, optional): RelativeColumn value.
            Row (int, optional): Row value.
            RelativeRow (int, optional): RelativeRow value.
            Sheet (int, optional): Sheet value.
            RelativeSheet (int, optional): RelativeSheet value.
            Flags (int, optional): Flags value.
        """
        super().__init__()

        if isinstance(Column, SingleReference):
            oth: SingleReference = Column
            self.Column = oth.Column
            self.RelativeColumn = oth.RelativeColumn
            self.Row = oth.Row
            self.RelativeRow = oth.RelativeRow
            self.Sheet = oth.Sheet
            self.RelativeSheet = oth.RelativeSheet
            self.Flags = oth.Flags
            return

        kargs = {
            "Column": Column,
            "RelativeColumn": RelativeColumn,
            "Row": Row,
            "RelativeRow": RelativeRow,
            "Sheet": Sheet,
            "RelativeSheet": RelativeSheet,
            "Flags": Flags,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._column = kwargs["Column"]
        self._relative_column = kwargs["RelativeColumn"]
        self._row = kwargs["Row"]
        self._relative_row = kwargs["RelativeRow"]
        self._sheet = kwargs["Sheet"]
        self._relative_sheet = kwargs["RelativeSheet"]
        self._flags = kwargs["Flags"]


    @property
    def Column(self) -> int:
        """
        is the absolute column number.
        """
        return self._column

    @Column.setter
    def Column(self, value: int) -> None:
        self._column = value

    @property
    def RelativeColumn(self) -> int:
        """
        is the relative column number.
        """
        return self._relative_column

    @RelativeColumn.setter
    def RelativeColumn(self, value: int) -> None:
        self._relative_column = value

    @property
    def Row(self) -> int:
        """
        is the absolute row number.
        """
        return self._row

    @Row.setter
    def Row(self, value: int) -> None:
        self._row = value

    @property
    def RelativeRow(self) -> int:
        """
        is the relative row number.
        """
        return self._relative_row

    @RelativeRow.setter
    def RelativeRow(self, value: int) -> None:
        self._relative_row = value

    @property
    def Sheet(self) -> int:
        """
        is the absolute sheet number.
        """
        return self._sheet

    @Sheet.setter
    def Sheet(self, value: int) -> None:
        self._sheet = value

    @property
    def RelativeSheet(self) -> int:
        """
        is the relative sheet number.
        """
        return self._relative_sheet

    @RelativeSheet.setter
    def RelativeSheet(self, value: int) -> None:
        self._relative_sheet = value

    @property
    def Flags(self) -> int:
        """
        contains flags.
        """
        return self._flags

    @Flags.setter
    def Flags(self, value: int) -> None:
        self._flags = value


__all__ = ['SingleReference']
