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
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from abc import abstractproperty
from ..chart.x3_d_default_setter import X3DDefaultSetter as X3DDefaultSetter_e9630d25
from .x_coordinate_system_container import XCoordinateSystemContainer as XCoordinateSystemContainer_995411d4
from .x_diagram import XDiagram as XDiagram_96fe0a59
from .x_titled import XTitled as XTitled_8d490a0a
if typing.TYPE_CHECKING:
    from .relative_position import RelativePosition as RelativePosition_fae10ddd
    from .relative_size import RelativeSize as RelativeSize_c6020c23

class Diagram(X3DDefaultSetter_e9630d25, XCoordinateSystemContainer_995411d4, XDiagram_96fe0a59, XTitled_8d490a0a):
    """
    Service Class


    See Also:
        `API Diagram <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1Diagram.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.Diagram'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ConnectBars(self) -> bool:
        """
        Draw connection lines for stacked bar charts.
        """
        ...

    @abstractproperty
    def DataTableHBorder(self) -> bool:
        """
        Chart Datatable flags.
        """
        ...

    @abstractproperty
    def DataTableOutline(self) -> bool:
        """
        """
        ...

    @abstractproperty
    def DataTableVBorder(self) -> bool:
        """
        """
        ...

    @abstractproperty
    def ExternalData(self) -> str:
        """
        """
        ...

    @abstractproperty
    def GroupBarsPerAxis(self) -> bool:
        """
        If bars of a bar or column chart are attached to different axis, this property determines how to display those.
        
        If TRUE, the bars are grouped together in one block for each axis, thus they are painted one group over the other.
        
        If FALSE, the bars are displayed side-by-side, as if they were all attached to the same axis.
        
        If all data series of a bar or column chart are attached to only one axis, this property has no effect.
        """
        ...

    @abstractproperty
    def MissingValueTreatment(self) -> int:
        """
        specifies how empty or invalid cells in the provided data should be handled when displayed
        """
        ...

    @abstractproperty
    def Perspective(self) -> int:
        """
        Perspective of 3D charts ( [0,100] ).
        """
        ...

    @abstractproperty
    def PosSizeExcludeLabels(self) -> bool:
        """
        The attributes RelativePosition and RelativeSize should be used for the inner coordinate region without axis labels and without data labels.
        """
        ...

    @abstractproperty
    def RelativePosition(self) -> RelativePosition_fae10ddd:
        """
        The position is as a relative position on the page.
        
        If a relative position is given the diagram is not automatically placed, but instead is placed relative on the page.
        """
        ...

    @abstractproperty
    def RelativeSize(self) -> RelativeSize_c6020c23:
        """
        The size of the diagram as relative size of the page size.
        """
        ...

    @abstractproperty
    def RightAngledAxes(self) -> bool:
        """
        """
        ...

    @abstractproperty
    def RotationHorizontal(self) -> int:
        """
        Horizontal rotation of 3D charts in degrees ( ]-180,180] ).
        """
        ...

    @abstractproperty
    def RotationVertical(self) -> int:
        """
        Vertical rotation of 3D charts in degrees ( ]-180,180] ).
        """
        ...

    @abstractproperty
    def SortByXValues(self) -> bool:
        """
        Sort data points by x values for rendering.
        """
        ...

    @abstractproperty
    def StartingAngle(self) -> int:
        """
        Starting angle in degrees for pie charts and doughnut charts.
        """
        ...


__all__ = ['Diagram']

