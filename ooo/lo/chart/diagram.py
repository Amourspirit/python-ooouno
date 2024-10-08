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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_axis_supplier import XAxisSupplier as XAxisSupplier_c81b0c5b
from .x_diagram import XDiagram as XDiagram_8e1e0a27
from .x_diagram_positioning import XDiagramPositioning as XDiagramPositioning_18f60eba
from .x_second_axis_title_supplier import XSecondAxisTitleSupplier as XSecondAxisTitleSupplier_680a10b9
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from com.sun.star.chart.ChartDataRowSource import ChartDataRowSourceProto  # type: ignore

class Diagram(UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa, XAxisSupplier_c81b0c5b, XDiagram_8e1e0a27, XDiagramPositioning_18f60eba, XSecondAxisTitleSupplier_680a10b9):
    """
    Service Class

    the base service for the diagram of the chart document.
    
    The diagram is the object that contains the actual plot.
    
    Different Diagram Types, e.g., PieDiagram or LineDiagram, can be instantiated by the com.sun.star.lang.XMultiServiceFactory of the XChartDocument.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Diagram <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1Diagram.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.Diagram'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def AutomaticPosition(self) -> bool:
        """
        If this property is TRUE the position is calculated by the application automatically.
        
        Setting this property to false will have no effect. Instead use the interface com.sun.star.drawing.XShape to set a concrete position (note com.sun.star.chart.XDiagram is derived from com.sun.star.drawing.XShape).
        """
        ...

    @property
    @abstractmethod
    def AutomaticSize(self) -> bool:
        """
        If this property is TRUE the size is calculated by the application automatically.
        
        Setting this property to false will have no effect. Instead use the interface com.sun.star.drawing.XShape to set a concrete size (note com.sun.star.chart.XDiagram is derived from com.sun.star.drawing.XShape).
        """
        ...

    @property
    @abstractmethod
    def DataCaption(self) -> int:
        """
        specifies how the caption of data points is displayed.
        """
        ...

    @property
    @abstractmethod
    def DataRowSource(self) -> ChartDataRowSourceProto:
        """
        determines if the data for a data row is contained in the columns or in the rows of the data array.
        """
        ...

    @property
    @abstractmethod
    def MissingValueTreatment(self) -> int:
        """
        specifies how empty or invalid cells in the provided data should be handled when displayed
        """
        ...


__all__ = ['Diagram']