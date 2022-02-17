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
# Namespace: com.sun.star.chart
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XSecondAxisTitleSupplier(XInterface_8f010a43):
    """

    See Also:
        `API XSecondAxisTitleSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XSecondAxisTitleSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.XSecondAxisTitleSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart.XSecondAxisTitleSupplier'

    @abstractmethod
    def getSecondXAxisTitle(self) -> 'XShape_8fd00a3d':
        """
        """
    @abstractmethod
    def getSecondYAxisTitle(self) -> 'XShape_8fd00a3d':
        """
        """

__all__ = ['XSecondAxisTitleSupplier']
