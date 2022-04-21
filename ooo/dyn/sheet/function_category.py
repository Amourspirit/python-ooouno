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
    from com.sun.star.sheet import FunctionCategory as FunctionCategory
    if hasattr(FunctionCategory, '_constants') and isinstance(FunctionCategory._constants, dict):
        FunctionCategory._constants['__ooo_ns__'] = 'com.sun.star.sheet'
        FunctionCategory._constants['__ooo_full_ns__'] = 'com.sun.star.sheet.FunctionCategory'
        FunctionCategory._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FunctionCategoryEnum
        ls = [f for f in dir(FunctionCategory) if not callable(getattr(FunctionCategory, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FunctionCategory, name)
        FunctionCategoryEnum = IntEnum('FunctionCategoryEnum', _dict)
    build_enum()
else:
    from ...lo.sheet.function_category import FunctionCategory as FunctionCategory

    class FunctionCategoryEnum(IntEnum):
        """
        Enum of Const Class FunctionCategory

        used to specify the category of a spreadsheet function.
        """
        DATABASE = FunctionCategory.DATABASE
        """
        specifies a database function.
        """
        DATETIME = FunctionCategory.DATETIME
        """
        specifies a function that calculates with dates and/or times.
        """
        FINANCIAL = FunctionCategory.FINANCIAL
        """
        specifies a financial function.
        """
        INFORMATION = FunctionCategory.INFORMATION
        """
        specifies a function that returns information about the cell, the cell contents or the current formula.
        """
        LOGICAL = FunctionCategory.LOGICAL
        """
        specifies a boolean function.
        """
        MATHEMATICAL = FunctionCategory.MATHEMATICAL
        """
        specifies a common mathematical function
        """
        MATRIX = FunctionCategory.MATRIX
        """
        specifies a matrix function.
        """
        STATISTICAL = FunctionCategory.STATISTICAL
        """
        specifies a statistical function
        """
        SPREADSHEET = FunctionCategory.SPREADSHEET
        """
        specifies a function that returns information using the spreadsheet contents or specific cell positions.
        """
        TEXT = FunctionCategory.TEXT
        """
        specifies a text function.
        """
        ADDIN = FunctionCategory.ADDIN
        """
        specifies a common add-in function.
        """

__all__ = ['FunctionCategory', 'FunctionCategoryEnum']
