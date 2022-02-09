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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .mouse_event import MouseEvent as MouseEvent_8f430a5f

class XMouseListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events from the mouse in a certain window.
    
    Use the following interfaces which allow to receive (and consume) mouse events even on windows which are not at the top:

    See Also:
        `API XMouseListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMouseListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XMouseListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XMouseListener'

    @abstractmethod
    def mouseEntered(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when the mouse enters a window.
        """
    @abstractmethod
    def mouseExited(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when the mouse exits a window.
        """
    @abstractmethod
    def mousePressed(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when a mouse button has been pressed on a window.
        
        Since mouse presses are usually also used to indicate requests for pop-up menus (also known as context menus) on objects, you might receive two events for a single mouse press: For example, if, on your operating system, pressing the right mouse button indicates the request for a context menu, then you will receive one call to mousePressed() indicating the mouse click, and another one indicating the context menu request. For the latter, the MouseEvent.PopupTrigger member of the event will be set to TRUE.
        """
    @abstractmethod
    def mouseReleased(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when a mouse button has been released on a window.
        """


__all__ = ['XMouseListener']

