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
# Namespace: com.sun.star.document
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XActionLockable(XInterface_8f010a43):
    """
    makes it possible to prevent object internal updates for a certain period to be able to quickly change multiple parts of the objects, where the updates would invalidate each other, anyway.

    See Also:
        `API XActionLockable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XActionLockable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XActionLockable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XActionLockable'

    @abstractmethod
    def addActionLock(self) -> None:
        """
        increments the lock count of the object by one.
        """
        ...
    @abstractmethod
    def isActionLocked(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def removeActionLock(self) -> None:
        """
        decrements the lock count of the object by one.
        """
        ...
    @abstractmethod
    def resetActionLocks(self) -> int:
        """
        resets the locking level.
        
        This method is used for debugging purposes. The debugging environment of a programming language can reset the locks to allow refreshing of the view if a breakpoint is reached or step execution is used.
        """
        ...
    @abstractmethod
    def setActionLocks(self, nLock: int) -> None:
        """
        sets the locking level.
        
        This method is used for debugging purposes. The programming environment can restore the locking after a break of a debug session.
        """
        ...

__all__ = ['XActionLockable']

