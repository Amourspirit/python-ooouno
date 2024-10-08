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
from .chart3_d_bar_properties import Chart3DBarProperties as Chart3DBarProperties_22f00ec5
from ..drawing.fill_properties import FillProperties as FillProperties_f1200da8
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc

class ChartDataPointProperties(Chart3DBarProperties_22f00ec5, FillProperties_f1200da8, LineProperties_f13f0da9, CharacterProperties_1d4f0ef3, UserDefinedAttributesSupplier_9fbe1222):
    """
    Service Class

    specifies all the properties for the graphic object of a data point (e.g., a single bar in a bar chart).
    
    Text properties correlate to the data description of the data point. There is a similar service for a group of graphic elements called ChartDataRowProperties for the properties of whole data rows.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartDataPointProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartDataPointProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataPointProperties'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def DataCaption(self) -> int:
        """
        specifies how the captions of data points are displayed.
        """
        ...

    @property
    @abstractmethod
    def LabelPlacement(self) -> int:
        """
        specifies a relative position for the data label
        """
        ...

    @property
    @abstractmethod
    def LabelSeparator(self) -> str:
        """
        specifies a string that is used to separate the parts of a data label (caption)
        """
        ...

    @property
    @abstractmethod
    def NumberFormat(self) -> int:
        """
        specifies a number format for the display of the value in the data label
        """
        ...

    @property
    @abstractmethod
    def PercentageNumberFormat(self) -> int:
        """
        specifies a number format for the display of the percentage value in the data label
        """
        ...

    @property
    @abstractmethod
    def SegmentOffset(self) -> int:
        """
        the offset by which pie segments in a PieDiagram are dragged outside from the center.
        
        This value is given in percent of the radius.
        """
        ...

    @property
    @abstractmethod
    def SymbolBitmap(self) -> XGraphic_a4da0afc:
        """
        In charts that support symbols, you can set this property to a graphic object.
        
        This graphic is then used as symbol for each data point.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @property
    @abstractmethod
    def SymbolBitmapURL(self) -> str:
        """
        In charts that support symbols, you can set this property to any valid URL that points to a graphic file.
        
        This graphic is then used as symbol for each data point.
        
        When you query this value you get an internal URL of the embedded graphic.
        """
        ...

    @property
    @abstractmethod
    def SymbolType(self) -> int:
        """
        specifies the type of symbols if the current chart type supports the usage of symbols.
        """
        ...

    @property
    @abstractmethod
    def TextWordWrap(self) -> bool:
        """
        specifies if the text of a data label (caption) must be wrapped
        
        **since**
        
            LibreOffice 5.1
        """
        ...


__all__ = ['ChartDataPointProperties']

