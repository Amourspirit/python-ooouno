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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_text_content import XTextContent as XTextContent_b16e0ba5
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class ContentControl(XTextContent_b16e0ba5):
    """
    Service Class

    This service specifies a content control with properties in a TextDocument.
    
    A content control wraps one or more text portions and controls the behavior of that content.
    
    **since**
    
        LibreOffice 7.4

    See Also:
        `API ContentControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1ContentControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.ContentControl'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Alias(self) -> str:
        """
        The alias: kind of a human-readable title / description, show up on the UI.
        
        -also used by VBA to group controls into a smaller, indexed collection
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def Appearance(self) -> str:
        """
        The appearance: just remembered.
        
        **since**
        
            LibreOffice 7.6
        """
        ...

    @property
    @abstractmethod
    def Checkbox(self) -> bool:
        """
        Display the content control as a checkbox.
        """
        ...

    @property
    @abstractmethod
    def Checked(self) -> bool:
        """
        If Checkbox is true, is the checkbox checked?
        """
        ...

    @property
    @abstractmethod
    def CheckedState(self) -> str:
        """
        If Checkbox is true, the value of a checked checkbox.
        """
        ...

    @property
    @abstractmethod
    def Color(self) -> str:
        """
        The color: just remembered.
        """
        ...

    @property
    @abstractmethod
    def ComboBox(self) -> bool:
        """
        Combo box that allows free-form text as well, i.e.
        
        not dropdown.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def CurrentDate(self) -> str:
        """
        Date in YYYY-MM-DDT00:00:00Z format.
        """
        ...

    @property
    @abstractmethod
    def DataBindingPrefixMappings(self) -> str:
        """
        The data bindings's prefix mappings: just remembered.
        """
        ...

    @property
    @abstractmethod
    def DataBindingStoreItemID(self) -> str:
        """
        The data bindings's store item ID: just remembered.
        """
        ...

    @property
    @abstractmethod
    def DataBindingXpath(self) -> str:
        """
        The data bindings's XPath: just remembered.
        """
        ...

    @property
    @abstractmethod
    def Date(self) -> bool:
        """
        Display the content control as a date.
        
        If true, a date picker is provided on the UI.
        """
        ...

    @property
    @abstractmethod
    def DateFormat(self) -> str:
        """
        If Date is true, the date format in a syntax accepted by the NumberFormatter.
        """
        ...

    @property
    @abstractmethod
    def DateLanguage(self) -> str:
        """
        If Date is true, the date's BCP 47 language tag.
        """
        ...

    @property
    @abstractmethod
    def DateString(self) -> str:
        """
        The formatted date string, based on DateFormat, DateLanguage and CurrentDate.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def DropDown(self) -> bool:
        """
        Drop-down that does not allow free-form text, i.e.
        
        not combo box.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def Id(self) -> int:
        """
        A unique numeric id, used by macros to identify a specific control.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def ListItems(self) -> typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]:
        """
        List items of a dropdown: DisplayText + Value pairs with string values for each item.
        """
        ...

    @property
    @abstractmethod
    def Lock(self) -> str:
        """
        Describes whether the control itself and/or its data can be modified or deleted by the user.
        
        **since**
        
            LibreOffice 7.6
        """
        ...

    @property
    @abstractmethod
    def MultiLine(self) -> str:
        """
        Indicates if the control accepts soft breaks.
        
        **since**
        
            LibreOffice 24.2
        """
        ...

    @property
    @abstractmethod
    def Picture(self) -> bool:
        """
        Display the content control as a picture.
        """
        ...

    @property
    @abstractmethod
    def PlaceholderDocPart(self) -> str:
        """
        The placeholder's doc part: just remembered.
        """
        ...

    @property
    @abstractmethod
    def PlainText(self) -> bool:
        """
        Plain text, i.e.
        
        not rich text.
        """
        ...

    @property
    @abstractmethod
    def ShowingPlaceHolder(self) -> bool:
        """
        Current content is placeholder text.
        """
        ...

    @property
    @abstractmethod
    def TabIndex(self) -> int:
        """
        Describes the order in which keyboard navigation moves between controls.
        
        **since**
        
            LibreOffice 7.6
        """
        ...

    @property
    @abstractmethod
    def Tag(self) -> str:
        """
        The tag: similar to Alias, but is meant to be machine-readable.
        
        -also used by VBA to group controls into a smaller, indexed collection
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def UncheckedState(self) -> str:
        """
        If Checkbox is true, the value of an unchecked checkbox.
        """
        ...


__all__ = ['ContentControl']

