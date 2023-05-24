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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XResultSetMetaData(XInterface_8f010a43):
    """
    can be used to find out about the types and properties of the columns in a ResultSet.

    See Also:
        `API XResultSetMetaData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XResultSetMetaData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XResultSetMetaData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XResultSetMetaData'

    @abstractmethod
    def getCatalogName(self, column: int) -> str:
        """
        gets a column's table's catalog name.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnCount(self) -> int:
        """
        returns the number of columns in this ResultSet.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnDisplaySize(self, column: int) -> int:
        """
        indicates the column's normal max width in chars.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnLabel(self, column: int) -> str:
        """
        gets the suggested column title for use in printouts and displays.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnName(self, column: int) -> str:
        """
        gets a column's name.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnServiceName(self, column: int) -> str:
        """
        returns the fully-qualified name of the service whose instances are manufactured if the method com.sun.star.sdbc.XResultSet..getObject() is called to retrieve a value from the column.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnType(self, column: int) -> int:
        """
        retrieves a column's SQL type.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getColumnTypeName(self, column: int) -> str:
        """
        retrieves a column's database-specific type name.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getPrecision(self, column: int) -> int:
        """
        gets a column's number of decimal digits.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getScale(self, column: int) -> int:
        """
        gets a column's number of digits to right of the decimal point.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getSchemaName(self, column: int) -> str:
        """
        gets a column's table's schema.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getTableName(self, column: int) -> str:
        """
        gets a column's table name.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isAutoIncrement(self, column: int) -> bool:
        """
        indicates whether the column is automatically numbered, thus read-only.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isCaseSensitive(self, column: int) -> bool:
        """
        indicates whether a column's case matters.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isCurrency(self, column: int) -> bool:
        """
        indicates whether the column is a cash value.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isDefinitelyWritable(self, column: int) -> bool:
        """
        indicates whether a write on the column will definitely succeed.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isNullable(self, column: int) -> int:
        """
        indicates the nullability of values in the designated column.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isReadOnly(self, column: int) -> bool:
        """
        indicates whether a column is definitely not writable.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isSearchable(self, column: int) -> bool:
        """
        indicates whether the column can be used in a where clause.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isSigned(self, column: int) -> bool:
        """
        indicates whether values in the column are signed numbers.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def isWritable(self, column: int) -> bool:
        """
        indicates whether it is possible for a write on the column to succeed.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XResultSetMetaData']

