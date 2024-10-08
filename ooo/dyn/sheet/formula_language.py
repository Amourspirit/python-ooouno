# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FormulaLanguage(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.FormulaLanguage", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.FormulaLanguage``"""
        pass

    class FormulaLanguageEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.FormulaLanguage", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.FormulaLanguage`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sheet import FormulaLanguage as FormulaLanguage
    else:
        # keep document generators happy
        from ...lo.sheet.formula_language import FormulaLanguage as FormulaLanguage

    class FormulaLanguageEnum(IntEnum):
        """
        Enum of Const Class FormulaLanguage

        Constants designating the formula language used with XFormulaOpCodeMapper methods.
        
        **since**
        
            LibreOffice 5.3
        """
        ODFF = FormulaLanguage.ODFF
        """
        Function names and operators as defined by the OASIS OpenDocument Format (ODF) Formula specification (ODFF aka OpenFormula).
        """
        ODF_11 = FormulaLanguage.ODF_11
        """
        Function names and operators as used in ODF documents prior to the ODFF specification, up to ODF v1.1.
        """
        ENGLISH = FormulaLanguage.ENGLISH
        """
        Function names and operators as used in the English language user interface.
        """
        NATIVE = FormulaLanguage.NATIVE
        """
        Function names and operators as used in the current native language user interface.
        """
        XL_ENGLISH = FormulaLanguage.XL_ENGLISH
        """
        Function names and operators as used in the English version of Excel.
        
        This formula language is also used in VBA formulas.
        """
        OOXML = FormulaLanguage.OOXML
        """
        Function names and operators as used in OOXML.
        
        **since**
        
            LibreOffice 4.2
        """
        API = FormulaLanguage.API
        """
        Function names and operators as used with XFunctionAccess and other API context.
        
        Names are mostly identical to ENGLISH and ODF_11, but while ENGLISH names can be adapted to UI needs and ODF_11 has to stay error compatible, the API names strive to stay compatible but may get corrected in case of errors. Earlier versions than LibreOffice 5.3 always used ODF_11 in API context.
        
        **since**
        
            LibreOffice 5.3
        """

__all__ = ['FormulaLanguage', 'FormulaLanguageEnum']
