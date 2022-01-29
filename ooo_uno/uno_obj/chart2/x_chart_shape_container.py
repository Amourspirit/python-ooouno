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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XChartShapeContainer(XInterface_8f010a43):
    """

    See Also:
        `API XChartShapeContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XChartShapeContainer.html>`_
    """

    @abstractmethod
    def addShape(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        a renderer creates ChartShapes and adds it to this container
        """
    @abstractmethod
    def getShape(self) -> 'XShape_8fd00a3d':
        """
        """
    @abstractmethod
    def removeShape(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        a renderer can remove ChartShapes from this container (e.g.
        
        if the visible range has changed)
        """

__all__ = ['XChartShapeContainer']

