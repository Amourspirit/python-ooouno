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
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class EndDockingEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an end docking event.

    See Also:
        `API EndDockingEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EndDockingEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.EndDockingEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.EndDockingEvent'
    """Literal Constant ``com.sun.star.awt.EndDockingEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, WindowRectangle: typing.Optional[Rectangle_84b109e9] = UNO_NONE, bFloating: typing.Optional[bool] = False, bCancelled: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            WindowRectangle (Rectangle, optional): WindowRectangle value.
            bFloating (bool, optional): bFloating value.
            bCancelled (bool, optional): bCancelled value.
        """

        if isinstance(Source, EndDockingEvent):
            oth: EndDockingEvent = Source
            self.Source = oth.Source
            self.WindowRectangle = oth.WindowRectangle
            self.bFloating = oth.bFloating
            self.bCancelled = oth.bCancelled
            return

        kargs = {
            "Source": Source,
            "WindowRectangle": WindowRectangle,
            "bFloating": bFloating,
            "bCancelled": bCancelled,
        }
        if kargs["WindowRectangle"] is UNO_NONE:
            kargs["WindowRectangle"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._window_rectangle = kwargs["WindowRectangle"]
        self._b_floating = kwargs["bFloating"]
        self._b_cancelled = kwargs["bCancelled"]
        inst_keys = ('WindowRectangle', 'bFloating', 'bCancelled')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def WindowRectangle(self) -> Rectangle_84b109e9:
        """
        specifies the new bounding rectangle of the window
        """
        return self._window_rectangle
    
    @WindowRectangle.setter
    def WindowRectangle(self, value: Rectangle_84b109e9) -> None:
        self._window_rectangle = value

    @property
    def bFloating(self) -> bool:
        """
        specifies if the window is now floating TRUE or docked FALSE
        """
        return self._b_floating
    
    @bFloating.setter
    def bFloating(self, value: bool) -> None:
        self._b_floating = value

    @property
    def bCancelled(self) -> bool:
        """
        specifies that the docking procedure was canceled
        """
        return self._b_cancelled
    
    @bCancelled.setter
    def bCancelled(self, value: bool) -> None:
        self._b_cancelled = value


__all__ = ['EndDockingEvent']
