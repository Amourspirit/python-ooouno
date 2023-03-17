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
# Libre Office Version: 7.4
# Namespace: com.sun.star.table
from ..container.x_named import XNamed as XNamed_a6520b08
from ..document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier_8b631174
from .x_table_chart import XTableChart as XTableChart_ae420b42

class TableChart(XNamed_a6520b08, XEmbeddedObjectSupplier_8b631174, XTableChart_ae420b42):
    """
    Service Class

    represents a chart based on data in a table or spreadsheet.
    
    This service does not represent the chart document model itself, but the object in the table that contains this chart document.

    See Also:
        `API TableChart <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1TableChart.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.TableChart'
    __ooo_type_name__: str = 'service'



__all__ = ['TableChart']

