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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_frame import XFrame as XFrame_7a570956
    from ..util.url import URL as URL_57ad07b9

class XDispatchRecorder(XInterface_8f010a43):
    """
    provides recording functionality of dispatches
    
    With such recorder it will be possible to record requests of type XDispatch by using additional interface XRecordableDispatch. The result of that will be a a script which can be used to start the dispatch at later time again. Such recorder objects are available on a XDispatchRecorderSupplier which is provided by the Frame service.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XDispatchRecorder <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatchRecorder.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDispatchRecorder'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDispatchRecorder'

    @abstractmethod
    def endRecording(self) -> None:
        """
        stops the recording process
        
        Must be called in pairs with XDispatchRecorder.startRecording().
        """
        ...
    @abstractmethod
    def getRecordedMacro(self) -> str:
        """
        returns the recorded source code
        
        This method must be used before endRecording() is called! Otherwise the macro will be released.
        """
        ...
    @abstractmethod
    def recordDispatch(self, URL: URL_57ad07b9, Arguments: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        records a single dispatch call identified by its command URL
        """
        ...
    @abstractmethod
    def recordDispatchAsComment(self, URL: URL_57ad07b9, Arguments: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        records a single dispatch call identified by its command URL, but comments it out
        
        This way calls that failed on execution can be documented.
        """
        ...
    @abstractmethod
    def startRecording(self, Frame: XFrame_7a570956) -> None:
        """
        initializes the recorder by passing the frame for which all macro statements shall be recorded
        """
        ...

__all__ = ['XDispatchRecorder']

