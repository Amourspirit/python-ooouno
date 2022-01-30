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
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class Command(object):
        """
        Struct Class

        contains a command.

        See Also:
            `API Command <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Command.html>`_


        Note:
            | At runtime Command will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | Command is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Argument: typing.Optional[object] = None, Handle: typing.Optional[int] = None, Name: typing.Optional[str] = None):
            self._argument = Argument
            self._handle = Handle
            self._name = Name

        @property
        def Argument(self) -> object:
            """
            contains the argument of the command
            """
            return self._argument
        
        @Argument.setter
        def Argument(self, value: object) -> None:
            self._argument = value

        @property
        def Handle(self) -> int:
            """
            contains an implementation specific handle for the command.
            
            It must be -1 if the implementation has no handle. 0 is a valid command handle.
            """
            return self._handle
        
        @Handle.setter
        def Handle(self, value: int) -> None:
            self._handle = value

        @property
        def Name(self) -> str:
            """
            contains the name of the command.
            """
            return self._name
        
        @Name.setter
        def Name(self, value: str) -> None:
            self._name = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global Command
        order = ('Argument', 'Handle', 'Name')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.Command')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Command = _struct_init

    _dynamic_struct()

__all__ = ['Command']
