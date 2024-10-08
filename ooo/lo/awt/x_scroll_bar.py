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
    from .x_adjustment_listener import XAdjustmentListener as XAdjustmentListener_fdfc0e11

class XScrollBar(XInterface_8f010a43):
    """
    gives access to the value and settings of a scroll bar and makes it possible to register adjustment event listeners.

    See Also:
        `API XScrollBar <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XScrollBar.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XScrollBar'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XScrollBar'

    @abstractmethod
    def addAdjustmentListener(self, l: XAdjustmentListener_fdfc0e11) -> None:
        """
        registers an adjustment event listener.
        """
        ...
    @abstractmethod
    def getBlockIncrement(self) -> int:
        """
        returns the currently set increment for a block move.
        """
        ...
    @abstractmethod
    def getLineIncrement(self) -> int:
        """
        returns the currently set increment for a single line move.
        """
        ...
    @abstractmethod
    def getMaximum(self) -> int:
        """
        returns the currently set maximum scroll value of the scroll bar.
        """
        ...
    @abstractmethod
    def getOrientation(self) -> int:
        """
        returns the currently set ScrollBarOrientation of the scroll bar.
        """
        ...
    @abstractmethod
    def getValue(self) -> int:
        """
        returns the current scroll value of the scroll bar.
        """
        ...
    @abstractmethod
    def getVisibleSize(self) -> int:
        """
        returns the currently visible size of the scroll bar.
        """
        ...
    @abstractmethod
    def removeAdjustmentListener(self, l: XAdjustmentListener_fdfc0e11) -> None:
        """
        unregisters an adjustment event listener.
        """
        ...
    @abstractmethod
    def setBlockIncrement(self, n: int) -> None:
        """
        sets the increment for a block move.
        """
        ...
    @abstractmethod
    def setLineIncrement(self, n: int) -> None:
        """
        sets the increment for a single line move.
        """
        ...
    @abstractmethod
    def setMaximum(self, n: int) -> None:
        """
        sets the maximum scroll value of the scroll bar.
        """
        ...
    @abstractmethod
    def setOrientation(self, n: int) -> None:
        """
        sets the ScrollBarOrientation of the scroll bar.
        """
        ...
    @abstractmethod
    def setValue(self, n: int) -> None:
        """
        sets the scroll value of the scroll bar.
        """
        ...
    @abstractmethod
    def setValues(self, nValue: int, nVisible: int, nMax: int) -> None:
        """
        sets the scroll value, visible area and maximum scroll value of the scroll bar.
        """
        ...
    @abstractmethod
    def setVisibleSize(self, n: int) -> None:
        """
        sets the visible size of the scroll bar.
        """
        ...

__all__ = ['XScrollBar']

