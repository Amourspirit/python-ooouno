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
# Namespace: com.sun.star.resource
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_string_resource_manager import XStringResourceManager as XStringResourceManager_80421142
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XStringResourcePersistence(XStringResourceManager_80421142):
    """
    Interface derived from XStringResourceManager containing basic persistence functionality limited to operations that are independent from an associated location or storage.

    See Also:
        `API XStringResourcePersistence <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourcePersistence.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.resource'
    __ooo_full_ns__: str = 'com.sun.star.resource.XStringResourcePersistence'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.resource.XStringResourcePersistence'

    @abstractmethod
    def exportBinary(self) -> typing.Tuple[int, ...]:
        """
        Returns a sequence of byte representing the complete string resource in a binary format.
        
        This method is intended to support datatransfer functionality, e.g. provided by com.sun.star.datatransfer.XTransferable and related interfaces.
        
        See importBinary()).
        """
        ...
    @abstractmethod
    def importBinary(self, Data: typing.Tuple[int, ...]) -> None:
        """
        Initializes the string resource with binary data.
        
        This method expects the data format returned by exportBinary().
        
        All locales and strings previously added to the string resource will be deleted. So after calling this method the string resource only contains the locales and strings specified in the binary data.
        
        This method is intended to support datatransfer functionality, e.g. provided by com.sun.star.datatransfer.XTransferable and related interfaces.
        
        See importBinary()).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def isModified(self) -> bool:
        """
        provides the current modify state of the StringResourceManager instance.
        """
        ...
    @abstractmethod
    def setComment(self, Comment: str) -> None:
        """
        Sets the comment stored first in each locale data file.
        
        This interface method can be used to overwrite the comment used during initialization of the services StringResourceWithLocation or StringResourceWithStorage
        """
        ...
    @abstractmethod
    def store(self) -> None:
        """
        Stores all string table data respectively all data modified since the last call to store() to the location or storage associated with the StringResourceManager.
        
        Each locale is stored in a single file following the format of Java properties files.
        
        This interface is supported by the services StringResourceWithLocation and StringResourceWithStorage
        
        The StringResourceWithLocation is initialized with a URL specifying a location used to load data from and store data to, see StringResourceWithLocation.
        
        The StringResourceWithStorage is initialized with an instance of com.sun.star.embed.XStorage used to load data from and store data to, see StringResourceWithStorage.
        
        If the string table isn't modified (see isModified()) this method does nothing.
        
        This method can throw all exceptions thrown by the methods of com.sun.star.embed.XStorage respectively a com.sun.star.ucb.CommandAbortedException in case of a StringResourceWithLocation for all exceptions that are not handled by a previously specified com.sun.star.task.XInteractionHandler. The handler to be used for the store operation can be specified during initialization of StringResourceWithLocation.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def storeToStorage(self, Storage: XStorage_8e460a32, BaseName: str, Comment: str) -> None:
        """
        Stores all string table data to the provided storage.
        
        Calling this method does not affect the association with a location (in case of a StringResourceWithLocation instance) respectively with a storage (in case of a StringResourceWithStorage instance). The modified state isn't affected either.
        
        This method can be used to make a copy of the current string table data to a storage. This method can throw all exceptions thrown by the methods of com.sun.star.embed.XStorage
        
        This method can throw all exceptions thrown by the methods of com.sun.star.embed.XStorage

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def storeToURL(self, URL: str, BaseName: str, Comment: str, Handler: XInteractionHandler_bf80e51) -> None:
        """
        Stores all string table data to the location specified by the passed URL string.
        
        Calling this method does not affect the association with a location (in case of a StringResourceWithLocation instance) respectively with a storage (in case of a StringResourceWithStorage instance). The modified state isn't affected either.
        
        This method can be used to make a copy of the current string table data to a location.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XStringResourcePersistence']

