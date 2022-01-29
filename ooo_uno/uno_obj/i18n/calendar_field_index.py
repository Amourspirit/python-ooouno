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
from ooo_uno.base.const import ConstIntBase


class CalendarFieldIndex(ConstIntBase):
    """
    Field indices to be passed to various XCalendar methods.
    
    Field is writable only if marked both Get/Set.
    
    ZONE_OFFSET and DST_OFFSET cooperate such that both values are added, for example, ZoneOffset=1*60 and DstOffset=1*60 results in a time difference of GMT+2. The calculation in minutes is GMT = LocalTime - ZoneOffset - DstOffset
    
    With introduction of ZONE_OFFSET_SECOND_MILLIS and DST_OFFSET_SECOND_MILLIS the exact calculation in milliseconds is GMT = LocalTime
    
    **since**
    
        OOo 3.1

    See Also:
        `API CalendarFieldIndex <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1CalendarFieldIndex.html>`_
    """
    AM_PM = 0
    """
    Get AmPmValue.
    """
    DAY_OF_MONTH = 1
    """
    Get/Set day of month [1-31].
    """
    DAY_OF_WEEK = 2
    """
    Get day of week [0-6].
    """
    DAY_OF_YEAR = 3
    """
    Get day of year.
    """
    DST_OFFSET = 4
    """
    Get daylight saving time offset in minutes, e.g.
    
    [0*60..1*60]
    
    The DST offset value depends on the actual date set at the calendar and is determined according to the timezone rules of the locale used with the calendar.
    
    Note that there is a bug in OpenOffice.org 1.0 / StarOffice 6.0 that prevents interpreting this value correctly.
    """
    HOUR = 5
    """
    Get/Set hour [0-23].
    """
    MINUTE = 6
    """
    Get/Set minute [0-59].
    """
    SECOND = 7
    """
    Get/Set second [0-59].
    """
    MILLISECOND = 8
    """
    Get/Set milliseconds [0-999].
    """
    WEEK_OF_MONTH = 9
    """
    Get week of month.
    """
    WEEK_OF_YEAR = 10
    """
    Get week of year.
    """
    YEAR = 11
    """
    Get/Set year.
    """
    MONTH = 12
    """
    Get/Set month [0-...].
    
    Note that the maximum value is not necessarily 11 for December but depends on the calendar used instead.
    """
    ERA = 13
    """
    Get/Set era, for example, 0:= Before Christ, 1:= After Christ.
    """
    ZONE_OFFSET = 14
    """
    Get/Set time zone offset in minutes, e.g. [-14*60..14*60].
    """
    FIELD_COUNT = 15
    """
    Total number of fields for < OOo 3.1.
    """
    ZONE_OFFSET_SECOND_MILLIS = 15
    """
    Get/Set additional offset in milliseconds that adds to the value of ZONE_OFFSET.
    
    This may be necessary to correctly interpret historical timezone data that consists of fractions of minutes, e.g. seconds. 1 minute == 60000 milliseconds.
    
    **since**
    
        OOo 3.1
    """
    DST_OFFSET_SECOND_MILLIS = 16
    """
    Get additional offset in milliseconds that adds to the value of DST_OFFSET.
    
    This may be necessary to correctly interpret historical timezone data that consists of fractions of minutes, e.g. seconds. 1 minute == 60000 milliseconds.
    
    **since**
    
        OOo 3.1
    """
    FIELD_COUNT2 = 17
    """
    Total number of fields as of OOo 3.1.
    
    **since**
    
        OOo 3.1
    """

