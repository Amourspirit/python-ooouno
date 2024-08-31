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
# Namespace: com.sun.star.io
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XConnectable(XInterface_8f010a43):
    """
    makes it possible to connect data sinks and sources.
    
    The predecessor-member is the element in the connection that is nearer to the source of the data. The successor-member is the element that is further away from the source of the data. (Note that this classification does not depend on whether the class implements XInputStream or XOutputStream; it only depends on the direction of data flow.)
    
    This interface allows generic services to navigate between arbitrary elements of a connection.

    See Also:
        `API XConnectable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XConnectable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XConnectable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XConnectable'

    @abstractmethod
    def getPredecessor(self) -> XConnectable:
        """
        """
        ...
    @abstractmethod
    def getSuccessor(self) -> XConnectable:
        """
        """
        ...
    @abstractmethod
    def setPredecessor(self, aPredecessor: XConnectable) -> None:
        """
        sets the source of the data flow for this object.
        """
        ...
    @abstractmethod
    def setSuccessor(self, aSuccessor: XConnectable) -> None:
        """
        sets the sink of the data flow for this object.
        """
        ...

__all__ = ['XConnectable']

