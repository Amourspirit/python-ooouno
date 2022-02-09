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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ui.dialogs
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ui.dialogs import ControlActions as ControlActions
else:
    from ....lo.ui.dialogs.control_actions import ControlActions as ControlActions


class ControlActionsEnum(IntEnum):
    """
    Enum of Const Class ControlActions

    Control actions for common and extended controls of a FilePicker.
    """
    ADD_ITEM = ControlActions.ADD_ITEM
    """
    Adds an item to the content of the listbox.
    
    The given item has to be a string.
    """
    ADD_ITEMS = ControlActions.ADD_ITEMS
    """
    Adds a sequence of strings to the content of the listbox.
    """
    DELETE_ITEM = ControlActions.DELETE_ITEM
    """
    Removes an item from a listbox.
    
    The given value has to be a position. If the position is invalid an exception will be thrown. The index of the first position is 0. The value should be a sal_Int32.
    """
    DELETE_ITEMS = ControlActions.DELETE_ITEMS
    """
    Removes all items from the listbox.
    """
    SET_SELECT_ITEM = ControlActions.SET_SELECT_ITEM
    """
    Selects an item in a listbox.
    
    The given value has to be a position. The index of the first position is 0. A value of -1 removes the selection. If the given position is invalid an exception will be thrown. The value should be a sal_Int32.
    """
    GET_ITEMS = ControlActions.GET_ITEMS
    """
    Returns all items of the listbox as a sequence of strings.
    """
    GET_SELECTED_ITEM = ControlActions.GET_SELECTED_ITEM
    """
    Returns the currently selected item.
    
    The returned item is an empty string if the listbox is empty or no item is selected.
    """
    GET_SELECTED_ITEM_INDEX = ControlActions.GET_SELECTED_ITEM_INDEX
    """
    Returns the zero based index of the currently selected item.
    
    If the listbox is empty or there is no item selected -1 will be returned. The returned value is a sal_Int32.
    """
    SET_HELP_URL = ControlActions.SET_HELP_URL
    """
    Sets the help URL of a control.
    """
    GET_HELP_URL = ControlActions.GET_HELP_URL
    """
    Retrieves the help URL of a control.
    """

__all__ = ['ControlActions', 'ControlActionsEnum']
