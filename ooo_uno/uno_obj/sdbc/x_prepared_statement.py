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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection import XConnection as XConnection_a36a0b0c
    from .x_result_set import XResultSet as XResultSet_98e30aa7

class XPreparedStatement(XInterface_8f010a43):
    """
    provides the possibility of executing a precompiled SQL statement.
    
    A SQL statement is pre-compiled and stored in a PreparedStatement object. This object can then be used to efficiently execute this statement multiple times.

    See Also:
        `API XPreparedStatement <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XPreparedStatement.html>`_
    """

    @abstractmethod
    def execute(self) -> bool:
        """
        executes any kind of SQL statement.
        
        Some prepared statements return multiple results; the execute method handles these complex statements as well as the simpler form of statements handled by executeQuery and executeUpdate.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def executeQuery(self) -> 'XResultSet_98e30aa7':
        """
        executes the SQL query in this PreparedStatement object and returns the result set generated by the query.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def executeUpdate(self) -> int:
        """
        executes the SQL INSERT, UPDATE or DELETE statement in this com.sun.star.sdbc.PreparedStatement object.
        
        In addition, SQL statements that return nothing, such as SQL DDL statements, can be executed.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def getConnection(self) -> 'XConnection_a36a0b0c':
        """
        returns the com.sun.star.sdbc.Connection object that produced this com.sun.star.sdbc.Statement object.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XPreparedStatement']

