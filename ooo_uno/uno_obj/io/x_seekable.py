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

class XSeekable(XInterface_8f010a43):
    """
    makes it possible to seek to a certain position within a stream.
    
    This interface should be supported, if it is possible to access the data at the new position quickly. You should not support this interface, if you have a continuous stream, for example, a video stream.

    See Also:
        `API XSeekable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XSeekable.html>`_
    """

    @abstractmethod
    def getLength(self) -> int:
        """
        returns the length of the stream.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def getPosition(self) -> int:
        """
        returns the current offset of the stream.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def seek(self, location: int) -> None:
        """
        changes the seek pointer to a new location relative to the beginning of the stream.
        
        This method changes the seek pointer so subsequent reads and writes can take place at a different location in the stream object. It is an error to seek before the beginning of the stream or after the end of the stream.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
        """

__all__ = ['XSeekable']

