# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222

class ChartGrid(LineProperties_f13f0da9, UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa):
    """
    Service Class

    specifies the grid of the diagram in a chart.
    
    The distance between the grid lines depends on the distance of the help or main tick marks, which may be set in ChartAxis.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartGrid <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartGrid.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartGrid'
    __ooo_type_name__: str = 'service'


__all__ = ['ChartGrid']

