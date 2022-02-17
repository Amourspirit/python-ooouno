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
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdbc import DataType as DataType
else:
    from ...lo.sdbc.data_type import DataType as DataType


class DataTypeEnum(IntEnum):
    """
    Enum of Const Class DataType

    These constants are used to specify database data types which are used to identify the generic SQL types.
    
    The definition is based on JDBC 3.0.
    
    The actual type constant values are equivalent to those in the X/Open CLI.
    
    Precise information about the specific types can be got from XDatabaseMetaData.getTypeInfo().
    
    **since**
    
        OOo 2.0
    """
    BIT = DataType.BIT
    TINYINT = DataType.TINYINT
    SMALLINT = DataType.SMALLINT
    INTEGER = DataType.INTEGER
    BIGINT = DataType.BIGINT
    FLOAT = DataType.FLOAT
    REAL = DataType.REAL
    DOUBLE = DataType.DOUBLE
    NUMERIC = DataType.NUMERIC
    DECIMAL = DataType.DECIMAL
    CHAR = DataType.CHAR
    VARCHAR = DataType.VARCHAR
    LONGVARCHAR = DataType.LONGVARCHAR
    DATE = DataType.DATE
    TIME = DataType.TIME
    TIMESTAMP = DataType.TIMESTAMP
    BINARY = DataType.BINARY
    VARBINARY = DataType.VARBINARY
    LONGVARBINARY = DataType.LONGVARBINARY
    SQLNULL = DataType.SQLNULL
    OTHER = DataType.OTHER
    """
    indicates that the SQL type is database-specific and gets mapped to an object that can be accessed via the method com.sun.star.sdbc.XRow.getObject().
    """
    OBJECT = DataType.OBJECT
    """
    indicates a type which is represented by an object which implements this type.
    """
    DISTINCT = DataType.DISTINCT
    """
    describes a type based on a built-in type.
    
    It is a user-defined data type (UDT).
    """
    STRUCT = DataType.STRUCT
    """
    indicates a type consisting of attributes that may be any type.
    
    It is a user-defined data type (UDT).
    """
    ARRAY = DataType.ARRAY
    """
    indicates a type representing an SQL ARRAY.
    """
    BLOB = DataType.BLOB
    """
    indicates a type representing an SQL Binary Large Object.
    """
    CLOB = DataType.CLOB
    """
    indicates a type representing an SQL Character Large Object.
    """
    REF = DataType.REF
    """
    indicates a type representing an SQL REF, a referencing type.
    """
    BOOLEAN = DataType.BOOLEAN
    """
    identifies the generic SQL type BOOLEAN.
    
    **since**
    
        OOo 2.0
    """

__all__ = ['DataType', 'DataTypeEnum']