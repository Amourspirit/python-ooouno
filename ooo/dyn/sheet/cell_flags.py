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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CellFlags(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.CellFlags", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.CellFlags``"""
        pass

    class CellFlagsEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.CellFlags", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.CellFlags`` as Enum values"""
        pass

else:
    from ...lo.sheet.cell_flags import CellFlags as CellFlags

    class CellFlagsEnum(IntFlag):
        """
        Enum of Const Class CellFlags

        These constants select different types of cell contents.
        
        The values can be combined. They are used to insert, copy, or delete contents.
        """
        VALUE = CellFlags.VALUE
        """
        selects constant numeric values that are not formatted as dates or times.
        """
        DATETIME = CellFlags.DATETIME
        """
        selects constant numeric values that have a date or time number format.
        """
        STRING = CellFlags.STRING
        """
        selects constant strings.
        """
        ANNOTATION = CellFlags.ANNOTATION
        """
        selects cell annotations.
        """
        FORMULA = CellFlags.FORMULA
        """
        selects formulas.
        """
        HARDATTR = CellFlags.HARDATTR
        """
        selects all explicit formatting, but not the formatting which is applied implicitly through style sheets.
        """
        STYLES = CellFlags.STYLES
        """
        selects cell styles.
        """
        OBJECTS = CellFlags.OBJECTS
        """
        selects drawing objects.
        """
        EDITATTR = CellFlags.EDITATTR
        """
        selects formatting within parts of the cell contents.
        """
        FORMATTED = CellFlags.FORMATTED
        """
        selects cells with formatting within the cells or cells with more than one paragraph within the cells.
        """

__all__ = ['CellFlags', 'CellFlagsEnum']
