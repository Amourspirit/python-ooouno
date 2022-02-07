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
# Namespace: com.sun.star.sdbc
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_connection import XConnection as XConnection_a36a0b0c
from .x_warnings_supplier import XWarningsSupplier as XWarningsSupplier_ef210d99

class Connection(XComponent_98dc0ab5, XConnection_a36a0b0c, XWarningsSupplier_ef210d99):
    """
    Service Class

    represents a connection (session) with a specific database.
    
    Within the context of a Connection, SQL statements are executed and results are returned.
    
    A Connection's database is able to provide information describing its tables, its supported SQL grammar, its stored procedures, and the capabilities of this connection. This information is obtained with the com.sun.star.sdbc.XConnection.getMetaData() method.
    
    Note:  By default the Connection automatically commits changes after executing each statement. If auto commit has been disabled, an explicit commit must be done or database changes will not be saved.

    See Also:
        `API Connection <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1Connection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.Connection'
    __ooo_type_name__: str = 'service'


__all__ = ['Connection']

