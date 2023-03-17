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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from ..container.x_child import XChild as XChild_a6390b07
from .x_queries_supplier import XQueriesSupplier as XQueriesSupplier_d4920ccb
from .xsql_query_composer_factory import XSQLQueryComposerFactory as XSQLQueryComposerFactory_42300fbf
from ..sdbc.connection import Connection as Connection_98fe0ab4
from ..sdbcx.database_definition import DatabaseDefinition as DatabaseDefinition_9d00e3a

class DatabaseAccessConnection(Connection_98fe0ab4, DatabaseDefinition_9d00e3a, XChild_a6390b07, XQueriesSupplier_d4920ccb, XSQLQueryComposerFactory_42300fbf):
    """
    Service Class

    specifies a component, which supplies and stores additional information related to a certain database connection, such as, DatabaseQueries, FormDocuments, and ReportDocuments.
    
    Objects for data definition are supplied as well, for instance, Tables, Views, etc.
    
    Implements the service com.sun.star.sdbc.Connection. It is possible to open more than one connection at the same time, but the method com.sun.star.sdb.DatabaseAccessConnection.dispose() will close only one of these connections. You have to close all connections in order to close the connection to the database.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseAccessConnection <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatabaseAccessConnection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DatabaseAccessConnection'
    __ooo_type_name__: str = 'service'



__all__ = ['DatabaseAccessConnection']

