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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..drawing.direction3_d import Direction3D as Direction3D_c9370c0c


class LightSource(object):
    """
    Struct Class


    See Also:
        `API LightSource <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1LightSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.LightSource'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.LightSource'
    """Literal Constant ``com.sun.star.chart2.LightSource``"""

    def __init__(self, nDiffuseColor: typing.Optional[int] = 0, aDirection: typing.Optional[Direction3D_c9370c0c] = UNO_NONE, bIsEnabled: typing.Optional[bool] = False, bSpecular: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            nDiffuseColor (int, optional): nDiffuseColor value.
            aDirection (Direction3D, optional): aDirection value.
            bIsEnabled (bool, optional): bIsEnabled value.
            bSpecular (bool, optional): bSpecular value.
        """
        super().__init__()
        kargs = {
            "nDiffuseColor": nDiffuseColor,
            "aDirection": aDirection,
            "bIsEnabled": bIsEnabled,
            "bSpecular": bSpecular,
        }
        if kargs["aDirection"] is UNO_NONE:
            kargs["aDirection"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._n_diffuse_color = kwargs["nDiffuseColor"]
        self._a_direction = kwargs["aDirection"]
        self._b_is_enabled = kwargs["bIsEnabled"]
        self._b_specular = kwargs["bSpecular"]


    @property
    def nDiffuseColor(self) -> int:
        """
        the light source's color
        """
        return self._n_diffuse_color
    
    @nDiffuseColor.setter
    def nDiffuseColor(self, value: int) -> None:
        self._n_diffuse_color = value

    @property
    def aDirection(self) -> Direction3D_c9370c0c:
        """
        the direction into which the light-source points
        """
        return self._a_direction
    
    @aDirection.setter
    def aDirection(self, value: Direction3D_c9370c0c) -> None:
        self._a_direction = value

    @property
    def bIsEnabled(self) -> bool:
        return self._b_is_enabled
    
    @bIsEnabled.setter
    def bIsEnabled(self, value: bool) -> None:
        self._b_is_enabled = value

    @property
    def bSpecular(self) -> bool:
        """
        When TRUE, the specularity of material is taken into account when lighting an object.
        """
        return self._b_specular
    
    @bSpecular.setter
    def bSpecular(self, value: bool) -> None:
        self._b_specular = value


__all__ = ['LightSource']
