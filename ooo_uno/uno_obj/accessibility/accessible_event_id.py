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
# Namespace: com.sun.star.accessibility
from ooo_uno.base.const import ConstIntBase


class AccessibleEventId(ConstIntBase):
    """
    These constants identify the type of AccessibleEventObject objects.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain, where applicable and not otherwise stated, the old and new value of the property in question.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleEventId <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleEventId.html>`_
    """
    NAME_CHANGED = 1
    """
    Use this event type to indicate a change of the name string of an accessible object.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the name before and after the change.
    """
    DESCRIPTION_CHANGED = 2
    """
    Use this event type to indicate a change of the description string of an accessible object.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the description before and after the change.
    """
    ACTION_CHANGED = 3
    """
    The change of the number or attributes of actions of an accessible object is signaled by events of this type.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new number of actions.
    """
    STATE_CHANGED = 4
    """
    State changes are signaled with this event type.
    
    Use one event for every state that is set or reset. The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new value respectively. To set a state put the state id into the AccessibleEventObject.NewValue field and leave AccessibleEventObject.OldValue empty. To reset a state put the state id into the AccessibleEventObject.OldValue field and leave AccessibleEventObject.NewValue empty.
    """
    ACTIVE_DESCENDANT_CHANGED = 5
    """
    Constant used to determine when the active descendant of a component has changed.
    
    The active descendant is used in objects with transient children. The AccessibleEventObject.NewValue contains the now active object. The AccessibleEventObject.OldValue contains the previously active child. Empty references indicate that no child has been respectively is currently active.
    """
    BOUNDRECT_CHANGED = 6
    """
    This event indicates a change of the bounding rectangle of an accessible object with respect only to its size or relative position.
    
    If the absolute position changes but not the relative position then it is not necessary to send an event.
    
    Use this event rather than the VISIBLE_DATA_EVENT when really only the (relative) bounding box of an accessible object has changed. It is much more specific than the later one and reduces the number of calls an AT-Tool has to make to retrieve all affected data.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue remain empty. Use a call to the XAccessibleComponent.getBounds() method to determine the new bounding box.
    """
    CHILD = 7
    """
    A child event indicates the addition of a new or the removal of an existing child.
    
    The contents of the AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields determines which of both has taken place.
    
    If a new child has been added then the AccessibleEventObject.NewValue contains a reference to this new object and AccessibleEventObject.OldValue remains empty.
    
    If a child has been removed then the AccessibleEventObject.OldValue contains a reference to this object and AccessibleEventObject.NewValue remains empty.
    
    If a child has been added and another one has been removed don't set both fields at the same. Send separate events instead.
    
    Note that a child event is sent after a child has been added or removed. Especially in the case of a removal this means that the removed object does not have a parent anymore.
    """
    INVALIDATE_ALL_CHILDREN = 8
    """
    Use this event to tell the listeners to re-retrieve the whole set of children.
    
    This should be used by a parent object which exchanges all or most of its children. It is a short form of first sending one CHILD event for every old child indicating that this child is about to be removed and then sending one CHILD for every new child indicating that this child has been added to the list of children.
    
    When this API is used by Java or Gnome AT-Tools then a bridge can generate the events described above automatically.
    """
    SELECTION_CHANGED = 9
    """
    Events of this type indicate changes of the selection.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields remain empty.
    """
    VISIBLE_DATA_CHANGED = 10
    """
    A visible data event indicates the change of the visual appearance of an accessible object.
    
    This includes for example most of the attributes available over the XAccessibleComponent and XAccessibleExtendedComponent interfaces. The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields are left empty.
    """
    VALUE_CHANGED = 11
    """
    This constant indicates changes of the value of an XAccessibleValue interface.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue field contain the old and new value as a number. Its exact type is implementation dependent but has to be the same as is returned by the XAccessibleValue.getCurrentValue() function.
    """
    CONTENT_FLOWS_FROM_RELATION_CHANGED = 12
    """
    Identifies the change of a relation set: The content flow has changed.
    
    Not used: The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain references to the old and new predecessor. Note that both references my be NULL to indicate that a flow to the sending object has not existed or does not exist anymore.
    """
    CONTENT_FLOWS_TO_RELATION_CHANGED = 13
    """
    Identifies the change of a relation set: The content flow has changed.
    
    Not used: The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain references to the old and new successor. Note that both references my be NULL to indicate that a flow from the sending object has not existed or does not exist anymore.
    """
    CONTROLLED_BY_RELATION_CHANGED = 14
    """
    Identifies the change of a relation set: The target object that is doing the controlling has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new controlling objects.
    """
    CONTROLLER_FOR_RELATION_CHANGED = 15
    """
    Identifies the change of a relation set: The controller for the target object has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new number of controlled objects.
    """
    LABEL_FOR_RELATION_CHANGED = 16
    """
    Identifies the change of a relation set: The target group for a label has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new number labeled objects.
    """
    LABELED_BY_RELATION_CHANGED = 17
    """
    Identifies the change of a relation set: The objects that are doing the labeling have changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new accessible label.
    """
    MEMBER_OF_RELATION_CHANGED = 18
    """
    Identifies the change of a relation set: The group membership has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new number of members.
    """
    SUB_WINDOW_OF_RELATION_CHANGED = 19
    """
    Identifies the change of a relation set: The sub-window-of relation has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new accessible parent window objects.
    """
    CARET_CHANGED = 20
    """
    Events of this type are sent when the caret has moved to a new position.
    
    The old and new position can be found in the AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields.
    """
    TEXT_SELECTION_CHANGED = 21
    """
    Events of this type signal changes of the selection.
    
    The old or new selection is not available through the event object. You have to query the XAccessibleText interface of the event source for this information. The type of content of the AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields is not specified at the moment. This may change in the future.
    """
    TEXT_CHANGED = 22
    """
    Use this id to indicate general text changes, i.e.
    
    changes to text that is exposed through the XAccessibleText and XAccessibleEditableText interfaces.
    
    The affected text ranges are represented by com.sun.star.accessibility.TextSegment structures.
    
    The content of the AccessibleEventObject.OldValue and AccessibleEventObject.NewValue expresses the type of text change:
    
    When broadcasting an event always prefer the first three cases to the last one. Use it only as a last resort.
    
    Text ranges should be as small as possible but, of course, include all the text that is involved in a modification. That means that when two or more discontinuous text ranges are inserted, deleted, or otherwise modified the two fields of the event have to cover all the affected text ranges as well as the text in between.
    """
    TEXT_ATTRIBUTE_CHANGED = 23
    """
    This entry is reserved for future extension.
    
    Don't use it right now.
    """
    HYPERTEXT_CHANGED = 24
    """
    Constant used to indicate that a hypertext element has received focus.
    
    The AccessibleEventObject.OldValue field contains the start index of previously focused element. The AccessibleEventObject.NewValue field holds the start index in the document of the current element that has focus. A value of -1 indicates that an element does not or did not have focus.
    """
    TABLE_CAPTION_CHANGED = 25
    """
    Constant used to indicate that the table caption has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new accessible objects representing the table caption.
    """
    TABLE_COLUMN_DESCRIPTION_CHANGED = 26
    """
    Constant used to indicate that the column description has changed.
    
    The AccessibleEventObject.NewValue field contains the column index. The AccessibleEventObject.OldValue is left empty.
    """
    TABLE_COLUMN_HEADER_CHANGED = 27
    """
    Constant used to indicate that the column header has changed.
    
    The AccessibleEventObject.OldValue is empty, the AccessibleEventObject.NewValue field contains an AccessibleTableModelChange representing the header change.
    """
    TABLE_MODEL_CHANGED = 28
    """
    Constant used to indicate that the table data has changed.
    
    The AccessibleEventObject.OldValue is empty, the AccessibleEventObject.NewValue field contains an AccessibleTableModelChange representing the data change.
    """
    TABLE_ROW_DESCRIPTION_CHANGED = 29
    """
    Constant used to indicate that the row description has changed.
    
    The AccessibleEventObject.NewValue field contains the row index. The AccessibleEventObject.OldValue is left empty.
    """
    TABLE_ROW_HEADER_CHANGED = 30
    """
    Constant used to indicate that the row header has changed.
    
    The AccessibleEventObject.OldValue is empty, the AccessibleEventObject.NewValue field contains an AccessibleTableModelChange representing the header change.
    """
    TABLE_SUMMARY_CHANGED = 31
    """
    Constant used to indicate that the table summary has changed.
    
    The AccessibleEventObject.OldValue and AccessibleEventObject.NewValue fields contain the old and new accessible objects representing the table summary.
    """
    LISTBOX_ENTRY_EXPANDED = 32
    """
    Constant used to indicate that a list box entry has been expanded.
    
    AccessibleEventObject.OldValue is empty. AccessibleEventObject.NewValue contains the expanded list box entry.
    
    **since**
    
        OOo 3.2
    """
    LISTBOX_ENTRY_COLLAPSED = 33
    """
    Constant used to indicate that a list box entry has been collapsed.
    
    AccessibleEventObject.OldValue is empty. AccessibleEventObject.NewValue contains the collapsed list box entry.
    
    **since**
    
        OOo 3.2
    """
    ACTIVE_DESCENDANT_CHANGED_NOFOCUS = 34
    """
    Constant used to determine when the active descendant of a component has been removed but unlike ACTIVE_DESCENDANT_CHANGED the descendant that is to be removed does not have focus.
    
    The active descendant is used in objects with transient children.
    
    AccessibleEventObject.OldValue contains the item to be removed.
    
    AccessibleEventObject.NewValue is empty.
    
    **since**
    
        LibreOffice 4.3
    """
    SELECTION_CHANGED_ADD = 35
    """
    An item in a container has been added to an already present selection.
    
    Example: a second list item has been selected in a listbox.
    
    AccessibleEventObject.OldValue is empty.
    
    AccessibleEventObject.NewValue contains the item to be added.
    
    **since**
    
        LibreOffice 4.3
    """
    SELECTION_CHANGED_REMOVE = 36
    """
    An item in a container has been removed from the selection.
    
    AccessibleEventObject.OldValue contains the item to be removed.
    
    AccessibleEventObject.NewValue is empty.
    
    **since**
    
        LibreOffice 4.3
    """
    SELECTION_CHANGED_WITHIN = 37
    """
    Multiple items in a container object have been added or removed from the selection.
    
    AccessibleEventObject.OldValue and AccessibleEventObject.NewValue is empty.
    
    **since**
    
        LibreOffice 4.3
    """
    PAGE_CHANGED = 38
    """
    A change of page or slide.
    
    **since**
    
        LibreOffice 4.3
    """
    SECTION_CHANGED = 39
    """
    The cursor has moved to/from a section.
    
    **since**
    
        LibreOffice 4.3
    """
    COLUMN_CHANGED = 40
    """
    The cursor has moved to/from a section.
    
    **since**
    
        LibreOffice 4.3
    """
    ROLE_CHANGED = 41
    """
    Constant used to indicate that the role of an accessible object has changed.
    
    **since**
    
        LibreOffice 4.3
    """

