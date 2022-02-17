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
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class PaintEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies the paint event for a component.
    
    This event is a special type which is used to ensure that paint/update method calls are serialized along with the other events delivered from the event queue.

    See Also:
        `API PaintEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1PaintEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.PaintEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.PaintEvent'
    """Literal Constant ``com.sun.star.awt.PaintEvent``"""

    def __init__(self, UpdateRect: Rectangle_84b109e9 = UNO_NONE, Count: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``UpdateRect`` can be another ``PaintEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            UpdateRect (Rectangle, optional): UpdateRect value
            Count (int, optional): Count value
        """
        super().__init__(**kwargs)
        if isinstance(UpdateRect, PaintEvent):
            oth: PaintEvent = UpdateRect
            self._update_rect = oth.UpdateRect
            self._count = oth.Count
            return
        else:
            if UpdateRect is UNO_NONE:
                self._update_rect = Rectangle_84b109e9()
            else:
                self._update_rect = UpdateRect
            self._count = Count



    @property
    def UpdateRect(self) -> Rectangle_84b109e9:
        """
        contains the rectangle area which needs to be repainted.
        """
        return self._update_rect
    
    @UpdateRect.setter
    def UpdateRect(self, value: Rectangle_84b109e9) -> None:
        self._update_rect = value

    @property
    def Count(self) -> int:
        """
        contains the number of paint events that follows this event if it is a multiple PaintEvent.
        
        You can collect the PaintEvent until Count is zero.
        """
        return self._count
    
    @Count.setter
    def Count(self, value: int) -> None:
        self._count = value


__all__ = ['PaintEvent']
