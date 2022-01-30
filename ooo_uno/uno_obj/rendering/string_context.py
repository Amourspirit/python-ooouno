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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class StringContext(object):
        """
        Struct Class

        Collection of string-related arguments used on all canvas text interfaces.
        
        A possibly much larger string than later rendered is necessary here, because in several languages, glyph selection is context dependent.
        
        **since**
        
            OOo 2.0

        See Also:
            `API StringContext <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1StringContext.html>`_


        Note:
            | At runtime StringContext will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | StringContext is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Length: typing.Optional[int] = None, StartPosition: typing.Optional[int] = None, Text: typing.Optional[str] = None):
            self._length = Length
            self._start_position = StartPosition
            self._text = Text

        @property
        def Length(self) -> int:
            """
            Length of the substring to actually use.
            
            Must be within the range [0,INTMAX].
            """
            return self._length
        
        @Length.setter
        def Length(self, value: int) -> None:
            self._length = value

        @property
        def StartPosition(self) -> int:
            """
            Start position within the string.
            
            The first character has index 0.
            """
            return self._start_position
        
        @StartPosition.setter
        def StartPosition(self, value: int) -> None:
            self._start_position = value

        @property
        def Text(self) -> str:
            """
            The complete text, from which a subset is selected by the parameters below.
            """
            return self._text
        
        @Text.setter
        def Text(self, value: str) -> None:
            self._text = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global StringContext
        order = ('Length', 'StartPosition', 'Text')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.rendering.StringContext')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        StringContext = _struct_init

    _dynamic_struct()

__all__ = ['StringContext']
