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

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``Date`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``Date``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Day (int, optional): Day value
            Month (int, optional): Month value
            Year (int, optional): Year value
        """
        self._day = None
        self._month = None
        self._year = None

        key_order = ('Day', 'Month', 'Year')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], Date):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("Date.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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
