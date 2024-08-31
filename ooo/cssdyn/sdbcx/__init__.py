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
    from ...dyn.sdbcx.check_option import CheckOption as CheckOption
with suppress(ImportError):
    from ...dyn.sdbcx.check_option import CheckOptionEnum as CheckOptionEnum
with suppress(ImportError):
    from ...dyn.sdbcx.column import Column as Column
with suppress(ImportError):
    from ...dyn.sdbcx.column_descriptor import ColumnDescriptor as ColumnDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.compare_bookmark import CompareBookmark as CompareBookmark
with suppress(ImportError):
    from ...dyn.sdbcx.compare_bookmark import CompareBookmarkEnum as CompareBookmarkEnum
with suppress(ImportError):
    from ...dyn.sdbcx.container import Container as Container
with suppress(ImportError):
    from ...dyn.sdbcx.database_definition import DatabaseDefinition as DatabaseDefinition
with suppress(ImportError):
    from ...dyn.sdbcx.descriptor import Descriptor as Descriptor
with suppress(ImportError):
    from ...dyn.sdbcx.driver import Driver as Driver
with suppress(ImportError):
    from ...dyn.sdbcx.group import Group as Group
with suppress(ImportError):
    from ...dyn.sdbcx.group_descriptor import GroupDescriptor as GroupDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.index import Index as Index
with suppress(ImportError):
    from ...dyn.sdbcx.index_column import IndexColumn as IndexColumn
with suppress(ImportError):
    from ...dyn.sdbcx.index_column_descriptor import IndexColumnDescriptor as IndexColumnDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.index_descriptor import IndexDescriptor as IndexDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.key import Key as Key
with suppress(ImportError):
    from ...dyn.sdbcx.key_column import KeyColumn as KeyColumn
with suppress(ImportError):
    from ...dyn.sdbcx.key_column_descriptor import KeyColumnDescriptor as KeyColumnDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.key_descriptor import KeyDescriptor as KeyDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.key_type import KeyType as KeyType
with suppress(ImportError):
    from ...dyn.sdbcx.key_type import KeyTypeEnum as KeyTypeEnum
with suppress(ImportError):
    from ...dyn.sdbcx.prepared_statement import PreparedStatement as PreparedStatement
with suppress(ImportError):
    from ...dyn.sdbcx.privilege import Privilege as Privilege
with suppress(ImportError):
    from ...dyn.sdbcx.privilege import PrivilegeEnum as PrivilegeEnum
with suppress(ImportError):
    from ...dyn.sdbcx.privilege_object import PrivilegeObject as PrivilegeObject
with suppress(ImportError):
    from ...dyn.sdbcx.privilege_object import PrivilegeObjectEnum as PrivilegeObjectEnum
with suppress(ImportError):
    from ...dyn.sdbcx.reference_column import ReferenceColumn as ReferenceColumn
with suppress(ImportError):
    from ...dyn.sdbcx.result_set import ResultSet as ResultSet
with suppress(ImportError):
    from ...dyn.sdbcx.statement import Statement as Statement
with suppress(ImportError):
    from ...dyn.sdbcx.table import Table as Table
with suppress(ImportError):
    from ...dyn.sdbcx.table_descriptor import TableDescriptor as TableDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.user import User as User
with suppress(ImportError):
    from ...dyn.sdbcx.user_descriptor import UserDescriptor as UserDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.view import View as View
with suppress(ImportError):
    from ...dyn.sdbcx.view_descriptor import ViewDescriptor as ViewDescriptor
with suppress(ImportError):
    from ...dyn.sdbcx.x_alter_table import XAlterTable as XAlterTable
with suppress(ImportError):
    from ...dyn.sdbcx.x_alter_view import XAlterView as XAlterView
with suppress(ImportError):
    from ...dyn.sdbcx.x_append import XAppend as XAppend
with suppress(ImportError):
    from ...dyn.sdbcx.x_authorizable import XAuthorizable as XAuthorizable
with suppress(ImportError):
    from ...dyn.sdbcx.x_columns_supplier import XColumnsSupplier as XColumnsSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_create_catalog import XCreateCatalog as XCreateCatalog
with suppress(ImportError):
    from ...dyn.sdbcx.x_data_definition_supplier import XDataDefinitionSupplier as XDataDefinitionSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory
with suppress(ImportError):
    from ...dyn.sdbcx.x_delete_rows import XDeleteRows as XDeleteRows
with suppress(ImportError):
    from ...dyn.sdbcx.x_drop import XDrop as XDrop
with suppress(ImportError):
    from ...dyn.sdbcx.x_drop_catalog import XDropCatalog as XDropCatalog
with suppress(ImportError):
    from ...dyn.sdbcx.x_groups_supplier import XGroupsSupplier as XGroupsSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_indexes_supplier import XIndexesSupplier as XIndexesSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_keys_supplier import XKeysSupplier as XKeysSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_rename import XRename as XRename
with suppress(ImportError):
    from ...dyn.sdbcx.x_row_locate import XRowLocate as XRowLocate
with suppress(ImportError):
    from ...dyn.sdbcx.x_tables_supplier import XTablesSupplier as XTablesSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_user import XUser as XUser
with suppress(ImportError):
    from ...dyn.sdbcx.x_users_supplier import XUsersSupplier as XUsersSupplier
with suppress(ImportError):
    from ...dyn.sdbcx.x_views_supplier import XViewsSupplier as XViewsSupplier
