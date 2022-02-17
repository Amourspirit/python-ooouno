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
from .x_multiple_results import XMultipleResults as XMultipleResults_e1b50d3a
from .x_parameters import XParameters as XParameters_a36c0b10
from .x_prepared_batch_execution import XPreparedBatchExecution as XPreparedBatchExecution_44d80fc5
from .x_prepared_statement import XPreparedStatement as XPreparedStatement_fbc80de4
from .x_result_set_meta_data_supplier import XResultSetMetaDataSupplier as XResultSetMetaDataSupplier_777010fc
from .x_warnings_supplier import XWarningsSupplier as XWarningsSupplier_ef210d99
from ..util.x_cancellable import XCancellable as XCancellable_afc30b64

class PreparedStatement(XPropertySet_bc180bfa, XComponent_98dc0ab5, XCloseable_98290a86, XMultipleResults_e1b50d3a, XParameters_a36c0b10, XPreparedBatchExecution_44d80fc5, XPreparedStatement_fbc80de4, XResultSetMetaDataSupplier_777010fc, XWarningsSupplier_ef210d99, XCancellable_afc30b64):
    """
    Service Class

    represents a precompiled SQL statement.
    
    A SQL statement is pre-compiled and stored in a PreparedStatement object. This object can then be used to efficiently execute this statement multiple times.
    
    Note:  The setXXX methods for setting IN parameter values must specify types that are compatible with the defined SQL type of the input parameter. For instance, if the IN parameter has SQL type Integer, then the method com.sun.star.sdbc.XParameters.setInt() should be used.
    
    If arbitrary parameter type conversions are required, the method com.sun.star.sdbc.XParameters.setObject() should be used with a target SQL type.
    
    Example of setting a parameter; con is an active connection.
    
    Only one com.sun.star.sdbc.ResultSet per com.sun.star.sdbc.Statement can be open at any point in time. Therefore, if the reading of one ResultSet is interleaved with the reading of another, each must have been generated by different Statements. All statement execute methods implicitly close a statement's current ResultSet if an open one exists.

    See Also:
        `API PreparedStatement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1PreparedStatement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.PreparedStatement'
    __ooo_type_name__: str = 'service'



__all__ = ['PreparedStatement']
