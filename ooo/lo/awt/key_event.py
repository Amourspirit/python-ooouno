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
from ooo.oenv import UNO_NONE
from .input_event import InputEvent as InputEvent_8f520a66
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class KeyEvent(InputEvent_8f520a66):
    """
    Struct Class

    specifies a key event.

    See Also:
        `API KeyEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1KeyEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.KeyEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.KeyEvent'
    """Literal Constant ``com.sun.star.awt.KeyEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Modifiers: typing.Optional[int] = 0, KeyCode: typing.Optional[int] = 0, KeyChar: typing.Optional[str] = '\u0000', KeyFunc: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Modifiers (int, optional): Modifiers value.
            KeyCode (int, optional): KeyCode value.
            KeyChar (str, optional): KeyChar value.
            KeyFunc (int, optional): KeyFunc value.
        """
        kargs = {
            "Source": Source,
            "Modifiers": Modifiers,
            "KeyCode": KeyCode,
            "KeyChar": KeyChar,
            "KeyFunc": KeyFunc,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._key_code = kwargs["KeyCode"]
        self._key_char = kwargs["KeyChar"]
        self._key_func = kwargs["KeyFunc"]
        inst_keys = ('KeyCode', 'KeyChar', 'KeyFunc')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def KeyCode(self) -> int:
        """
        contains the integer code representing the key of the event.
        
        This is a constant from the constant group Key.
        """
        return self._key_code
    
    @KeyCode.setter
    def KeyCode(self, value: int) -> None:
        self._key_code = value

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
    def KeyFunc(self) -> int:
        """
        contains the function type of the key event.
        
        This is a constant from the constant group KeyFunction.
        """
        return self._key_func
    
    @KeyFunc.setter
    def KeyFunc(self, value: int) -> None:
        self._key_func = value


__all__ = ['KeyEvent']
