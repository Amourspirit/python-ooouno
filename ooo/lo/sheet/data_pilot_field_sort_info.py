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
from ooo.oenv import UNO_NONE
import typing


class DataPilotFieldSortInfo(object):
    """
    Struct Class

    describes how to sort a single DataPilotField

    See Also:
        `API DataPilotFieldSortInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldSortInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldSortInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotFieldSortInfo'
    """Literal Constant ``com.sun.star.sheet.DataPilotFieldSortInfo``"""

    def __init__(self, Field: typing.Optional[str] = '', IsAscending: typing.Optional[bool] = False, Mode: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Field (str, optional): Field value.
            IsAscending (bool, optional): IsAscending value.
            Mode (int, optional): Mode value.
        """
        super().__init__()
        kargs = {
            "Field": Field,
            "IsAscending": IsAscending,
            "Mode": Mode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._field = kwargs["Field"]
        self._is_ascending = kwargs["IsAscending"]
        self._mode = kwargs["Mode"]


    @property
    def Field(self) -> str:
        """
        contains the data field to sort by if the Mode is DATA
        """
        return self._field
    
    @Field.setter
    def Field(self, value: str) -> None:
        self._field = value

    @property
    def IsAscending(self) -> bool:
        """
        TRUE if data are sorted in ascending order, FALSE if in descending order.
        """
        return self._is_ascending
    
    @IsAscending.setter
    def IsAscending(self, value: bool) -> None:
        self._is_ascending = value

    @property
    def Mode(self) -> int:
        """
        contains the sort mode
        """
        return self._mode
    
    @Mode.setter
    def Mode(self, value: int) -> None:
        self._mode = value


__all__ = ['DataPilotFieldSortInfo']
