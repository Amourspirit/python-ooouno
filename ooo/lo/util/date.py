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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Date(object):
    """
    Struct Class

    represents a date value.
    
    The time zone is unknown.

    See Also:
        `API Date <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Date.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.Date'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.Date'
    """Literal Constant ``com.sun.star.util.Date``"""

    def __init__(self, Day: typing.Optional[int] = 0, Month: typing.Optional[int] = 0, Year: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Day (int, optional): Day value.
            Month (int, optional): Month value.
            Year (int, optional): Year value.
        """
        super().__init__()

        if isinstance(Day, Date):
            oth: Date = Day
            self.Day = oth.Day
            self.Month = oth.Month
            self.Year = oth.Year
            return

        kargs = {
            "Day": Day,
            "Month": Month,
            "Year": Year,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._day = kwargs["Day"]
        self._month = kwargs["Month"]
        self._year = kwargs["Year"]


    @property
    def Day(self) -> int:
        """
        contains the day of month (1-31 or 0 for a void date).
        """
        return self._day
    
    @Day.setter
    def Day(self, value: int) -> None:
        self._day = value

    @property
    def Month(self) -> int:
        """
        contains the month of year (1-12 or 0 for a void date).
        """
        return self._month
    
    @Month.setter
    def Month(self, value: int) -> None:
        self._month = value

    @property
    def Year(self) -> int:
        """
        contains the year.
        """
        return self._year
    
    @Year.setter
    def Year(self, value: int) -> None:
        self._year = value


__all__ = ['Date']
