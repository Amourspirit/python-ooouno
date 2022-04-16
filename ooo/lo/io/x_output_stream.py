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
# Libre Office Version: 7.3
# Namespace: com.sun.star.io
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XOutputStream(XInterface_8f010a43):
    """
    This is the basic interface to write data to a stream.
    
    See the streaming document for further information on chaining and piping streams.

    See Also:
        `API XOutputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XOutputStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XOutputStream'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XOutputStream'

    @abstractmethod
    def closeOutput(self) -> None:
        """
        gets called to indicate that all data has been written.
        
        If this method has not yet been called, no attached XInputStream receives an EOF signal. No further bytes may be written after this method has been called.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def flush(self) -> None:
        """
        flushes out of the stream any data that may exist in buffers.
        
        The semantics of this method are rather vague. See com.sun.star.io.XAsyncOutputMonitor.waitForCompletion() for a similar method with very specific semantics, that is useful in certain scenarios.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def writeBytes(self, aData: 'typing.Tuple[int, ...]') -> None:
        """
        writes the whole sequence to the stream.
        
        (blocking call)

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """

__all__ = ['XOutputStream']

