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
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_chart_data_change_event_listener import XChartDataChangeEventListener as XChartDataChangeEventListener_bb19126c

class XChartData(XInterface_8f010a43):
    """
    manages the data of the chart.

    See Also:
        `API XChartData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XChartData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.XChartData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart.XChartData'

    @abstractmethod
    def addChartDataChangeEventListener(self, aListener: XChartDataChangeEventListener_bb19126c) -> None:
        """
        allows a component supporting the XChartDataChangeEventListener interface to register as listener.
        
        The component will be notified with a ChartDataChangeEvent every time the chart's data changes.
        """
        ...
    @abstractmethod
    def getNotANumber(self) -> float:
        """
        In IEEE arithmetic format it is one of the NaN values, so there are no conflicts with existing numeric values.
        """
        ...
    @abstractmethod
    def isNotANumber(self, nNumber: float) -> bool:
        """
        checks whether the value given is equal to the indicator value for a missing value.
        
        In IEEE arithmetic format it is one of the NaN values, so there are no conflicts with existing numeric values.
        
        Always use this method to check, if a value is not a number. If you compare the value returned by XChartData.getNotANumber() to another double value using the = operator, you may not get the desired result!
        """
        ...
    @abstractmethod
    def removeChartDataChangeEventListener(self, aListener: XChartDataChangeEventListener_bb19126c) -> None:
        """
        removes a previously registered listener.
        """
        ...

__all__ = ['XChartData']

