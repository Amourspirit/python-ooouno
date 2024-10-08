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
from .hatch_style import HatchStyle as HatchStyle_bcfe0bed
from ..util.color import Color as Color_68e908c5


class Hatch(object):
    """
    Struct Class

    This struct defines the appearance of a hatch.
    
    A hatch is a texture made of straight lines.

    See Also:
        `API Hatch <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1Hatch.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.Hatch'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.Hatch'
    """Literal Constant ``com.sun.star.drawing.Hatch``"""

    def __init__(self, Style: typing.Optional[HatchStyle_bcfe0bed] = HatchStyle_bcfe0bed.SINGLE, Color: typing.Optional[Color_68e908c5] = Color_68e908c5(0), Distance: typing.Optional[int] = 0, Angle: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Style (HatchStyle, optional): Style value.
            Color (Color, optional): Color value.
            Distance (int, optional): Distance value.
            Angle (int, optional): Angle value.
        """
        super().__init__()

        if isinstance(Style, Hatch):
            oth: Hatch = Style
            self.Style = oth.Style
            self.Color = oth.Color
            self.Distance = oth.Distance
            self.Angle = oth.Angle
            return

        kargs = {
            "Style": Style,
            "Color": Color,
            "Distance": Distance,
            "Angle": Angle,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._style = kwargs["Style"]
        self._color = kwargs["Color"]
        self._distance = kwargs["Distance"]
        self._angle = kwargs["Angle"]


    @property
    def Style(self) -> HatchStyle_bcfe0bed:
        """
        The HatchStyle defines the kind of lines used to draw this hatch.
        """
        return self._style

    @Style.setter
    def Style(self, value: HatchStyle_bcfe0bed) -> None:
        self._style = value

    @property
    def Color(self) -> Color_68e908c5:
        """
        This is the color of the hatch lines.
        """
        return self._color

    @Color.setter
    def Color(self, value: Color_68e908c5) -> None:
        self._color = value

    @property
    def Distance(self) -> int:
        """
        This is the distance between the lines in the hatch.
        """
        return self._distance

    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value

    @property
    def Angle(self) -> int:
        """
        You can rotate the lines of the hatch with this angle.
        
        Specified in tenths of a degree.
        """
        return self._angle

    @Angle.setter
    def Angle(self, value: int) -> None:
        self._angle = value


__all__ = ['Hatch']
