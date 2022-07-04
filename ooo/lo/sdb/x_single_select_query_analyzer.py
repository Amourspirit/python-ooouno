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
# Namespace: com.sun.star.sdb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XSingleSelectQueryAnalyzer(XInterface_8f010a43):
    """
    simplifies the analyzing of single select statements.
    
    The interface can be used for analyzing single SELECT statements without knowing the structure of the used query.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API XSingleSelectQueryAnalyzer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XSingleSelectQueryAnalyzer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XSingleSelectQueryAnalyzer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XSingleSelectQueryAnalyzer'

    @abstractmethod
    def getFilter(self) -> str:
        """
        returns the used filter.
        
        The filter criteria returned is part of the where condition of the select command, but it does not contain the where token.
        """
        ...
    @abstractmethod
    def getGroup(self) -> str:
        """
        returns the currently used GROUP BY.
        
        The group criteria returned is part of the GROUP BY clause of the select command, but it does not contain the GROUP BY keyword .
        """
        ...
    @abstractmethod
    def getGroupColumns(self) -> 'XIndexAccess_f0910d6d':
        """
        returns the currently used group.
        
        The columns returned from the GROUP BY clause.
        """
        ...
    @abstractmethod
    def getHavingClause(self) -> str:
        """
        returns the used HAVING filter.
        
        The HAVING filter criteria returned is part of the HAVING condition of the select command, but it does not contain the HAVING token.
        """
        ...
    @abstractmethod
    def getOrder(self) -> str:
        """
        returns the currently used sort order.
        
        The order criteria returned is part of the ORDER BY clause of the select command, but it does not contain the ORDER BY keyword .
        """
        ...
    @abstractmethod
    def getOrderColumns(self) -> 'XIndexAccess_f0910d6d':
        """
        returns the currently used sort order.
        
        The order criteria returned is part of the ORDER BY clause of the select command, but it does not contain the ORDER BY keyword .
        """
        ...
    @abstractmethod
    def getQuery(self) -> str:
        """
        returns the query.
        """
        ...
    @abstractmethod
    def getQueryWithSubstitution(self) -> str:
        """
        returns the query previously set at the analyzer, with all application-level features being substituted by their database-level counterparts.
        
        The XSingleSelectQueryAnalyzer is an application-level component, which in some respect understands SQL features usually not present at the database level. As a prominent example, you might pass a SELECT statement to the analyzer which is based on another query.
        
        While all other methods will handle those additional features transparently - e.g. the query in the FROM part of a SELECT statement will be handled as if it really is a table -, getQueryWithSubstitution gives you the SQL statement where all those features have been stripped, and replaced with appropriate standard SQL.
        
        For example, consider a database document which contains a client-side query named All Orders. This query is not known to the underlying database, so an SQL statement like SELECT * from \"All Orders\" would be rejected by the database. However, instantiating a SingleSelectQueryAnalyzer at the Connection object, and passing it the above query, you can then use getQueryWithSubstitution to retrieve a statement where \"All Orders\" has been replaced with the SELECT statement which actually constitutes the \"All Orders\" query.
        
        **since**
        
            OOo 2.0.4

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getStructuredFilter(self) -> 'typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]':
        """
        returns the currently used filter.
        
        The filter criteria is split into levels. Each level represents the OR criteria. Within each level, the filters are provided as an AND criteria with the name of the column and the filter condition. The filter condition is of type string. The operator used, is defined by com.sun.star.sdb.SQLFilterOperator.
        """
        ...
    @abstractmethod
    def getStructuredHavingClause(self) -> 'typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]':
        """
        returns the currently used HAVING filter.
        
        The HAVING filter criteria is split into levels. Each level represents the OR criteria. Within each level, the filters are provided as an AND criteria with the name of the column and the filter condition. The filter condition is of type string. The operator used, is defined by com.sun.star.sdb.SQLFilterOperator.
        """
        ...
    @abstractmethod
    def setCommand(self, Command: str, CommandType: int) -> None:
        """
        sets a new query for the composer, which may be expanded by filters, group by, having and sort criteria.
        
        In case of a CommandType of com.sun.star.sdb.CommandType.COMMAND, means in case the Command specifies an SQL statement, the inherited com.sun.star.sdbc.RowSet.EscapeProcessing becomes relevant:It then can be to used to specify whether the SQL statement should be analyzed on the client side before sending it to the database server.The default value for com.sun.star.sdbc.RowSet.EscapeProcessing is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setQuery(self, command: str) -> None:
        """
        sets a new query for the composer, which may be expanded by filters, group by, having and sort criteria.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...

__all__ = ['XSingleSelectQueryAnalyzer']

