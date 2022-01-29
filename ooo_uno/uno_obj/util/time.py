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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class Time(object):
    """
    Struct Class

    represents a time value.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API Time <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Time.html>`_


    Note:
        | At runtime Time will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | Time is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Hours: typing.Optional[int] = None, IsUTC: typing.Optional[bool] = None, Minutes: typing.Optional[int] = None, NanoSeconds: typing.Optional[int] = None, Seconds: typing.Optional[int] = None):
        self._hours = Hours
        self._is_utc = IsUTC
        self._minutes = Minutes
        self._nano_seconds = NanoSeconds
        self._seconds = Seconds

    @property
    def Hours(self) -> int:
        """
        contains the hour (0-23).
        """
        return self._hours
    
    @Hours.setter
    def Hours(self, value: int) -> None:
        self._hours = value

    @property
    def IsUTC(self) -> bool:
        """
        true: time zone is UTC false: unknown time zone.
        
        **since**
        
            LibreOffice 4.1
        """
        return self._is_utc
    
    @IsUTC.setter
    def IsUTC(self, value: bool) -> None:
        self._is_utc = value

    @property
    def Minutes(self) -> int:
        """
        contains the minutes (0-59).
        """
        return self._minutes
    
    @Minutes.setter
    def Minutes(self, value: int) -> None:
        self._minutes = value

    @property
    def NanoSeconds(self) -> int:
        """
        contains the nanoseconds (0 - 999 999 999).
        """
        return self._nano_seconds
    
    @NanoSeconds.setter
    def NanoSeconds(self, value: int) -> None:
        self._nano_seconds = value

    @property
    def Seconds(self) -> int:
        """
        contains the seconds (0-59).
        """
        return self._seconds
    
    @Seconds.setter
    def Seconds(self, value: int) -> None:
        self._seconds = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global Time
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Hours', 'IsUTC', 'Minutes', 'NanoSeconds', 'Seconds')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.util.Time')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Time = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['Time']
