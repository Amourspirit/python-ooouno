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
# Namespace: com.sun.star.sdb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdb import BooleanComparisonMode as BooleanComparisonMode
    if hasattr(BooleanComparisonMode, '_constants') and isinstance(BooleanComparisonMode._constants, dict):
        BooleanComparisonMode._constants['__ooo_ns__'] = 'com.sun.star.sdb'
        BooleanComparisonMode._constants['__ooo_full_ns__'] = 'com.sun.star.sdb.BooleanComparisonMode'
        BooleanComparisonMode._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global BooleanComparisonModeEnum
        ls = [f for f in dir(BooleanComparisonMode) if not callable(getattr(BooleanComparisonMode, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(BooleanComparisonMode, name)
        BooleanComparisonModeEnum = IntEnum('BooleanComparisonModeEnum', _dict)
    build_enum()
else:
    from ...lo.sdb.boolean_comparison_mode import BooleanComparisonMode as BooleanComparisonMode

    class BooleanComparisonModeEnum(IntEnum):
        """
        Enum of Const Class BooleanComparisonMode

        specifies different mode how boolean comparison predicates are to be generated by a SingleSelectQueryComposer.
        """
        EQUAL_INTEGER = BooleanComparisonMode.EQUAL_INTEGER
        """
        denotes the default comparison
        
        Most databases support comparing boolean expressions or column values directly with integer values: column = 0 respectively column = 1.
        """
        IS_LITERAL = BooleanComparisonMode.IS_LITERAL
        """
        requires to use IS boolean_literal for boolean comparison.
        
        That is, the generated comparison predicates will be column IS TRUE resp. column IS FALSE.
        """
        EQUAL_LITERAL = BooleanComparisonMode.EQUAL_LITERAL
        """
        requires to use = boolean_literal for boolean comparison.
        
        That is, the generated comparison predicates will be column = TRUE resp. column = FALSE.
        """
        ACCESS_COMPAT = BooleanComparisonMode.ACCESS_COMPAT
        """
        requires to use an Microsoft Access compatible syntax for boolean comparison.
        """

__all__ = ['BooleanComparisonMode', 'BooleanComparisonModeEnum']
