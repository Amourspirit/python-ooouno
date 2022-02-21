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
# Namespace: com.sun.star.chart
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.chart import ErrorBarStyle as ErrorBarStyle
    if hasattr(ErrorBarStyle, '_constants') and isinstance(ErrorBarStyle._constants, dict):
        ErrorBarStyle._constants['__ooo_ns__'] = 'com.sun.star.chart'
        ErrorBarStyle._constants['__ooo_full_ns__'] = 'com.sun.star.chart.ErrorBarStyle'
        ErrorBarStyle._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ErrorBarStyleEnum
        ls = [f for f in dir(ErrorBarStyle) if not callable(getattr(ErrorBarStyle, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ErrorBarStyle, name)
        ErrorBarStyleEnum = IntEnum('ErrorBarStyleEnum', _dict)
    build_enum()
else:
    from ...lo.chart.error_bar_style import ErrorBarStyle as ErrorBarStyle

    class ErrorBarStyleEnum(IntEnum):
        """
        Enum of Const Class ErrorBarStyle

        specifies the style of error indicators.
        """
        NONE = ErrorBarStyle.NONE
        """
        error indicators are not displayed.
        """
        VARIANCE = ErrorBarStyle.VARIANCE
        """
        displays error indicators for the variance of the data.
        """
        STANDARD_DEVIATION = ErrorBarStyle.STANDARD_DEVIATION
        """
        displays error indicators for the standard deviation (square root of variance) of the data.
        """
        ABSOLUTE = ErrorBarStyle.ABSOLUTE
        """
        the error indicators for all data points have the same absolute value as length for either direction.
        
        The values for these are given as absolute numbers in ChartStatistics.ConstantErrorLow and ChartStatistics.ConstantErrorHigh
        """
        RELATIVE = ErrorBarStyle.RELATIVE
        """
        The length of the error indicators is calculated for each data point by taking the percentage given as ChartStatistics.PercentageError of its value.
        """
        ERROR_MARGIN = ErrorBarStyle.ERROR_MARGIN
        """
        The length of the error indicators for all data points is calculated by taking the percentage given as ChartStatistics.ErrorMargin of the largest data point value.
        """
        STANDARD_ERROR = ErrorBarStyle.STANDARD_ERROR
        """
        displays error indicators for the standard error, also known as the standard deviation of the mean (SDOM).
        """
        FROM_DATA = ErrorBarStyle.FROM_DATA
        """
        Uses values given by cell ranges of the container document.
        
        The values for the cell ranges are given in the properties ChartStatistics.ErrorBarRangePositive for positive indicators and ChartStatistics.ErrorBarRangeNegative for negative indicators.
        """

__all__ = ['ErrorBarStyle', 'ErrorBarStyleEnum']
