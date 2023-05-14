# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_flush_listener import XFlushListener as XFlushListener_c92a0c66

class XFlushable(XInterface_8f010a43):
    """
    is supported by objects with data that can be flushed to a data source.

    See Also:
        `API XFlushable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XFlushable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XFlushable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XFlushable'

    @abstractmethod
    def addFlushListener(self, l: 'XFlushListener_c92a0c66') -> None:
        """
        adds the specified listener to receive event \"flushed.\"
        """
        ...
    @abstractmethod
    def flush(self) -> None:
        """
        flushes the data of the object to the connected data source.
        """
        ...
    @abstractmethod
    def removeFlushListener(self, l: 'XFlushListener_c92a0c66') -> None:
        """
        removes the specified listener.
        """
        ...

__all__ = ['XFlushable']

