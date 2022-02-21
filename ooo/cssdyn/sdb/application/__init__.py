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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ....dyn.sdb.application.copy_table_continuation import CopyTableContinuation as CopyTableContinuation
except ImportError:
    pass
try:
    from ....dyn.sdb.application.copy_table_continuation import CopyTableContinuationEnum as CopyTableContinuationEnum
except ImportError:
    pass
try:
    from ....dyn.sdb.application.copy_table_operation import CopyTableOperation as CopyTableOperation
except ImportError:
    pass
try:
    from ....dyn.sdb.application.copy_table_operation import CopyTableOperationEnum as CopyTableOperationEnum
except ImportError:
    pass
try:
    from ....dyn.sdb.application.copy_table_row_event import CopyTableRowEvent as CopyTableRowEvent
except ImportError:
    pass
try:
    from ....dyn.sdb.application.copy_table_wizard import CopyTableWizard as CopyTableWizard
except ImportError:
    pass
try:
    from ....dyn.sdb.application.database_object import DatabaseObject as DatabaseObject
except ImportError:
    pass
try:
    from ....dyn.sdb.application.database_object import DatabaseObjectEnum as DatabaseObjectEnum
except ImportError:
    pass
try:
    from ....dyn.sdb.application.database_object_container import DatabaseObjectContainer as DatabaseObjectContainer
except ImportError:
    pass
try:
    from ....dyn.sdb.application.database_object_container import DatabaseObjectContainerEnum as DatabaseObjectContainerEnum
except ImportError:
    pass
try:
    from ....dyn.sdb.application.default_view_controller import DefaultViewController as DefaultViewController
except ImportError:
    pass
try:
    from ....dyn.sdb.application.named_database_object import NamedDatabaseObject as NamedDatabaseObject
except ImportError:
    pass
try:
    from ....dyn.sdb.application.x_copy_table_listener import XCopyTableListener as XCopyTableListener
except ImportError:
    pass
try:
    from ....dyn.sdb.application.x_copy_table_wizard import XCopyTableWizard as XCopyTableWizard
except ImportError:
    pass
try:
    from ....dyn.sdb.application.x_database_document_ui import XDatabaseDocumentUI as XDatabaseDocumentUI
except ImportError:
    pass
try:
    from ....dyn.sdb.application.x_table_ui_provider import XTableUIProvider as XTableUIProvider
except ImportError:
    pass
