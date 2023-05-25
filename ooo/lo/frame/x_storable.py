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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XStorable(XInterface_8f010a43):
    """
    offers a simple way to store a component to a URL.
    
    It is usually only useful for two cases:

    See Also:
        `API XStorable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XStorable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XStorable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XStorable'

    @abstractmethod
    def getLocation(self) -> str:
        """
        After XStorable.storeAsURL() it returns the URL the object was stored to.
        """
        ...
    @abstractmethod
    def hasLocation(self) -> bool:
        """
        The object may know the location because it was loaded from there, or because it is stored there.
        """
        ...
    @abstractmethod
    def isReadonly(self) -> bool:
        """
        It is not possible to call XStorable.store() successfully when the data store is read-only.
        """
        ...
    @abstractmethod
    def store(self) -> None:
        """
        stores the data to the URL from which it was loaded.
        
        Only objects which know their locations can be stored.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def storeAsURL(self, sURL: str, lArguments: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        stores the object's persistent data to a URL and makes this URL the new location of the object.
        
        This is the normal behavior for UI's \"save-as\" feature.
        
        The change of the location makes it necessary to store the document in a format that the object can load. For this reason the implementation of XStorable.storeAsURL() will throw an exception if a pure export filter is used, it will accept only combined import/export filters. For such filters the method XStorable.storeToURL() must be used that does not change the location of the object.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def storeToURL(self, sURL: str, lArguments: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        stores the object's persistent data to a URL and continues to be a representation of the old URL.
        
        This is the normal behavior for UI's export feature.
        
        This method accepts all kinds of export filters, not only combined import/export filters because it implements an exporting capability, not a persistence capability.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XStorable']


