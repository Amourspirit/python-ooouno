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
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class Rectangle(object):
    """
    Struct Class

    specifies a rectangular area by position and size.

    See Also:
        `API Rectangle <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Rectangle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.Rectangle'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.Rectangle'
    """Literal Constant ``com.sun.star.awt.Rectangle``"""

    def __init__(self, X: typing.Optional[int] = 0, Y: typing.Optional[int] = 0, Width: typing.Optional[int] = 0, Height: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            X (int, optional): X value.
            Y (int, optional): Y value.
            Width (int, optional): Width value.
            Height (int, optional): Height value.
        """
        super().__init__()

        if isinstance(X, Rectangle):
            oth: Rectangle = X
            self.X = oth.X
            self.Y = oth.Y
            self.Width = oth.Width
            self.Height = oth.Height
            return

        kargs = {
            "X": X,
            "Y": Y,
            "Width": Width,
            "Height": Height,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._x = kwargs["X"]
        self._y = kwargs["Y"]
        self._width = kwargs["Width"]
        self._height = kwargs["Height"]


    @property
    def X(self) -> int:
        """
        specifies the x-coordinate.
        """
        return self._x

    @X.setter
    def X(self, value: int) -> None:
        self._x = value

    @property
    def Y(self) -> int:
        """
        specifies the y-coordinate.
        """
        return self._y

    @Y.setter
    def Y(self, value: int) -> None:
        self._y = value

    @property
    def Width(self) -> int:
        """
        specifies the width.
        """
        return self._width

    @Width.setter
    def Width(self, value: int) -> None:
        self._width = value

    @property
    def Height(self) -> int:
        """
        specifies the height.
        """
        return self._height

    @Height.setter
    def Height(self, value: int) -> None:
        self._height = value


__all__ = ['Rectangle']
