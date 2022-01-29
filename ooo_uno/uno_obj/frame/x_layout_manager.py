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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.size import Size as Size_576707ef
    from .x_frame import XFrame as XFrame_7a570956
    from ..ui.docking_area import DockingArea as DockingArea_8daf0a1e
    from ..ui.x_docking_area_acceptor import XDockingAreaAcceptor as XDockingAreaAcceptor_f8d90da7
    from ..ui.xui_element import XUIElement as XUIElement_820509a6

class XLayoutManager(XInterface_8f010a43):
    """
    central interface to query for, create, destroy and manipulate user interface elements which are bound to a layout manager.
    
    Every user interface element which is controlled by a layout manager has a unique identifier called resource URL.
    
    A resource URL must meet the following syntax: \"private:resource/$type/$name\". It is only allowed to use ASCII characters for type and name.
    
    Currently the following user interface element types are defined:
    
    **since**
    
        OOo 2.0

    See Also:
        `API XLayoutManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XLayoutManager.html>`_
    """

    @abstractmethod
    def attachFrame(self, Frame: 'XFrame_7a570956') -> None:
        """
        attaches a com.sun.star.frame.XFrame to a layout manager.
        
        A layout manager needs a com.sun.star.frame.XFrame to be able to work. Without a it no user interface elements can be created.
        """
    @abstractmethod
    def createElement(self, ResourceURL: str) -> None:
        """
        creates a new user interface element.
        """
    @abstractmethod
    def destroyElement(self, ResourceURL: str) -> None:
        """
        destroys a user interface element.
        """
    @abstractmethod
    def doLayout(self) -> None:
        """
        forces a complete new layouting of all user interface elements.
        """
    @abstractmethod
    def dockAllWindows(self, nElementType: int) -> bool:
        """
        docks all windows which are member of the provided user interface element type.
        """
    @abstractmethod
    def dockWindow(self, ResourceURL: str, DockingArea: 'DockingArea_8daf0a1e', Pos: 'Point_5fb2085e') -> bool:
        """
        docks a window based user interface element to a specified docking area.
        """
    @abstractmethod
    def floatWindow(self, ResourceURL: str) -> bool:
        """
        forces a window based user interface element to float.
        """
    @abstractmethod
    def getCurrentDockingArea(self) -> 'Rectangle_84b109e9':
        """
        provides the current docking area size of the layout manager.
        """
    @abstractmethod
    def getDockingAreaAcceptor(self) -> 'XDockingAreaAcceptor_f8d90da7':
        """
        retrieves the current docking area acceptor that controls the border space of the frame's container window.
        
        A docking area acceptor retrieved by this method is owned by the layout manager. It is not allowed to dispose this object, it will be destroyed on reference count!
        """
    @abstractmethod
    def getElement(self, ResourceURL: str) -> 'XUIElement_820509a6':
        """
        retrieves a user interface element which has been created before.
        
        The layout manager instance is owner of the returned user interface element. That means that the life time of the user interface element is controlled by the layout manager. It can be disposed at every time!
        """
    @abstractmethod
    def getElementPos(self, ResourceURL: str) -> 'Point_5fb2085e':
        """
        retrieves the current pixel position of a window based user interface element.
        """
    @abstractmethod
    def getElementSize(self, ResourceURL: str) -> 'Size_576707ef':
        """
        retrieves the current size of a window based user interface element.
        """
    @abstractmethod
    def getElements(self) -> 'typing.List[XUIElement_820509a6]':
        """
        retrieves all user interface elements which are currently instantiated.
        
        The layout manager instance is owner of the returned user interface elements. That means that the life time of the user interface elements is controlled by the layout manager. They can be disposed at every time!
        """
    @abstractmethod
    def hideElement(self, ResourceURL: str) -> bool:
        """
        hides a user interface element.
        """
    @abstractmethod
    def isElementDocked(self, ResourceURL: str) -> bool:
        """
        retrieves the current docking state of a window based user interface element.
        """
    @abstractmethod
    def isElementFloating(self, ResourceURL: str) -> bool:
        """
        retrieves the current floating state of a window based user interface element.
        """
    @abstractmethod
    def isElementLocked(self, ResourceURL: str) -> bool:
        """
        retrieves the current lock state of a window based user interface element.
        """
    @abstractmethod
    def isElementVisible(self, ResourceURL: str) -> bool:
        """
        retrieves the current visibility state of a window based user interface element.
        """
    @abstractmethod
    def isVisible(self) -> bool:
        """
        retrieves the visibility state of a layout manager.
        
        A layout manager can be set to invisible state to force it to hide all of its user interface elements. If another component wants to use the window for its own user interface elements it can use this function. This function is normally used to implement inplace editing.
        """
    @abstractmethod
    def lock(self) -> None:
        """
        prohibit all layout updates until unlock is called again.
        
        This call can be used to speed up the creation process of several user interface elements. Otherwise the layout manager would calculate the layout for every creation.
        """
    @abstractmethod
    def lockWindow(self, ResourceURL: str) -> bool:
        """
        locks a window based user interface element if it's in a docked state.
        """
    @abstractmethod
    def requestElement(self, ResourceURL: str) -> bool:
        """
        request to make a user interface element visible if it is not in hidden state.
        
        If a user interface element should forced to the visible state XLayoutManager.showElement() should be used. This function can be used for context dependent elements which should respect the current visibility state.
        """
    @abstractmethod
    def reset(self) -> None:
        """
        resets the layout manager and remove all of its internal user interface elements.
        
        This call should be handled with care as all user interface elements will be destroyed and the layout manager is reset to a state after a attachFrame() has been made. That means an attached frame which has been set by attachFrame() is not released. The layout manager itself calls reset after a component has been attached or reattached to a frame.
        """
    @abstractmethod
    def setDockingAreaAcceptor(self, xDockingAreaAcceptor: 'XDockingAreaAcceptor_f8d90da7') -> None:
        """
        sets a docking area acceptor that controls the border space of the frame's container window.
        
        A docking area acceptor decides if the layout manager can use requested border space for docking windows. If the acceptor denies the requested space the layout manager automatically set all docked windows into floating state and will not use this space for docking.
        After setting a docking area acceptor the object is owned by the layout manager. It is not allowed to dispose this object, it will be destroyed on reference count!
        """
    @abstractmethod
    def setElementPos(self, ResourceURL: str, Pos: 'Point_5fb2085e') -> None:
        """
        sets a new position for a window based user interface element.
        
        It is up to the layout manager to decide if the user interface element can be moved. The new position can be retrieved by calling getElementPos().
        """
    @abstractmethod
    def setElementPosSize(self, ResourceURL: str, Pos: 'Point_5fb2085e', Size: 'Size_576707ef') -> None:
        """
        sets a new position and size for a window based user interface element.
        
        It is up to the layout manager to decide if the user interface element can be moved and resized. The new position and size can be retrieved by calling getElementPos() and getElementSize().
        """
    @abstractmethod
    def setElementSize(self, ResourceURL: str, Size: 'Size_576707ef') -> None:
        """
        sets a new size for a window based user interface element.
        
        It is up to the layout manager to decide if the user interface element can be resized. The new size can be retrieved by calling getElementSize().
        """
    @abstractmethod
    def setVisible(self, Visible: bool) -> None:
        """
        sets the layout manager to invisible state and hides all user interface elements.
        
        A layout manager can be set to invisible state to force it to hide all of its user interface elements. If another component wants to use the window for its own user interface elements it can use this function. This function is normally used to implement inplace editing.
        """
    @abstractmethod
    def showElement(self, ResourceURL: str) -> bool:
        """
        shows a user interface element.
        """
    @abstractmethod
    def unlock(self) -> None:
        """
        permit layout updates again.
        
        This function should be called to permit layout updates. The layout manager starts to calculate the new layout after this call.
        """
    @abstractmethod
    def unlockWindow(self, ResourceURL: str) -> bool:
        """
        unlocks a window based user interface element if it's in a docked state.
        """

__all__ = ['XLayoutManager']

