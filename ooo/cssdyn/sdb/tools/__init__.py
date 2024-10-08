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
    from ....dyn.sdb.tools.composition_type import CompositionType as CompositionType
with suppress(ImportError):
    from ....dyn.sdb.tools.composition_type import CompositionTypeEnum as CompositionTypeEnum
with suppress(ImportError):
    from ....dyn.sdb.tools.connection_tools import ConnectionTools as ConnectionTools
with suppress(ImportError):
    from ....dyn.sdb.tools.x_connection_supplier import XConnectionSupplier as XConnectionSupplier
with suppress(ImportError):
    from ....dyn.sdb.tools.x_connection_tools import XConnectionTools as XConnectionTools
with suppress(ImportError):
    from ....dyn.sdb.tools.x_data_source_meta_data import XDataSourceMetaData as XDataSourceMetaData
with suppress(ImportError):
    from ....dyn.sdb.tools.x_index_alteration import XIndexAlteration as XIndexAlteration
with suppress(ImportError):
    from ....dyn.sdb.tools.x_key_alteration import XKeyAlteration as XKeyAlteration
with suppress(ImportError):
    from ....dyn.sdb.tools.x_object_names import XObjectNames as XObjectNames
with suppress(ImportError):
    from ....dyn.sdb.tools.x_table_alteration import XTableAlteration as XTableAlteration
with suppress(ImportError):
    from ....dyn.sdb.tools.x_table_name import XTableName as XTableName
with suppress(ImportError):
    from ....dyn.sdb.tools.x_table_rename import XTableRename as XTableRename
with suppress(ImportError):
    from ....dyn.sdb.tools.x_view_access import XViewAccess as XViewAccess
