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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_data_series import XDataSeries as XDataSeries_b8150b89

class XDataSeriesContainer(XInterface_8f010a43):
    """

    See Also:
        `API XDataSeriesContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XDataSeriesContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XDataSeriesContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XDataSeriesContainer'

    @abstractmethod
    def addDataSeries(self, aDataSeries: XDataSeries_b8150b89) -> None:
        """
        add a data series to the data series container

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getDataSeries(self) -> typing.Tuple[XDataSeries_b8150b89, ...]:
        """
        retrieve all data series
        """
        ...
    @abstractmethod
    def removeDataSeries(self, aDataSeries: XDataSeries_b8150b89) -> None:
        """
        removes one data series from the data series container.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def setDataSeries(self, aDataSeries: typing.Tuple[XDataSeries_b8150b89, ...]) -> None:
        """
        set all data series

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XDataSeriesContainer']

