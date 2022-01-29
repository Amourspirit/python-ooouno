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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class KeyStroke(object):
    """
    Struct Class

    Describes a key stroke for hotkeys etc.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API KeyStroke <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1KeyStroke.html>`_


    Note:
        | At runtime KeyStroke will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | KeyStroke is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, KeyChar: typing.Optional[str] = None, KeyCode: typing.Optional[int] = None, KeyFunc: typing.Optional[int] = None, Modifiers: typing.Optional[int] = None):
        self._key_char = KeyChar
        self._key_code = KeyCode
        self._key_func = KeyFunc
        self._modifiers = Modifiers

    @property
    def KeyChar(self) -> str:
        """
        contains the Unicode character generated by this event or 0.
        """
        return self._key_char
    
    @KeyChar.setter
    def KeyChar(self, value: str) -> None:
        self._key_char = value

    @property
    def KeyCode(self) -> int:
        """
        contains the integer code representing the key of the event.
        
        This is a constant from the constant group com.sun.star.awt.Key.
        """
        return self._key_code
    
    @KeyCode.setter
    def KeyCode(self, value: int) -> None:
        self._key_code = value

    @property
    def KeyFunc(self) -> int:
        """
        contains the function type of the key event.
        
        This is a constant from the constant group com.sun.star.awt.KeyFunction.
        """
        return self._key_func
    
    @KeyFunc.setter
    def KeyFunc(self, value: int) -> None:
        self._key_func = value

    @property
    def Modifiers(self) -> int:
        """
        contains the modifier keys which were pressed while the event occurred.
        
        Zero or more constants from the group com.sun.star.awt.KeyModifier.
        """
        return self._modifiers
    
    @Modifiers.setter
    def Modifiers(self, value: int) -> None:
        self._modifiers = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global KeyStroke
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('KeyChar', 'KeyCode', 'KeyFunc', 'Modifiers')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.KeyStroke')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        KeyStroke = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['KeyStroke']
