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
# Namespace: com.sun.star.table
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..util.color import Color as Color_68e908c5


class BorderLine(object):
    """
    Struct Class

    describes the line type for a single cell edge.

    See Also:
        `API BorderLine <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1BorderLine.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.BorderLine'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.BorderLine'
    """Literal Constant ``com.sun.star.table.BorderLine``"""

    def __init__(self, Color: typing.Optional[Color_68e908c5] = Color_68e908c5(0), InnerLineWidth: typing.Optional[int] = 0, OuterLineWidth: typing.Optional[int] = 0, LineDistance: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Color (Color, optional): Color value.
            InnerLineWidth (int, optional): InnerLineWidth value.
            OuterLineWidth (int, optional): OuterLineWidth value.
            LineDistance (int, optional): LineDistance value.
        """
        super().__init__()

        if isinstance(Color, BorderLine):
            oth: BorderLine = Color
            self.Color = oth.Color
            self.InnerLineWidth = oth.InnerLineWidth
            self.OuterLineWidth = oth.OuterLineWidth
            self.LineDistance = oth.LineDistance
            return

        kargs = {
            "Color": Color,
            "InnerLineWidth": InnerLineWidth,
            "OuterLineWidth": OuterLineWidth,
            "LineDistance": LineDistance,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._color = kwargs["Color"]
        self._inner_line_width = kwargs["InnerLineWidth"]
        self._outer_line_width = kwargs["OuterLineWidth"]
        self._line_distance = kwargs["LineDistance"]


    @property
    def Color(self) -> Color_68e908c5:
        """
        contains the color value of the line.
        """
        return self._color

    @Color.setter
    def Color(self, value: Color_68e908c5) -> None:
        self._color = value

    @property
    def InnerLineWidth(self) -> int:
        """
        contains the width of the inner part of a double line (in 1/100 mm).
        
        If this value is zero, only a single line is drawn.
        """
        return self._inner_line_width

    @InnerLineWidth.setter
    def InnerLineWidth(self, value: int) -> None:
        self._inner_line_width = value

    @property
    def OuterLineWidth(self) -> int:
        """
        contains the width of a single line or the width of outer part of a double line (in 1/100 mm).
        
        If this value is zero, no line is drawn.
        """
        return self._outer_line_width

    @OuterLineWidth.setter
    def OuterLineWidth(self, value: int) -> None:
        self._outer_line_width = value

    @property
    def LineDistance(self) -> int:
        """
        contains the distance between the inner and outer parts of a double line (in 1/100 mm).
        """
        return self._line_distance

    @LineDistance.setter
    def LineDistance(self, value: int) -> None:
        self._line_distance = value


__all__ = ['BorderLine']
