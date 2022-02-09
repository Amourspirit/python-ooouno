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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from .calendar_item import CalendarItem as CalendarItem_a86c0af1


class CalendarItem2(CalendarItem_a86c0af1):
    """
    Struct Class

    One entry in a calendar, for example, a day of week or a month or an era.
    
    Derived from com.sun.star.i18n.CalendarItem this provides an additional member for narrow names.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API CalendarItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1CalendarItem2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.CalendarItem2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.CalendarItem2'
    """Literal Constant ``com.sun.star.i18n.CalendarItem2``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``CalendarItem2`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``CalendarItem2``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            NarrowName (str, optional): NarrowName value
        """
        self._narrow_name = None

        key_order = ('NarrowName',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], CalendarItem2):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("CalendarItem2.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def NarrowName(self) -> str:
        """
        The narrow name, for example, \"S\" for Sunday or \"J\" for January.
        """
        return self._narrow_name
    
    @NarrowName.setter
    def NarrowName(self, value: str) -> None:
        self._narrow_name = value


__all__ = ['CalendarItem2']
