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
# Namespace: com.sun.star.inspection
from ooo_uno.base.const import ConstIntBase


class PropertyControlType(ConstIntBase):
    """
    describes pre-defined possible control types to be used to display and enter property values within an ObjectInspector.
    
    The type of a control determines its visual appearance, its behavior, and - important for property handlers using a control - the expected type when reading and writing the control's value.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API PropertyControlType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1inspection_1_1PropertyControlType.html>`_
    """
    ListBox = 1
    """
    denotes a control which allows the user to choose from a list of possible property values
    
    Controls of type ListBox exchange their values as string.
    
    Additionally, those controls support the XStringListControl interface.
    """
    ComboBox = 2
    """
    denotes a control which allows the user to choose from a list of possible property values, combined with the possibility to enter a new property value.
    
    Controls of type ComboBox exchange their values as string.
    
    Additionally, those controls support the XStringListControl interface.
    """
    TextField = 3
    """
    denotes a control which allows the user to enter property values consisting of a single line of text
    
    Controls of type TextField exchange their values as string.
    """
    MultiLineTextField = 4
    """
    denotes a control which allows the user to enter pure text, including line breaks
    
    Controls of type MultiLineTextField exchange their values as string.
    """
    CharacterField = 5
    """
    denotes a control which allows the user to enter a single character
    
    Controls of type CharacterField exchange their values as short, being a single UTF-16 character.
    """
    StringListField = 6
    """
    denotes a control which allows the user to enter a list of single-line strings
    
    Controls of type StringListField exchange their values as sequence< string >.
    """
    ColorListBox = 7
    """
    denotes a control which allows the user to choose from a list of colors.
    
    Controls of type ColorListBox usually exchange their values as com.sun.star.util.Color.
    
    Additionally, those controls support the XStringListControl interface. If you use this interface to add additional entries to the list box, which have no color associated with it, then you can also exchange values as string. That is, if you write a string into XPropertyControl.Value, and if this string has previously been added to the list using the XStringListControl interface, this string is selected. Vice versa, if the user selects one of those non-color strings in the list, then reading XPropertyControl.Value will retrieve you this string.
    """
    NumericField = 8
    """
    denotes a control which allows the user to enter a numerical value
    
    Controls of type NumericField exchange their values as double.
    
    Additionally, those controls support the XNumericControl interface.
    """
    DateField = 9
    """
    denotes a control which allows the user to enter a date value
    
    Controls of type DateField exchange their values as com.sun.star.util.Date.
    """
    TimeField = 10
    """
    denotes a control which allows the user to enter a time value
    
    Controls of type TimeField exchange their values as com.sun.star.util.Time.
    """
    DateTimeField = 11
    """
    denotes a control which allows the user to enter a combined date/time value
    
    Controls of type DateTimeField exchange their values as com.sun.star.util.DateTime.
    """
    HyperlinkField = 12
    """
    denotes a control which displays a string in a hyperlink-like appearance
    
    Controls of type HyperlinkField exchange their values as string.
    
    Additionally, those controls support the XHyperlinkControl interface.
    """
    Unknown = 13
    """
    denotes a non-standard property control, which is usually provided by an XPropertyHandler
    """

