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
from .x_data_pilot_data_layout_field_supplier import XDataPilotDataLayoutFieldSupplier as XDataPilotDataLayoutFieldSupplier_c07142b
from .x_data_pilot_descriptor import XDataPilotDescriptor as XDataPilotDescriptor_27650f1a
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class DataPilotDescriptor(XPropertySet_bc180bfa, XDataPilotDataLayoutFieldSupplier_c07142b, XDataPilotDescriptor_27650f1a):
    """
    Service Class

    represents the description of the layout of a data pilot table.
    
    **since**
    
        OOo 3.3

    See Also:
        `API DataPilotDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ImportDescriptor(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        specifies parameters to create the data pilot table from a database.
        
        **since**
        
            OOo 3.3
        """
        ...

    @abstractproperty
    def ServiceArguments(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        specifies arguments that are passed to the implementation named by SourceServiceName.
        
        **since**
        
            OOo 3.3
        """
        ...

    @abstractproperty
    def ColumnGrand(self) -> bool:
        """
        specifies if columns for grand total results are created.
        """
        ...

    @abstractproperty
    def DrillDownOnDoubleClick(self) -> bool:
        """
        specifies whether to drill down to details or go into edit mode.
        """
        ...

    @abstractproperty
    def GrandTotalName(self) -> str:
        """
        specifies a label for grand total results.
        
        **since**
        
            OOo 3.4
        """
        ...

    @abstractproperty
    def IgnoreEmptyRows(self) -> bool:
        """
        specifies if empty rows in the source data are ignored.
        """
        ...

    @abstractproperty
    def RepeatIfEmpty(self) -> bool:
        """
        specifies if empty category cells in the source data should be treated as repetition of the content from the previous row.
        """
        ...

    @abstractproperty
    def RowGrand(self) -> bool:
        """
        specifies if rows for grand total results are created.
        """
        ...

    @abstractproperty
    def ShowFilterButton(self) -> bool:
        """
        specifies whether the filter button is shown.
        """
        ...

    @abstractproperty
    def SourceServiceName(self) -> str:
        """
        specifies the name of a DataPilotSource implementation for the data pilot table.
        
        **since**
        
            OOo 3.3
        """
        ...



__all__ = ['DataPilotDescriptor']

