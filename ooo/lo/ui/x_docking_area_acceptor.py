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
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.x_window import XWindow as XWindow_713b0924

class XDockingAreaAcceptor(XInterface_8f010a43):
    """
    this interface enables developer to implement different docking area acceptors which are used by the frame based layout manager.
    
    A docking area acceptor is responsible to control the docking area of a container window. As OLE for example supports inplace and outplace editing, there are different parts of code responsible for the container window. This interface enables developer to make support implementations for these scenarios.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XDockingAreaAcceptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XDockingAreaAcceptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XDockingAreaAcceptor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XDockingAreaAcceptor'

    @abstractmethod
    def getContainerWindow(self) -> 'XWindow_713b0924':
        """
        provide the container window where the layout manager can request border space for docking windows.
        
        Additionally the layout manager uses this window to create its own child windows for docking purposes.
        """
    @abstractmethod
    def requestDockingAreaSpace(self, RequestedSpace: 'Rectangle_84b109e9') -> bool:
        """
        method to ask an implementation if the provided space for docking windows is available or not.
        
        The com.sun.star.awt.Rectangle parameter is filled by the caller with pixel data. The members of com.sun.star.awt.Rectangle must be filled as following:
        """
    @abstractmethod
    def setDockingAreaSpace(self, BorderSpace: 'Rectangle_84b109e9') -> None:
        """
        method to brief an implementation that we need new border space.
        
        The callee must size its document window so that we have the amount of space we have provided. The com.sun.star.awt.Rectangle parameter is filled by the caller with pixel data. The members of com.sun.star.awt.Rectangle must be filled as following:
        """

__all__ = ['XDockingAreaAcceptor']

