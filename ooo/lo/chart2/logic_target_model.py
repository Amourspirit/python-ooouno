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
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class LogicTargetModel(ABC):
    """
    Service Class

    The properties of this service correspond to the similar named attributes and subelements of the XML element chart2:increment in the chart2 file format.

    See Also:
        `API LogicTargetModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1LogicTargetModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.LogicTargetModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CoordinateSystems(self) -> 'typing.Tuple[XPropertySet_bc180bfa, ...]':
        """
        not BOUND nor CONSTRAINED in terms of Listener notifications, each element in the sequence must implement the service com.sun.star.chart2.CoordinateSystem
        """

    @abstractproperty
    def LogicTargetModels(self) -> 'typing.Tuple[XPropertySet_bc180bfa, ...]':
        """
        MAYBEVOID, not BOUND nor CONSTRAINED in terms of Listener notifications, each element in the sequence must implement the service com.sun.star.chart2.LogicTargetModel.
        """

    @abstractproperty
    def ID(self) -> str:
        """
        identifies an instance of this service within one chart document.
        """

    @abstractproperty
    def LegendID(self) -> str:
        """
        identifies an instance of the service com.sun.star.chart2.LegendModel within one chart document.
        
        that instance is used to automatically calculate missing properties
        """



__all__ = ['LogicTargetModel']

