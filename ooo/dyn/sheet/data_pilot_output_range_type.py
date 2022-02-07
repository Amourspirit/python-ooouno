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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from enum import IntEnum
from ...lo.sheet.data_pilot_output_range_type import DataPilotOutputRangeType as DataPilotOutputRangeType


class DataPilotOutputRangeTypeEnum(IntEnum):
    """
    Enum of Const Class DataPilotOutputRangeType

    specifies region type of DataPilot table range
    
    This constant set is used to indicate the type of output range desired when XDataPilotTable2.getOutputRangeByType() is called, which returns a different cell range depending upon the value passed to it as the argument.
    
    **since**
    
        OOo 3.0
    """
    WHOLE = DataPilotOutputRangeType.WHOLE
    """
    whole DataPilot output range including the header area above the table where the filter and page field buttons are located.
    """
    TABLE = DataPilotOutputRangeType.TABLE
    """
    whole table but without the header area where the filter and page field buttons are located.
    """
    RESULT = DataPilotOutputRangeType.RESULT
    """
    result area where the result values are displayed.
    
    This also includes the column and row subtotal areas when they are displayed.
    """

__all__ = ['DataPilotOutputRangeType', 'DataPilotOutputRangeTypeEnum']
