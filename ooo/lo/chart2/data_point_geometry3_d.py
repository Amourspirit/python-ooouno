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
# Namespace: com.sun.star.chart2


class DataPointGeometry3D(object):
    """
    Const Class

    These values specify the geometry of data points in 3D bar charts.

    See Also:
        `API DataPointGeometry3D <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2_1_1DataPointGeometry3D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.DataPointGeometry3D'
    __ooo_type_name__: str = 'const'

    CUBOID = 0
    """
    a cuboid
    """
    CYLINDER = 1
    """
    a cylinder with a circle as base
    """
    CONE = 2
    """
    a cone with a circle as base
    """
    PYRAMID = 3
    """
    a pyramid with a square as base
    """

__all__ = ['DataPointGeometry3D']
