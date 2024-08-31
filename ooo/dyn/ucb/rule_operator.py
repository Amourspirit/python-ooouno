# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class RuleOperator(metaclass=UnoConstMeta, type_name="com.sun.star.ucb.RuleOperator", name_space="com.sun.star.ucb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ucb.RuleOperator``"""
        pass

    class RuleOperatorEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ucb.RuleOperator", name_space="com.sun.star.ucb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ucb.RuleOperator`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.ucb import RuleOperator as RuleOperator
    else:
        # keep document generators happy
        from ...lo.ucb.rule_operator import RuleOperator as RuleOperator

    class RuleOperatorEnum(IntEnum):
        """
        Enum of Const Class RuleOperator

        These are the possible values for RuleTerm.RuleOperator.
        """
        CONTAINS = RuleOperator.CONTAINS
        """
        \"Contains\" - Object contains RuleTerm.Operand.
        """
        CONTAINSNOT = RuleOperator.CONTAINSNOT
        """
        \"ContainsNot\" - Object does not contain RuleTerm.Operand.
        """
        GREATEREQUAL = RuleOperator.GREATEREQUAL
        """
        \"GreaterEqual\" - Object is greater than or equal to RuleTerm.Operand.
        """
        LESSEQUAL = RuleOperator.LESSEQUAL
        """
        \"LessEqual\" - Object is less than or equal to RuleTerm.Operand.
        """
        EQUAL = RuleOperator.EQUAL
        """
        \"Equal\" - Object is equal to RuleTerm.Operand.
        """
        NOTEQUAL = RuleOperator.NOTEQUAL
        """
        \"NotEqual\" - Object is not equal to RuleTerm.Operand.
        """
        VALUE_TRUE = RuleOperator.VALUE_TRUE
        """
        \"True\" - Object has the value TRUE.
        """
        VALUE_FALSE = RuleOperator.VALUE_FALSE
        """
        \"False\" - Object has the value FALSE.
        """

__all__ = ['RuleOperator', 'RuleOperatorEnum']
