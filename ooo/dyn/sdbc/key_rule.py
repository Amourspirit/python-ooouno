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
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdbc import KeyRule as KeyRule
    if hasattr(KeyRule, '_constants') and isinstance(KeyRule._constants, dict):
        KeyRule._constants['__ooo_ns__'] = 'com.sun.star.sdbc'
        KeyRule._constants['__ooo_full_ns__'] = 'com.sun.star.sdbc.KeyRule'
        KeyRule._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global KeyRuleEnum
        ls = [f for f in dir(KeyRule) if not callable(getattr(KeyRule, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(KeyRule, name)
        KeyRuleEnum = IntEnum('KeyRuleEnum', _dict)
    build_enum()
else:
    from ...lo.sdbc.key_rule import KeyRule as KeyRule

    class KeyRuleEnum(IntEnum):
        """
        Enum of Const Class KeyRule

        determines the rules for foreign key constraints.
        """
        CASCADE = KeyRule.CASCADE
        """
        a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
        
        For the column UPDATE_RULE , it indicates that when the primary key is updated, the foreign key (imported key) is changed to agree with it.
        
        For the column DELETE_RULE , it indicates that when the primary key is deleted, rows that imported that key are deleted.
        """
        RESTRICT = KeyRule.RESTRICT
        """
        a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
        
        For the column UPDATE_RULE , it indicates that a primary key may not be updated if it has been imported by another table as a foreign key.
        
        For the column DELETE_RULE , it indicates that a primary key may not be deleted if it has been imported by another table as a foreign key.
        """
        SET_NULL = KeyRule.SET_NULL
        """
        a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
        
        For the columns UPDATE_RULE and DELETE_RULE , it indicates that when the primary key is updated or deleted, the foreign key (imported key) is changed to NULL.
        """
        NO_ACTION = KeyRule.NO_ACTION
        """
        a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
        
        For the columns UPDATE_RULE and DELETE_RULE , it indicates that if the primary key has been imported, it cannot be updated or deleted.
        """
        SET_DEFAULT = KeyRule.SET_DEFAULT
        """
        a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
        
        For the columns UPDATE_RULE and DELETE_RULE , it indicates that if the primary key is updated or deleted, the foreign key (imported key) is set to the default value.
        """

__all__ = ['KeyRule', 'KeyRuleEnum']
