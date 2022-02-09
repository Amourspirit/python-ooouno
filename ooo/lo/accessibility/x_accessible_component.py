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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_accessible import XAccessible as XAccessible_1cbc0eb6
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.size import Size as Size_576707ef
    from ..util.color import Color as Color_68e908c5

class XAccessibleComponent(XInterface_8f010a43):
    """
    The XAccessibleComponent interface should be supported by any class that can be rendered on the screen.
    
    This interface provides the standard mechanism for an assistive technology to retrieve information concerning the graphical representation of an object. This interface combines methods from the Java interfaces javax.accessibility.AccessibleComponent and javax.accessibility.AccessibleExtendedComponent.
    
    Further information about the graphical appearance of an object can be expressed with the XAccessibleExtendedComponent interface.
    
    Coordinates used by the functions of this interface are specified in different coordinate systems. Their scale is the same and is equal to that of the screen coordinate system. In other words all coordinates are measured in pixel. They differ in their respective origin:
    
    Key bindings which are associated with an accessible component can be retrieved at the component's action. The reason for this is that key bindings are associated with actions and directly with a component. This distinction becomes important when there are more than one action. To get access to the key bindings you have to get the XAccessibleAction interface of a component, provided that it is supported, and use the XAccessibleAction.getAccessibleKeyBinding().
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleComponent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleComponent'

    @abstractmethod
    def containsPoint(self, Point: 'Point_5fb2085e') -> bool:
        """
        Tests whether the specified point lies within this object's bounds.
        
        The test point's coordinates are defined relative to the coordinate system of the object. That means that when the object is an opaque rectangle then both the points (0,0) and (with-1,height-1) would yield a TRUE value.
        """
    @abstractmethod
    def getAccessibleAtPoint(self, Point: 'Point_5fb2085e') -> 'XAccessible_1cbc0eb6':
        """
        Returns the Accessible child that is rendered under the given point.
        
        The test point's coordinates are defined relative to the coordinate system of the object. That means that when the object is an opaque rectangle then both the points (0,0) and (with-1,height-1) would yield a TRUE value.
        """
    @abstractmethod
    def getBackground(self) -> 'Color_68e908c5':
        """
        Returns the background color of this object.
        """
    @abstractmethod
    def getBounds(self) -> 'Rectangle_84b109e9':
        """
        Returns the bounding box of this object.
        
        The returned bounding box has the form of a rectangle. Its coordinates are relative to the object's parent coordinate system. Note that the two methods getLocation() and getSize() return the same information. With method getLocationOnScreen() you can get the bound box position in screen coordinates.
        """
    @abstractmethod
    def getForeground(self) -> 'Color_68e908c5':
        """
        Returns the foreground color of this object.
        """
    @abstractmethod
    def getLocation(self) -> 'Point_5fb2085e':
        """
        Returns the location of the upper left corner of the object's bounding box relative to the parent.
        
        The coordinates of the bounding box are given relative to the parent's coordinate system.
        """
    @abstractmethod
    def getLocationOnScreen(self) -> 'Point_5fb2085e':
        """
        Returns the location of the upper left corner of the object's bounding box in screen coordinates.
        
        This method returns the same point as does the method getLocation(). The difference is that the coordinates are absolute screen coordinates of the screen to which the object is rendered instead of being relative to the object's parent.
        """
    @abstractmethod
    def getSize(self) -> 'Size_576707ef':
        """
        Returns the size of this object's bounding box.
        """
    @abstractmethod
    def grabFocus(self) -> None:
        """
        Grabs the focus to this object.
        
        If this object can not accept the focus, i.e. isFocusTraversable() returns FALSE for this object then nothing happens. Otherwise the object will attempt to take the focus. Nothing happens if that fails, otherwise the object has the focus. This method is called requestFocus in the Java Accessibility API 1.4.
        """


__all__ = ['XAccessibleComponent']

