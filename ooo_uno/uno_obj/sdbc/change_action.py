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


class ChangeAction(object):
    """
    Const Class

    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChangeAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1ChangeAction.html>`_
    """
    INSERT = 1
    """
    indicates that an insert will be performed.
    """
    UPDATE = 2
    """
    indicates that an update will be performed.
    """
    DELETE = 3
    """
    indicates that a delete will be performed.
    """
    UNDO = 4
    """
    indicates that an undo will be performed.
    """


class ChangeActionEnum(IntEnum):
    """
    Enum of Const Class ChangeAction

    
    .. deprecated::
    
        Class is deprecated.
    """
    INSERT = ChangeAction.INSERT
    """
    indicates that an insert will be performed.
    """
    UPDATE = ChangeAction.UPDATE
    """
    indicates that an update will be performed.
    """
    DELETE = ChangeAction.DELETE
    """
    indicates that a delete will be performed.
    """
    UNDO = ChangeAction.UNDO
    """
    indicates that an undo will be performed.
    """

__all__ = ['ChangeAction', 'ChangeActionEnum']
