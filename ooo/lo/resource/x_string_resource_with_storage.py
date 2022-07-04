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
# Libre Office Version: 7.3
# Namespace: com.sun.star.resource
import typing
from abc import abstractmethod
from .x_string_resource_persistence import XStringResourcePersistence as XStringResourcePersistence_cabc130c
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class XStringResourceWithStorage(XStringResourcePersistence_cabc130c):
    """
    Extends XStringResourcePersistence by methods to handle an associated com.sun.star.embed.XStorage instance.

    See Also:
        `API XStringResourceWithStorage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourceWithStorage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.resource'
    __ooo_full_ns__: str = 'com.sun.star.resource.XStringResourceWithStorage'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.resource.XStringResourceWithStorage'

    @abstractmethod
    def setStorage(self, Storage: 'XStorage_8e460a32') -> None:
        """
        Associates a storage to the StringResourceWithStorage instance which is used on subsequent calls of store().
        
        This call has to be used carefully as it removes the storage previously connected to the StringResourceWithStorage. It may force the implementation to reload data from the previous storage before releasing it. The StringResourceManager will be modified after calling this method as the data isn't stored to the new storage yet. storeAsStorage() should be preferred as it directly stores the data to the new storage and afterwards this storage is in sync with the resource data.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def storeAsStorage(self, Storage: 'XStorage_8e460a32') -> None:
        """
        Stores all string table data to a storage and associates this storage to this instance as if setStorage() was called with this storage.
        
        The modified state will be unmodified after the call.
        
        This method can throw all exceptions thrown by the methods of com.sun.star.embed.XStorage

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XStringResourceWithStorage']

