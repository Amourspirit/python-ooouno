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
# Namespace: com.sun.star.io
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMarkableStream(XInterface_8f010a43):
    """
    makes it possible to set and remove seekable marks to a stream.

    See Also:
        `API XMarkableStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XMarkableStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XMarkableStream'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XMarkableStream'

    @abstractmethod
    def createMark(self) -> int:
        """
        creates a mark of the current position and returns an identifier to it.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def deleteMark(self, Mark: int) -> None:
        """
        deletes the mark that you previously created with XMarkableStream.createMark().
        
        It is an error to delete a mark if other marks after this exist. In this case, for reasons of robustness, the implementation must delete this mark and all others after this mark.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def jumpToFurthest(self) -> None:
        """
        jumps to the furthest position of the stream.
        
        In the inputstream case, a subsequent read call returns data, that was never read or skipped over before. In the outputstream case, a subsequent write call will add new data at the end of the stream without overwriting existing data.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def jumpToMark(self, nMark: int) -> None:
        """
        jumps to a previously created mark.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def offsetToMark(self, nMark: int) -> int:
        """

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XMarkableStream']

