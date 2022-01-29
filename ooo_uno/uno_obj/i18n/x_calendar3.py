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
from .x_extended_calendar import XExtendedCalendar as XExtendedCalendar_e5480ceb
if typing.TYPE_CHECKING:
    from .calendar2 import Calendar2 as Calendar2_88c10994
    from .calendar_item2 import CalendarItem2 as CalendarItem2_b38f0b23

class XCalendar3(XExtendedCalendar_e5480ceb):
    """
    This interface provides access to locale specific calendar systems.
    
    It is derived from com.sun.star.i18n.XExtendedCalendar and provides additional methods to obtain Calendar2 items that include the possessive genitive case month names and sequences of CalendarItem2 items...
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XCalendar3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XCalendar3.html>`_
    """

    @abstractmethod
    def getDays2(self) -> 'typing.List[CalendarItem2_b38f0b23]':
        """
        returns a sequence of CalendarItem2 describing the day names.
        """
    @abstractmethod
    def getGenitiveMonths2(self) -> 'typing.List[CalendarItem2_b38f0b23]':
        """
        returns a sequence of CalendarItem2 describing the genitive case month names.
        """
    @abstractmethod
    def getLoadedCalendar2(self) -> 'Calendar2_88c10994':
        """
        Get the currently loaded Calendar2.
        """
    @abstractmethod
    def getMonths2(self) -> 'typing.List[CalendarItem2_b38f0b23]':
        """
        returns a sequence of CalendarItem2 describing the month names.
        """
    @abstractmethod
    def getPartitiveMonths2(self) -> 'typing.List[CalendarItem2_b38f0b23]':
        """
        returns a sequence of CalendarItem2 describing the partitive case month names.
        """

__all__ = ['XCalendar3']

