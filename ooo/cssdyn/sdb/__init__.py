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
    from ...dyn.sdb.boolean_comparison_mode import BooleanComparisonMode as BooleanComparisonMode
with suppress(ImportError):
    from ...dyn.sdb.boolean_comparison_mode import BooleanComparisonModeEnum as BooleanComparisonModeEnum
with suppress(ImportError):
    from ...dyn.sdb.callable_statement import CallableStatement as CallableStatement
with suppress(ImportError):
    from ...dyn.sdb.column import Column as Column
with suppress(ImportError):
    from ...dyn.sdb.column_descriptor_control import ColumnDescriptorControl as ColumnDescriptorControl
with suppress(ImportError):
    from ...dyn.sdb.column_descriptor_control_model import ColumnDescriptorControlModel as ColumnDescriptorControlModel
with suppress(ImportError):
    from ...dyn.sdb.column_settings import ColumnSettings as ColumnSettings
with suppress(ImportError):
    from ...dyn.sdb.command_definition import CommandDefinition as CommandDefinition
with suppress(ImportError):
    from ...dyn.sdb.command_type import CommandType as CommandType
with suppress(ImportError):
    from ...dyn.sdb.command_type import CommandTypeEnum as CommandTypeEnum
with suppress(ImportError):
    from ...dyn.sdb.connection import Connection as Connection
with suppress(ImportError):
    from ...dyn.sdb.content_loader import ContentLoader as ContentLoader
with suppress(ImportError):
    from ...dyn.sdb.data_access_descriptor import DataAccessDescriptor as DataAccessDescriptor
with suppress(ImportError):
    from ...dyn.sdb.data_access_descriptor_factory import DataAccessDescriptorFactory as DataAccessDescriptorFactory
with suppress(ImportError):
    from ...dyn.sdb.data_column import DataColumn as DataColumn
with suppress(ImportError):
    from ...dyn.sdb.data_settings import DataSettings as DataSettings
with suppress(ImportError):
    from ...dyn.sdb.data_source import DataSource as DataSource
with suppress(ImportError):
    from ...dyn.sdb.data_source_browser import DataSourceBrowser as DataSourceBrowser
with suppress(ImportError):
    from ...dyn.sdb.database_access import DatabaseAccess as DatabaseAccess
with suppress(ImportError):
    from ...dyn.sdb.database_access_connection import DatabaseAccessConnection as DatabaseAccessConnection
with suppress(ImportError):
    from ...dyn.sdb.database_access_context import DatabaseAccessContext as DatabaseAccessContext
with suppress(ImportError):
    from ...dyn.sdb.database_access_data_source import DatabaseAccessDataSource as DatabaseAccessDataSource
with suppress(ImportError):
    from ...dyn.sdb.database_context import DatabaseContext as DatabaseContext
with suppress(ImportError):
    from ...dyn.sdb.database_document import DatabaseDocument as DatabaseDocument
with suppress(ImportError):
    from ...dyn.sdb.database_environment import DatabaseEnvironment as DatabaseEnvironment
with suppress(ImportError):
    from ...dyn.sdb.database_interaction_handler import DatabaseInteractionHandler as DatabaseInteractionHandler
with suppress(ImportError):
    from ...dyn.sdb.database_registration_event import DatabaseRegistrationEvent as DatabaseRegistrationEvent
with suppress(ImportError):
    from ...dyn.sdb.datasource_administration_dialog import DatasourceAdministrationDialog as DatasourceAdministrationDialog
with suppress(ImportError):
    from ...dyn.sdb.definition_container import DefinitionContainer as DefinitionContainer
with suppress(ImportError):
    from ...dyn.sdb.definition_content import DefinitionContent as DefinitionContent
with suppress(ImportError):
    from ...dyn.sdb.document import Document as Document
with suppress(ImportError):
    from ...dyn.sdb.document_container import DocumentContainer as DocumentContainer
with suppress(ImportError):
    from ...dyn.sdb.document_data_source import DocumentDataSource as DocumentDataSource
with suppress(ImportError):
    from ...dyn.sdb.document_definition import DocumentDefinition as DocumentDefinition
with suppress(ImportError):
    from ...dyn.sdb.document_save_request import DocumentSaveRequest as DocumentSaveRequest
with suppress(ImportError):
    from ...dyn.sdb.error_condition import ErrorCondition as ErrorCondition
with suppress(ImportError):
    from ...dyn.sdb.error_condition import ErrorConditionEnum as ErrorConditionEnum
with suppress(ImportError):
    from ...dyn.sdb.error_message_dialog import ErrorMessageDialog as ErrorMessageDialog
with suppress(ImportError):
    from ...dyn.sdb.filter_dialog import FilterDialog as FilterDialog
with suppress(ImportError):
    from ...dyn.sdb.forms import Forms as Forms
with suppress(ImportError):
    from ...dyn.sdb.interaction_handler import InteractionHandler as InteractionHandler
with suppress(ImportError):
    from ...dyn.sdb.office_database_document import OfficeDatabaseDocument as OfficeDatabaseDocument
with suppress(ImportError):
    from ...dyn.sdb.order_column import OrderColumn as OrderColumn
with suppress(ImportError):
    from ...dyn.sdb.order_dialog import OrderDialog as OrderDialog
with suppress(ImportError):
    from ...dyn.sdb.parameters_request import ParametersRequest as ParametersRequest
with suppress(ImportError):
    from ...dyn.sdb.prepared_statement import PreparedStatement as PreparedStatement
with suppress(ImportError):
    from ...dyn.sdb.query import Query as Query
with suppress(ImportError):
    from ...dyn.sdb.query_definition import QueryDefinition as QueryDefinition
with suppress(ImportError):
    from ...dyn.sdb.query_descriptor import QueryDescriptor as QueryDescriptor
with suppress(ImportError):
    from ...dyn.sdb.query_design import QueryDesign as QueryDesign
with suppress(ImportError):
    from ...dyn.sdb.relation_design import RelationDesign as RelationDesign
with suppress(ImportError):
    from ...dyn.sdb.report_design import ReportDesign as ReportDesign
with suppress(ImportError):
    from ...dyn.sdb.reports import Reports as Reports
with suppress(ImportError):
    from ...dyn.sdb.result_column import ResultColumn as ResultColumn
with suppress(ImportError):
    from ...dyn.sdb.result_set import ResultSet as ResultSet
with suppress(ImportError):
    from ...dyn.sdb.row_change_action import RowChangeAction as RowChangeAction
with suppress(ImportError):
    from ...dyn.sdb.row_change_action import RowChangeActionEnum as RowChangeActionEnum
with suppress(ImportError):
    from ...dyn.sdb.row_change_event import RowChangeEvent as RowChangeEvent
with suppress(ImportError):
    from ...dyn.sdb.row_set import RowSet as RowSet
with suppress(ImportError):
    from ...dyn.sdb.row_set_veto_exception import RowSetVetoException as RowSetVetoException
with suppress(ImportError):
    from ...dyn.sdb.rows_change_event import RowsChangeEvent as RowsChangeEvent
with suppress(ImportError):
    from ...dyn.sdb.sql_context import SQLContext as SQLContext
with suppress(ImportError):
    from ...dyn.sdb.sql_error_event import SQLErrorEvent as SQLErrorEvent
with suppress(ImportError):
    from ...dyn.sdb.sql_filter_operator import SQLFilterOperator as SQLFilterOperator
with suppress(ImportError):
    from ...dyn.sdb.sql_filter_operator import SQLFilterOperatorEnum as SQLFilterOperatorEnum
with suppress(ImportError):
    from ...dyn.sdb.sql_query_composer import SQLQueryComposer as SQLQueryComposer
with suppress(ImportError):
    from ...dyn.sdb.single_select_query_analyzer import SingleSelectQueryAnalyzer as SingleSelectQueryAnalyzer
with suppress(ImportError):
    from ...dyn.sdb.single_select_query_composer import SingleSelectQueryComposer as SingleSelectQueryComposer
with suppress(ImportError):
    from ...dyn.sdb.table import Table as Table
with suppress(ImportError):
    from ...dyn.sdb.table_definition import TableDefinition as TableDefinition
with suppress(ImportError):
    from ...dyn.sdb.table_descriptor import TableDescriptor as TableDescriptor
with suppress(ImportError):
    from ...dyn.sdb.table_design import TableDesign as TableDesign
with suppress(ImportError):
    from ...dyn.sdb.text_connection_settings import TextConnectionSettings as TextConnectionSettings
with suppress(ImportError):
    from ...dyn.sdb.x_alter_query import XAlterQuery as XAlterQuery
with suppress(ImportError):
    from ...dyn.sdb.x_bookmarks_supplier import XBookmarksSupplier as XBookmarksSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_column import XColumn as XColumn
with suppress(ImportError):
    from ...dyn.sdb.x_column_update import XColumnUpdate as XColumnUpdate
with suppress(ImportError):
    from ...dyn.sdb.x_command_preparation import XCommandPreparation as XCommandPreparation
with suppress(ImportError):
    from ...dyn.sdb.x_completed_connection import XCompletedConnection as XCompletedConnection
with suppress(ImportError):
    from ...dyn.sdb.x_completed_execution import XCompletedExecution as XCompletedExecution
with suppress(ImportError):
    from ...dyn.sdb.x_data_access_descriptor_factory import XDataAccessDescriptorFactory as XDataAccessDescriptorFactory
with suppress(ImportError):
    from ...dyn.sdb.x_database_access import XDatabaseAccess as XDatabaseAccess
with suppress(ImportError):
    from ...dyn.sdb.x_database_access_listener import XDatabaseAccessListener as XDatabaseAccessListener
with suppress(ImportError):
    from ...dyn.sdb.x_database_context import XDatabaseContext as XDatabaseContext
with suppress(ImportError):
    from ...dyn.sdb.x_database_environment import XDatabaseEnvironment as XDatabaseEnvironment
with suppress(ImportError):
    from ...dyn.sdb.x_database_registrations import XDatabaseRegistrations as XDatabaseRegistrations
with suppress(ImportError):
    from ...dyn.sdb.x_database_registrations_listener import XDatabaseRegistrationsListener as XDatabaseRegistrationsListener
with suppress(ImportError):
    from ...dyn.sdb.x_document_data_source import XDocumentDataSource as XDocumentDataSource
with suppress(ImportError):
    from ...dyn.sdb.x_form_documents_supplier import XFormDocumentsSupplier as XFormDocumentsSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_interaction_document_save import XInteractionDocumentSave as XInteractionDocumentSave
with suppress(ImportError):
    from ...dyn.sdb.x_interaction_supply_parameters import XInteractionSupplyParameters as XInteractionSupplyParameters
with suppress(ImportError):
    from ...dyn.sdb.x_office_database_document import XOfficeDatabaseDocument as XOfficeDatabaseDocument
with suppress(ImportError):
    from ...dyn.sdb.x_parameters_supplier import XParametersSupplier as XParametersSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_queries_supplier import XQueriesSupplier as XQueriesSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_query_definition import XQueryDefinition as XQueryDefinition
with suppress(ImportError):
    from ...dyn.sdb.x_query_definitions_supplier import XQueryDefinitionsSupplier as XQueryDefinitionsSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_report_documents_supplier import XReportDocumentsSupplier as XReportDocumentsSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_result_set_access import XResultSetAccess as XResultSetAccess
with suppress(ImportError):
    from ...dyn.sdb.x_row_set_approve_broadcaster import XRowSetApproveBroadcaster as XRowSetApproveBroadcaster
with suppress(ImportError):
    from ...dyn.sdb.x_row_set_approve_listener import XRowSetApproveListener as XRowSetApproveListener
with suppress(ImportError):
    from ...dyn.sdb.x_row_set_change_broadcaster import XRowSetChangeBroadcaster as XRowSetChangeBroadcaster
with suppress(ImportError):
    from ...dyn.sdb.x_row_set_change_listener import XRowSetChangeListener as XRowSetChangeListener
with suppress(ImportError):
    from ...dyn.sdb.x_row_set_supplier import XRowSetSupplier as XRowSetSupplier
with suppress(ImportError):
    from ...dyn.sdb.x_rows_change_broadcaster import XRowsChangeBroadcaster as XRowsChangeBroadcaster
with suppress(ImportError):
    from ...dyn.sdb.x_rows_change_listener import XRowsChangeListener as XRowsChangeListener
with suppress(ImportError):
    from ...dyn.sdb.xsql_error_broadcaster import XSQLErrorBroadcaster as XSQLErrorBroadcaster
with suppress(ImportError):
    from ...dyn.sdb.xsql_error_listener import XSQLErrorListener as XSQLErrorListener
with suppress(ImportError):
    from ...dyn.sdb.xsql_query_composer import XSQLQueryComposer as XSQLQueryComposer
with suppress(ImportError):
    from ...dyn.sdb.xsql_query_composer_factory import XSQLQueryComposerFactory as XSQLQueryComposerFactory
with suppress(ImportError):
    from ...dyn.sdb.x_single_select_query_analyzer import XSingleSelectQueryAnalyzer as XSingleSelectQueryAnalyzer
with suppress(ImportError):
    from ...dyn.sdb.x_single_select_query_composer import XSingleSelectQueryComposer as XSingleSelectQueryComposer
with suppress(ImportError):
    from ...dyn.sdb.x_sub_document import XSubDocument as XSubDocument
with suppress(ImportError):
    from ...dyn.sdb.x_text_connection_settings import XTextConnectionSettings as XTextConnectionSettings
