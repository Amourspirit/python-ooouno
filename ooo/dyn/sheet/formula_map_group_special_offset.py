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
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import FormulaMapGroupSpecialOffset as FormulaMapGroupSpecialOffset
else:
    from ...lo.sheet.formula_map_group_special_offset import FormulaMapGroupSpecialOffset as FormulaMapGroupSpecialOffset


class FormulaMapGroupSpecialOffsetEnum(IntEnum):
    """
    Enum of Const Class FormulaMapGroupSpecialOffset

    Constants designating the offsets within the sequence returned by XFormulaOpCodeMapper.getAvailableMappings() when called for group FormulaMapGroup.SPECIAL.
    
    The number of constants may grow in future versions!
    """
    PUSH = FormulaMapGroupSpecialOffset.PUSH
    """
    Formula tokens containing the op-code obtained from this offset describe a formula operand token that will be pushed onto the formula stack while the formula is interpreted.
    
    The FormulaToken.Data member shall contain one of the following values:
    """
    CALL = FormulaMapGroupSpecialOffset.CALL
    STOP = FormulaMapGroupSpecialOffset.STOP
    """
    Formula tokens containing the op-code obtained from this offset instruct the formula interpreter to immediately stop interpreting the formula.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    EXTERNAL = FormulaMapGroupSpecialOffset.EXTERNAL
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to an external function (e.g.
    
    add-in function) used in formulas.
    
    The FormulaToken.Data member shall contain a string with the programmatic name of the function, e.g. \"com.sun.star.sheet.addin.Analysis.getEomonth\" for the EOMONTH function from the Analysis add-in.
    """
    NAME = FormulaMapGroupSpecialOffset.NAME
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a defined name (also known as named range) used in formulas.
    
    The FormulaToken.Data member shall contain an integer value of type long specifying the index of the defined name. This index can be obtained from the defined name using its NamedRange.TokenIndex property.
    """
    NO_NAME = FormulaMapGroupSpecialOffset.NO_NAME
    """
    Formula tokens containing the op-code obtained from this offset describe an invalid name that resolves to the NAME? error in formulas.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    MISSING = FormulaMapGroupSpecialOffset.MISSING
    """
    Formula tokens containing the op-code obtained from this offset describe an empty function parameter.
    
    Example: In the formula =SUM(1;;2) the second parameter is empty and represented by a formula token containing the \"missing\" op-code.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    BAD = FormulaMapGroupSpecialOffset.BAD
    """
    Formula tokens containing the op-code obtained from this offset describe \"bad\" data in a formula, e.g.
    
    data the formula parser was not able to parse.
    
    The FormulaToken.Data member shall contain a string with the bad data. This string will be displayed literally in the formula.
    """
    SPACES = FormulaMapGroupSpecialOffset.SPACES
    """
    Formula tokens containing the op-code obtained from this offset describe whitespace characters within the string representation of a formula.
    
    Whitespace characters in formulas are used for readability and do not affect the result of the formula.
    
    The FormulaToken.Data member shall contain a positive integer value of type long specifying the number of space characters.
    
    Attention: This may change in next versions to support other characters than simple space characters (e.g. line feeds, horizontal tabulators, non-breakable spaces).
    """
    MAT_REF = FormulaMapGroupSpecialOffset.MAT_REF
    DB_AREA = FormulaMapGroupSpecialOffset.DB_AREA
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a database range used in formulas.
    
    The FormulaToken.Data member shall contain an integer value of type long specifying the index of the database range. This index can be obtained from the database range using its DatabaseRange.TokenIndex property.
    """
    MACRO = FormulaMapGroupSpecialOffset.MACRO
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a macro function called in a formula.
    
    The FormulaToken.Data member shall contain a string specifying the name of the macro function.
    """
    COL_ROW_NAME = FormulaMapGroupSpecialOffset.COL_ROW_NAME

__all__ = ['FormulaMapGroupSpecialOffset', 'FormulaMapGroupSpecialOffsetEnum']
