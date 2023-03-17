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
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_window import XWindow as XWindow_713b0924
    from ..datatransfer.clipboard.x_clipboard import XClipboard as XClipboard_a18a11cd
    from ..datatransfer.dnd.x_drag_gesture_recognizer import XDragGestureRecognizer as XDragGestureRecognizer_10741438
    from ..datatransfer.dnd.x_drag_source import XDragSource as XDragSource_49900fb2
    from ..datatransfer.dnd.x_drop_target import XDropTarget as XDropTarget_49e50fbf

class XDataTransferProviderAccess(XInterface_8f010a43):
    """
    This interface extends the XToolkit interface with clipboard and drag-and-drop support.

    See Also:
        `API XDataTransferProviderAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDataTransferProviderAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XDataTransferProviderAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XDataTransferProviderAccess'

    @abstractmethod
    def getClipboard(self, clipboardName: str) -> 'XClipboard_a18a11cd':
        """
        returns the specified clipboard.
        """
        ...
    @abstractmethod
    def getDragGestureRecognizer(self, window: 'XWindow_713b0924') -> 'XDragGestureRecognizer_10741438':
        """
        returns the drag gesture recognizer of the specified window.
        """
        ...
    @abstractmethod
    def getDragSource(self, window: 'XWindow_713b0924') -> 'XDragSource_49900fb2':
        """
        returns the drag source of the specified window.
        """
        ...
    @abstractmethod
    def getDropTarget(self, window: 'XWindow_713b0924') -> 'XDropTarget_49e50fbf':
        """
        returns the drop target of the specified window.
        """
        ...

__all__ = ['XDataTransferProviderAccess']

