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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import AddressConvention as AddressConvention
else:
    from ...lo.sheet.address_convention import AddressConvention as AddressConvention


class AddressConventionEnum(IntEnum):
    """
    Enum of Const Class AddressConvention

    These constants specify which address convention to use in the formula parser.
    
    Each variation specifies a different cell and cell range address syntax.
    """
    UNSPECIFIED = AddressConvention.UNSPECIFIED
    OOO = AddressConvention.OOO
    XL_A1 = AddressConvention.XL_A1
    XL_R1C1 = AddressConvention.XL_R1C1
    XL_OOX = AddressConvention.XL_OOX
    LOTUS_A1 = AddressConvention.LOTUS_A1

__all__ = ['AddressConvention', 'AddressConventionEnum']