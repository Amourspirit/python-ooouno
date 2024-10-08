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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from .x_array import XArray as XArray_708108fb
    from .x_blob import XBlob as XBlob_6773087b
    from .x_clob import XClob as XClob_6777087c
    from .x_ref import XRef as XRef_5f110819
    from .xsql_data import XSQLData as XSQLData_81fe0966
    from .x_struct import XStruct as XStruct_7a760981
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XSQLOutput(XInterface_8f010a43):
    """
    is used as an output stream for writing the attributes of a user-defined type back to the database.
    
    This interface, used only for custom mapping, is used by the driver, and its methods are never directly invoked by a programmer.
    
    When an object of a class implementing interface com.sun.star.sdbc.XSQLData is passed as an argument to a SQL statement, the JDBC driver calls com.sun.star.sdbc.SQLData.getSQLType() to determine the kind of SQL datum being passed to the database. The driver then creates an instance of XSQLOutput and passes it to the method com.sun.star.sdbc.XSQLData.writeSQL() . The method writeSQL in turn calls the appropriate XSQLOutput.writeXXX methods to write data from the com.sun.star.sdbc.XSQLData object to the XSQLOutput output stream as the representation of a SQL user-defined type.

    See Also:
        `API XSQLOutput <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XSQLOutput.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XSQLOutput'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XSQLOutput'

    @abstractmethod
    def writeArray(self, x: XArray_708108fb) -> None:
        """
        writes an array to the stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeBinaryStream(self, x: XInputStream_98d40ab4) -> None:
        """
        writes the next attribute to the stream as a stream of uninterpreted bytes.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeBlob(self, x: XBlob_6773087b) -> None:
        """
        writes a BLOB to the stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeBoolean(self, x: bool) -> None:
        """
        writes the next attribute to the stream as boolean.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeByte(self, x: int) -> None:
        """
        writes the next attribute to the stream as byte.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeBytes(self, x: typing.Tuple[int, ...]) -> None:
        """
        writes the next attribute to the stream as byte sequence.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeCharacterStream(self, x: XInputStream_98d40ab4) -> None:
        """
        writes the next attribute to the stream as a stream of Unicode string.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeClob(self, x: XClob_6777087c) -> None:
        """
        writes a CLOB to the stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeDate(self, x: Date_60040844) -> None:
        """
        writes the next attribute to the stream as a date.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeDouble(self, x: float) -> None:
        """
        writes the next attribute to the stream as double.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeFloat(self, x: float) -> None:
        """
        writes the next attribute to the stream as float.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeInt(self, x: int) -> None:
        """
        writes the next attribute to the stream as long.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeLong(self, x: int) -> None:
        """
        writes the next attribute to the stream as hyper.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeObject(self, x: XSQLData_81fe0966) -> None:
        """
        writes to the stream the data contained in the given XSQLData object.
        
        When the XSQLData object is NULL , this method writes an SQL NULL to the stream. Otherwise, it calls the com.sun.star.sdbc.XSQLData.writeSQL() method of the given object, which writes the object's attributes to the stream. The implementation of the method XSQLData.writeSQL() calls the appropriate XSQLOutput.writeXXX method(s) for writing each of the object's attributes in order. The attributes must be read from an com.sun.star.sdbc.XSQLInput input stream and written to an XSQLOutput output stream in the same order in which they were listed in the SQL definition of the user-defined type.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeRef(self, x: XRef_5f110819) -> None:
        """
        writes a REF(&lt;structured-type&gt;) to the stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeShort(self, x: int) -> None:
        """
        writes the next attribute to the stream as short.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeString(self, x: str) -> None:
        """
        writes the next attribute to the stream as a string.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeStruct(self, x: XStruct_7a760981) -> None:
        """
        writes a structured-type to the stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeTime(self, x: Time_604e0855) -> None:
        """
        writes the next attribute to the stream as a time.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def writeTimestamp(self, x: DateTime_84de09d3) -> None:
        """
        writes the next attribute to the stream as a datetime.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XSQLOutput']

