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
# Namespace: com.sun.star.chart2
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.chart2 import DataPointGeometry3D
else:
    from ...lo.chart2.data_point_geometry3_d import DataPointGeometry3D as DataPointGeometry3D


class DataPointGeometry3DEnum(IntEnum):
    """
    Enum of Const Class DataPointGeometry3D

    These values specify the geometry of data points in 3D bar charts.
    """
    CUBOID = DataPointGeometry3D.CUBOID
    """
    a cuboid
    """
    CYLINDER = DataPointGeometry3D.CYLINDER
    """
    a cylinder with a circle as base
    """
    CONE = DataPointGeometry3D.CONE
    """
    a cone with a circle as base
    """
    PYRAMID = DataPointGeometry3D.PYRAMID
    """
    a pyramid with a square as base
    """

__all__ = ['DataPointGeometry3D', 'DataPointGeometry3DEnum']
