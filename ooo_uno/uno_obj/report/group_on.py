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
# Namespace: com.sun.star.report
from enum import IntEnum


class GroupOn(object):
    """
    Const Class

    Specifies how to group data.

    See Also:
        `API GroupOn <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1report_1_1GroupOn.html>`_
    """
    DEFAULT = 0
    """
    The same value in the column value or expression.
    """
    PREFIX_CHARACTERS = 1
    """
    The same first nth of characters in the column value or expression.
    """
    YEAR = 2
    """
    Dates in the same calendar year.
    """
    QUARTAL = 3
    """
    Dates in the same calendar quarter.
    """
    MONTH = 4
    """
    Dates in the same month.
    """
    WEEK = 5
    """
    Dates in the same week.
    """
    DAY = 6
    """
    Dates on the same date.
    """
    HOUR = 7
    """
    Times in the same hour.
    """
    MINUTE = 8
    """
    Times in the same minute.
    """
    INTERVAL = 9
    """
    Values within an interval you specify.
    """


class GroupOnEnum(IntEnum):
    """
    Enum of Const Class GroupOn

    Specifies how to group data.
    """
    DEFAULT = GroupOn.DEFAULT
    """
    The same value in the column value or expression.
    """
    PREFIX_CHARACTERS = GroupOn.PREFIX_CHARACTERS
    """
    The same first nth of characters in the column value or expression.
    """
    YEAR = GroupOn.YEAR
    """
    Dates in the same calendar year.
    """
    QUARTAL = GroupOn.QUARTAL
    """
    Dates in the same calendar quarter.
    """
    MONTH = GroupOn.MONTH
    """
    Dates in the same month.
    """
    WEEK = GroupOn.WEEK
    """
    Dates in the same week.
    """
    DAY = GroupOn.DAY
    """
    Dates on the same date.
    """
    HOUR = GroupOn.HOUR
    """
    Times in the same hour.
    """
    MINUTE = GroupOn.MINUTE
    """
    Times in the same minute.
    """
    INTERVAL = GroupOn.INTERVAL
    """
    Values within an interval you specify.
    """

__all__ = ['GroupOn', 'GroupOnEnum']
