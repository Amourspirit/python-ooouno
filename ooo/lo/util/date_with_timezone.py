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
import typing
if typing.TYPE_CHECKING:
    from .date import Date as Date_60040844


class DateWithTimezone(object):
    """
    Struct Class

    represents a date value with time zone.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateWithTimezone <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateWithTimezone.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.DateWithTimezone'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.DateWithTimezone'
    """Literal Constant ``com.sun.star.util.DateWithTimezone``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DateWithTimezone`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DateWithTimezone``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            DateInTZ (Date, optional): DateInTZ value
            Timezone (int, optional): Timezone value
        """
        self._date_in_tz = None
        self._timezone = None

        key_order = ('DateInTZ', 'Timezone')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DateWithTimezone):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DateWithTimezone.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def DateInTZ(self) -> 'Date_60040844':
        """
        the date.
        """
        return self._date_in_tz
    
    @DateInTZ.setter
    def DateInTZ(self, value: 'Date_60040844') -> None:
        self._date_in_tz = value

    @property
    def Timezone(self) -> int:
        """
        contains the time zone, as signed offset in minutes from UTC, that is east of UTC, that is the amount of minutes that should be added to UTC time to obtain time in that timezone.
        """
        return self._timezone
    
    @Timezone.setter
    def Timezone(self, value: int) -> None:
        self._timezone = value


__all__ = ['DateWithTimezone']
