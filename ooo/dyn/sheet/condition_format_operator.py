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
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class ConditionFormatOperator(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.ConditionFormatOperator", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.ConditionFormatOperator``"""
        pass

    class ConditionFormatOperatorEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.ConditionFormatOperator", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.ConditionFormatOperator`` as Enum values"""
        pass

else:
    from ...lo.sheet.condition_format_operator import ConditionFormatOperator as ConditionFormatOperator

    class ConditionFormatOperatorEnum(IntEnum):
        """
        Enum of Const Class ConditionFormatOperator

        """
        EQUAL = ConditionFormatOperator.EQUAL
        LESS = ConditionFormatOperator.LESS
        GREATER = ConditionFormatOperator.GREATER
        LESS_EQUAL = ConditionFormatOperator.LESS_EQUAL
        GREATER_EQUAL = ConditionFormatOperator.GREATER_EQUAL
        NOT_EQUAL = ConditionFormatOperator.NOT_EQUAL
        BETWEEN = ConditionFormatOperator.BETWEEN
        NOT_BETWEEN = ConditionFormatOperator.NOT_BETWEEN
        DUPLICATE = ConditionFormatOperator.DUPLICATE
        UNIQUE = ConditionFormatOperator.UNIQUE
        TOP_N_ELEMENTS = ConditionFormatOperator.TOP_N_ELEMENTS
        BOTTOM_N_ELEMENTS = ConditionFormatOperator.BOTTOM_N_ELEMENTS
        TOP_N_PERCENT = ConditionFormatOperator.TOP_N_PERCENT
        BOTTOM_N_PERCENT = ConditionFormatOperator.BOTTOM_N_PERCENT
        ABOVE_AVERAGE = ConditionFormatOperator.ABOVE_AVERAGE
        BELOW_AVERAGE = ConditionFormatOperator.BELOW_AVERAGE
        ABOVE_EQUAL_AVERAGE = ConditionFormatOperator.ABOVE_EQUAL_AVERAGE
        BELOW_EQUAL_AVERAGE = ConditionFormatOperator.BELOW_EQUAL_AVERAGE
        ERROR = ConditionFormatOperator.ERROR
        NO_ERROR = ConditionFormatOperator.NO_ERROR
        BEGINS_WITH = ConditionFormatOperator.BEGINS_WITH
        ENDS_WITH = ConditionFormatOperator.ENDS_WITH
        CONTAINS = ConditionFormatOperator.CONTAINS
        NOT_CONTAINS = ConditionFormatOperator.NOT_CONTAINS
        EXPRESSION = ConditionFormatOperator.EXPRESSION

__all__ = ['ConditionFormatOperator', 'ConditionFormatOperatorEnum']
