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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart
from abc import abstractproperty, ABC

class StackableDiagram(ABC):
    """
    Service Class

    a helper service for stackable chart types (e.g., charts in which the data rows may be displayed stacked on each other or in percent relation).

    See Also:
        `API StackableDiagram <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1StackableDiagram.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.StackableDiagram'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Percent(self) -> bool:
        """
        If TRUE, the series of the diagram are stacked and each category sums up to 100%.
        """

    @abstractproperty
    def Stacked(self) -> bool:
        """
        If TRUE, the series of the diagram are stacked.
        
        If you have a stacked bar chart, you can easily determine the sum of data in each category, by taking the top of the topmost bar.
        """



__all__ = ['StackableDiagram']

