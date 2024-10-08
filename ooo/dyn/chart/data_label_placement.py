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
# Namespace: com.sun.star.chart
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

    class DataLabelPlacement(metaclass=UnoConstMeta, type_name="com.sun.star.chart.DataLabelPlacement", name_space="com.sun.star.chart"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.chart.DataLabelPlacement``"""
        pass

    class DataLabelPlacementEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.chart.DataLabelPlacement", name_space="com.sun.star.chart"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.chart.DataLabelPlacement`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.chart import DataLabelPlacement as DataLabelPlacement
    else:
        # keep document generators happy
        from ...lo.chart.data_label_placement import DataLabelPlacement as DataLabelPlacement

    class DataLabelPlacementEnum(IntEnum):
        """
        Enum of Const Class DataLabelPlacement

        These values specify where the captions/labels of data points are displayed.
        
        **since**
        
            LibreOffice 7.0
        """
        AVOID_OVERLAP = DataLabelPlacement.AVOID_OVERLAP
        CENTER = DataLabelPlacement.CENTER
        TOP = DataLabelPlacement.TOP
        TOP_LEFT = DataLabelPlacement.TOP_LEFT
        LEFT = DataLabelPlacement.LEFT
        BOTTOM_LEFT = DataLabelPlacement.BOTTOM_LEFT
        BOTTOM = DataLabelPlacement.BOTTOM
        BOTTOM_RIGHT = DataLabelPlacement.BOTTOM_RIGHT
        RIGHT = DataLabelPlacement.RIGHT
        TOP_RIGHT = DataLabelPlacement.TOP_RIGHT
        INSIDE = DataLabelPlacement.INSIDE
        OUTSIDE = DataLabelPlacement.OUTSIDE
        NEAR_ORIGIN = DataLabelPlacement.NEAR_ORIGIN
        CUSTOM = DataLabelPlacement.CUSTOM

__all__ = ['DataLabelPlacement', 'DataLabelPlacementEnum']
