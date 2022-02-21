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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb.application
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdb.application import CopyTableOperation as CopyTableOperation
    if hasattr(CopyTableOperation, '_constants') and isinstance(CopyTableOperation._constants, dict):
        CopyTableOperation._constants['__ooo_ns__'] = 'com.sun.star.sdb.application'
        CopyTableOperation._constants['__ooo_full_ns__'] = 'com.sun.star.sdb.application.CopyTableOperation'
        CopyTableOperation._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CopyTableOperationEnum
        ls = [f for f in dir(CopyTableOperation) if not callable(getattr(CopyTableOperation, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CopyTableOperation, name)
        CopyTableOperationEnum = IntEnum('CopyTableOperationEnum', _dict)
    build_enum()
else:
    from ....lo.sdb.application.copy_table_operation import CopyTableOperation as CopyTableOperation

    class CopyTableOperationEnum(IntEnum):
        """
        Enum of Const Class CopyTableOperation

        specifies the different basic operations a CopyTableWizard can do.
        
        **since**
        
            OOo 2.4
        """
        CopyDefinitionAndData = CopyTableOperation.CopyDefinitionAndData
        """
        specifies that the wizard should copy the source table to the target database, by creating a new table and copying all data.
        """
        CopyDefinitionOnly = CopyTableOperation.CopyDefinitionOnly
        """
        specifies that the wizard should copy the source table to the target database, by only creating a new table with the same structure as the source table.
        """
        CreateAsView = CopyTableOperation.CreateAsView
        """
        specifies the wizard should create the source table as view
        
        This option is not available if the target database does not support views.
        """
        AppendData = CopyTableOperation.AppendData
        """
        specifies the wizard should append the source table's data to an existing table in the target database.
        """

__all__ = ['CopyTableOperation', 'CopyTableOperationEnum']
