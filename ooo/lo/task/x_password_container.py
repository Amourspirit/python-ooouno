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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .url_record import UrlRecord as UrlRecord_8f510a4d
    from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XPasswordContainer(XInterface_8f010a43):
    """
    Allows to save passwords with URL-pattern, to use them later.

    See Also:
        `API XPasswordContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XPasswordContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XPasswordContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XPasswordContainer'

    @abstractmethod
    def add(self, Url: str, UserName: str, Passwords: typing.Tuple[str, ...], Handler: XInteractionHandler_bf80e51) -> None:
        """
        Save passwords into the container.
        """
        ...
    @abstractmethod
    def addPersistent(self, Url: str, UserName: str, Passwords: typing.Tuple[str, ...], Handler: XInteractionHandler_bf80e51) -> None:
        """
        Save passwords into the container, and store them in the file.
        """
        ...
    @abstractmethod
    def find(self, Url: str, Handler: XInteractionHandler_bf80e51) -> UrlRecord_8f510a4d:
        """
        Find users with passwords for the url pattern.
        """
        ...
    @abstractmethod
    def findForName(self, Url: str, UserName: str, Handler: XInteractionHandler_bf80e51) -> UrlRecord_8f510a4d:
        """
        Find passwords for the url pattern and username.
        """
        ...
    @abstractmethod
    def getAllPersistent(self, Handler: XInteractionHandler_bf80e51) -> typing.Tuple[UrlRecord_8f510a4d, ...]:
        """
        Get all records from the file.
        """
        ...
    @abstractmethod
    def remove(self, Url: str, UserName: str) -> None:
        """
        Remove passwords for the url pattern and username.
        """
        ...
    @abstractmethod
    def removeAllPersistent(self) -> None:
        """
        Clean the file.
        """
        ...
    @abstractmethod
    def removePersistent(self, Url: str, UserName: str) -> None:
        """
        Remove passwords for the url pattern and username from the file.
        """
        ...

__all__ = ['XPasswordContainer']


