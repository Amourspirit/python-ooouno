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
# Namespace: com.sun.star.sheet
from ooo_uno.base.const import ConstIntBase


class DataPilotFieldGroupBy(ConstIntBase):
    """
    These constants select different types for grouping members of a DataPilot field by date or time.

    See Also:
        `API DataPilotFieldGroupBy <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldGroupBy.html>`_
    """
    SECONDS = 1
    """
    Groups all members of a DataPilot field containing a date/time value by their current value for seconds.
    
    Example: The group :02 will contain all members that contain a time with a seconds value of 2, regardless of the date, hours and minutes of the member, e.g. 2002-Jan-03 00:00:02 or 1999-May-02 12:45:02.
    """
    MINUTES = 2
    """
    Groups all members of a DataPilot field containing a date/time value by their current value for minutes.
    
    Example: The group :02 will contain all members that contain a time with a minutes value of 2, regardless of the date, hours and seconds of the member, e.g. 2002-Jan-03 00:02:00 or 1999-May-02 12:02:45.
    """
    HOURS = 4
    """
    Groups all members of a DataPilot field containing a date/time value by their current value for hours.
    
    Example: The group 02 will contain all members that contain a time with a hour value of 2, regardless of the date, minutes and seconds of the member, e.g. 2002-Jan-03 02:00:00 or 1999-May-02 02:12:45.
    """
    DAYS = 8
    """
    Groups all members of a DataPilot field containing a date/time value by their calendar day, or by ranges of days.
    
    Examples:
    
    See descriptions for XDataPilotFieldGrouping.createDateGroup() for more details about day grouping.
    """
    MONTHS = 16
    """
    Groups all members of a DataPilot field containing a date/time value by their month.
    
    Example: The group Jan will contain all members with a date in the month January, regardless of the year, day, or time of the member, e.g. 2002-Jan-03 00:00:00 or 1999-Jan-02 02:12:45.
    """
    QUARTERS = 32
    """
    Groups all members of a DataPilot field containing a date/time value by their quarter.
    
    Example: The group Q1 will contain all members with a date in the first quarter of a year (i.e. the months January, February, and march), regardless of the year, day, or time of the member, e.g. 2002-Jan-03 00:00:00 or 1999-Mar-02 02:12:45.
    """
    YEARS = 64
    """
    Groups all members of a DataPilot field containing a date/time value by their year.
    
    Example: The group 1999 will contain all members with a date in the year 1999, regardless of the month, day, or time of the member, e.g. 1999-Jan-03 00:00:00 or 1999-May-02 02:12:45.
    """

