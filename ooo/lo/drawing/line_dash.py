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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .dash_style import DashStyle as DashStyle_b10d0b85


class LineDash(object):
    """
    Struct Class

    A LineDash defines a non-continuous line.

    See Also:
        `API LineDash <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1LineDash.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.LineDash'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.LineDash'
    """Literal Constant ``com.sun.star.drawing.LineDash``"""

    def __init__(self, Style: typing.Optional[DashStyle_b10d0b85] = DashStyle_b10d0b85.RECT, Dots: typing.Optional[int] = 0, DotLen: typing.Optional[int] = 0, Dashes: typing.Optional[int] = 0, DashLen: typing.Optional[int] = 0, Distance: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Style (DashStyle, optional): Style value.
            Dots (int, optional): Dots value.
            DotLen (int, optional): DotLen value.
            Dashes (int, optional): Dashes value.
            DashLen (int, optional): DashLen value.
            Distance (int, optional): Distance value.
        """
        super().__init__()

        if isinstance(Style, LineDash):
            oth: LineDash = Style
            self.Style = oth.Style
            self.Dots = oth.Dots
            self.DotLen = oth.DotLen
            self.Dashes = oth.Dashes
            self.DashLen = oth.DashLen
            self.Distance = oth.Distance
            return

        kargs = {
            "Style": Style,
            "Dots": Dots,
            "DotLen": DotLen,
            "Dashes": Dashes,
            "DashLen": DashLen,
            "Distance": Distance,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._style = kwargs["Style"]
        self._dots = kwargs["Dots"]
        self._dot_len = kwargs["DotLen"]
        self._dashes = kwargs["Dashes"]
        self._dash_len = kwargs["DashLen"]
        self._distance = kwargs["Distance"]


    @property
    def Style(self) -> DashStyle_b10d0b85:
        """
        This sets the style of this LineDash.
        """
        return self._style

    @Style.setter
    def Style(self, value: DashStyle_b10d0b85) -> None:
        self._style = value

    @property
    def Dots(self) -> int:
        """
        This is the number of dots in this LineDash.
        """
        return self._dots

    @Dots.setter
    def Dots(self, value: int) -> None:
        self._dots = value

    @property
    def DotLen(self) -> int:
        """
        This is the length of a dot.
        """
        return self._dot_len

    @DotLen.setter
    def DotLen(self, value: int) -> None:
        self._dot_len = value

    @property
    def Dashes(self) -> int:
        """
        This is the number of dashes.
        """
        return self._dashes

    @Dashes.setter
    def Dashes(self, value: int) -> None:
        self._dashes = value

    @property
    def DashLen(self) -> int:
        """
        This is the length of a single dash.
        """
        return self._dash_len

    @DashLen.setter
    def DashLen(self, value: int) -> None:
        self._dash_len = value

    @property
    def Distance(self) -> int:
        """
        This is the distance between the dots.
        """
        return self._distance

    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value


__all__ = ['LineDash']
