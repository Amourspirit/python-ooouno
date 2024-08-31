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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_stream import XStream as XStream_678908a4

class XActiveDataStreamer(XInterface_8f010a43):
    """
    makes it possible to read and write the corresponding stream.
    
    If you want to allow control from outside, also implement the XActiveDataControl interface.

    See Also:
        `API XActiveDataStreamer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XActiveDataStreamer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XActiveDataStreamer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XActiveDataStreamer'

    @abstractmethod
    def getStream(self) -> XStream_678908a4:
        """
        """
        ...
    @abstractmethod
    def setStream(self, aStream: XStream_678908a4) -> None:
        """
        plugs the input/output stream.
        
        If XConnectable is also implemented, this method should query aStream for a XConnectable and connect both.
        """
        ...

__all__ = ['XActiveDataStreamer']

