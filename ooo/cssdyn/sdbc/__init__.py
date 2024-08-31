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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.sdbc.batch_update_exception import BatchUpdateException as BatchUpdateException
with suppress(ImportError):
    from ...dyn.sdbc.best_row_scope import BestRowScope as BestRowScope
with suppress(ImportError):
    from ...dyn.sdbc.best_row_scope import BestRowScopeEnum as BestRowScopeEnum
with suppress(ImportError):
    from ...dyn.sdbc.best_row_type import BestRowType as BestRowType
with suppress(ImportError):
    from ...dyn.sdbc.best_row_type import BestRowTypeEnum as BestRowTypeEnum
with suppress(ImportError):
    from ...dyn.sdbc.callable_statement import CallableStatement as CallableStatement
with suppress(ImportError):
    from ...dyn.sdbc.change_action import ChangeAction as ChangeAction
with suppress(ImportError):
    from ...dyn.sdbc.change_action import ChangeActionEnum as ChangeActionEnum
with suppress(ImportError):
    from ...dyn.sdbc.change_event import ChangeEvent as ChangeEvent
with suppress(ImportError):
    from ...dyn.sdbc.column_search import ColumnSearch as ColumnSearch
with suppress(ImportError):
    from ...dyn.sdbc.column_search import ColumnSearchEnum as ColumnSearchEnum
with suppress(ImportError):
    from ...dyn.sdbc.column_type import ColumnType as ColumnType
with suppress(ImportError):
    from ...dyn.sdbc.column_type import ColumnTypeEnum as ColumnTypeEnum
with suppress(ImportError):
    from ...dyn.sdbc.column_value import ColumnValue as ColumnValue
with suppress(ImportError):
    from ...dyn.sdbc.column_value import ColumnValueEnum as ColumnValueEnum
with suppress(ImportError):
    from ...dyn.sdbc.connection import Connection as Connection
with suppress(ImportError):
    from ...dyn.sdbc.connection_pool import ConnectionPool as ConnectionPool
with suppress(ImportError):
    from ...dyn.sdbc.connection_properties import ConnectionProperties as ConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.dbase_connection_properties import DBASEConnectionProperties as DBASEConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.data_truncation import DataTruncation as DataTruncation
with suppress(ImportError):
    from ...dyn.sdbc.data_type import DataType as DataType
with suppress(ImportError):
    from ...dyn.sdbc.data_type import DataTypeEnum as DataTypeEnum
with suppress(ImportError):
    from ...dyn.sdbc.deferrability import Deferrability as Deferrability
with suppress(ImportError):
    from ...dyn.sdbc.deferrability import DeferrabilityEnum as DeferrabilityEnum
with suppress(ImportError):
    from ...dyn.sdbc.driver import Driver as Driver
with suppress(ImportError):
    from ...dyn.sdbc.driver_manager import DriverManager as DriverManager
with suppress(ImportError):
    from ...dyn.sdbc.driver_property_info import DriverPropertyInfo as DriverPropertyInfo
with suppress(ImportError):
    from ...dyn.sdbc.file_connection_properties import FILEConnectionProperties as FILEConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.flat_connection_properties import FLATConnectionProperties as FLATConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.fetch_direction import FetchDirection as FetchDirection
with suppress(ImportError):
    from ...dyn.sdbc.fetch_direction import FetchDirectionEnum as FetchDirectionEnum
with suppress(ImportError):
    from ...dyn.sdbc.index_type import IndexType as IndexType
with suppress(ImportError):
    from ...dyn.sdbc.index_type import IndexTypeEnum as IndexTypeEnum
with suppress(ImportError):
    from ...dyn.sdbc.jdbc_connection_properties import JDBCConnectionProperties as JDBCConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.key_rule import KeyRule as KeyRule
with suppress(ImportError):
    from ...dyn.sdbc.key_rule import KeyRuleEnum as KeyRuleEnum
with suppress(ImportError):
    from ...dyn.sdbc.odbc_connection_properties import ODBCConnectionProperties as ODBCConnectionProperties
with suppress(ImportError):
    from ...dyn.sdbc.prepared_statement import PreparedStatement as PreparedStatement
with suppress(ImportError):
    from ...dyn.sdbc.procedure_column import ProcedureColumn as ProcedureColumn
with suppress(ImportError):
    from ...dyn.sdbc.procedure_column import ProcedureColumnEnum as ProcedureColumnEnum
with suppress(ImportError):
    from ...dyn.sdbc.procedure_result import ProcedureResult as ProcedureResult
with suppress(ImportError):
    from ...dyn.sdbc.procedure_result import ProcedureResultEnum as ProcedureResultEnum
with suppress(ImportError):
    from ...dyn.sdbc.result_set import ResultSet as ResultSet
with suppress(ImportError):
    from ...dyn.sdbc.result_set_concurrency import ResultSetConcurrency as ResultSetConcurrency
with suppress(ImportError):
    from ...dyn.sdbc.result_set_concurrency import ResultSetConcurrencyEnum as ResultSetConcurrencyEnum
with suppress(ImportError):
    from ...dyn.sdbc.result_set_type import ResultSetType as ResultSetType
with suppress(ImportError):
    from ...dyn.sdbc.result_set_type import ResultSetTypeEnum as ResultSetTypeEnum
with suppress(ImportError):
    from ...dyn.sdbc.row_set import RowSet as RowSet
with suppress(ImportError):
    from ...dyn.sdbc.sql_exception import SQLException as SQLException
with suppress(ImportError):
    from ...dyn.sdbc.sql_warning import SQLWarning as SQLWarning
with suppress(ImportError):
    from ...dyn.sdbc.statement import Statement as Statement
with suppress(ImportError):
    from ...dyn.sdbc.transaction_isolation import TransactionIsolation as TransactionIsolation
with suppress(ImportError):
    from ...dyn.sdbc.transaction_isolation import TransactionIsolationEnum as TransactionIsolationEnum
with suppress(ImportError):
    from ...dyn.sdbc.x_array import XArray as XArray
with suppress(ImportError):
    from ...dyn.sdbc.x_batch_execution import XBatchExecution as XBatchExecution
with suppress(ImportError):
    from ...dyn.sdbc.x_blob import XBlob as XBlob
with suppress(ImportError):
    from ...dyn.sdbc.x_clob import XClob as XClob
with suppress(ImportError):
    from ...dyn.sdbc.x_closeable import XCloseable as XCloseable
with suppress(ImportError):
    from ...dyn.sdbc.x_column_locate import XColumnLocate as XColumnLocate
with suppress(ImportError):
    from ...dyn.sdbc.x_connection import XConnection as XConnection
with suppress(ImportError):
    from ...dyn.sdbc.x_connection_pool import XConnectionPool as XConnectionPool
with suppress(ImportError):
    from ...dyn.sdbc.x_data_source import XDataSource as XDataSource
with suppress(ImportError):
    from ...dyn.sdbc.x_database_meta_data import XDatabaseMetaData as XDatabaseMetaData
with suppress(ImportError):
    from ...dyn.sdbc.x_database_meta_data2 import XDatabaseMetaData2 as XDatabaseMetaData2
with suppress(ImportError):
    from ...dyn.sdbc.x_driver import XDriver as XDriver
with suppress(ImportError):
    from ...dyn.sdbc.x_driver_access import XDriverAccess as XDriverAccess
with suppress(ImportError):
    from ...dyn.sdbc.x_driver_manager import XDriverManager as XDriverManager
with suppress(ImportError):
    from ...dyn.sdbc.x_driver_manager2 import XDriverManager2 as XDriverManager2
with suppress(ImportError):
    from ...dyn.sdbc.x_generated_result_set import XGeneratedResultSet as XGeneratedResultSet
with suppress(ImportError):
    from ...dyn.sdbc.x_isolated_connection import XIsolatedConnection as XIsolatedConnection
with suppress(ImportError):
    from ...dyn.sdbc.x_multiple_results import XMultipleResults as XMultipleResults
with suppress(ImportError):
    from ...dyn.sdbc.x_out_parameters import XOutParameters as XOutParameters
with suppress(ImportError):
    from ...dyn.sdbc.x_parameters import XParameters as XParameters
with suppress(ImportError):
    from ...dyn.sdbc.x_pooled_connection import XPooledConnection as XPooledConnection
with suppress(ImportError):
    from ...dyn.sdbc.x_prepared_batch_execution import XPreparedBatchExecution as XPreparedBatchExecution
with suppress(ImportError):
    from ...dyn.sdbc.x_prepared_statement import XPreparedStatement as XPreparedStatement
with suppress(ImportError):
    from ...dyn.sdbc.x_ref import XRef as XRef
with suppress(ImportError):
    from ...dyn.sdbc.x_result_set import XResultSet as XResultSet
with suppress(ImportError):
    from ...dyn.sdbc.x_result_set_meta_data import XResultSetMetaData as XResultSetMetaData
with suppress(ImportError):
    from ...dyn.sdbc.x_result_set_meta_data_supplier import XResultSetMetaDataSupplier as XResultSetMetaDataSupplier
with suppress(ImportError):
    from ...dyn.sdbc.x_result_set_update import XResultSetUpdate as XResultSetUpdate
with suppress(ImportError):
    from ...dyn.sdbc.x_row import XRow as XRow
with suppress(ImportError):
    from ...dyn.sdbc.x_row_set import XRowSet as XRowSet
with suppress(ImportError):
    from ...dyn.sdbc.x_row_set_listener import XRowSetListener as XRowSetListener
with suppress(ImportError):
    from ...dyn.sdbc.x_row_update import XRowUpdate as XRowUpdate
with suppress(ImportError):
    from ...dyn.sdbc.xsql_data import XSQLData as XSQLData
with suppress(ImportError):
    from ...dyn.sdbc.xsql_input import XSQLInput as XSQLInput
with suppress(ImportError):
    from ...dyn.sdbc.xsql_output import XSQLOutput as XSQLOutput
with suppress(ImportError):
    from ...dyn.sdbc.x_statement import XStatement as XStatement
with suppress(ImportError):
    from ...dyn.sdbc.x_struct import XStruct as XStruct
with suppress(ImportError):
    from ...dyn.sdbc.x_warnings_supplier import XWarningsSupplier as XWarningsSupplier
