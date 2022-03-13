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
from .mouse_event import MouseEvent as MouseEvent_8f430a5f
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class EnhancedMouseEvent(MouseEvent_8f430a5f):
    """
    Struct Class

    specifies an event from the mouse.
    
    **since**
    
        OOo 2.0

    See Also:
        `API EnhancedMouseEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EnhancedMouseEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.EnhancedMouseEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.EnhancedMouseEvent'
    """Literal Constant ``com.sun.star.awt.EnhancedMouseEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Modifiers: typing.Optional[int] = 0, Buttons: typing.Optional[int] = 0, X: typing.Optional[int] = 0, Y: typing.Optional[int] = 0, ClickCount: typing.Optional[int] = 0, PopupTrigger: typing.Optional[bool] = False, Target: typing.Optional[XInterface_8f010a43] = None) -> None:
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
            Target (XInterface, optional): Target value.
        """

        if isinstance(Source, EnhancedMouseEvent):
            oth: EnhancedMouseEvent = Source
            self.Source = oth.Source
            self.Modifiers = oth.Modifiers
            self.Buttons = oth.Buttons
            self.X = oth.X
            self.Y = oth.Y
            self.ClickCount = oth.ClickCount
            self.PopupTrigger = oth.PopupTrigger
            self.Target = oth.Target
            return

        kargs = {
            "Source": Source,
            "Modifiers": Modifiers,
            "Buttons": Buttons,
            "X": X,
            "Y": Y,
            "ClickCount": ClickCount,
            "PopupTrigger": PopupTrigger,
            "Target": Target,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._target = kwargs["Target"]
        inst_keys = ('Target',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Target(self) -> XInterface_8f010a43:
        """
        contains the object on the location of the mouse.
        """
        return self._target
    
    @Target.setter
    def Target(self, value: XInterface_8f010a43) -> None:
        self._target = value


__all__ = ['EnhancedMouseEvent']
