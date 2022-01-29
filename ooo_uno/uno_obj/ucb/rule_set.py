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
# Libre Office Version: 7.2
import os
import typing
if typing.TYPE_CHECKING:
    from .rule import Rule as Rule_571307da
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class RuleSet(object):
    """
    Struct Class

    describes a set of Rules.
    
    A RuleSet is applied to a folder. It consists of a sequence of rules. Each rule consists of a sequence of RuleTerms describing the objects to which the rule should by applied and the RuleAction which should be performed on the matching objects.

    See Also:
        `API RuleSet <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RuleSet.html>`_


    Note:
        | At runtime RuleSet will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | RuleSet is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, HandleFolder: typing.Optional[bool] = None, Rules: 'typing.Optional[typing.List[Rule_571307da]]' = None):
        self._handle_folder = HandleFolder
        self._rules = Rules

    @property
    def HandleFolder(self) -> bool:
        """
        is a flag indicating whether the rules apply to folders, too.
        """
        return self._handle_folder
    
    @HandleFolder.setter
    def HandleFolder(self, value: bool) -> None:
        self._handle_folder = value

    @property
    def Rules(self) -> 'typing.List[Rule_571307da]':
        """
        contains a number of rules.
        """
        return self._rules
    
    @Rules.setter
    def Rules(self, value: 'typing.List[Rule_571307da]') -> None:
        self._rules = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global RuleSet
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('HandleFolder', 'Rules')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.RuleSet')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        RuleSet = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['RuleSet']
