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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..beans.named_value import NamedValue as NamedValue_a37a0af3


class ControlCommand(object):
    """
    Struct Class

    describes a command which can be send to a generic toolbar control.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API ControlCommand <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1ControlCommand.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.ControlCommand'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.ControlCommand'
    """Literal Constant ``com.sun.star.frame.ControlCommand``"""

    def __init__(self, Arguments: typing.Tuple[NamedValue_a37a0af3, ...] = UNO_NONE, Command: str = '') -> None:
        """
        Constructor

        Other Arguments:
            ``Arguments`` can be another ``ControlCommand`` instance,
                in which case other named args are ignored.

        Arguments:
            Arguments (Tuple[NamedValue, ...], optional): Arguments value
            Command (str, optional): Command value
        """
        if isinstance(Arguments, ControlCommand):
            oth: ControlCommand = Arguments
            self._arguments = oth.Arguments
            self._command = oth.Command
            return
        else:
            if Arguments is UNO_NONE:
                self._arguments = None
            else:
                self._arguments = Arguments
            self._command = Command



    @property
    def Arguments(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        specifies a sequence of named values which are used as argument for the command.
        
        The number and type of arguments depend on the command and control.
        """
        return self._arguments
    
    @Arguments.setter
    def Arguments(self, value: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        self._arguments = value

    @property
    def Command(self) -> str:
        """
        specifies the command which should be processed by the toolbar control.
        """
        return self._command
    
    @Command.setter
    def Command(self, value: str) -> None:
        self._command = value


__all__ = ['ControlCommand']