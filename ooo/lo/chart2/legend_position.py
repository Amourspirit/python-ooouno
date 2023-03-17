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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from enum import Enum


class LegendPosition(Enum):
    """
    Enum Class

    ENUM LegendPosition

    See Also:
        `API LegendPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a85df18f245c9e4d24e32ebb9ee879042>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.LegendPosition'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart2.LegendPosition'

    CUSTOM = 'CUSTOM'
    """
    The position of the legend is given by an offset value.
    """
    LINE_END = 'LINE_END'
    """
    In LTR mode this is the right-hand side.
    """
    LINE_START = 'LINE_START'
    """
    In LTR mode this is the left-hand side.
    """
    PAGE_END = 'PAGE_END'
    """
    In LTR mode this is the bottom side.
    """
    PAGE_START = 'PAGE_START'
    """
    In LTR mode this is the top side.
    """

__all__ = ['LegendPosition']

