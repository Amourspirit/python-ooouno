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
from .time import Time as Time_604e0855


class TimeWithTimezone(object):
    """
    Struct Class

    represents a combined time value with time zone.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API TimeWithTimezone <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1TimeWithTimezone.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.TimeWithTimezone'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.TimeWithTimezone'
    """Literal Constant ``com.sun.star.util.TimeWithTimezone``"""

    def __init__(self, TimeInTZ: Time_604e0855 = UNO_NONE, Timezone: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``TimeInTZ`` can be another ``TimeWithTimezone`` instance,
                in which case other named args are ignored.

        Arguments:
            TimeInTZ (Time, optional): TimeInTZ value
            Timezone (int, optional): Timezone value
        """
        if isinstance(TimeInTZ, TimeWithTimezone):
            oth: TimeWithTimezone = TimeInTZ
            self._time_in_tz = oth.TimeInTZ
            self._timezone = oth.Timezone
            return
        else:
            if TimeInTZ is UNO_NONE:
                self._time_in_tz = Time_604e0855()
            else:
                self._time_in_tz = TimeInTZ
            self._timezone = Timezone



    @property
    def TimeInTZ(self) -> Time_604e0855:
        """
        the time (in TimeZone)
        """
        return self._time_in_tz
    
    @TimeInTZ.setter
    def TimeInTZ(self, value: Time_604e0855) -> None:
        self._time_in_tz = value

    @property
    def Timezone(self) -> int:
        """
        contains the time zone, as signed offset in minutes from UTC, that is east of UTC, that is the amount of minutes that should be added to UTC time to obtain the time in that timezone.
        
        To obtain UTC time from TimeInTZ, you need to subtract TimeZone minutes.
        """
        return self._timezone
    
    @Timezone.setter
    def Timezone(self, value: int) -> None:
        self._timezone = value


__all__ = ['TimeWithTimezone']
