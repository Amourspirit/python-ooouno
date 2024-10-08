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
# Namespace: com.sun.star.connection
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XConnection(XInterface_8f010a43):
    """
    A bidirectional bytestream.
    
    You should additionally implement XConnection2.

    See Also:
        `API XConnection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1connection_1_1XConnection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.connection'
    __ooo_full_ns__: str = 'com.sun.star.connection.XConnection'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.connection.XConnection'

    @abstractmethod
    def close(self) -> None:
        """
        Immediately terminates any ongoing read or write calls.
        
        All subsequent read or write calls()

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def flush(self) -> None:
        """
        Empties all internal buffers.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getDescription(self) -> str:
        """
        A unique string describing the connection.
        
        This string is different from the arguments to XConnection.accept() and XConnector.connect(). In general, the string contains an additional handle value. For example, \"socket,host=localhost,port=2002,uniqueValue=2324\".
        """
        ...
    @abstractmethod
    def read(self, aReadBytes: typing.Tuple[int, ...], nBytesToRead: int) -> int:
        """
        reads a requested number of bytes from the connection.
        
        This method is blocking, meaning that it always returns a bytesequence with the requested number of bytes, unless it has reached end of file (which often means, that close() has been called).
        
        please see also the readSomeBytes() method of XConnection2.

        * ``aReadBytes`` is an out direction argument.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def write(self, aData: typing.Tuple[int, ...]) -> None:
        """
        writes the given bytesequence to the stream.
        
        The method blocks until the whole sequence is written.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XConnection']

