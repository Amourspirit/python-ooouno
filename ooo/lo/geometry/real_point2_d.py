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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class RealPoint2D(object):
    """
    Struct Class

    This structure defines a two-dimensional point.
    
    This structure contains x and y real-valued coordinates of a two-dimensional point.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealPoint2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealPoint2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.RealPoint2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.RealPoint2D'
    """Literal Constant ``com.sun.star.geometry.RealPoint2D``"""

    def __init__(self, X: float = 0.0, Y: float = 0.0) -> None:
        """
        Constructor

        Other Arguments:
            ``X`` can be another ``RealPoint2D`` instance,
                in which case other named args are ignored.

        Arguments:
            X (float, optional): X value
            Y (float, optional): Y value
        """
        if isinstance(X, RealPoint2D):
            oth: RealPoint2D = X
            self._x = oth.X
            self._y = oth.Y
            return
        else:
            self._x = X
            self._y = Y



    @property
    def X(self) -> float:
        """
        The x coordinate of the point.
        """
        return self._x
    
    @X.setter
    def X(self, value: float) -> None:
        self._x = value

    @property
    def Y(self) -> float:
        """
        The x coordinate of the point.
        """
        return self._y
    
    @Y.setter
    def Y(self, value: float) -> None:
        self._y = value


__all__ = ['RealPoint2D']
