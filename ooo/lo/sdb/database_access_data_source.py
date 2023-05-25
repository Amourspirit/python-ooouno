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
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_completed_connection import XCompletedConnection as XCompletedConnection_98a0e46
from ..sdbc.x_data_source import XDataSource as XDataSource_a2990ae7
if typing.TYPE_CHECKING:
    from com.sun.star.ucb.RememberAuthentication import RememberAuthenticationProto  # type: ignore

class DatabaseAccessDataSource(XPropertySet_bc180bfa, XCompletedConnection_98a0e46, XDataSource_a2990ae7):
    """
    Service Class

    is a factory to create data access beans.
    
    Data access beans are shared among components, so if an already existing bean is requested, the existing one is returned.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseAccessDataSource <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatabaseAccessDataSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DatabaseAccessDataSource'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def PasswordMode(self) -> RememberAuthenticationProto:
        """
        determines the password handling.
        """
        ...

    @abstractproperty
    def URL(self) -> str:
        """
        locates the database access bean.
        """
        ...


__all__ = ['DatabaseAccessDataSource']