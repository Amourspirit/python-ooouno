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
import typing
from abc import abstractproperty
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_completed_connection import XCompletedConnection as XCompletedConnection_98a0e46
from .x_database_access import XDatabaseAccess as XDatabaseAccess_c47a0c00
if typing.TYPE_CHECKING:
    from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class DatabaseAccess(XPropertySet_bc180bfa, XCompletedConnection_98a0e46, XDatabaseAccess_c47a0c00):
    """
    Service Class

    specifies a component, which controls DatabaseAccessConnections and acts like a shared DataSource.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatabaseAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DatabaseAccess'
    __ooo_type_name__: str = 'service'

    ConnectInfo: typing.TypeAlias = typing.Tuple[PropertyValue_c9610c73, ...]
    """
    is a list of arbitrary string tag/value pairs as connection arguments; normally at least a \"user\" and \"password\" property should be included.
    """

    TableFilter: typing.TypeAlias = typing.Tuple[str, ...]
    """
    defines a list of tables, on which the bean should have it's focus.
    
    If empty, all tables are rejected.
    """

    TableTypeFilter: typing.TypeAlias = typing.Tuple[str, ...]
    """
    defines a list of table types, on which the bean should have it's focus.
    
    If empty, all tables types are rejected.
    """

    @abstractproperty
    def ConnectURL(self) -> str:
        """
        indicates a database url of the form
        jdbc:subprotocol:subname or  sdbc:subprotocol:subname
        """
    @abstractproperty
    def IsPasswordRequired(self) -> bool:
        """
        indicates that a password is always necessary.
        """
    @abstractproperty
    def IsReadOnly(self) -> bool:
        """
        determines whether modifications on the data access bean are allowed or not.
        """
    @abstractproperty
    def NumberFormatsSupplier(self) -> 'XNumberFormatsSupplier_3afb0fb7':
        """
        provides an object for formatting numbers.
        """
    @abstractproperty
    def Title(self) -> str:
        """
        is the title of the bean.
        """
    @abstractproperty
    def URL(self) -> str:
        """
        is the URL of the bean.
        """

__all__ = ['DatabaseAccess']

