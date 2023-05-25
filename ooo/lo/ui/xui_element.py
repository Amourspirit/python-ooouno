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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..frame.x_frame import XFrame as XFrame_7a570956

class XUIElement(XInterface_8f010a43):
    """
    provides a function to retrieve a special purpose interface dependent on the user interface element type.
    
    The type of the interface depends on the real type of the user interface element. A menubar user interface element provides access to its com.sun.star.awt.XSystemDependentMenuBarPeer which supports to retrieve the system dependent menu handle. A floating window or a toolbar user interface element return a com.sun.star.awt.XWindow interface.

    See Also:
        `API XUIElement <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIElement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIElement'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIElement'

    @abstractmethod
    def getRealInterface(self) -> XInterface_8f010a43:
        """
        returns an interface to get access to user interface type specific functions.
        """
        ...
    @abstractproperty
    def Frame(self) -> XFrame_7a570956:
        """
        determines the document frame to which this element is bound to.
        
        The life time of a user interface element does not explicitly depend on the frame itself but on the visible component attached to the frame. It is possible to exchange the visible component of a frame and that will lead to the end of life of all user interface elements.
        """
        ...

    @abstractproperty
    def ResourceURL(self) -> str:
        """
        a resource URL which is a unique identifier of a user interface element.
        """
        ...

    @abstractproperty
    def Type(self) -> int:
        """
        determines the type of the user interface element.
        """
        ...


__all__ = ['XUIElement']


