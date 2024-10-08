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
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_control_model import XControlModel as XControlModel_affc0b7e
    from .x_toolkit import XToolkit as XToolkit_7adf0992
    from .x_view import XView as XView_5f670847
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class XControl(XComponent_98dc0ab5):
    """
    identifies a control.
    
    Implementations of this interface are abstract windows. The main reason to instantiate this implementation is to show the window on the screen. Before the window appears on the screen, the XControl.createPeer() method must be called.
    
    If the implementation of the control does not distinguish between model, view and controller, it must allow to set a new XGraphics in the view, so that the control can be printed.

    See Also:
        `API XControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XControl'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XControl'

    @abstractmethod
    def createPeer(self, Toolkit: XToolkit_7adf0992, Parent: XWindowPeer_99760ab0) -> None:
        """
        creates a \"child\" window on the screen.
        
        If the parent is NULL, then the desktop window of the toolkit is the parent.
        """
        ...
    @abstractmethod
    def getContext(self) -> XInterface_8f010a43:
        """
        gets the context of the control.
        """
        ...
    @abstractmethod
    def getModel(self) -> XControlModel_affc0b7e:
        """
        returns the model for this control.
        """
        ...
    @abstractmethod
    def getPeer(self) -> XWindowPeer_99760ab0:
        """
        returns the peer which was previously created or set.
        """
        ...
    @abstractmethod
    def getView(self) -> XView_5f670847:
        """
        returns the view of this control.
        """
        ...
    @abstractmethod
    def isDesignMode(self) -> bool:
        """
        returns TRUE if the control is in design mode, FALSE otherwise.
        """
        ...
    @abstractmethod
    def isTransparent(self) -> bool:
        """
        returns TRUE if the control is transparent, FALSE otherwise.
        """
        ...
    @abstractmethod
    def setContext(self, Context: XInterface_8f010a43) -> None:
        """
        sets the context of the control.
        """
        ...
    @abstractmethod
    def setDesignMode(self, bOn: bool) -> None:
        """
        sets the design mode for use in a design editor.
        
        Normally the control will be painted directly without a peer.
        """
        ...
    @abstractmethod
    def setModel(self, Model: XControlModel_affc0b7e) -> bool:
        """
        sets a model for the control.
        """
        ...

__all__ = ['XControl']

