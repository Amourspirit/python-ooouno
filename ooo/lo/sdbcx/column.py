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
# Namespace: com.sun.star.sdbcx
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5

class Column(XPropertySet_bc180bfa, XDataDescriptorFactory_46170fe5):
    """
    Service Class

    describes the common properties of a database column.

    See Also:
        `API Column <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Column.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Column'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultValue(self) -> str:
        """
        keeps a default value for a column, is provided as string.
        """
    @abstractproperty
    def Description(self) -> str:
        """
        keeps a description of the object.
        """
    @abstractproperty
    def IsAutoIncrement(self) -> bool:
        """
        indicates whether the column is automatically numbered, thus read-only.
        """
    @abstractproperty
    def IsCurrency(self) -> bool:
        """
        indicates whether the column is a cash value.
        """
    @abstractproperty
    def IsNullable(self) -> int:
        """
        indicates the nullability of values in the designated column.
        """
    @abstractproperty
    def IsRowVersion(self) -> bool:
        """
        indicates that the column contains some kind of time or date stamp used to track updates.
        """
    @abstractproperty
    def Name(self) -> str:
        """
        is the name of the column.
        """
    @abstractproperty
    def Precision(self) -> int:
        """
        gets a column's number of decimal digits.
        """
    @abstractproperty
    def Scale(self) -> int:
        """
        gets a column's number of digits to right of the decimal point.
        """
    @abstractproperty
    def Type(self) -> int:
        """
        is the com.sun.star.sdbc.DataType of the column.
        """
    @abstractproperty
    def TypeName(self) -> str:
        """
        is the type name used by the database.
        
        If the column type is a user-defined type, then a fully-qualified type name is returned.  Note:  May be empty.
        """

__all__ = ['Column']

