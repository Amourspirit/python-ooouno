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
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XUrlContainer(XInterface_8f010a43):
    """
    Allows to store and retrieve URLs.
    
    URLs can be stored persistently or until end of OOo session.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XUrlContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XUrlContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XUrlContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XUrlContainer'

    @abstractmethod
    def addUrl(self, Url: str, MakePersistent: bool) -> None:
        """
        Add a URL to the container.
        """
    @abstractmethod
    def findUrl(self, Url: str) -> str:
        """
        Lookup a URL in the container.
        """
    @abstractmethod
    def getUrls(self, OnlyPersistent: bool) -> 'typing.Tuple[str, ...]':
        """
        Get all URLs.
        """
    @abstractmethod
    def removeUrl(self, Url: str) -> None:
        """
        Remove a URL from the container.
        """

__all__ = ['XUrlContainer']

