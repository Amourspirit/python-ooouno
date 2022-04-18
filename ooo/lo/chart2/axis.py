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
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart2
import typing
from abc import abstractproperty
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from .x_axis import XAxis as XAxis_796b0939
from .x_titled import XTitled as XTitled_8d490a0a
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from ..chart.chart_axis_arrange_order_type import ChartAxisArrangeOrderType as ChartAxisArrangeOrderType_783b10ff
    from ..chart.chart_axis_label_position import ChartAxisLabelPosition as ChartAxisLabelPosition_463a0fd6
    from ..chart.chart_axis_mark_position import ChartAxisMarkPosition as ChartAxisMarkPosition_373b0f81
    from ..chart.chart_axis_position import ChartAxisPosition as ChartAxisPosition_fcaa0df6

class Axis(PropertySet_b0e70ba2, LineProperties_f13f0da9, CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, XAxis_796b0939, XTitled_8d490a0a):
    """
    Service Class

    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API Axis <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1Axis.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.Axis'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ArrangeOrder(self) -> 'ChartAxisArrangeOrderType_783b10ff':
        """
        Determines how to stagger the labels at the axis (side by side, even, odd, auto )
        """

    @abstractproperty
    def BuiltInUnit(self) -> str:
        """
        Determines built in display unit value for axis.
        
        **since**
        
            LibreOffice 4.3
        """

    @abstractproperty
    def CrossoverPosition(self) -> 'ChartAxisPosition_fcaa0df6':
        """
        Determines where the axis crosses the other axis.
        """

    @abstractproperty
    def CrossoverValue(self) -> float:
        """
        Determines the scale value on the other axis when CrossoverPosition is set to VALUE.
        """

    @abstractproperty
    def DisplayLabels(self) -> bool:
        """
        Determines whether to display text at the axis or not.
        """

    @abstractproperty
    def DisplayUnits(self) -> bool:
        """
        Determines display units are available for axis.
        
        **since**
        
            LibreOffice 4.3
        """

    @abstractproperty
    def LabelPosition(self) -> 'ChartAxisLabelPosition_463a0fd6':
        """
        Determines where the axis labels are placed.
        """

    @abstractproperty
    def MajorOrigin(self) -> int:
        """
        This attribute specifies the shift of the first major tick from the origin.
        
        **since**
        
            LibreOffice 7.0
        """

    @abstractproperty
    def MajorTickmarks(self) -> int:
        """
        determines what kind of tickmarks should be shown for major ticks.
        """

    @abstractproperty
    def MarkPosition(self) -> 'ChartAxisMarkPosition_373b0f81':
        """
        Determines where the interval marks are placed.
        """

    @abstractproperty
    def MinorTickmarks(self) -> int:
        """
        determines what kind of tickmarks should be shown for minor ticks.
        """

    @abstractproperty
    def NumberFormat(self) -> int:
        """
        A NumberFormat key.
        
        If this property is not set, it is treated as auto. This means linked to the source format.
        
        To determine a source format, the axis can query the XDataSequences used by the data series attached to it (see XDataSequence.getNumberFormatKeyByIndex()).
        """

    @abstractproperty
    def ReferencePageSize(self) -> 'Size_576707ef':
        """
        """

    @abstractproperty
    def Show(self) -> bool:
        """
        Determines, whether the axis should be rendered by the view.
        """

    @abstractproperty
    def StackCharacters(self) -> bool:
        """
        Determines whether the characters in a single labels should be stacked one upon each other.
        """

    @abstractproperty
    def TextBreak(self) -> bool:
        """
        Determines whether the labels are allowed to break into more than one line.
        """

    @abstractproperty
    def TextOverlap(self) -> bool:
        """
        Determines whether the labels are allowed to overlap.
        """

    @abstractproperty
    def TextRotation(self) -> float:
        """
        Determines the rotation of the text labels in degrees.
        """

    @abstractproperty
    def TryStaggeringFirst(self) -> bool:
        """
        Compatibility option: determines which strategy should be tried first for fixing axis labels overlapping issues.
        
        **since**
        
            LibreOffice 5.1
        """



__all__ = ['Axis']

