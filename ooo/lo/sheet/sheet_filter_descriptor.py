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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_sheet_filter_descriptor import XSheetFilterDescriptor as XSheetFilterDescriptor_47cc0ff7
from .x_sheet_filter_descriptor2 import XSheetFilterDescriptor2 as XSheetFilterDescriptor2_57f51029
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.table_orientation import TableOrientation as TableOrientation_ee780d84

class SheetFilterDescriptor(XPropertySet_bc180bfa, XSheetFilterDescriptor2_57f51029, XSheetFilterDescriptor_47cc0ff7):
    """
    Service Class

    represents a description of how a cell range is to be filtered.
    
    The descriptor contains properties and a collection of filter conditions (filter fields) which control the behavior of a filter operation.
    
    **since**
    
        OOo 3.2

    See Also:
        `API SheetFilterDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetFilterDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SheetFilterDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ContainsHeader(self) -> bool:
        """
        specifies if the first row (or column) contains headers which should not be filtered.
        """

    @abstractproperty
    def CopyOutputData(self) -> bool:
        """
        specifies if the filtered data should be copied to another position in the document.
        """

    @abstractproperty
    def IsCaseSensitive(self) -> bool:
        """
        specifies if the case of letters is important when comparing entries.
        """

    @abstractproperty
    def MaxFieldCount(self) -> int:
        """
        returns the maximum number of filter fields in the descriptor.
        
        This read-only property indicates the maximum count of fields the current implementation supports.
        """

    @abstractproperty
    def Orientation(self) -> 'TableOrientation_ee780d84':
        """
        specifies if columns or rows are filtered.
        """

    @abstractproperty
    def OutputPosition(self) -> 'CellAddress_ae5f0b56':
        """
        specifies the position where filtered data are to be copied.
        
        This is only used if SheetFilterDescriptor.CopyOutputData is TRUE.
        """

    @abstractproperty
    def SaveOutputPosition(self) -> bool:
        """
        specifies if the SheetFilterDescriptor.OutputPosition position is saved for future calls.
        
        This is only used if SheetFilterDescriptor.CopyOutputData is TRUE.
        """

    @abstractproperty
    def SkipDuplicates(self) -> bool:
        """
        specifies if duplicate entries are left out of the result.
        """

    @abstractproperty
    def UseRegularExpressions(self) -> bool:
        """
        specifies if the TableFilterField.StringValue strings are interpreted as regular expressions.
        """



__all__ = ['SheetFilterDescriptor']

