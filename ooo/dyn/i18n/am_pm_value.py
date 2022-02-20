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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import AmPmValue as AmPmValue
    if hasattr(AmPmValue, '_constants') and isinstance(AmPmValue._constants, dict):
        AmPmValue._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        AmPmValue._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.AmPmValue'
        AmPmValue._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global AmPmValueEnum
        ls = [f for f in dir(AmPmValue) if not callable(getattr(AmPmValue, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(AmPmValue, name)
        AmPmValueEnum = IntEnum('AmPmValueEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.am_pm_value import AmPmValue as AmPmValue

    class AmPmValueEnum(IntEnum):
        """
        Enum of Const Class AmPmValue

        Constants for AM/PM used in calls to XCalendar.getDisplayName().
        """
        AM = AmPmValue.AM
        """
        get display name string for AM
        """
        PM = AmPmValue.PM
        """
        get display name string for PM
        """

__all__ = ['AmPmValue', 'AmPmValueEnum']
