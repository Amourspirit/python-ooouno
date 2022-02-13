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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
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

    def __init__(self, X: int = 0, Y: int = 0, Width: int = 0, Height: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``X`` can be another ``Rectangle`` instance,
                in which case other named args are ignored.

        Arguments:
            X (int, optional): X value
            Y (int, optional): Y value
            Width (int, optional): Width value
            Height (int, optional): Height value
        """
        if isinstance(X, Rectangle):
            oth: Rectangle = X
            self._x = oth.X
            self._y = oth.Y
            self._width = oth.Width
            self._height = oth.Height
            return
        else:
            self._x = X
            self._y = Y
            self._width = Width
            self._height = Height



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
