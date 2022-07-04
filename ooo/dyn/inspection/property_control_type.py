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
# Libre Office Version: 7.3
# Namespace: com.sun.star.inspection
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class PropertyControlType(metaclass=UnoConstMeta, type_name="com.sun.star.inspection.PropertyControlType", name_space="com.sun.star.inspection"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.inspection.PropertyControlType``"""
        pass

    class PropertyControlTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.inspection.PropertyControlType", name_space="com.sun.star.inspection"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.inspection.PropertyControlType`` as Enum values"""
        pass

else:
    from ...lo.inspection.property_control_type import PropertyControlType as PropertyControlType

    class PropertyControlTypeEnum(IntEnum):
        """
        Enum of Const Class PropertyControlType

        describes pre-defined possible control types to be used to display and enter property values within an ObjectInspector.
        
        The type of a control determines its visual appearance, its behavior, and - important for property handlers using a control - the expected type when reading and writing the control's value.
        
        **since**
        
            OOo 2.0.3
        """
        ListBox = PropertyControlType.ListBox
        """
        denotes a control which allows the user to choose from a list of possible property values
        
        Controls of type ListBox exchange their values as string.
        
        Additionally, those controls support the XStringListControl interface.
        """
        ComboBox = PropertyControlType.ComboBox
        """
        denotes a control which allows the user to choose from a list of possible property values, combined with the possibility to enter a new property value.
        
        Controls of type ComboBox exchange their values as string.
        
        Additionally, those controls support the XStringListControl interface.
        """
        TextField = PropertyControlType.TextField
        """
        denotes a control which allows the user to enter property values consisting of a single line of text
        
        Controls of type TextField exchange their values as string.
        """
        MultiLineTextField = PropertyControlType.MultiLineTextField
        """
        denotes a control which allows the user to enter pure text, including line breaks
        
        Controls of type MultiLineTextField exchange their values as string.
        """
        CharacterField = PropertyControlType.CharacterField
        """
        denotes a control which allows the user to enter a single character
        
        Controls of type CharacterField exchange their values as short, being a single UTF-16 character.
        """
        StringListField = PropertyControlType.StringListField
        """
        denotes a control which allows the user to enter a list of single-line strings
        
        Controls of type StringListField exchange their values as sequence< string >.
        """
        ColorListBox = PropertyControlType.ColorListBox
        """
        denotes a control which allows the user to choose from a list of colors.
        
        Controls of type ColorListBox usually exchange their values as com.sun.star.util.Color.
        
        Additionally, those controls support the XStringListControl interface. If you use this interface to add additional entries to the list box, which have no color associated with it, then you can also exchange values as string. That is, if you write a string into XPropertyControl.Value, and if this string has previously been added to the list using the XStringListControl interface, this string is selected. Vice versa, if the user selects one of those non-color strings in the list, then reading XPropertyControl.Value will retrieve you this string.
        """
        NumericField = PropertyControlType.NumericField
        """
        denotes a control which allows the user to enter a numerical value
        
        Controls of type NumericField exchange their values as double.
        
        Additionally, those controls support the XNumericControl interface.
        """
        DateField = PropertyControlType.DateField
        """
        denotes a control which allows the user to enter a date value
        
        Controls of type DateField exchange their values as com.sun.star.util.Date.
        """
        TimeField = PropertyControlType.TimeField
        """
        denotes a control which allows the user to enter a time value
        
        Controls of type TimeField exchange their values as com.sun.star.util.Time.
        """
        DateTimeField = PropertyControlType.DateTimeField
        """
        denotes a control which allows the user to enter a combined date/time value
        
        Controls of type DateTimeField exchange their values as com.sun.star.util.DateTime.
        """
        HyperlinkField = PropertyControlType.HyperlinkField
        """
        denotes a control which displays a string in a hyperlink-like appearance
        
        Controls of type HyperlinkField exchange their values as string.
        
        Additionally, those controls support the XHyperlinkControl interface.
        """
        Unknown = PropertyControlType.Unknown
        """
        denotes a non-standard property control, which is usually provided by an XPropertyHandler
        """

__all__ = ['PropertyControlType', 'PropertyControlTypeEnum']
