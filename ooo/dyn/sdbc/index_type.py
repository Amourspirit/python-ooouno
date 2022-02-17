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
    from com.sun.star.sdbc import IndexType as IndexType
else:
    from ...lo.sdbc.index_type import IndexType as IndexType


class IndexTypeEnum(IntEnum):
    """
    Enum of Const Class IndexType

    indicates the type of index.
    """
    STATISTIC = IndexType.STATISTIC
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Identifies table statistics that are returned in conjunction with a table's index description.
    """
    CLUSTERED = IndexType.CLUSTERED
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is a clustered index.
    """
    HASHED = IndexType.HASHED
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is a hashed index.
    """
    OTHER = IndexType.OTHER
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is not a clustered index, a hashed index, or table statistics; it is something other than these.
    """

__all__ = ['IndexType', 'IndexTypeEnum']