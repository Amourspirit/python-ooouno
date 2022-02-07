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
# Namespace: com.sun.star.container
from abc import abstractmethod, abstractproperty, ABC

class XStringKeyMap(ABC):
    """
    maps strings to anys.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XStringKeyMap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XStringKeyMap.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.XStringKeyMap'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.container.XStringKeyMap'

    @abstractmethod
    def getKeyByIndex(self, nIndex: int) -> str:
        """
        obtains the key of an element by index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getValue(self, aKey: str) -> object:
        """
        reads data from the map.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    @abstractmethod
    def getValueByIndex(self, nIndex: int) -> object:
        """
        obtains the value of an element by index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def hasValue(self, aKey: str) -> bool:
        """
        checks for element existence.
        """
    @abstractmethod
    def insertValue(self, aKey: str, aValue: object) -> None:
        """
        writes data to the map.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
    @abstractproperty
    def Count(self) -> int:
        """
        the number of elements in the map.
        """

__all__ = ['XStringKeyMap']

