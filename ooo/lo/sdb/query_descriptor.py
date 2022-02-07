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
# Namespace: com.sun.star.sdb
from abc import abstractproperty
from .data_settings import DataSettings as DataSettings_a3000b0c
from ..sdbcx.descriptor import Descriptor as Descriptor_a5200b3b
from ..sdbcx.x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from ..sdbcx.x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5

class QueryDescriptor(DataSettings_a3000b0c, Descriptor_a5200b3b, XColumnsSupplier_f0600da9, XDataDescriptorFactory_46170fe5):
    """
    Service Class

    is a stored definition of a SQL \"Select statement\".
    
    It can be used, if there is a need to execute SQL statement more than once or if you want to format the query result fields different from the underlying table definitions.

    See Also:
        `API QueryDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1QueryDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.QueryDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Command(self) -> str:
        """
        is the command of the query, this is typically a select statement.
        """
    @abstractproperty
    def EscapeProcessing(self) -> bool:
        """
        should we use escape processing for the query.
        """
    @abstractproperty
    def UpdateCatalogName(self) -> str:
        """
        is the name of the update table catalog.
        """
    @abstractproperty
    def UpdateSchemaName(self) -> str:
        """
        is the name of the update table schema.
        """
    @abstractproperty
    def UpdateTableName(self) -> str:
        """
        is the name of the table which should be updated.
        
        This is usually used for queries which relate on more than one table.
        """

__all__ = ['QueryDescriptor']

