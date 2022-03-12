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
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class Duration(object):
    """
    Struct Class

    represents a duration.
    
    A duration is the difference of 2 DateTimes.
    
    Note that there are no constraints on the ranges of the members, except that every member must be non-negative: for example, a Duration of 400 Days is valid.
    
    **since**
    
        OOo 3.3

    See Also:
        `API Duration <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Duration.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.Duration'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.Duration'
    """Literal Constant ``com.sun.star.util.Duration``"""

    def __init__(self, Negative: typing.Optional[bool] = False, Years: typing.Optional[int] = 0, Months: typing.Optional[int] = 0, Days: typing.Optional[int] = 0, Hours: typing.Optional[int] = 0, Minutes: typing.Optional[int] = 0, Seconds: typing.Optional[int] = 0, NanoSeconds: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Negative (bool, optional): Negative value.
            Years (int, optional): Years value.
            Months (int, optional): Months value.
            Days (int, optional): Days value.
            Hours (int, optional): Hours value.
            Minutes (int, optional): Minutes value.
            Seconds (int, optional): Seconds value.
            NanoSeconds (int, optional): NanoSeconds value.
        """
        super().__init__()
        kargs = {
            "Negative": Negative,
            "Years": Years,
            "Months": Months,
            "Days": Days,
            "Hours": Hours,
            "Minutes": Minutes,
            "Seconds": Seconds,
            "NanoSeconds": NanoSeconds,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._negative = kwargs["Negative"]
        self._years = kwargs["Years"]
        self._months = kwargs["Months"]
        self._days = kwargs["Days"]
        self._hours = kwargs["Hours"]
        self._minutes = kwargs["Minutes"]
        self._seconds = kwargs["Seconds"]
        self._nano_seconds = kwargs["NanoSeconds"]


    @property
    def Negative(self) -> bool:
        """
        explicit sign bit.
        """
        return self._negative
    
    @Negative.setter
    def Negative(self, value: bool) -> None:
        self._negative = value

    @property
    def Years(self) -> int:
        """
        contains the years.
        """
        return self._years
    
    @Years.setter
    def Years(self, value: int) -> None:
        self._years = value

    @property
    def Months(self) -> int:
        """
        contains the months.
        """
        return self._months
    
    @Months.setter
    def Months(self, value: int) -> None:
        self._months = value

    @property
    def Days(self) -> int:
        """
        contains the days.
        """
        return self._days
    
    @Days.setter
    def Days(self, value: int) -> None:
        self._days = value

    @property
    def Hours(self) -> int:
        """
        contains the hours.
        """
        return self._hours
    
    @Hours.setter
    def Hours(self, value: int) -> None:
        self._hours = value

    @property
    def Minutes(self) -> int:
        """
        contains the minutes.
        """
        return self._minutes
    
    @Minutes.setter
    def Minutes(self, value: int) -> None:
        self._minutes = value

    @property
    def Seconds(self) -> int:
        """
        contains the seconds.
        """
        return self._seconds
    
    @Seconds.setter
    def Seconds(self, value: int) -> None:
        self._seconds = value

    @property
    def NanoSeconds(self) -> int:
        """
        contains the nanoseconds.
        """
        return self._nano_seconds
    
    @NanoSeconds.setter
    def NanoSeconds(self, value: int) -> None:
        self._nano_seconds = value


__all__ = ['Duration']
