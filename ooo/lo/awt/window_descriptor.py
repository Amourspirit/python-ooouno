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
import typing
from .rectangle import Rectangle as Rectangle_84b109e9
from .window_class import WindowClass as WindowClass_99f60ac2
from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0


class WindowDescriptor(object):
    """
    Struct Class

    describes a window.

    See Also:
        `API WindowDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1WindowDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.WindowDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.WindowDescriptor'
    """Literal Constant ``com.sun.star.awt.WindowDescriptor``"""

    def __init__(self, Type: WindowClass_99f60ac2 = WindowClass_99f60ac2.TOP, WindowServiceName: str = '', Parent: XWindowPeer_99760ab0 = None, ParentIndex: int = 0, Bounds: Rectangle_84b109e9 = UNO_NONE, WindowAttributes: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``Type`` can be another ``WindowDescriptor`` instance,
                in which case other named args are ignored.

        Arguments:
            Type (WindowClass, optional): Type value
            WindowServiceName (str, optional): WindowServiceName value
            Parent (XWindowPeer, optional): Parent value
            ParentIndex (int, optional): ParentIndex value
            Bounds (Rectangle, optional): Bounds value
            WindowAttributes (int, optional): WindowAttributes value
        """
        if isinstance(Type, WindowDescriptor):
            oth: WindowDescriptor = Type
            self._type = oth.Type
            self._window_service_name = oth.WindowServiceName
            self._parent = oth.Parent
            self._parent_index = oth.ParentIndex
            self._bounds = oth.Bounds
            self._window_attributes = oth.WindowAttributes
            return
        else:
            self._type = Type
            self._window_service_name = WindowServiceName
            self._parent = Parent
            self._parent_index = ParentIndex
            if Bounds is UNO_NONE:
                self._bounds = Rectangle_84b109e9()
            else:
                self._bounds = Bounds
            self._window_attributes = WindowAttributes



    @property
    def Type(self) -> WindowClass_99f60ac2:
        """
        specifies the type of window.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: WindowClass_99f60ac2) -> None:
        self._type = value

    @property
    def WindowServiceName(self) -> str:
        """
        specifies the name of the component service.
        
        A zero length name means that the VCL creates a blank top, a container, or a simple window. The following service names are defined:
        """
        return self._window_service_name
    
    @WindowServiceName.setter
    def WindowServiceName(self, value: str) -> None:
        self._window_service_name = value

    @property
    def Parent(self) -> XWindowPeer_99760ab0:
        """
        specifies the parent of the component.
        
        If Parent == 0 && ParentIndex == -1, then the window is on the desktop.
        """
        return self._parent
    
    @Parent.setter
    def Parent(self, value: XWindowPeer_99760ab0) -> None:
        self._parent = value

    @property
    def ParentIndex(self) -> int:
        """
        specifies the index of the parent window, if available.
        
        If Parent == 0 and this struct is a member of an array, then this is the offset from the beginning of the array to the parent. A value of -1 means desktop.
        """
        return self._parent_index
    
    @ParentIndex.setter
    def ParentIndex(self, value: int) -> None:
        self._parent_index = value

    @property
    def Bounds(self) -> Rectangle_84b109e9:
        """
        specifies the position and size of the window.
        
        This member is ignored if the window attribute is com.sun.star.awt.WindowAttribute.FULLSIZE.
        """
        return self._bounds
    
    @Bounds.setter
    def Bounds(self, value: Rectangle_84b109e9) -> None:
        self._bounds = value

    @property
    def WindowAttributes(self) -> int:
        """
        specifies the window attributes.
        
        Use one value out of the constant group com.sun.star.awt.WindowAttribute.
        """
        return self._window_attributes
    
    @WindowAttributes.setter
    def WindowAttributes(self, value: int) -> None:
        self._window_attributes = value


__all__ = ['WindowDescriptor']