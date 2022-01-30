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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class AliasProgrammaticPair(object):
        """
        Struct Class

        represents an entry from a component which implements the XLocalizedAliases.

        See Also:
            `API AliasProgrammaticPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1AliasProgrammaticPair.html>`_


        Note:
            | At runtime AliasProgrammaticPair will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | AliasProgrammaticPair is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Alias: typing.Optional[str] = None, ProgrammaticName: typing.Optional[str] = None):
            self._alias = Alias
            self._programmatic_name = ProgrammaticName

        @property
        def Alias(self) -> str:
            """
            determines the name which is registered as an alias for a programmatic name.
            """
            return self._alias
        
        @Alias.setter
        def Alias(self, value: str) -> None:
            self._alias = value

        @property
        def ProgrammaticName(self) -> str:
            """
            determines which programmatic name belongs to the alias.
            """
            return self._programmatic_name
        
        @ProgrammaticName.setter
        def ProgrammaticName(self, value: str) -> None:
            self._programmatic_name = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global AliasProgrammaticPair
        order = ('Alias', 'ProgrammaticName')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.util.AliasProgrammaticPair')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        AliasProgrammaticPair = _struct_init

    _dynamic_struct()

__all__ = ['AliasProgrammaticPair']
