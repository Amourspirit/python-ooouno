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
import typing
from abc import abstractproperty
from .chart_data_point_properties import ChartDataPointProperties as ChartDataPointProperties_677c10bd
from .chart_statistics import ChartStatistics as ChartStatistics_e2190d37
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class ChartDataRowProperties(ChartDataPointProperties_677c10bd, ChartStatistics_e2190d37):
    """
    Service Class

    specifies the properties for a group of graphic elements which belong to a data row (also known as data series).
    
    For this service, the properties supported by ChartDataPointProperties are applied to all data point elements contained in this group. They serve as a template; thus, when changing a data point property afterwards
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartDataRowProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartDataRowProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataRowProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Axis(self) -> int:
        """
        determines to which axis the data row is assigned.
        
        The axis must be a primary or secondary y-axis
        """
    @abstractproperty
    def DataErrorProperties(self) -> 'XPropertySet_bc180bfa':
        """
        holds the properties of the error markers, if those are enabled.
        """
    @abstractproperty
    def DataMeanValueProperties(self) -> 'XPropertySet_bc180bfa':
        """
        holds the properties of the average line, if such one is enabled.
        """
    @abstractproperty
    def DataRegressionProperties(self) -> 'XPropertySet_bc180bfa':
        """
        holds the properties of the regression line, if such one is enabled.
        """

__all__ = ['ChartDataRowProperties']

