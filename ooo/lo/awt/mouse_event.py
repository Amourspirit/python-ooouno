# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from .input_event import InputEvent as InputEvent_8f520a66
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class MouseEvent(InputEvent_8f520a66):
    """
    Struct Class

    specifies an event from the mouse.
    
    This event is also used for pop-up menu requests on objects. See PopupTrigger for details.

    See Also:
        `API MouseEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1MouseEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.MouseEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.MouseEvent'
    """Literal Constant ``com.sun.star.awt.MouseEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Modifiers: typing.Optional[int] = 0, Buttons: typing.Optional[int] = 0, X: typing.Optional[int] = 0, Y: typing.Optional[int] = 0, ClickCount: typing.Optional[int] = 0, PopupTrigger: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Modifiers (int, optional): Modifiers value.
            Buttons (int, optional): Buttons value.
            X (int, optional): X value.
            Y (int, optional): Y value.
            ClickCount (int, optional): ClickCount value.
            PopupTrigger (bool, optional): PopupTrigger value.
        """

        if isinstance(Source, MouseEvent):
            oth: MouseEvent = Source
            self.Source = oth.Source
            self.Modifiers = oth.Modifiers
            self.Buttons = oth.Buttons
            self.X = oth.X
            self.Y = oth.Y
            self.ClickCount = oth.ClickCount
            self.PopupTrigger = oth.PopupTrigger
            return

        kargs = {
            "Source": Source,
            "Modifiers": Modifiers,
            "Buttons": Buttons,
            "X": X,
            "Y": Y,
            "ClickCount": ClickCount,
            "PopupTrigger": PopupTrigger,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._buttons = kwargs["Buttons"]
        self._x = kwargs["X"]
        self._y = kwargs["Y"]
        self._click_count = kwargs["ClickCount"]
        self._popup_trigger = kwargs["PopupTrigger"]
        inst_keys = ('Buttons', 'X', 'Y', 'ClickCount', 'PopupTrigger')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Buttons(self) -> int:
        """
        contains the pressed mouse buttons.
        
        Zero ore more constants from the com.sun.star.awt.MouseButton group.
        """
        return self._buttons

    @Buttons.setter
    def Buttons(self, value: int) -> None:
        self._buttons = value

    @property
    def X(self) -> int:
        """
        contains the x coordinate location of the mouse.
        """
        return self._x

    @X.setter
    def X(self, value: int) -> None:
        self._x = value

    @property
    def Y(self) -> int:
        """
        contains the y coordinate location of the mouse.
        """
        return self._y

    @Y.setter
    def Y(self, value: int) -> None:
        self._y = value

    @property
    def ClickCount(self) -> int:
        """
        contains the number of mouse clicks associated with event.
        """
        return self._click_count

    @ClickCount.setter
    def ClickCount(self, value: int) -> None:
        self._click_count = value

    @property
    def PopupTrigger(self) -> bool:
        """
        specifies if this event is a pop-up menu trigger event.
        
        If this member is TRUE, the event describes a request for a pop-up menu, also known as context menu, on an object.
        
        In this case, X and Y describe the position where the request was issued. If those members are -1, then the request was issued using the keyboard, by pressing the operating-system dependent key combination for this purpose.
        """
        return self._popup_trigger

    @PopupTrigger.setter
    def PopupTrigger(self, value: bool) -> None:
        self._popup_trigger = value


__all__ = ['MouseEvent']
