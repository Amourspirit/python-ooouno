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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class FolderListEntry(object):
    """
    Struct Class

    Information about a single folder in a FolderList.

    See Also:
        `API FolderListEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1FolderListEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.FolderListEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.FolderListEntry'
    """Literal Constant ``com.sun.star.ucb.FolderListEntry``"""

    def __init__(self, Title: str = '', ID: str = '', Subscribed: bool = False, New: bool = False, Removed: bool = False, Purge: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``Title`` can be another ``FolderListEntry`` instance,
                in which case other named args are ignored.

        Arguments:
            Title (str, optional): Title value
            ID (str, optional): ID value
            Subscribed (bool, optional): Subscribed value
            New (bool, optional): New value
            Removed (bool, optional): Removed value
            Purge (bool, optional): Purge value
        """
        if isinstance(Title, FolderListEntry):
            oth: FolderListEntry = Title
            self._title = oth.Title
            self._id = oth.ID
            self._subscribed = oth.Subscribed
            self._new = oth.New
            self._removed = oth.Removed
            self._purge = oth.Purge
            return
        else:
            self._title = Title
            self._id = ID
            self._subscribed = Subscribed
            self._new = New
            self._removed = Removed
            self._purge = Purge



    @property
    def Title(self) -> str:
        """
        The title of the folder.
        """
        return self._title
    
    @Title.setter
    def Title(self, value: str) -> None:
        self._title = value

    @property
    def ID(self) -> str:
        """
        A (unique) identifier for the folder (used by IMAP, where different folders with equal human-readable titles may exist; otherwise, it may be left empty).
        """
        return self._id
    
    @ID.setter
    def ID(self, value: str) -> None:
        self._id = value

    @property
    def Subscribed(self) -> bool:
        """
        The folder is subscribed.
        """
        return self._subscribed
    
    @Subscribed.setter
    def Subscribed(self, value: bool) -> None:
        self._subscribed = value

    @property
    def New(self) -> bool:
        """
        The folder is new.
        """
        return self._new
    
    @New.setter
    def New(self, value: bool) -> None:
        self._new = value

    @property
    def Removed(self) -> bool:
        """
        The folder has been removed.
        """
        return self._removed
    
    @Removed.setter
    def Removed(self, value: bool) -> None:
        self._removed = value

    @property
    def Purge(self) -> bool:
        """
        The folder shall be purged (only used in conjunction with the FolderListCommand.SET).
        """
        return self._purge
    
    @Purge.setter
    def Purge(self, value: bool) -> None:
        self._purge = value


__all__ = ['FolderListEntry']
