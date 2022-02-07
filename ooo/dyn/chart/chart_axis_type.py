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
from ...lo.chart.chart_axis_type import ChartAxisType as ChartAxisType


class ChartAxisTypeEnum(IntEnum):
    """
    Enum of Const Class ChartAxisType

    
    **since**
    
        OOo 3.4
    """
    AUTOMATIC = ChartAxisType.AUTOMATIC
    """
    the type of the axis is chosen automatically dependent on the chart type, the dimension and the underlying data
    """
    CATEGORY = ChartAxisType.CATEGORY
    """
    the axis represent discrete category texts if chart type and the dimension allows
    """
    DATE = ChartAxisType.DATE
    """
    the axis shows dates if the given data and chart type and the dimension allows
    """

__all__ = ['ChartAxisType', 'ChartAxisTypeEnum']
