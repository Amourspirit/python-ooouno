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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_sheet_condition import XSheetCondition as XSheetCondition_e1940d19
if typing.TYPE_CHECKING:
    from com.sun.star.sheet.ValidationAlertStyle import ValidationAlertStyleProto
    from com.sun.star.sheet.ValidationType import ValidationTypeProto

class TableValidation(XPropertySet_bc180bfa, XSheetCondition_e1940d19):
    """
    Service Class

    represents the data validation settings for a cell or cell range.

    See Also:
        `API TableValidation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1TableValidation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TableValidation'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ErrorAlertStyle(self) -> ValidationAlertStyleProto:
        """
        specifies the style of the error message.
        
        This is used only if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...

    @abstractproperty
    def ErrorMessage(self) -> str:
        """
        specifies the text of the error message.
        
        This is only used if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...

    @abstractproperty
    def ErrorTitle(self) -> str:
        """
        specifies the title of the window showing the error message.
        
        This is only used if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...

    @abstractproperty
    def IgnoreBlankCells(self) -> bool:
        """
        specifies if blank cells should be allowed.
        """
        ...

    @abstractproperty
    def InputMessage(self) -> str:
        """
        specifies the text of the input message.
        
        This is only used if TableValidation.ShowInputMessage is set to TRUE.
        """
        ...

    @abstractproperty
    def InputTitle(self) -> str:
        """
        specifies the title of the window showing the input message.
        
        This is only used if TableValidation.ShowInputMessage is set to TRUE.
        """
        ...

    @abstractproperty
    def ShowErrorMessage(self) -> bool:
        """
        specifies if an error message is displayed when invalid data is entered.
        """
        ...

    @abstractproperty
    def ShowInputMessage(self) -> bool:
        """
        specifies if an input message is shown when the cursor is in a cell with these validation settings.
        """
        ...

    @abstractproperty
    def ShowList(self) -> int:
        """
        specifies if the list of possible values should be shown on the cell and how.
        
        See also TableValidationVisibility
        """
        ...

    @abstractproperty
    def Type(self) -> ValidationTypeProto:
        """
        specifies the type of validation.
        """
        ...


__all__ = ['TableValidation']

