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
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a

class XStreamListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events from an active data control.

    See Also:
        `API XStreamListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XStreamListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XStreamListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XStreamListener'

    @abstractmethod
    def closed(self) -> None:
        """
        gets called when data transfer terminates normally or when data transfer is terminated from outside.
        
        The termination could be done using the method XActiveDataControl.terminate().
        """
    @abstractmethod
    def error(self, aException: object) -> None:
        """
        gets called when an internal error in source or sink has occurred.
        
        After the method is called, the close is called on the connected streams.
        """
    @abstractmethod
    def started(self) -> None:
        """
        gets called as soon as data transfer has started.
        """
    @abstractmethod
    def terminated(self) -> None:
        """
        gets called when XActiveDataControl.terminate() is called.
        """


__all__ = ['XStreamListener']

