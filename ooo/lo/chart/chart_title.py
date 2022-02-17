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
from ..drawing.shape import Shape as Shape_85cc09e5
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222

class ChartTitle(Shape_85cc09e5, UserDefinedAttributesSupplier_9fbe1222):
    """
    Service Class

    specifies titles in a chart.
    
    In a chart there may be the following titles: the main title, the sub title, and axis titles of the x- and y-axis.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartTitle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartTitle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartTitle'
    __ooo_type_name__: str = 'service'



__all__ = ['ChartTitle']
