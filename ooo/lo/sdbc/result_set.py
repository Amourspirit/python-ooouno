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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_closeable import XCloseable as XCloseable_98290a86
from .x_column_locate import XColumnLocate as XColumnLocate_ba5e0bc2
from .x_result_set import XResultSet as XResultSet_98e30aa7
from .x_result_set_meta_data_supplier import XResultSetMetaDataSupplier as XResultSetMetaDataSupplier_777010fc
from .x_result_set_update import XResultSetUpdate as XResultSetUpdate_e0fb0d0a
from .x_row import XRow as XRow_5f360834
from .x_row_update import XRowUpdate as XRowUpdate_989c0a97
from .x_warnings_supplier import XWarningsSupplier as XWarningsSupplier_ef210d99

class ResultSet(XPropertySet_bc180bfa, XComponent_98dc0ab5, XCloseable_98290a86, XColumnLocate_ba5e0bc2, XResultSet_98e30aa7, XResultSetMetaDataSupplier_777010fc, XResultSetUpdate_e0fb0d0a, XRow_5f360834, XRowUpdate_989c0a97, XWarningsSupplier_ef210d99):
    """
    Service Class

    provides access to a table of data.
    
    A ResultSet object is usually generated by executing a Statement.
    
    A ResultSet maintains a cursor pointing to its current row of data. Initially the cursor is positioned before the first row. The \"next\" method moves the cursor to the next row.
    
    The getXXX methods retrieve column values for the current row. You can retrieve values using either the index number of the column. Columns are numbered from 1.
    
    For maximum portability, ResultSet columns within each row should be read in left-to-right order and each column should be read only once.
    
    For the getXXX methods, the SDBC driver attempts to convert the underlying data to the specified type and returns a suitable value.
    
    Column names used as input to the findColumn method are case insensitive. When several columns have the same name, then the value of the first matching column will be returned. The column name option is designed to be used when column names are used in the SQL query. For columns that are NOT explicitly named in the query, it is best to use column numbers. If column names are used, there is no way for the programmer to guarantee that they actually refer to the intended columns.
    
    A ResultSet is automatically closed (disposed) by the Statement that generated it when that Statement is closed, re-executed, or used to retrieve the next result from a sequence of multiple results.
    
    The number, types, and properties of a ResultSet's columns are provided by the ResultSetMetaData object returned by the getMetaData method.

    See Also:
        `API ResultSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1ResultSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ResultSet'
    __ooo_type_name__: str = 'service'



__all__ = ['ResultSet']

