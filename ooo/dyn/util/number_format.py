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
# Namespace: com.sun.star.util
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.util import NumberFormat as NumberFormat
else:
    from ...lo.util.number_format import NumberFormat as NumberFormat


class NumberFormatEnum(IntEnum):
    """
    Enum of Const Class NumberFormat

    contains constants that are used to specify the type of a number format.
    """
    ALL = NumberFormat.ALL
    """
    selects all number formats.
    """
    DEFINED = NumberFormat.DEFINED
    """
    selects only user-defined number formats.
    """
    DATE = NumberFormat.DATE
    """
    selects date formats.
    """
    TIME = NumberFormat.TIME
    """
    selects time formats.
    """
    CURRENCY = NumberFormat.CURRENCY
    """
    selects currency formats.
    """
    NUMBER = NumberFormat.NUMBER
    """
    selects decimal number formats.
    """
    SCIENTIFIC = NumberFormat.SCIENTIFIC
    """
    selects scientific number formats.
    """
    FRACTION = NumberFormat.FRACTION
    """
    selects number formats for fractions.
    """
    PERCENT = NumberFormat.PERCENT
    """
    selects percentage number formats.
    """
    TEXT = NumberFormat.TEXT
    """
    selects text number formats.
    """
    DATETIME = NumberFormat.DATETIME
    """
    selects number formats which contain date and time.
    """
    LOGICAL = NumberFormat.LOGICAL
    """
    selects boolean number formats.
    """
    UNDEFINED = NumberFormat.UNDEFINED
    """
    is used as a return value if no format exists.
    """
    EMPTY = NumberFormat.EMPTY
    DURATION = NumberFormat.DURATION

__all__ = ['NumberFormat', 'NumberFormatEnum']