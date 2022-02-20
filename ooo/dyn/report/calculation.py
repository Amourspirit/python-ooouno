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
# Namespace: com.sun.star.report
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.report import Calculation as Calculation
    if hasattr(Calculation, '_constants') and isinstance(Calculation._constants, dict):
        Calculation._constants['__ooo_ns__'] = 'com.sun.star.report'
        Calculation._constants['__ooo_full_ns__'] = 'com.sun.star.report.Calculation'
        Calculation._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CalculationEnum
        ls = [f for f in dir(Calculation) if not callable(getattr(Calculation, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(Calculation, name)
        CalculationEnum = IntEnum('CalculationEnum', _dict)
    build_enum()
else:
    from ...lo.report.calculation import Calculation as Calculation

    class CalculationEnum(IntEnum):
        """
        Enum of Const Class Calculation

        Specifies how to calculate a value.
        """
        NONE = Calculation.NONE
        """
        returns the average of a field.
        """
        AVERAGE = Calculation.AVERAGE
        """
        returns the average of a field.
        """
        CORRELATION = Calculation.CORRELATION
        """
        returns the correlation of two fields.
        """
        COUNT = Calculation.COUNT
        """
        counts the number of values, from the field.
        """
        COVARIANCE = Calculation.COVARIANCE
        """
        returns the measure of the linear relation between paired variables.
        """
        DISTINCTCOUNT = Calculation.DISTINCTCOUNT
        """
        returns the number of none repeating values, from the field.
        """
        MAXIMUM = Calculation.MAXIMUM
        """
        returns the largest value from the field.
        """
        MEDIAN = Calculation.MEDIAN
        """
        returns the middle value in a sequence of numeric values.
        """
        MINIMUM = Calculation.MINIMUM
        """
        returns the smallest value from the field.
        """
        MODE = Calculation.MODE
        """
        returns the most frequently returning value from the field.
        """
        NTHLARGEST = Calculation.NTHLARGEST
        """
        returns the Nth largest value from the field.
        """
        NTHMOSTFREQUENT = Calculation.NTHMOSTFREQUENT
        """
        returns the Nth most commonly occurring value from the field.
        """
        NTHSMALLEST = Calculation.NTHSMALLEST
        """
        returns the Nth smallest value from the field.
        """
        PERCENTAGE = Calculation.PERCENTAGE
        """
        returns as a percentage of the grand total summary.
        """
        PERCENTILE = Calculation.PERCENTILE
        """
        returns the value for a specified percentile in a Number or Currency field.
        """
        POPSTANDARDDEVIATION = Calculation.POPSTANDARDDEVIATION
        """
        returns how much each value in the field deviate from the mean or average value for that field.
        """
        POPVARIANCE = Calculation.POPVARIANCE
        """
        returns the square of the standard deviation.
        """
        SAMPLESTANDARDDEVIATION = Calculation.SAMPLESTANDARDDEVIATION
        """
        returns the sample standard deviation for the field.
        """
        SAMPLEVARIANCE = Calculation.SAMPLEVARIANCE
        """
        returns the sample variance for the field.
        """
        SUM = Calculation.SUM
        """
        returns the total of all the values for the field.
        """
        WEIGHTEDAVG = Calculation.WEIGHTEDAVG
        """
        returns the weighted average for the field.
        """

__all__ = ['Calculation', 'CalculationEnum']
