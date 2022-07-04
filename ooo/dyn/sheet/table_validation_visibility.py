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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class TableValidationVisibility(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.TableValidationVisibility", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.TableValidationVisibility``"""
        pass

    class TableValidationVisibilityEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.TableValidationVisibility", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.TableValidationVisibility`` as Enum values"""
        pass

else:
    from ...lo.sheet.table_validation_visibility import TableValidationVisibility as TableValidationVisibility

    class TableValidationVisibilityEnum(IntEnum):
        """
        Enum of Const Class TableValidationVisibility

        These constants specify whether and how a list of possible values of a cell should be shown.
        """
        INVISIBLE = TableValidationVisibility.INVISIBLE
        """
        The List is not shown.
        """
        UNSORTED = TableValidationVisibility.UNSORTED
        """
        The List is shown unsorted.
        """
        SORTEDASCENDING = TableValidationVisibility.SORTEDASCENDING
        """
        The List is shown sorted ascending.
        """

__all__ = ['TableValidationVisibility', 'TableValidationVisibilityEnum']
