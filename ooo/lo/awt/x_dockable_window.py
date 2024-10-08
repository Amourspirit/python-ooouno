# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .rectangle import Rectangle as Rectangle_84b109e9
    from .x_dockable_window_listener import XDockableWindowListener as XDockableWindowListener_36b80f7f

class XDockableWindow(XInterface_8f010a43):
    """
    specifies the docking interface for a window component.
    
    A window can either be docked where it resides as a child window in an application frame window or it can be floating where it will reside in its own decorated top level window.

    See Also:
        `API XDockableWindow <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDockableWindow.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XDockableWindow'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XDockableWindow'

    @abstractmethod
    def addDockableWindowListener(self, xListener: XDockableWindowListener_36b80f7f) -> None:
        """
        adds a docking listener to the object.
        
        only a single listener may be registered at any time.
        """
        ...
    @abstractmethod
    def enableDocking(self, bEnable: bool) -> None:
        """
        enable or disable docking, docking is disabled by default
        """
        ...
    @abstractmethod
    def isFloating(self) -> bool:
        """
        queries the current window state
        """
        ...
    @abstractmethod
    def isInPopupMode(self) -> bool:
        """
        queries the current pop-up mode
        """
        ...
    @abstractmethod
    def isLocked(self) -> bool:
        """
        queries the current locking state
        """
        ...
    @abstractmethod
    def lock(self) -> None:
        """
        prevents the window from being undocked this has no effect if the window is floating
        """
        ...
    @abstractmethod
    def removeDockableWindowListener(self, xListener: XDockableWindowListener_36b80f7f) -> None:
        """
        removes the specified docking listener from the object.
        """
        ...
    @abstractmethod
    def setFloatingMode(self, bFloating: bool) -> None:
        """
        toggle between floating and docked state
        """
        ...
    @abstractmethod
    def startPopupMode(self, WindowRect: Rectangle_84b109e9) -> None:
        """
        shows the window in a menu like style, i.e.
        
        without decoration a special indicator will allow for tearing off the window see com.sun.star.awt.XDockableWindowListener for the corresponding events
        """
        ...
    @abstractmethod
    def unlock(self) -> None:
        """
        enables undocking this has no effect if the window is floating
        """
        ...

__all__ = ['XDockableWindow']

