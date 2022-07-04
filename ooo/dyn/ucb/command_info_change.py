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
# Libre Office Version: 7.3
# Namespace: com.sun.star.ucb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CommandInfoChange(metaclass=UnoConstMeta, type_name="com.sun.star.ucb.CommandInfoChange", name_space="com.sun.star.ucb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ucb.CommandInfoChange``"""
        pass

    class CommandInfoChangeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ucb.CommandInfoChange", name_space="com.sun.star.ucb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ucb.CommandInfoChange`` as Enum values"""
        pass

else:
    from ...lo.ucb.command_info_change import CommandInfoChange as CommandInfoChange

    class CommandInfoChangeEnum(IntEnum):
        """
        Enum of Const Class CommandInfoChange

        specifies reasons for sending CommandInfoChangeEvents.
        """
        COMMAND_INSERTED = CommandInfoChange.COMMAND_INSERTED
        """
        A command was inserted into a XCommandInfo.
        """
        COMMAND_REMOVED = CommandInfoChange.COMMAND_REMOVED
        """
        A command was removed from a XCommandInfo.
        """

__all__ = ['CommandInfoChange', 'CommandInfoChangeEnum']
