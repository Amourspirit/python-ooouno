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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_refresh_listener import XRefreshListener as XRefreshListener_e2f20d33

class XRefreshable(XInterface_8f010a43):
    """
    is supported by objects with data that can be refreshed from a data source.

    See Also:
        `API XRefreshable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XRefreshable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XRefreshable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XRefreshable'

    @abstractmethod
    def addRefreshListener(self, l: 'XRefreshListener_e2f20d33') -> None:
        """
        adds the specified listener to receive the event \"refreshed.\"
        """
        ...
    @abstractmethod
    def refresh(self) -> None:
        """
        refreshes the data of the object from the connected data source.
        """
        ...
    @abstractmethod
    def removeRefreshListener(self, l: 'XRefreshListener_e2f20d33') -> None:
        """
        removes the specified listener.
        """
        ...

__all__ = ['XRefreshable']

