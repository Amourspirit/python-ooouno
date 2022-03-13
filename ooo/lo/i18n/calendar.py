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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from .calendar_item import CalendarItem as CalendarItem_a86c0af1


class Calendar(object):
    """
    Struct Class

    A calendar as returned in a sequence by XLocaleData.getAllCalendars().

    See Also:
        `API Calendar <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Calendar.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.Calendar'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.Calendar'
    """Literal Constant ``com.sun.star.i18n.Calendar``"""

    def __init__(self, Days: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = UNO_NONE, Months: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = UNO_NONE, Eras: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = UNO_NONE, StartOfWeek: typing.Optional[str] = '', MinimumNumberOfDaysForFirstWeek: typing.Optional[int] = 0, Default: typing.Optional[bool] = False, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Days (typing.Tuple[CalendarItem, ...], optional): Days value.
            Months (typing.Tuple[CalendarItem, ...], optional): Months value.
            Eras (typing.Tuple[CalendarItem, ...], optional): Eras value.
            StartOfWeek (str, optional): StartOfWeek value.
            MinimumNumberOfDaysForFirstWeek (int, optional): MinimumNumberOfDaysForFirstWeek value.
            Default (bool, optional): Default value.
            Name (str, optional): Name value.
        """
        super().__init__()

        if isinstance(Days, Calendar):
            oth: Calendar = Days
            self.Days = oth.Days
            self.Months = oth.Months
            self.Eras = oth.Eras
            self.StartOfWeek = oth.StartOfWeek
            self.MinimumNumberOfDaysForFirstWeek = oth.MinimumNumberOfDaysForFirstWeek
            self.Default = oth.Default
            self.Name = oth.Name
            return

        kargs = {
            "Days": Days,
            "Months": Months,
            "Eras": Eras,
            "StartOfWeek": StartOfWeek,
            "MinimumNumberOfDaysForFirstWeek": MinimumNumberOfDaysForFirstWeek,
            "Default": Default,
            "Name": Name,
        }
        if kargs["Days"] is UNO_NONE:
            kargs["Days"] = None
        if kargs["Months"] is UNO_NONE:
            kargs["Months"] = None
        if kargs["Eras"] is UNO_NONE:
            kargs["Eras"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._days = kwargs["Days"]
        self._months = kwargs["Months"]
        self._eras = kwargs["Eras"]
        self._start_of_week = kwargs["StartOfWeek"]
        self._minimum_number_of_days_for_first_week = kwargs["MinimumNumberOfDaysForFirstWeek"]
        self._default = kwargs["Default"]
        self._name = kwargs["Name"]


    @property
    def Days(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the days of the week, see also CalendarItem.
        """
        return self._days
    
    @Days.setter
    def Days(self, value: typing.Tuple[CalendarItem_a86c0af1, ...]) -> None:
        self._days = value

    @property
    def Months(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the months of the year, see also CalendarItem.
        """
        return self._months
    
    @Months.setter
    def Months(self, value: typing.Tuple[CalendarItem_a86c0af1, ...]) -> None:
        self._months = value

    @property
    def Eras(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the possible eras, see also CalendarItem.
        """
        return self._eras
    
    @Eras.setter
    def Eras(self, value: typing.Tuple[CalendarItem_a86c0af1, ...]) -> None:
        self._eras = value

    @property
    def StartOfWeek(self) -> str:
        """
        the ID of the day with which the week begins.
        """
        return self._start_of_week
    
    @StartOfWeek.setter
    def StartOfWeek(self, value: str) -> None:
        self._start_of_week = value

    @property
    def MinimumNumberOfDaysForFirstWeek(self) -> int:
        """
        how many days must reside in the first week of a year.
        """
        return self._minimum_number_of_days_for_first_week
    
    @MinimumNumberOfDaysForFirstWeek.setter
    def MinimumNumberOfDaysForFirstWeek(self, value: int) -> None:
        self._minimum_number_of_days_for_first_week = value

    @property
    def Default(self) -> bool:
        """
        if this is the default calendar for a given locale.
        """
        return self._default
    
    @Default.setter
    def Default(self, value: bool) -> None:
        self._default = value

    @property
    def Name(self) -> str:
        """
        the name of the calendar, for example, Gregorian.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['Calendar']
