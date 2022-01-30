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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.chart.ChartLegendPosition import (BOTTOM, LEFT, NONE, RIGHT, TOP)

if TYPE_CHECKING or _DYNAMIC is False:


    class ChartLegendPosition(Enum):
        """
        Enum Class

        

        See Also:
            `API ChartLegendPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a65c2b55fdf73cbbf2fdcfef7d305b6c3>`_
        """
        BOTTOM = 'BOTTOM'
        """
        displays the chart legend beneath the diagram.
        """
        LEFT = 'LEFT'
        """
        displays the chart legend on the left side of the diagram.
        """
        NONE = 'NONE'
        """
        error indicators are not displayed.
        
        displays no regression curve.
        
        no chart legend is displayed.
        
        displays no error indicators.
        """
        RIGHT = 'RIGHT'
        """
        displays the chart legend on the right side of the diagram.
        """
        TOP = 'TOP'
        """
        displays the chart legend above the diagram.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global ChartLegendPosition
        _dict = {
            "BOTTOM": BOTTOM,
            "LEFT": LEFT,
            "NONE": NONE,
            "RIGHT": RIGHT,
            "TOP": TOP,
        }

        ChartLegendPosition = type('ChartLegendPosition', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(ChartLegendPosition, k, v)

    _dynamic_enum()

__all__ = ['ChartLegendPosition']

