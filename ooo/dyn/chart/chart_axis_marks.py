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
    from com.sun.star.chart import ChartAxisMarks as ChartAxisMarks
else:
    from ...lo.chart.chart_axis_marks import ChartAxisMarks as ChartAxisMarks


class ChartAxisMarksEnum(IntEnum):
    """
    Enum of Const Class ChartAxisMarks

    With these constants you can specify how the tick-marks of an axis are displayed.
    
    You can combine INNER and OUTER with an arithmetical or-operation to get tick-marks that extend in both directions.
    """
    NONE = ChartAxisMarks.NONE
    """
    Do not display any marks.
    """
    INNER = ChartAxisMarks.INNER
    """
    Display marks that point into the diagram area.
    """
    OUTER = ChartAxisMarks.OUTER
    """
    Display marks that point out of the diagram area.
    """

__all__ = ['ChartAxisMarks', 'ChartAxisMarksEnum']
