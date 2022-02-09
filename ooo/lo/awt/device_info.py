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


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DeviceInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DeviceInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Width (int, optional): Width value
            Height (int, optional): Height value
            LeftInset (int, optional): LeftInset value
            TopInset (int, optional): TopInset value
            RightInset (int, optional): RightInset value
            BottomInset (int, optional): BottomInset value
            PixelPerMeterX (float, optional): PixelPerMeterX value
            PixelPerMeterY (float, optional): PixelPerMeterY value
            BitsPerPixel (int, optional): BitsPerPixel value
            Capabilities (int, optional): Capabilities value
        """
        self._width = None
        self._height = None
        self._left_inset = None
        self._top_inset = None
        self._right_inset = None
        self._bottom_inset = None
        self._pixel_per_meter_x = None
        self._pixel_per_meter_y = None
        self._bits_per_pixel = None
        self._capabilities = None

        key_order = ('Width', 'Height', 'LeftInset', 'TopInset', 'RightInset', 'BottomInset', 'PixelPerMeterX', 'PixelPerMeterY', 'BitsPerPixel', 'Capabilities')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DeviceInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DeviceInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

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
