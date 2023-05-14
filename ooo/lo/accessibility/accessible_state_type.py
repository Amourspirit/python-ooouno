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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility


class AccessibleStateType(object):
    """
    Const Class

    Collection of state types.
    
    This list of constants defines the available set of states that an object that implements XAccessibleContext can be in.
    
    The comments describing the states is taken verbatim from the Java Accessibility API 1.4 documentation.
    
    We are using constants instead of a more typesafe enum. The reason for this is that IDL enums may not be extended. Therefore, in order to include future extensions to the set of roles we have to use constants here.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleStateType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleStateType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.AccessibleStateType'
    __ooo_type_name__: str = 'const'

    INVALID = 0
    """
    Indicates an invalid state.
    """
    ACTIVE = 1
    """
    Indicates a window is currently the active window.
    """
    ARMED = 2
    """
    Indicates that the object is armed.
    """
    BUSY = 3
    """
    Indicates the current object is busy.
    """
    CHECKED = 4
    """
    Indicates this object is currently checked.
    """
    DEFUNC = 5
    """
    User interface object corresponding to this object no longer exists.
    
    Indicates the user interface object corresponding to this object no longer exists.
    """
    EDITABLE = 6
    """
    Indicates the user can change the contents of this object.
    """
    ENABLED = 7
    """
    Indicates this object is enabled.
    """
    EXPANDABLE = 8
    """
    Indicates this object allows progressive disclosure of its children.
    """
    EXPANDED = 9
    """
    Indicates this object is expanded.
    """
    FOCUSABLE = 10
    """
    Object can accept the keyboard focus.
    
    Indicates this object can accept keyboard focus, which means all events resulting from typing on the keyboard will normally be passed to it when it has focus.
    """
    FOCUSED = 11
    """
    Indicates this object currently has the keyboard focus.
    """
    HORIZONTAL = 12
    """
    Indicates the orientation of this object is horizontal.
    """
    ICONIFIED = 13
    """
    Indicates this object is minimized and is represented only by an icon.
    """
    INDETERMINATE = 14
    """
    Sometimes UI elements can have a state indeterminate.
    
    This can happen e.g. if a check box reflects the bold state of text in a text processor. When the current selection contains text which is bold and also text which is not bold, the state is indeterminate.
    """
    MANAGES_DESCENDANTS = 15
    """
    Indicates the most (all) children are transient and it is not necessary to add listener to the children.
    
    Only the active descendant (given by the event) should be not transient to make it possible to add listener to this object and recognize changes in this object.
    
    The state is added to make a performance improvement. Now it is no longer necessary to iterate over all children to find out whether they are transient or not to decide whether to add listener or not. If there is an object with this state no one should iterate over the children to add listener. Only the active descendant should get listener if it is not transient.
    """
    MODAL = 16
    """
    Object is modal.
    
    Indicates something must be done with this object before the user can interact with an object in a different window.
    """
    MULTI_LINE = 17
    """
    Indicates this (text) object can contain multiple lines of text.
    """
    MULTI_SELECTABLE = 18
    """
    More than one child may be selected at the same time.
    
    Indicates this object allows more than one of its children to be selected at the same time.
    """
    OPAQUE = 19
    """
    Indicates this object paints every pixel within its rectangular region.
    """
    PRESSED = 20
    """
    Indicates this object is currently pressed.
    """
    RESIZABLE = 21
    """
    Indicates the size of this object is not fixed.
    """
    SELECTABLE = 22
    """
    Object is selectable.
    
    Indicates this object is the child of an object that allows its children to be selected, and that this child is one of those children that can be selected.
    """
    SELECTED = 23
    """
    Object is selected.
    
    Indicates this object is the child of an object that allows its children to be selected, and that this child is one of those children that has been selected.
    """
    SENSITIVE = 24
    """
    Indicates this object is sensitive.
    """
    SHOWING = 25
    """
    Object is displayed on the screen.
    
    An object has set the SHOWING state if itself and all of its parents have set the VISIBLE state and it lies at least partly inside the visible area of its parent. It is, though, not necessarily visible on the screen because it may be occluded by other objects.
    """
    SINGLE_LINE = 26
    """
    Indicates this (text) object can contain only a single line of text.
    """
    STALE = 27
    """
    Object information is stale and might not be up to date.
    
    Indicates that the information that is returned from this object might be out of sync with the application.
    """
    TRANSIENT = 28
    """
    Indicates this object is transient.
    """
    VERTICAL = 29
    """
    Indicates the orientation of this object is vertical.
    """
    VISIBLE = 30
    """
    Object wants to be displayed on the screen.
    
    A set VISIBLE state indicates that an object wants to be displayed on the screen. It is displayed, as indicated by a set SHOWING state, if all of its parents have also set the VISIBLE state and the object lies at least partly in the visible area of its parent.
    """
    MOVEABLE = 31
    """
    Indicates the position of the object is not fixed.
    """
    DEFAULT = 32
    """
    Indicates the object is the default button in a window.
    """
    OFFSCREEN = 33
    """
    Indicates the object is outside of the screen area.
    """
    COLLAPSE = 34
    """
    Indicates that the object is collapsed.
    """

__all__ = ['AccessibleStateType']
