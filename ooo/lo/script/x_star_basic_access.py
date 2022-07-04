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
# Namespace: com.sun.star.script
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class XStarBasicAccess(XInterface_8f010a43):
    """
    Interface representing a library and provides access to its modules.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XStarBasicAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XStarBasicAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XStarBasicAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XStarBasicAccess'

    @abstractmethod
    def addDialog(self, LibraryName: str, DialogName: str, Data: uno.ByteSequence) -> None:
        """
        Adds an old style basic dialog (SI controls) to an existing (e.g., created by createLibrary) library.
        
        By using this method together with createLibrary the caller does not have to implement XStarBasicLibraryInfo and XStarBasicDialogInfo

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def addModule(self, LibraryName: str, ModuleName: str, Language: str, Source: str) -> None:
        """
        Adds a module to an existing (e.g., created by createLibrary) library.
        
        By using this method together with createLibrary the caller does not have to implement XStarBasicLibraryInfo and XModuleInfo.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def createLibrary(self, LibName: str, Password: str, ExternalSourceURL: str, LinkTargetURL: str) -> None:
        """
        Creates an empty library.
        
        This method can be called alternatively to accessing directly the NameContainer returned by getLibraryContainer. By using this method together with addModule and addStarBasicDialog the caller does not have to implement XStarBasicLibraryInfo, XModuleInfo, and XStarBasicDialogInfo

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    @abstractmethod
    def getLibraryContainer(self) -> 'XNameContainer_cb90e47':
        """
        returns the library container giving access to the libraries stored in a document or basic library file.
        """
        ...

__all__ = ['XStarBasicAccess']

