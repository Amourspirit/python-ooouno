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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class MenuMultipleChange(object):
    """
    Struct Class

    Explains properties of a menu item.

    See Also:
        `API MenuMultipleChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mozilla_1_1MenuMultipleChange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.MenuMultipleChange'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.mozilla.MenuMultipleChange'
    """Literal Constant ``com.sun.star.mozilla.MenuMultipleChange``"""

    def __init__(self, Image: typing.Tuple[int, ...] = UNO_NONE, ID: int = 0, GroupID: int = 0, PreItemID: int = 0, ItemText: str = '', IsVisible: bool = False, IsActive: bool = False, IsCheckable: bool = False, IsChecked: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``Image`` can be another ``MenuMultipleChange`` instance,
                in which case other named args are ignored.

        Arguments:
            Image (Tuple[int, ...], optional): Image value
            ID (int, optional): ID value
            GroupID (int, optional): GroupID value
            PreItemID (int, optional): PreItemID value
            ItemText (str, optional): ItemText value
            IsVisible (bool, optional): IsVisible value
            IsActive (bool, optional): IsActive value
            IsCheckable (bool, optional): IsCheckable value
            IsChecked (bool, optional): IsChecked value
        """
        if isinstance(Image, MenuMultipleChange):
            oth: MenuMultipleChange = Image
            self._image = oth.Image
            self._id = oth.ID
            self._group_id = oth.GroupID
            self._pre_item_id = oth.PreItemID
            self._item_text = oth.ItemText
            self._is_visible = oth.IsVisible
            self._is_active = oth.IsActive
            self._is_checkable = oth.IsCheckable
            self._is_checked = oth.IsChecked
            return
        else:
            if Image is UNO_NONE:
                self._image = None
            else:
                self._image = Image
            self._id = ID
            self._group_id = GroupID
            self._pre_item_id = PreItemID
            self._item_text = ItemText
            self._is_visible = IsVisible
            self._is_active = IsActive
            self._is_checkable = IsCheckable
            self._is_checked = IsChecked



    @property
    def Image(self) -> typing.Tuple[int, ...]:
        """
        sequence of bytes representing a possible image
        """
        return self._image
    
    @Image.setter
    def Image(self, value: typing.Tuple[int, ...]) -> None:
        self._image = value

    @property
    def ID(self) -> int:
        """
        unique ID of this menu item
        """
        return self._id
    
    @ID.setter
    def ID(self, value: int) -> None:
        self._id = value

    @property
    def GroupID(self) -> int:
        """
        unique ID of the group this menu item belongs to
        """
        return self._group_id
    
    @GroupID.setter
    def GroupID(self, value: int) -> None:
        self._group_id = value

    @property
    def PreItemID(self) -> int:
        """
        unique ID of the item directly above this menu item, used for fuzzy placement
        """
        return self._pre_item_id
    
    @PreItemID.setter
    def PreItemID(self, value: int) -> None:
        self._pre_item_id = value

    @property
    def ItemText(self) -> str:
        """
        text of the menu item
        """
        return self._item_text
    
    @ItemText.setter
    def ItemText(self, value: str) -> None:
        self._item_text = value

    @property
    def IsVisible(self) -> bool:
        """
        true if visible
        """
        return self._is_visible
    
    @IsVisible.setter
    def IsVisible(self, value: bool) -> None:
        self._is_visible = value

    @property
    def IsActive(self) -> bool:
        """
        true if active, so clickable
        """
        return self._is_active
    
    @IsActive.setter
    def IsActive(self, value: bool) -> None:
        self._is_active = value

    @property
    def IsCheckable(self) -> bool:
        """
        true if checkable, so there can be a checkmark
        """
        return self._is_checkable
    
    @IsCheckable.setter
    def IsCheckable(self, value: bool) -> None:
        self._is_checkable = value

    @property
    def IsChecked(self) -> bool:
        """
        true if there is a checkmark
        """
        return self._is_checked
    
    @IsChecked.setter
    def IsChecked(self, value: bool) -> None:
        self._is_checked = value


__all__ = ['MenuMultipleChange']
