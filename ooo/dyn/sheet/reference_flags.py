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
# Namespace: com.sun.star.sheet
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import ReferenceFlags as ReferenceFlags
else:
    from ...lo.sheet.reference_flags import ReferenceFlags as ReferenceFlags


class ReferenceFlagsEnum(IntFlag):
    """
    Enum of Const Class ReferenceFlags

    defines flags for references.
    
    The values can be combined.
    """
    COLUMN_RELATIVE = ReferenceFlags.COLUMN_RELATIVE
    """
    selects a relative column reference.
    """
    COLUMN_DELETED = ReferenceFlags.COLUMN_DELETED
    """
    marks a deleted column reference.
    """
    ROW_RELATIVE = ReferenceFlags.ROW_RELATIVE
    """
    selects a relative row reference.
    """
    ROW_DELETED = ReferenceFlags.ROW_DELETED
    """
    marks a deleted row reference.
    """
    SHEET_RELATIVE = ReferenceFlags.SHEET_RELATIVE
    """
    selects a relative sheet reference.
    """
    SHEET_DELETED = ReferenceFlags.SHEET_DELETED
    """
    marks a deleted sheet reference.
    """
    SHEET_3D = ReferenceFlags.SHEET_3D
    """
    selects a 3D sheet reference.
    """
    RELATIVE_NAME = ReferenceFlags.RELATIVE_NAME
    """
    marks a reference from a relative range name.
    """

__all__ = ['ReferenceFlags', 'ReferenceFlagsEnum']
