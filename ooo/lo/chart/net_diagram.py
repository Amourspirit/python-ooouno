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
from .chart_axis_y_supplier import ChartAxisYSupplier as ChartAxisYSupplier_a9e0e4e
from .diagram import Diagram as Diagram_844409cf
from .stackable_diagram import StackableDiagram as StackableDiagram_ee760d59

class NetDiagram(ChartAxisYSupplier_a9e0e4e, Diagram_844409cf, StackableDiagram_ee760d59):
    """
    Service Class

    specifies net diagrams.
    
    Net diagrams are also known as radar diagrams.

    See Also:
        `API NetDiagram <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1NetDiagram.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.NetDiagram'
    __ooo_type_name__: str = 'service'



__all__ = ['NetDiagram']

