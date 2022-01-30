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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class SingleReference(object):
        """
        Struct Class

        contains a reference to a single cell.

        See Also:
            `API SingleReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1SingleReference.html>`_


        Note:
            | At runtime SingleReference will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | SingleReference is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Column: typing.Optional[int] = None, Flags: typing.Optional[int] = None, RelativeColumn: typing.Optional[int] = None, RelativeRow: typing.Optional[int] = None, RelativeSheet: typing.Optional[int] = None, Row: typing.Optional[int] = None, Sheet: typing.Optional[int] = None):
            self._column = Column
            self._flags = Flags
            self._relative_column = RelativeColumn
            self._relative_row = RelativeRow
            self._relative_sheet = RelativeSheet
            self._row = Row
            self._sheet = Sheet

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
        def Flags(self) -> int:
            """
            contains flags.
            """
            return self._flags
        
        @Flags.setter
        def Flags(self, value: int) -> None:
            self._flags = value

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
        def RelativeRow(self) -> int:
            """
            is the relative row number.
            """
            return self._relative_row
        
        @RelativeRow.setter
        def RelativeRow(self, value: int) -> None:
            self._relative_row = value

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
        def Row(self) -> int:
            """
            is the absolute row number.
            """
            return self._row
        
        @Row.setter
        def Row(self, value: int) -> None:
            self._row = value

        @property
        def Sheet(self) -> int:
            """
            is the absolute sheet number.
            """
            return self._sheet
        
        @Sheet.setter
        def Sheet(self, value: int) -> None:
            self._sheet = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global SingleReference
        order = ('Column', 'Flags', 'RelativeColumn', 'RelativeRow', 'RelativeSheet', 'Row', 'Sheet')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sheet.SingleReference')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        SingleReference = _struct_init

    _dynamic_struct()

__all__ = ['SingleReference']
