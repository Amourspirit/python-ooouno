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
# Namespace: com.sun.star.datatransfer.dnd
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XDropTargetDragContext(XInterface_8f010a43):
    """
    This interface is implemented by any drop target context object.
    
    A drop target context is created whenever the logical cursor associated with a Drag and Drop operation moves within the visible geometry of a window associated with a drop target.
    
    The drop target context provides the mechanism for a potential receiver of a drop operation to both provide the end user with the appropriate drag under feedback and effect the subsequent data transfer, if appropriate.

    See Also:
        `API XDropTargetDragContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDropTargetDragContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.XDropTargetDragContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.XDropTargetDragContext'

    @abstractmethod
    def acceptDrag(self, dragOperation: int) -> None:
        """
        Accept the Drag.
        
        This method should be called from the methods of XDropTargetListener
        
        if the implementation wishes to accept the drag operation with the specified action.
        """
    @abstractmethod
    def rejectDrag(self) -> None:
        """
        Reject the drag as a result of examining the available com.sun.star.datatransfer.DataFlavor types received in the com.sun.star.datatransfer.dnd.XDropTargetListener.dragEnter() method.
        """


__all__ = ['XDropTargetDragContext']

