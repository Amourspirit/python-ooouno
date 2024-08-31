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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_hierarchies_supplier import XHierarchiesSupplier as XHierarchiesSupplier_29a50f34
from ..util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .table_filter_field import TableFilterField as TableFilterField_ee760d53
    from com.sun.star.sheet.GeneralFunction import GeneralFunctionProto  # type: ignore
    from com.sun.star.sheet.DataPilotFieldOrientation import DataPilotFieldOrientationProto  # type: ignore

class DataPilotSourceDimension(XPropertySet_bc180bfa, XNamed_a6520b08, XHierarchiesSupplier_29a50f34, XCloneable_99d00aa3):
    """
    Service Class

    represents a dimension in a data pilot source.
    
    A dimension is equivalent to a column of a cell range in a spreadsheet used for a data pilot field.
    
    In more complex data sources, a dimension may contain several hierarchies, which consolidate items of a complex data type, called levels.
    
    Example: In a database, a column contains date values. This column will be a dimension of the data pilot source. One hierarchy may contain the 3 levels year, month, day. Another hierarchy may contain the 2 levels year and week number.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API DataPilotSourceDimension <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotSourceDimension.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotSourceDimension'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Filter(self) -> typing.Tuple[TableFilterField_ee760d53, ...]:
        """
        specifies which values are used.
        """
        ...

    @property
    @abstractmethod
    def Flags(self) -> int:
        """
        contains flags that control the usage of the dimension.
        """
        ...

    @property
    @abstractmethod
    def Function(self) -> GeneralFunctionProto:
        """
        specifies how data are aggregated.
        """
        ...

    @property
    @abstractmethod
    def Function2(self) -> int:
        """
        specifies how data are aggregated.
        
        **since**
        
            LibreOffice 5.3
        """
        ...

    @property
    @abstractmethod
    def IsDataLayoutDimension(self) -> bool:
        """
        contains TRUE if this is the dimension used to layout the different data dimensions.
        """
        ...

    @property
    @abstractmethod
    def Orientation(self) -> DataPilotFieldOrientationProto:
        """
        specifies where the dimension is used.
        """
        ...

    @property
    @abstractmethod
    def Original(self) -> XNamed_a6520b08:
        """
        returns the name of the dimension from which this dimension was cloned, or NULL if it was not cloned.
        """
        ...

    @property
    @abstractmethod
    def Position(self) -> int:
        """
        specifies the position of the dimension within its orientation.
        """
        ...

    @property
    @abstractmethod
    def UsedHierarchy(self) -> int:
        """
        specifies which hierarchy of the dimension is used.
        """
        ...


__all__ = ['DataPilotSourceDimension']