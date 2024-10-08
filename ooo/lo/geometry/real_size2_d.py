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


class RealSize2D(object):
    """
    Struct Class

    This structure contains data representing a two-dimensional size.
    
    The data is stored real-valued.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealSize2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealSize2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.RealSize2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.RealSize2D'
    """Literal Constant ``com.sun.star.geometry.RealSize2D``"""

    def __init__(self, Width: typing.Optional[float] = 0.0, Height: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Width (float, optional): Width value.
            Height (float, optional): Height value.
        """
        super().__init__()

        if isinstance(Width, RealSize2D):
            oth: RealSize2D = Width
            self.Width = oth.Width
            self.Height = oth.Height
            return

        kargs = {
            "Width": Width,
            "Height": Height,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._width = kwargs["Width"]
        self._height = kwargs["Height"]


    @property
    def Width(self) -> float:
        """
        Amount of space occupied in the x direction.
        """
        return self._width

    @Width.setter
    def Width(self, value: float) -> None:
        self._width = value

    @property
    def Height(self) -> float:
        """
        Amount of space occupied in the y direction.
        """
        return self._height

    @Height.setter
    def Height(self, value: float) -> None:
        self._height = value


__all__ = ['RealSize2D']
