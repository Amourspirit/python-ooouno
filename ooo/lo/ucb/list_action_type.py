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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb


class ListActionType(object):
    """
    Const Class

    These values are used to specify the type of change happened to a list.
    
    A change happened is sent from an XDynamicResultSet as ListAction to a XDynamicResultSetListener.
    
    The values are contained in ListAction.ListActionType.

    See Also:
        `API ListActionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1ListActionType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ListActionType'
    __ooo_type_name__: str = 'const'

    WELCOME = 20
    """
    First notification to a single listener for purpose of initialization.
    
    This type of notification is required to be sent first and only once to a new listener.
    
    The member ListAction.ActionInfo is required to contain a struct WelcomeDynamicResultSetStruct. This struct contains two com.sun.star.sdbc.XResultSets (old and new). During and after the notification only the new set is valid for access. But the listener is required to remind both com.sun.star.sdbc.XResultSets as he will not get another chance to get them again.
    
    The members ListAction.Count and ListAction.Position are not used.
    """
    INSERTED = 21
    """
    One or more rows were inserted into the list.
    
    This action is related to ContentAction.INSERTED.
    
    The members ListAction.Count and ListAction.Position contain the position and count of newly inserted rows. If the count is greater than one, the inserted rows have to be one after the other.
    
    ListAction.ActionInfo could contain something but this is not required. For example, it could contain the properties of the new rows (i.e. for remote optimizing), but this is not required nor unrestrictedly recommended.
    """
    REMOVED = 22
    """
    One or more rows were removed from the list.
    
    This action is related to ContentAction.REMOVED.
    
    The members ListAction.Count and ListAction.Position contain the position and count of the removed rows. If the count is greater than one, the removed rows have to be one after the other.
    
    The member ListAction.ListActionType is not used.
    """
    CLEARED = 23
    """
    The whole list was destroyed and independently rebuild.
    
    If \"CLEARED\" is sent you don't need to refer to the old ResultSet.
    
    The members ListAction.ListActionType, ListAction.Count and ListAction.Position are ignored.
    """
    MOVED = 24
    """
    One or more rows were moved to another position.
    
    The members ListAction.Count and ListAction.Position contain the position and count of the moved rows. If the count is greater than one, the moved rows have to be one after the other.
    
    ListAction.ListActionType is required to contain a \"long\", which gives the shift of position. (i.e. When two rows at position 3 and 4 are moved for a shift \"+1\", they will appear at the positions 4 and 5. In this action is included, that the row on old position 5 now appears on position 3. No other notification is needed, to explain or complete this action).
    """
    PROPERTIES_CHANGED = 25
    """
    The properties of one or more rows have changed.
    
    This action is related to a com.sun.star.beans.PropertyChangeEvent.
    
    The members ListAction.Count and ListAction.Position contain the position and count of the rows, whose properties have changed. If the count is greater than one, the rows with modified properties have to be one after the other.
    
    ListAction.ActionInfo could contain something but this is not required. For example, it could contain the new properties (i.e. for remote optimizing), but this is not required nor unrestrictedly recommended.
    """
    COMPLETED = 27

__all__ = ['ListActionType']
