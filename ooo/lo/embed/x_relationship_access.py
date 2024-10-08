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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14

class XRelationshipAccess(XInterface_8f010a43):
    """
    This interface allows to get access to relationship data.
    
    The relationship data is organized as a set of entries. Each of entry is represented by a set of tags, where each tag has unique for this entry name and a string value. An entry must contain at least one tag named \"ID\", the value of this tag must be unique for the whole set of entries, this tag is used as a unique identifier of an entry.

    See Also:
        `API XRelationshipAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XRelationshipAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XRelationshipAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XRelationshipAccess'

    @abstractmethod
    def clearRelationships(self) -> None:
        """
        allows to clear the set of entries.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getAllRelationships(self) -> typing.Tuple[typing.Tuple[StringPair_a4bc0b14, ...], ...]:
        """
        retrieves the sequence containing all the entries controlled by the object.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getRelationshipByID(self, sID: str) -> typing.Tuple[StringPair_a4bc0b14, ...]:
        """
        retrieves the sequence containing all the tags from the entry with specified value of \"ID\" tag.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getRelationshipsByType(self, sType: str) -> typing.Tuple[typing.Tuple[StringPair_a4bc0b14, ...], ...]:
        """
        retrieves the sequence containing all the entries which \"Type\" tag takes the specified value.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getTargetByID(self, sID: str) -> str:
        """
        retrieves the value of \"Target\" tag from the entry with specified \"ID\" tag.
        
        If the entry has no \"Target\" tag an empty string is returned.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getTypeByID(self, sID: str) -> str:
        """
        retrieves the value of \"Type\" tag from the entry with specified \"ID\" tag.
        
        If the entry has no \"Type\" tag an empty string is returned.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def hasByID(self, sID: str) -> bool:
        """
        allows to detect whether there is an entry with specified value of \"ID\" tag.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def insertRelationshipByID(self, sID: str, aEntry: typing.Tuple[StringPair_a4bc0b14, ...], bReplace: bool) -> None:
        """
        allows to insert an entry.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def insertRelationships(self, aEntries: typing.Tuple[typing.Tuple[StringPair_a4bc0b14, ...], ...], bReplace: bool) -> None:
        """
        allows to insert a set of entries

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def removeRelationshipByID(self, sID: str) -> None:
        """
        allows to remove an entry.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XRelationshipAccess']

