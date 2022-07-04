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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from .x_calendar3 import XCalendar3 as XCalendar3_927a09ed
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XCalendar4(XCalendar3_927a09ed):
    """
    This interface provides access to locale specific calendar systems.
    
    It is derived from com.sun.star.i18n.XCalendar3 and provides additional methods to set and get the local time.
    
    **since**
    
        LibreOffice 5.0

    See Also:
        `API XCalendar4 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XCalendar4.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XCalendar4'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XCalendar4'

    @abstractmethod
    def getLocalDateTime(self) -> float:
        """
        Get the local date/time as an offset to the start of the calendar at 1-Jan-1970 00:00.
        
        The integer part represents the number of days passed since start date. The fractional part represents fractions of a day, thus 0.5 means 12 hours.
        
        The actual timezone and daylight saving time offsets effective at the given date and time are considered and added to the UTC time at the calendar.
        """
        ...
    @abstractmethod
    def loadCalendarTZ(self, uniqueID: str, rLocale: 'Locale_70d308fa', TimeZone: str) -> None:
        """
        Load a specific calendar for the given locale with a given time zone.
        
        **since**
        
            LibreOffice 6.3
        """
        ...
    @abstractmethod
    def loadDefaultCalendarTZ(self, rLocale: 'Locale_70d308fa', TimeZone: str) -> None:
        """
        Load the default calendar for the given locale with a given time zone.
        
        **since**
        
            LibreOffice 6.3
        """
        ...
    @abstractmethod
    def setLocalDateTime(self, TimeInDays: float) -> None:
        """
        Set the local date/time as an offset to the start of the calendar at 1-Jan-1970 00:00.
        
        The integer part represents the number of days passed since start date. The fractional part represents fractions of a day, thus 0.5 means 12 hours.
        
        The actual timezone and daylight saving time offsets effective at the given date and time are considered and subtracted before setting the UTC time at the calendar.
        """
        ...

__all__ = ['XCalendar4']

