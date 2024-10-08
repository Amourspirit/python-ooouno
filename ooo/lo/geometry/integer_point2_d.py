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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.geometry
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class IntegerPoint2D(object):
    """
    Struct Class

    This structure defines a two-dimensional point.
    
    This structure contains x and y integer-valued coordinates of a two-dimensional point.
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerPoint2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerPoint2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.IntegerPoint2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.IntegerPoint2D'
    """Literal Constant ``com.sun.star.geometry.IntegerPoint2D``"""

    def __init__(self, X: typing.Optional[int] = 0, Y: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            X (int, optional): X value.
            Y (int, optional): Y value.
        """
        super().__init__()

        if isinstance(X, IntegerPoint2D):
            oth: IntegerPoint2D = X
            self.X = oth.X
            self.Y = oth.Y
            return

        kargs = {
            "X": X,
            "Y": Y,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._x = kwargs["X"]
        self._y = kwargs["Y"]


    @property
    def X(self) -> int:
        """
        The x coordinate of the point.
        """
        return self._x

    @X.setter
    def X(self, value: int) -> None:
        self._x = value

    @property
    def Y(self) -> int:
        """
        The x coordinate of the point.
        """
        return self._y

    @Y.setter
    def Y(self, value: int) -> None:
        self._y = value


__all__ = ['IntegerPoint2D']
