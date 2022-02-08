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
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import DataResultFlags
else:
    from ...lo.sheet.data_result_flags import DataResultFlags as DataResultFlags


class DataResultFlagsEnum(IntFlag):
    """
    Enum of Const Class DataResultFlags

    used to specify the result type of one element in the data pilot data array.
    """
    HASDATA = DataResultFlags.HASDATA
    """
    The element contains data.
    """
    SUBTOTAL = DataResultFlags.SUBTOTAL
    """
    The element contains a subtotal.
    """
    ERROR = DataResultFlags.ERROR
    """
    The element has an error.
    """

__all__ = ['DataResultFlags', 'DataResultFlagsEnum']
