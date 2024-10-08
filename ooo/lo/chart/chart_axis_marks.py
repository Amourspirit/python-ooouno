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


class ChartAxisMarks(object):
    """
    Const Class

    With these constants you can specify how the tick-marks of an axis are displayed.
    
    You can combine INNER and OUTER with an arithmetical or-operation to get tick-marks that extend in both directions.

    See Also:
        `API ChartAxisMarks <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ChartAxisMarks.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisMarks'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    Do not display any marks.
    """
    INNER = 1
    """
    Display marks that point into the diagram area.
    """
    OUTER = 2
    """
    Display marks that point out of the diagram area.
    """

__all__ = ['ChartAxisMarks']
