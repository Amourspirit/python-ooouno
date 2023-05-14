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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import uno
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

    def __init__(self, Image: typing.Optional[uno.ByteSequence] = UNO_NONE, ID: typing.Optional[int] = 0, GroupID: typing.Optional[int] = 0, PreItemID: typing.Optional[int] = 0, ItemText: typing.Optional[str] = '', IsVisible: typing.Optional[bool] = False, IsActive: typing.Optional[bool] = False, IsCheckable: typing.Optional[bool] = False, IsChecked: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Image (uno.ByteSequence, optional): Image value.
            ID (int, optional): ID value.
            GroupID (int, optional): GroupID value.
            PreItemID (int, optional): PreItemID value.
            ItemText (str, optional): ItemText value.
            IsVisible (bool, optional): IsVisible value.
            IsActive (bool, optional): IsActive value.
            IsCheckable (bool, optional): IsCheckable value.
            IsChecked (bool, optional): IsChecked value.
        """
        super().__init__()

        if isinstance(Image, MenuMultipleChange):
            oth: MenuMultipleChange = Image
            self.Image = oth.Image
            self.ID = oth.ID
            self.GroupID = oth.GroupID
            self.PreItemID = oth.PreItemID
            self.ItemText = oth.ItemText
            self.IsVisible = oth.IsVisible
            self.IsActive = oth.IsActive
            self.IsCheckable = oth.IsCheckable
            self.IsChecked = oth.IsChecked
            return

        kargs = {
            "Image": Image,
            "ID": ID,
            "GroupID": GroupID,
            "PreItemID": PreItemID,
            "ItemText": ItemText,
            "IsVisible": IsVisible,
            "IsActive": IsActive,
            "IsCheckable": IsCheckable,
            "IsChecked": IsChecked,
        }
        if kargs["Image"] is UNO_NONE:
            kargs["Image"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._image = kwargs["Image"]
        self._id = kwargs["ID"]
        self._group_id = kwargs["GroupID"]
        self._pre_item_id = kwargs["PreItemID"]
        self._item_text = kwargs["ItemText"]
        self._is_visible = kwargs["IsVisible"]
        self._is_active = kwargs["IsActive"]
        self._is_checkable = kwargs["IsCheckable"]
        self._is_checked = kwargs["IsChecked"]


    @property
    def Image(self) -> uno.ByteSequence:
        """
        sequence of bytes representing a possible image
        """
        return self._image

    @Image.setter
    def Image(self, value: uno.ByteSequence) -> None:
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
