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
if typing.TYPE_CHECKING:
    from .data_pilot_field_filter import DataPilotFieldFilter as DataPilotFieldFilter_271e0eed
    from .data_result import DataResult as DataResult_a47d0b1a
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class DataPilotTableResultData(object):
    """
    Struct Class

    information about a cell positioned within the result area of a DataPilot table.
    
    DataPilotTableResultData contains information about a particular cell positioned within the result area of a DataPilot table.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DataPilotTableResultData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotTableResultData.html>`_


    Note:
        | At runtime DataPilotTableResultData will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | DataPilotTableResultData is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, DataFieldIndex: typing.Optional[int] = None, FieldFilters: 'typing.Optional[typing.List[DataPilotFieldFilter_271e0eed]]' = None, Result: 'typing.Optional[DataResult_a47d0b1a]' = None):
        self._data_field_index = DataFieldIndex
        self._field_filters = FieldFilters
        self._result = Result

    @property
    def DataFieldIndex(self) -> int:
        """
        This is a 0-based index that specifies which data field the data displayed in the cell is for; the value of 0 means the cell is for the first data field, 1 for the second, and so on.
        """
        return self._data_field_index
    
    @DataFieldIndex.setter
    def DataFieldIndex(self, value: int) -> None:
        self._data_field_index = value

    @property
    def FieldFilters(self) -> 'typing.List[DataPilotFieldFilter_271e0eed]':
        """
        This is a set of filter criteria that can be used to re-create those data rows that contribute to the value shown in the cell.
        """
        return self._field_filters
    
    @FieldFilters.setter
    def FieldFilters(self, value: 'typing.List[DataPilotFieldFilter_271e0eed]') -> None:
        self._field_filters = value

    @property
    def Result(self) -> 'DataResult_a47d0b1a':
        """
        more information about the result contained in the DataResult type.
        """
        return self._result
    
    @Result.setter
    def Result(self, value: 'DataResult_a47d0b1a') -> None:
        self._result = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global DataPilotTableResultData
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('DataFieldIndex', 'FieldFilters', 'Result')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sheet.DataPilotTableResultData')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        DataPilotTableResultData = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['DataPilotTableResultData']
