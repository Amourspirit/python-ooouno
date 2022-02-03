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


class AxisType(object):
    """
    Const Class


    See Also:
        `API AxisType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2_1_1AxisType.html>`_
    """
    REALNUMBER = 0
    """
    the axis represent real numbers
    """
    PERCENT = 1
    """
    the axis represent real numbers in percent
    """
    CATEGORY = 2
    """
    the axis represent discrete categories
    """
    SERIES = 3
    """
    the axis shows the series names (z axis)
    """
    DATE = 4
    """
    the axis shows dates
    """


class AxisTypeEnum(IntEnum):
    """
    Enum of Const Class AxisType

    """
    REALNUMBER = AxisType.REALNUMBER
    """
    the axis represent real numbers
    """
    PERCENT = AxisType.PERCENT
    """
    the axis represent real numbers in percent
    """
    CATEGORY = AxisType.CATEGORY
    """
    the axis represent discrete categories
    """
    SERIES = AxisType.SERIES
    """
    the axis shows the series names (z axis)
    """
    DATE = AxisType.DATE
    """
    the axis shows dates
    """

__all__ = ['AxisType', 'AxisTypeEnum']
