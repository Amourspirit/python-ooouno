# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class DeviceInfo(object):
    """
    Struct Class

    contains information about a device.

    See Also:
        `API DeviceInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1DeviceInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.DeviceInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.DeviceInfo'
    """Literal Constant ``com.sun.star.awt.DeviceInfo``"""

    def __init__(self, Width: typing.Optional[int] = 0, Height: typing.Optional[int] = 0, LeftInset: typing.Optional[int] = 0, TopInset: typing.Optional[int] = 0, RightInset: typing.Optional[int] = 0, BottomInset: typing.Optional[int] = 0, PixelPerMeterX: typing.Optional[float] = 0.0, PixelPerMeterY: typing.Optional[float] = 0.0, BitsPerPixel: typing.Optional[int] = 0, Capabilities: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Width (int, optional): Width value.
            Height (int, optional): Height value.
            LeftInset (int, optional): LeftInset value.
            TopInset (int, optional): TopInset value.
            RightInset (int, optional): RightInset value.
            BottomInset (int, optional): BottomInset value.
            PixelPerMeterX (float, optional): PixelPerMeterX value.
            PixelPerMeterY (float, optional): PixelPerMeterY value.
            BitsPerPixel (int, optional): BitsPerPixel value.
            Capabilities (int, optional): Capabilities value.
        """
        super().__init__()

        if isinstance(Width, DeviceInfo):
            oth: DeviceInfo = Width
            self.Width = oth.Width
            self.Height = oth.Height
            self.LeftInset = oth.LeftInset
            self.TopInset = oth.TopInset
            self.RightInset = oth.RightInset
            self.BottomInset = oth.BottomInset
            self.PixelPerMeterX = oth.PixelPerMeterX
            self.PixelPerMeterY = oth.PixelPerMeterY
            self.BitsPerPixel = oth.BitsPerPixel
            self.Capabilities = oth.Capabilities
            return

        kargs = {
            "Width": Width,
            "Height": Height,
            "LeftInset": LeftInset,
            "TopInset": TopInset,
            "RightInset": RightInset,
            "BottomInset": BottomInset,
            "PixelPerMeterX": PixelPerMeterX,
            "PixelPerMeterY": PixelPerMeterY,
            "BitsPerPixel": BitsPerPixel,
            "Capabilities": Capabilities,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._width = kwargs["Width"]
        self._height = kwargs["Height"]
        self._left_inset = kwargs["LeftInset"]
        self._top_inset = kwargs["TopInset"]
        self._right_inset = kwargs["RightInset"]
        self._bottom_inset = kwargs["BottomInset"]
        self._pixel_per_meter_x = kwargs["PixelPerMeterX"]
        self._pixel_per_meter_y = kwargs["PixelPerMeterY"]
        self._bits_per_pixel = kwargs["BitsPerPixel"]
        self._capabilities = kwargs["Capabilities"]


    @property
    def Width(self) -> int:
        """
        contains the width of the device in pixels.
        """
        return self._width

    @Width.setter
    def Width(self, value: int) -> None:
        self._width = value

    @property
    def Height(self) -> int:
        """
        contains the height of the device in pixels.
        """
        return self._height

    @Height.setter
    def Height(self, value: int) -> None:
        self._height = value

    @property
    def LeftInset(self) -> int:
        """
        contains the inset from the left.
        """
        return self._left_inset

    @LeftInset.setter
    def LeftInset(self, value: int) -> None:
        self._left_inset = value

    @property
    def TopInset(self) -> int:
        """
        contains the inset from the top.
        """
        return self._top_inset

    @TopInset.setter
    def TopInset(self, value: int) -> None:
        self._top_inset = value

    @property
    def RightInset(self) -> int:
        """
        contains the inset from the right.
        """
        return self._right_inset

    @RightInset.setter
    def RightInset(self, value: int) -> None:
        self._right_inset = value

    @property
    def BottomInset(self) -> int:
        """
        contains the inset from the bottom.
        """
        return self._bottom_inset

    @BottomInset.setter
    def BottomInset(self, value: int) -> None:
        self._bottom_inset = value

    @property
    def PixelPerMeterX(self) -> float:
        """
        contains the X-axis resolution of the device in pixel/meter.
        """
        return self._pixel_per_meter_x

    @PixelPerMeterX.setter
    def PixelPerMeterX(self, value: float) -> None:
        self._pixel_per_meter_x = value

    @property
    def PixelPerMeterY(self) -> float:
        """
        contains the Y-axis resolution of the device in pixel/meter.
        """
        return self._pixel_per_meter_y

    @PixelPerMeterY.setter
    def PixelPerMeterY(self, value: float) -> None:
        self._pixel_per_meter_y = value

    @property
    def BitsPerPixel(self) -> int:
        """
        contains the color-depth of the device.
        """
        return self._bits_per_pixel

    @BitsPerPixel.setter
    def BitsPerPixel(self, value: int) -> None:
        self._bits_per_pixel = value

    @property
    def Capabilities(self) -> int:
        """
        specifies special operations which are possible on the device.
        """
        return self._capabilities

    @Capabilities.setter
    def Capabilities(self, value: int) -> None:
        self._capabilities = value


__all__ = ['DeviceInfo']
