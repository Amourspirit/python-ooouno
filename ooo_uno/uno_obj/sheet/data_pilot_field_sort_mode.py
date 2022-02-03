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


class DataPilotFieldSortMode(object):
    """
    Const Class

    describes the sort mode of the data field

    See Also:
        `API DataPilotFieldSortMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldSortMode.html>`_
    """
    NONE = 0
    """
    the data are taken as they come from the DataPilotSource.
    """
    MANUAL = 1
    """
    the user can sort the fields
    """
    NAME = 2
    """
    the field is sorted by its names
    """
    DATA = 3
    """
    the field is sorted by the data in the given field
    """


class DataPilotFieldSortModeEnum(IntEnum):
    """
    Enum of Const Class DataPilotFieldSortMode

    describes the sort mode of the data field
    """
    NONE = DataPilotFieldSortMode.NONE
    """
    the data are taken as they come from the DataPilotSource.
    """
    MANUAL = DataPilotFieldSortMode.MANUAL
    """
    the user can sort the fields
    """
    NAME = DataPilotFieldSortMode.NAME
    """
    the field is sorted by its names
    """
    DATA = DataPilotFieldSortMode.DATA
    """
    the field is sorted by the data in the given field
    """

__all__ = ['DataPilotFieldSortMode', 'DataPilotFieldSortModeEnum']
