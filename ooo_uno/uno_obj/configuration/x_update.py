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
# Namespace: com.sun.star.configuration
import typing
from abc import abstractmethod, ABC

class XUpdate(ABC):
    """

    See Also:
        `API XUpdate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1XUpdate.html>`_
    """

    @abstractmethod
    def insertExtensionXcsFile(self, shared: bool, fileUri: str) -> None:
        """
        """
    @abstractmethod
    def insertExtensionXcuFile(self, shared: bool, fileUri: str) -> None:
        """
        """
    @abstractmethod
    def insertModificationXcuFile(self, fileUri: str, includedPaths: 'typing.List[str]', excludedPaths: 'typing.List[str]') -> None:
        """
        """
    @abstractmethod
    def removeExtensionXcuFile(self, fileUri: str) -> None:
        """
        """

__all__ = ['XUpdate']

