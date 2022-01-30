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
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class CalendarItem2(CalendarItem_a86c0af1):
        """
        Struct Class

        One entry in a calendar, for example, a day of week or a month or an era.
        
        Derived from com.sun.star.i18n.CalendarItem this provides an additional member for narrow names.
        
        **since**
        
            LibreOffice 3.5

        See Also:
            `API CalendarItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1CalendarItem2.html>`_


        Note:
            | At runtime CalendarItem2 will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | CalendarItem2 is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, NarrowName: typing.Optional[str] = None):
            self._narrow_name = NarrowName

        @property
        def NarrowName(self) -> str:
            """
            The narrow name, for example, \"S\" for Sunday or \"J\" for January.
            """
            return self._narrow_name
        
        @NarrowName.setter
        def NarrowName(self, value: str) -> None:
            self._narrow_name = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global CalendarItem2
        order = ('NarrowName',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.i18n.CalendarItem2')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        CalendarItem2 = _struct_init

    _dynamic_struct()

__all__ = ['CalendarItem2']
