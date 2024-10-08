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
from .gradient_style import GradientStyle as GradientStyle_b02b0b93
from ..util.color import Color as Color_68e908c5


class Gradient(object):
    """
    Struct Class

    Describes a gradient between two colors.
    
    Many aspects of the gradient are undefined, like the algorithm and color space to use to interpolate between the colors and what \"intensity\" means.

    See Also:
        `API Gradient <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Gradient.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.Gradient'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.Gradient'
    """Literal Constant ``com.sun.star.awt.Gradient``"""

    def __init__(self, Style: typing.Optional[GradientStyle_b02b0b93] = GradientStyle_b02b0b93.LINEAR, StartColor: typing.Optional[Color_68e908c5] = Color_68e908c5(0), EndColor: typing.Optional[Color_68e908c5] = Color_68e908c5(0), Angle: typing.Optional[int] = 0, Border: typing.Optional[int] = 0, XOffset: typing.Optional[int] = 0, YOffset: typing.Optional[int] = 0, StartIntensity: typing.Optional[int] = 0, EndIntensity: typing.Optional[int] = 0, StepCount: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Style (GradientStyle, optional): Style value.
            StartColor (Color, optional): StartColor value.
            EndColor (Color, optional): EndColor value.
            Angle (int, optional): Angle value.
            Border (int, optional): Border value.
            XOffset (int, optional): XOffset value.
            YOffset (int, optional): YOffset value.
            StartIntensity (int, optional): StartIntensity value.
            EndIntensity (int, optional): EndIntensity value.
            StepCount (int, optional): StepCount value.
        """
        super().__init__()

        if isinstance(Style, Gradient):
            oth: Gradient = Style
            self.Style = oth.Style
            self.StartColor = oth.StartColor
            self.EndColor = oth.EndColor
            self.Angle = oth.Angle
            self.Border = oth.Border
            self.XOffset = oth.XOffset
            self.YOffset = oth.YOffset
            self.StartIntensity = oth.StartIntensity
            self.EndIntensity = oth.EndIntensity
            self.StepCount = oth.StepCount
            return

        kargs = {
            "Style": Style,
            "StartColor": StartColor,
            "EndColor": EndColor,
            "Angle": Angle,
            "Border": Border,
            "XOffset": XOffset,
            "YOffset": YOffset,
            "StartIntensity": StartIntensity,
            "EndIntensity": EndIntensity,
            "StepCount": StepCount,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._style = kwargs["Style"]
        self._start_color = kwargs["StartColor"]
        self._end_color = kwargs["EndColor"]
        self._angle = kwargs["Angle"]
        self._border = kwargs["Border"]
        self._x_offset = kwargs["XOffset"]
        self._y_offset = kwargs["YOffset"]
        self._start_intensity = kwargs["StartIntensity"]
        self._end_intensity = kwargs["EndIntensity"]
        self._step_count = kwargs["StepCount"]


    @property
    def Style(self) -> GradientStyle_b02b0b93:
        """
        specifies the style of the gradient.
        """
        return self._style

    @Style.setter
    def Style(self, value: GradientStyle_b02b0b93) -> None:
        self._style = value

    @property
    def StartColor(self) -> Color_68e908c5:
        """
        specifies the color at the start point of the gradient.
        """
        return self._start_color

    @StartColor.setter
    def StartColor(self, value: Color_68e908c5) -> None:
        self._start_color = value

    @property
    def EndColor(self) -> Color_68e908c5:
        """
        specifies the color at the end point of the gradient.
        """
        return self._end_color

    @EndColor.setter
    def EndColor(self, value: Color_68e908c5) -> None:
        self._end_color = value

    @property
    def Angle(self) -> int:
        """
        angle of the gradient in 1/10 degree.
        """
        return self._angle

    @Angle.setter
    def Angle(self, value: int) -> None:
        self._angle = value

    @property
    def Border(self) -> int:
        """
        per cent of the total width where just the start color is used.
        """
        return self._border

    @Border.setter
    def Border(self, value: int) -> None:
        self._border = value

    @property
    def XOffset(self) -> int:
        """
        Specifies the X-coordinate, where the gradient begins.
        
        This is effectively the center of the RADIAL, ELLIPTICAL, SQUARE and RECT style gradients.
        """
        return self._x_offset

    @XOffset.setter
    def XOffset(self, value: int) -> None:
        self._x_offset = value

    @property
    def YOffset(self) -> int:
        """
        Specifies the Y-coordinate, where the gradient begins.
        
        See previous field.
        """
        return self._y_offset

    @YOffset.setter
    def YOffset(self, value: int) -> None:
        self._y_offset = value

    @property
    def StartIntensity(self) -> int:
        """
        Specifies the intensity at the start point of the gradient.
        
        What that means is undefined.
        """
        return self._start_intensity

    @StartIntensity.setter
    def StartIntensity(self, value: int) -> None:
        self._start_intensity = value

    @property
    def EndIntensity(self) -> int:
        """
        specifies the intensity at the end point of the gradient.
        """
        return self._end_intensity

    @EndIntensity.setter
    def EndIntensity(self, value: int) -> None:
        self._end_intensity = value

    @property
    def StepCount(self) -> int:
        """
        Specifies the number of steps of change color.
        
        What that means is undefined.
        """
        return self._step_count

    @StepCount.setter
    def StepCount(self, value: int) -> None:
        self._step_count = value


__all__ = ['Gradient']
