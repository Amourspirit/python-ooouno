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
# Namespace: com.sun.star.form
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FormComponentType(metaclass=UnoConstMeta, type_name="com.sun.star.form.FormComponentType", name_space="com.sun.star.form"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.form.FormComponentType``"""
        pass

    class FormComponentTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.form.FormComponentType", name_space="com.sun.star.form"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.form.FormComponentType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.form import FormComponentType as FormComponentType
    else:
        # keep document generators happy
        from ...lo.form.form_component_type import FormComponentType as FormComponentType

    class FormComponentTypeEnum(IntEnum):
        """
        Enum of Const Class FormComponentType

        These constants specify the class types used to identify a component.
        """
        CONTROL = FormComponentType.CONTROL
        """
        This generic identifier is for controls which cannot be identified by another specific identifier.
        """
        COMMANDBUTTON = FormComponentType.COMMANDBUTTON
        """
        specifies a control that is used to begin, interrupt, or end a process.
        """
        RADIOBUTTON = FormComponentType.RADIOBUTTON
        """
        specifies a control that acts like a radio button.
        
        Grouped together, such radio buttons present a set of two or more mutually exclusive choices to the user.
        """
        IMAGEBUTTON = FormComponentType.IMAGEBUTTON
        """
        specifies a control that displays an image that responds to mouse clicks.
        """
        CHECKBOX = FormComponentType.CHECKBOX
        """
        specifies a control that is used to check or uncheck to turn an option on or off.
        """
        LISTBOX = FormComponentType.LISTBOX
        """
        specifies a control that displays a list from which the user can select one or more items.
        """
        COMBOBOX = FormComponentType.COMBOBOX
        """
        specifies a control that is used when a list box combined with a static text control or an edit control is needed.
        """
        GROUPBOX = FormComponentType.GROUPBOX
        """
        specifies a control that displays a frame around a group of controls with or without a caption.
        """
        TEXTFIELD = FormComponentType.TEXTFIELD
        """
        specifies a control that is a text component that allows for the editing of a single line of text.
        """
        FIXEDTEXT = FormComponentType.FIXEDTEXT
        """
        specifies a control to display a fixed text, usually used to label other controls.
        """
        GRIDCONTROL = FormComponentType.GRIDCONTROL
        """
        is a table like control to display database data.
        """
        FILECONTROL = FormComponentType.FILECONTROL
        """
        specifies a control which can be used to enter text, extended by an (user-startable) file dialog to browse for files.
        """
        HIDDENCONTROL = FormComponentType.HIDDENCONTROL
        """
        specifies a control that should not be visible.
        """
        IMAGECONTROL = FormComponentType.IMAGECONTROL
        """
        specifies a control to display an image.
        """
        DATEFIELD = FormComponentType.DATEFIELD
        """
        specifies a control to display and edit a date value.
        """
        TIMEFIELD = FormComponentType.TIMEFIELD
        """
        specifies a control to display and edit a time value.
        """
        NUMERICFIELD = FormComponentType.NUMERICFIELD
        """
        specifies a field to display and edit a numeric value.
        """
        CURRENCYFIELD = FormComponentType.CURRENCYFIELD
        """
        specifies a field to display and edit a currency value.
        """
        PATTERNFIELD = FormComponentType.PATTERNFIELD
        """
        specifies a control to display and edit a string according to a pattern.
        """
        SCROLLBAR = FormComponentType.SCROLLBAR
        """
        specifies a control to display and edit, in the form of a scrollbar, a value from a continuous value range
        """
        SPINBUTTON = FormComponentType.SPINBUTTON
        """
        specifies a control to edit, in the form of a spin field, a value from a continuous range of values
        """
        NAVIGATIONBAR = FormComponentType.NAVIGATIONBAR
        """
        specifies a control which provides controller functionality for the com.sun.star.form.component.DataForm it belongs to, such as functionality to navigate or filter this form.
        """

__all__ = ['FormComponentType', 'FormComponentTypeEnum']
