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
from abc import abstractproperty
from .connection_properties import ConnectionProperties as ConnectionProperties_1a9f0ee1

class ODBCConnectionProperties(ConnectionProperties_1a9f0ee1):
    """
    represents the properties for an ODBC connection (session) with a specific database.
    
    These properties can be used when calling the method com.sun.star.sdbc.XDriver.connect() or com.sun.star.sdbc.XDriverManager.getConnectionWithInfo().
    
    The properties for a connection contain additional information about how to connect to a database and how to control the behavior of the resulting connection should be.

    See Also:
        `API ODBCConnectionProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1ODBCConnectionProperties.html>`_
    """

    @abstractproperty
    def AutoRetrievingStatement(self) -> str:
        """
        specifies the statement which should be executed when asking an \"INSERT\" statement for the XGeneratedResultSet (future concept) interface.
        """
    @abstractproperty
    def CharSet(self) -> str:
        """
        specifies the encoding to use to translate the backend data
        
        See the IANA character set list for a list of valid values.
        """
    @abstractproperty
    def IsAutoRetrievingEnabled(self) -> bool:
        """
        specifies if retrieving of auto generated values should be enabled or not.
        
        If TRUE than the statement will support the XGeneratedResultSet (future concept) interface, otherwise not.
        """
    @abstractproperty
    def ParameterNameSubstitution(self) -> bool:
        """
        should the parameter \"?\" in prepared statement be substituted with an distinct name
        """
    @abstractproperty
    def Silent(self) -> bool:
        """
        Silent - should the connection be silent.
        
        No user interaction while creating the connection.
        """
    @abstractproperty
    def Timeout(self) -> int:
        """
        the Timeout after which time a timeout should happen
        """
    @abstractproperty
    def UseCatalog(self) -> bool:
        """
        should the driver should support a catalog.
        """

__all__ = ['ODBCConnectionProperties']

