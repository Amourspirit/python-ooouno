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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class DataPilotFieldSortInfo(object):
    """
    Struct Class

    describes how to sort a single DataPilotField

    See Also:
        `API DataPilotFieldSortInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldSortInfo.html>`_


    Note:
        | At runtime DataPilotFieldSortInfo will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | DataPilotFieldSortInfo is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Field: typing.Optional[str] = None, IsAscending: typing.Optional[bool] = None, Mode: typing.Optional[int] = None):
        self._field = Field
        self._is_ascending = IsAscending
        self._mode = Mode

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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global DataPilotFieldSortInfo
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Field', 'IsAscending', 'Mode')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sheet.DataPilotFieldSortInfo')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        DataPilotFieldSortInfo = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['DataPilotFieldSortInfo']
