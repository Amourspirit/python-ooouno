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
    from com.sun.star.sheet import GeneralFunction2 as GeneralFunction2
    if hasattr(GeneralFunction2, '_constants') and isinstance(GeneralFunction2._constants, dict):
        GeneralFunction2._constants['__ooo_ns__'] = 'com.sun.star.sheet'
        GeneralFunction2._constants['__ooo_full_ns__'] = 'com.sun.star.sheet.GeneralFunction2'
        GeneralFunction2._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global GeneralFunction2Enum
        ls = [f for f in dir(GeneralFunction2) if not callable(getattr(GeneralFunction2, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(GeneralFunction2, name)
        GeneralFunction2Enum = IntEnum('GeneralFunction2Enum', _dict)
    build_enum()
else:
    from ...lo.sheet.general_function2 import GeneralFunction2 as GeneralFunction2

    class GeneralFunction2Enum(IntEnum):
        """
        Enum of Const Class GeneralFunction2

        used to specify a function to be calculated from values.
        
        **since**
        
            LibreOffice 5.3
        """
        NONE = GeneralFunction2.NONE
        """
        nothing is calculated.
        """
        AUTO = GeneralFunction2.AUTO
        """
        function is determined automatically.
        
        If the values are all numerical, SUM is used, otherwise COUNT.
        """
        SUM = GeneralFunction2.SUM
        """
        sum of all numerical values is calculated.
        """
        COUNT = GeneralFunction2.COUNT
        """
        all values, including non-numerical values, are counted.
        """
        AVERAGE = GeneralFunction2.AVERAGE
        """
        average of all numerical values is calculated.
        """
        MAX = GeneralFunction2.MAX
        """
        maximum value of all numerical values is calculated.
        """
        MIN = GeneralFunction2.MIN
        """
        minimum value of all numerical values is calculated.
        """
        PRODUCT = GeneralFunction2.PRODUCT
        """
        product of all numerical values is calculated.
        """
        COUNTNUMS = GeneralFunction2.COUNTNUMS
        """
        numerical values are counted.
        """
        STDEV = GeneralFunction2.STDEV
        """
        standard deviation is calculated based on a sample.
        """
        STDEVP = GeneralFunction2.STDEVP
        """
        standard deviation is calculated based on the entire population.
        """
        VAR = GeneralFunction2.VAR
        """
        variance is calculated based on a sample.
        """
        VARP = GeneralFunction2.VARP
        """
        variance is calculated based on the entire population.
        """
        MEDIAN = GeneralFunction2.MEDIAN
        """
        median of all numerical values is calculated.
        
        **since**
        
            LibreOffice 5.3
        """

__all__ = ['GeneralFunction2', 'GeneralFunction2Enum']
