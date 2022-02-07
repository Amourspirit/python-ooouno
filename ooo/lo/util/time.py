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


class Time(object):
    """
    Struct Class

    represents a time value.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API Time <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Time.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.Time'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.Time'
    """Literal Constant ``com.sun.star.util.Time``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``Time`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``Time``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            NanoSeconds (int, optional): NanoSeconds value
            Seconds (int, optional): Seconds value
            Minutes (int, optional): Minutes value
            Hours (int, optional): Hours value
            IsUTC (bool, optional): IsUTC value
        """
        self._nano_seconds = None
        self._seconds = None
        self._minutes = None
        self._hours = None
        self._is_utc = None

        key_order = ('NanoSeconds', 'Seconds', 'Minutes', 'Hours', 'IsUTC')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], Time):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("Time.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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


__all__ = ['Time']
