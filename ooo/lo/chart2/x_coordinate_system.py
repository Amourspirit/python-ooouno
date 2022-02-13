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
    from .x_axis import XAxis as XAxis_796b0939

class XCoordinateSystem(XInterface_8f010a43):
    """

    See Also:
        `API XCoordinateSystem <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XCoordinateSystem.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XCoordinateSystem'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XCoordinateSystem'

    @abstractmethod
    def getAxisByDimension(self, nDimension: int, nIndex: int) -> 'XAxis_796b0939':
        """
        The dimension says whether it is a x, y or z axis.
        
        The index indicates whether it is a primary or a secondary axis or maybe more in future. Use nIndex == 0 for a primary axis. An empty Reference will be returned if the given nDimension and nIndex are in the valid range but no axis is set for those values. An IndexOutOfBoundsException will be thrown if nDimension is lower than 0 or greater than the value returned by getDimension() and/or if nIndex is lower 0 or greater than the value returned by getMaxAxisIndexByDimension(nDimension).

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getCoordinateSystemType(self) -> str:
        """
        identifies the type of coordinate system (e.g.
        
        Cartesian, polar ...)
        """
    @abstractmethod
    def getDimension(self) -> int:
        """
        the dimension of the coordinate-system.
        """
    @abstractmethod
    def getMaximumAxisIndexByDimension(self, nDimension: int) -> int:
        """
        In one dimension there could be several axes to enable main and secondary axis and maybe more in future.
        
        This method returns the maximum index at which an axis exists for the given dimension. It is allowed that some indexes in between do not have an axis.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getViewServiceName(self) -> str:
        """
        return a service name from which the view component for this coordinate system can be created
        """
    @abstractmethod
    def setAxisByDimension(self, nDimension: int, xAxis: 'XAxis_796b0939', nIndex: int) -> None:
        """
        The dimension says whether it is a x, y or z axis.
        
        The index says whether it is a primary or a secondary axis. Use nIndex == 0 for a primary axis.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """

__all__ = ['XCoordinateSystem']

