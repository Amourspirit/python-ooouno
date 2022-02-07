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
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from ...lo.sdbc.result_set_type import ResultSetType as ResultSetType


class ResultSetTypeEnum(IntEnum):
    """
    Enum of Const Class ResultSetType

    describes the different scroll capabilities of a result set.
    """
    FORWARD_ONLY = ResultSetType.FORWARD_ONLY
    """
    is the type for a com.sun.star.sdb.ResultSet object whose cursor may move only forward.
    """
    SCROLL_INSENSITIVE = ResultSetType.SCROLL_INSENSITIVE
    """
    is the type for a com.sun.star.sdb.ResultSet object that is scrollable but generally not sensitive to changes made by others.
    """
    SCROLL_SENSITIVE = ResultSetType.SCROLL_SENSITIVE
    """
    is the type for a com.sun.star.sdb.ResultSet object that is scrollable and generally sensitive to changes made by others.
    """

__all__ = ['ResultSetType', 'ResultSetTypeEnum']
