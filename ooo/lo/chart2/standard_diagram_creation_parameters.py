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
# Namespace: com.sun.star.chart2
from abc import abstractproperty, ABC

class StandardDiagramCreationParameters(ABC):
    """
    Service Class

    parameters that may be passed to XChartTypeTemplate.createDiagramByDataSource().

    See Also:
        `API StandardDiagramCreationParameters <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1StandardDiagramCreationParameters.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.StandardDiagramCreationParameters'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HasCategories(self) -> bool:
        """
        States whether the first XLabeledDataSequence in a data-source is used as categories.
        """

    @abstractproperty
    def UseCategoriesAsX(self) -> bool:
        """
        If categories are given they should be used as x values also if a chart type requires x values.
        
        Default is true.
        """



__all__ = ['StandardDiagramCreationParameters']

