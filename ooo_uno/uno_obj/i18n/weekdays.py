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
# Namespace: com.sun.star.i18n
from enum import IntEnum


class Weekdays(object):
    """
    Const Class

    Constants for days of a week.
    
    used with XCalendar.getFirstDayOfWeek(), XCalendar.setFirstDayOfWeek() and XCalendar.getDisplayName()

    See Also:
        `API Weekdays <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1Weekdays.html>`_
    """
    SUNDAY = 0
    """
    Sunday.
    """
    MONDAY = 1
    """
    Monday.
    """
    TUESDAY = 2
    """
    Tuesday.
    """
    WEDNESDAY = 3
    """
    Wednesday.
    """
    THURSDAY = 4
    """
    Thursday.
    """
    FRIDAY = 5
    """
    Friday.
    """
    SATURDAY = 6
    """
    Saturday.
    """


class WeekdaysEnum(IntEnum):
    """
    Enum of Const Class Weekdays

    Constants for days of a week.
    
    used with XCalendar.getFirstDayOfWeek(), XCalendar.setFirstDayOfWeek() and XCalendar.getDisplayName()
    """
    SUNDAY = Weekdays.SUNDAY
    """
    Sunday.
    """
    MONDAY = Weekdays.MONDAY
    """
    Monday.
    """
    TUESDAY = Weekdays.TUESDAY
    """
    Tuesday.
    """
    WEDNESDAY = Weekdays.WEDNESDAY
    """
    Wednesday.
    """
    THURSDAY = Weekdays.THURSDAY
    """
    Thursday.
    """
    FRIDAY = Weekdays.FRIDAY
    """
    Friday.
    """
    SATURDAY = Weekdays.SATURDAY
    """
    Saturday.
    """

__all__ = ['Weekdays', 'WeekdaysEnum']
