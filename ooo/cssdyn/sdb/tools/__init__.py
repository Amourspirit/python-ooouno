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
    from ....dyn.sdb.tools.composition_type import CompositionType as CompositionType
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.composition_type import CompositionTypeEnum as CompositionTypeEnum
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.connection_tools import ConnectionTools as ConnectionTools
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_connection_supplier import XConnectionSupplier as XConnectionSupplier
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_connection_tools import XConnectionTools as XConnectionTools
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_data_source_meta_data import XDataSourceMetaData as XDataSourceMetaData
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_index_alteration import XIndexAlteration as XIndexAlteration
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_key_alteration import XKeyAlteration as XKeyAlteration
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_object_names import XObjectNames as XObjectNames
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_table_alteration import XTableAlteration as XTableAlteration
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_table_name import XTableName as XTableName
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_table_rename import XTableRename as XTableRename
except ImportError:
    pass
try:
    from ....dyn.sdb.tools.x_view_access import XViewAccess as XViewAccess
except ImportError:
    pass
