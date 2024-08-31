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
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
from abc import abstractmethod
from .descriptor import Descriptor as Descriptor_a5200b3b
from .x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from .x_keys_supplier import XKeysSupplier as XKeysSupplier_c8a70c64

class TableDescriptor(Descriptor_a5200b3b, XColumnsSupplier_f0600da9, XKeysSupplier_c8a70c64):
    """
    Service Class

    is used to define a table of a database.
    
    A table is described by its name and one or more columns and the keys for semantic rules.
    
    In addition, it may contain keys, and to define semantic rules for the table.  Note:  Indexes can only be appended when the table is already appended at the database.

    See Also:
        `API TableDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1TableDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.TableDescriptor'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CatalogName(self) -> str:
        """
        is the name of the table catalog.
        """
        ...

    @property
    @abstractmethod
    def Description(self) -> str:
        """
        supplies a comment on the table, Could be empty if not supported by the driver.
        """
        ...

    @property
    @abstractmethod
    def SchemaName(self) -> str:
        """
        is the name of the table schema.
        """
        ...


__all__ = ['TableDescriptor']

