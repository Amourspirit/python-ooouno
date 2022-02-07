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
# Namespace: com.sun.star.sdb
from enum import IntEnum
from ...lo.sdb.row_change_action import RowChangeAction as RowChangeAction


class RowChangeActionEnum(IntEnum):
    """
    Enum of Const Class RowChangeAction

    determines the type of change which is going to be performed.
    """
    INSERT = RowChangeAction.INSERT
    """
    indicates that an insert will be performed.
    """
    UPDATE = RowChangeAction.UPDATE
    """
    indicates that an update will be performed.
    """
    DELETE = RowChangeAction.DELETE
    """
    indicates that a delete will be performed.
    """

__all__ = ['RowChangeAction', 'RowChangeActionEnum']
