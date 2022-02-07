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
# Namespace: com.sun.star.accessibility
from enum import IntEnum
from ...lo.accessibility.accessible_table_model_change_type import AccessibleTableModelChangeType as AccessibleTableModelChangeType


class AccessibleTableModelChangeTypeEnum(IntEnum):
    """
    Enum of Const Class AccessibleTableModelChangeType

    Type of a change made to a table model.
    
    **since**
    
        OOo 1.1.2
    """
    INSERT = AccessibleTableModelChangeType.INSERT
    """
    One or more rows and/or columns have been inserted.
    
    Use the fields of the AccessibleTableModelChange structure to determine the indices of the rows and/or columns that have been inserted.
    """
    DELETE = AccessibleTableModelChangeType.DELETE
    """
    One or more rows and/or columns have been deleted.
    
    The affected area of the table is stored in the fields of the AccessibleTableModelChange structure.
    """
    UPDATE = AccessibleTableModelChangeType.UPDATE
    """
    Some of the table data has changed.
    
    The number of rows and columns remains unchanged. Only (some of) the content of the cells in the range that is specified by the fields of the AccessibleTableModelChange structure have been changed.
    """

__all__ = ['AccessibleTableModelChangeType', 'AccessibleTableModelChangeTypeEnum']
