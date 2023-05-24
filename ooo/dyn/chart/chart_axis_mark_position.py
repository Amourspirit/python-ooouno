# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class ChartAxisMarkPosition(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartAxisMarkPosition", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartAxisMarkPosition`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.chart.ChartAxisMarkPosition import AT_AXIS as CHART_AXIS_MARK_POSITION_AT_AXIS
        from com.sun.star.chart.ChartAxisMarkPosition import AT_LABELS as CHART_AXIS_MARK_POSITION_AT_LABELS
        from com.sun.star.chart.ChartAxisMarkPosition import AT_LABELS_AND_AXIS as CHART_AXIS_MARK_POSITION_AT_LABELS_AND_AXIS

        class ChartAxisMarkPosition(uno.Enum):
            """
            Enum Class


            See Also:
                `API ChartAxisMarkPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#aed594287d3f18573f625e8f708a27555>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.chart.ChartAxisMarkPosition', value)

            __ooo_ns__: str = 'com.sun.star.chart'
            __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisMarkPosition'
            __ooo_type_name__: str = 'enum'

            AT_AXIS = CHART_AXIS_MARK_POSITION_AT_AXIS
            """
            The interval marks are drawn at the axis line.

            This makes a difference to \"AT_LABELS\" only when the labels are not placed near the axis (
            """
            AT_LABELS = CHART_AXIS_MARK_POSITION_AT_LABELS
            """
            The interval marks are drawn besides the axis labels.
            """
            AT_LABELS_AND_AXIS = CHART_AXIS_MARK_POSITION_AT_LABELS_AND_AXIS
            """
            Interval marks are drawn at the axis line and also besides the axis labels.

            This makes a difference to \"AT_LABELS\" only when the labels are not placed near the axis (
            """
    else:
        # keep document generators happy
        from ...lo.chart.chart_axis_mark_position import ChartAxisMarkPosition as ChartAxisMarkPosition


__all__ = ['ChartAxisMarkPosition']
