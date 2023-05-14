# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .rule_term import RuleTerm as RuleTerm_7a4b0972


class Rule(object):
    """
    Struct Class

    describes a rule that can be applies to a number of objects.
    
    A rule consists of a sequence of RuleTerms describing the objects to which the rule should be applied, the RuleAction which should be used on the matching objects, and a parameter.

    See Also:
        `API Rule <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Rule.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.Rule'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.Rule'
    """Literal Constant ``com.sun.star.ucb.Rule``"""

    def __init__(self, Terms: typing.Optional[typing.Tuple[RuleTerm_7a4b0972, ...]] = (), Parameter: typing.Optional[str] = '', Action: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Terms (typing.Tuple[RuleTerm, ...], optional): Terms value.
            Parameter (str, optional): Parameter value.
            Action (int, optional): Action value.
        """
        super().__init__()

        if isinstance(Terms, Rule):
            oth: Rule = Terms
            self.Terms = oth.Terms
            self.Parameter = oth.Parameter
            self.Action = oth.Action
            return

        kargs = {
            "Terms": Terms,
            "Parameter": Parameter,
            "Action": Action,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._terms = kwargs["Terms"]
        self._parameter = kwargs["Parameter"]
        self._action = kwargs["Action"]


    @property
    def Terms(self) -> typing.Tuple[RuleTerm_7a4b0972, ...]:
        """
        the rule terms describing the objects to which the rule should be applied.
        """
        return self._terms

    @Terms.setter
    def Terms(self, value: typing.Tuple[RuleTerm_7a4b0972, ...]) -> None:
        self._terms = value

    @property
    def Parameter(self) -> str:
        """
        Some RuleActions require a parameter.
        """
        return self._parameter

    @Parameter.setter
    def Parameter(self, value: str) -> None:
        self._parameter = value

    @property
    def Action(self) -> int:
        """
        the action to perform on the matching objects.
        
        The value can be one of the RuleAction constants.
        """
        return self._action

    @Action.setter
    def Action(self, value: int) -> None:
        self._action = value


__all__ = ['Rule']
