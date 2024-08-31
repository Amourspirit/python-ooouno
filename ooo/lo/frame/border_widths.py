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
# Namespace: com.sun.star.frame
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class BorderWidths(object):
    """
    Struct Class

    specifies a border area by offsets from each side.

    See Also:
        `API BorderWidths <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1BorderWidths.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.BorderWidths'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.BorderWidths'
    """Literal Constant ``com.sun.star.frame.BorderWidths``"""

    def __init__(self, Left: typing.Optional[int] = 0, Top: typing.Optional[int] = 0, Right: typing.Optional[int] = 0, Bottom: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Left (int, optional): Left value.
            Top (int, optional): Top value.
            Right (int, optional): Right value.
            Bottom (int, optional): Bottom value.
        """
        super().__init__()

        if isinstance(Left, BorderWidths):
            oth: BorderWidths = Left
            self.Left = oth.Left
            self.Top = oth.Top
            self.Right = oth.Right
            self.Bottom = oth.Bottom
            return

        kargs = {
            "Left": Left,
            "Top": Top,
            "Right": Right,
            "Bottom": Bottom,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._left = kwargs["Left"]
        self._top = kwargs["Top"]
        self._right = kwargs["Right"]
        self._bottom = kwargs["Bottom"]


    @property
    def Left(self) -> int:
        """
        specifies the offset from left border.
        """
        return self._left

    @Left.setter
    def Left(self, value: int) -> None:
        self._left = value

    @property
    def Top(self) -> int:
        """
        specifies the offset from top border.
        """
        return self._top

    @Top.setter
    def Top(self, value: int) -> None:
        self._top = value

    @property
    def Right(self) -> int:
        """
        specifies the offset from right border.
        """
        return self._right

    @Right.setter
    def Right(self, value: int) -> None:
        self._right = value

    @property
    def Bottom(self) -> int:
        """
        specifies the offset from bottom border.
        """
        return self._bottom

    @Bottom.setter
    def Bottom(self, value: int) -> None:
        self._bottom = value


__all__ = ['BorderWidths']
