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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .rule import Rule as Rule_571307da


class RuleSet(object):
    """
    Struct Class

    describes a set of Rules.
    
    A RuleSet is applied to a folder. It consists of a sequence of rules. Each rule consists of a sequence of RuleTerms describing the objects to which the rule should by applied and the RuleAction which should be performed on the matching objects.

    See Also:
        `API RuleSet <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RuleSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.RuleSet'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.RuleSet'
    """Literal Constant ``com.sun.star.ucb.RuleSet``"""

    def __init__(self, Rules: typing.Optional[typing.Tuple[Rule_571307da, ...]] = (), HandleFolder: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Rules (typing.Tuple[Rule, ...], optional): Rules value.
            HandleFolder (bool, optional): HandleFolder value.
        """
        super().__init__()

        if isinstance(Rules, RuleSet):
            oth: RuleSet = Rules
            self.Rules = oth.Rules
            self.HandleFolder = oth.HandleFolder
            return

        kargs = {
            "Rules": Rules,
            "HandleFolder": HandleFolder,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._rules = kwargs["Rules"]
        self._handle_folder = kwargs["HandleFolder"]


    @property
    def Rules(self) -> typing.Tuple[Rule_571307da, ...]:
        """
        contains a number of rules.
        """
        return self._rules
    
    @Rules.setter
    def Rules(self, value: typing.Tuple[Rule_571307da, ...]) -> None:
        self._rules = value

    @property
    def HandleFolder(self) -> bool:
        """
        is a flag indicating whether the rules apply to folders, too.
        """
        return self._handle_folder
    
    @HandleFolder.setter
    def HandleFolder(self, value: bool) -> None:
        self._handle_folder = value


__all__ = ['RuleSet']
