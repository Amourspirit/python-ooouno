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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdb import ErrorCondition
else:
    from ...lo.sdb.error_condition import ErrorCondition as ErrorCondition


class ErrorConditionEnum(IntEnum):
    """
    Enum of Const Class ErrorCondition

    defines error conditions for OpenOffice.org Base core components
    
    Core components of OpenOffice.org will use those error conditions as error codes (com.sun.star.sdbc.SQLException.ErrorCode) wherever possible.
    That is, if an SQLException is raised by such a component, caused by an error condition which is included in the ErrorCondition group, then the respective negative value will be used as ErrorCode.
    
    This allows to determine specific error conditions in your client code, and to handle it appropriately.
    
    Note that before you examine the ErrorCode member of a caught SQLException, you need to make sure that the exception is really thrown by an OpenOffice.org Base core component. To do so, check whether the error message (Exception.Message) starts with the vendor string [OOoBase].
    
    The list of defined error conditions, by nature, is expected to permanently grow, so never assume it being finalized.
    """
    ROW_SET_OPERATION_VETOED = ErrorCondition.ROW_SET_OPERATION_VETOED
    """
    is used by and RowSet to indicate that an operation has been vetoed by one of its approval listeners
    
    This error condition results in raising a RowSetVetoException.
    """
    PARSER_CYCLIC_SUB_QUERIES = ErrorCondition.PARSER_CYCLIC_SUB_QUERIES
    """
    indicates that while parsing an SQL statement, cyclic sub queries have been detected.
    
    Imagine you have a client-side query SELECT * FROM table, which is saved as \"query1\". Additionally, there is a query \"query2\" defined as SELECT * FROM query1. Now if you try to change the statement of query1 to SELECT * FROM query2, this is prohibited, because it would lead to a cyclic sub query.
    """
    DB_OBJECT_NAME_WITH_SLASHES = ErrorCondition.DB_OBJECT_NAME_WITH_SLASHES
    """
    indicates that the name of a client side database object - a query, a form, or a report - contains one or more slashes, which is forbidden.
    """
    DB_INVALID_SQL_NAME = ErrorCondition.DB_INVALID_SQL_NAME
    """
    indicates that an identifier is not SQL conform.
    """
    DB_QUERY_NAME_WITH_QUOTES = ErrorCondition.DB_QUERY_NAME_WITH_QUOTES
    """
    indicates that the name of a query contains quote characters.
    
    This error condition is met when the user attempts to save a query with a name which contains one of the possible database quote characters. This is an error since query names can potentially be used in SELECT statements, where quote identifiers would render the statement invalid.
    """
    DB_OBJECT_NAME_IS_USED = ErrorCondition.DB_OBJECT_NAME_IS_USED
    """
    indicates that an attempt was made to save a database object under a name which is already used in the database.
    
    In databases which support query names to appear in SELECT statements, this could mean that a table was attempted to be saved with the name of an existing query, or vice versa.
    
    Otherwise, it means an object was attempted to be saved with the name of an already existing object of the same type.
    """
    DB_NOT_CONNECTED = ErrorCondition.DB_NOT_CONNECTED
    """
    indicates an operation was attempted which needs a connection to the database, which did not exist at that time.
    """
    AB_ADDRESSBOOK_NOT_FOUND = ErrorCondition.AB_ADDRESSBOOK_NOT_FOUND
    """
    used by the component implementing address book access to indicate that a requested address book could not be accessed.
    
    For instance, this error code is used when you try to access the address book in a Thunderbird profile named MyProfile, but there does not exist a profile with this name.
    """
    DATA_CANNOT_SELECT_UNFILTERED = ErrorCondition.DATA_CANNOT_SELECT_UNFILTERED
    """
    used to indicate that a SELECT operation on a table needs a filter.
    
    Some database drivers are not able to SELECT from a table if the statement does not contain a WHERE clause. In this case, a statement like SELECT * FROM \"table\" will fail with the error code DATA_CANNOT_SELECT_UNFILTERED.
    
    It is also legitimate for the driver to report this error condition as warning, and provide an empty result set, instead of ungraceful failing.
    """

__all__ = ['ErrorCondition', 'ErrorConditionEnum']
