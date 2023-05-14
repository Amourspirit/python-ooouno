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
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_action_listener import XActionListener as XActionListener_c7560c50
    from .x_item_listener import XItemListener as XItemListener_af710b81

class XComboBox(XInterface_8f010a43):
    """
    gives access to the items of a combo box and makes it possible to register item and action event listeners.

    See Also:
        `API XComboBox <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XComboBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XComboBox'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XComboBox'

    @abstractmethod
    def addActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        registers a listener for action events.
        """
        ...
    @abstractmethod
    def addItem(self, aItem: str, nPos: int) -> None:
        """
        adds an item at the specified position.
        """
        ...
    @abstractmethod
    def addItemListener(self, l: 'XItemListener_af710b81') -> None:
        """
        registers a listener for item events.
        """
        ...
    @abstractmethod
    def addItems(self, aItems: 'typing.Tuple[str, ...]', nPos: int) -> None:
        """
        adds multiple items at the specified position.
        """
        ...
    @abstractmethod
    def getDropDownLineCount(self) -> int:
        """
        returns the number of visible lines in the drop down mode.
        """
        ...
    @abstractmethod
    def getItem(self, nPos: int) -> str:
        """
        returns the item at the specified position.
        """
        ...
    @abstractmethod
    def getItemCount(self) -> int:
        """
        returns the number of items in the combo box.
        """
        ...
    @abstractmethod
    def getItems(self) -> 'typing.Tuple[str, ...]':
        """
        returns all items of the combo box.
        """
        ...
    @abstractmethod
    def removeActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        unregisters a listener for action events.
        """
        ...
    @abstractmethod
    def removeItemListener(self, l: 'XItemListener_af710b81') -> None:
        """
        unregisters a listener for item events.
        """
        ...
    @abstractmethod
    def removeItems(self, nPos: int, nCount: int) -> None:
        """
        removes a number of items at the specified position.
        """
        ...
    @abstractmethod
    def setDropDownLineCount(self, nLines: int) -> None:
        """
        sets the number of visible lines for drop down mode.
        """
        ...

__all__ = ['XComboBox']

