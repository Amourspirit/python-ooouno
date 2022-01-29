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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class CellAddress(object):
    """
    Struct Class

    contains a cell address within a spreadsheet document.

    See Also:
        `API CellAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1CellAddress.html>`_


    Note:
        | At runtime CellAddress will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | CellAddress is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Column: typing.Optional[int] = None, Row: typing.Optional[int] = None, Sheet: typing.Optional[int] = None):
        self._column = Column
        self._row = Row
        self._sheet = Sheet

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

    @property
    def Sheet(self) -> int:
        """
        is the index of the sheet that contains the cell.
        """
        return self._sheet
    
    @Sheet.setter
    def Sheet(self, value: int) -> None:
        self._sheet = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global CellAddress
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Column', 'Row', 'Sheet')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.table.CellAddress')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        CellAddress = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['CellAddress']
