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
from .open_command_argument2 import OpenCommandArgument2 as OpenCommandArgument2_9210e08
import typing
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class OpenCommandArgument3(OpenCommandArgument2_9210e08):
        """
        Struct Class

        Extended argument for commands like \"open\".
        
        We're extending OpenCommandArgument even more, to provide some opening flags on to webdav.

        See Also:
            `API OpenCommandArgument3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument3.html>`_


        Note:
            | At runtime OpenCommandArgument3 will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | OpenCommandArgument3 is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, OpeningFlags: 'typing.Optional[typing.List[NamedValue_a37a0af3]]' = None):
            self._opening_flags = OpeningFlags

        @property
        def OpeningFlags(self) -> 'typing.List[NamedValue_a37a0af3]':
            """
            Flags to use for opening.
            
            WebDav e.g. uses \"KeepAlive\" to enable/disable the respective http feature.
            """
            return self._opening_flags
        
        @OpeningFlags.setter
        def OpeningFlags(self, value: 'typing.List[NamedValue_a37a0af3]') -> None:
            self._opening_flags = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global OpenCommandArgument3
        order = ('OpeningFlags',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.OpenCommandArgument3')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        OpenCommandArgument3 = _struct_init

    _dynamic_struct()

__all__ = ['OpenCommandArgument3']
