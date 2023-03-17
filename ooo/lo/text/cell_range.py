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
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..chart.x_chart_data_array import XChartDataArray as XChartDataArray_df4c0cdd
from ..sheet.x_cell_range_data import XCellRangeData as XCellRangeData_d2e70c60
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
from ..table.x_cell_range import XCellRange as XCellRange_a2f70ad5
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..style.graphic_location import GraphicLocation as GraphicLocation_e3ef0d30
    from ..util.color import Color as Color_68e908c5

class CellRange(CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, ParagraphPropertiesAsian_6e8c10e8, ParagraphPropertiesComplex_91de11d4, XChartDataArray_df4c0cdd, XCellRangeData_d2e70c60, XCellRange_a2f70ad5):
    """
    Service Class

    area of cells within a text table.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API CellRange <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1CellRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.CellRange'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BackColor(self) -> 'Color_68e908c5':
        """
        contains color of the background.
        """
        ...

    @abstractproperty
    def BackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @abstractproperty
    def BackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic.
        """
        ...

    @abstractproperty
    def BackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic.
        """
        ...

    @abstractproperty
    def BackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...

    @abstractproperty
    def BackTransparent(self) -> bool:
        """
        determines if the background color is transparent.
        """
        ...

    @abstractproperty
    def ChartColumnAsLabel(self) -> bool:
        """
        determines if the first column of the table should be treated as axis labels when a chart is to be created.
        """
        ...

    @abstractproperty
    def ChartRowAsLabel(self) -> bool:
        """
        determines if the first row of the table should be treated as axis labels when a chart is to be created.
        """
        ...

    @abstractproperty
    def NumberFormat(self) -> int:
        """
        contains the number format.
        """
        ...



__all__ = ['CellRange']

