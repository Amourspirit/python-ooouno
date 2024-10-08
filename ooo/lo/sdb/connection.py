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
# Namespace: com.sun.star.sdb
from __future__ import annotations
from ..container.x_child import XChild as XChild_a6390b07
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from .x_command_preparation import XCommandPreparation as XCommandPreparation_fad90ddd
from .x_queries_supplier import XQueriesSupplier as XQueriesSupplier_d4920ccb
from .xsql_query_composer_factory import XSQLQueryComposerFactory as XSQLQueryComposerFactory_42300fbf
from ..sdbc.connection import Connection as Connection_98fe0ab4
from ..sdbcx.database_definition import DatabaseDefinition as DatabaseDefinition_9d00e3a

class Connection(Connection_98fe0ab4, DatabaseDefinition_9d00e3a, XChild_a6390b07, XMultiServiceFactory_191e0eb6, XCommandPreparation_fad90ddd, XQueriesSupplier_d4920ccb, XSQLQueryComposerFactory_42300fbf):
    """
    Service Class

    extends the com.sun.star.sdbc.Connection of SDBC by providing the data definitions of a connected database.

    See Also:
        `API Connection <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1Connection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.Connection'
    __ooo_type_name__: str = 'service'


__all__ = ['Connection']

