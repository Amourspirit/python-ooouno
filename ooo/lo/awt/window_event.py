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
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class WindowEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a window event.

    See Also:
        `API WindowEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1WindowEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.WindowEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.WindowEvent'
    """Literal Constant ``com.sun.star.awt.WindowEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, X: typing.Optional[int] = 0, Y: typing.Optional[int] = 0, Width: typing.Optional[int] = 0, Height: typing.Optional[int] = 0, LeftInset: typing.Optional[int] = 0, TopInset: typing.Optional[int] = 0, RightInset: typing.Optional[int] = 0, BottomInset: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            X (int, optional): X value.
            Y (int, optional): Y value.
            Width (int, optional): Width value.
            Height (int, optional): Height value.
            LeftInset (int, optional): LeftInset value.
            TopInset (int, optional): TopInset value.
            RightInset (int, optional): RightInset value.
            BottomInset (int, optional): BottomInset value.
        """

        if isinstance(Source, WindowEvent):
            oth: WindowEvent = Source
            self.Source = oth.Source
            self.X = oth.X
            self.Y = oth.Y
            self.Width = oth.Width
            self.Height = oth.Height
            self.LeftInset = oth.LeftInset
            self.TopInset = oth.TopInset
            self.RightInset = oth.RightInset
            self.BottomInset = oth.BottomInset
            return

        kargs = {
            "Source": Source,
            "X": X,
            "Y": Y,
            "Width": Width,
            "Height": Height,
            "LeftInset": LeftInset,
            "TopInset": TopInset,
            "RightInset": RightInset,
            "BottomInset": BottomInset,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._x = kwargs["X"]
        self._y = kwargs["Y"]
        self._width = kwargs["Width"]
        self._height = kwargs["Height"]
        self._left_inset = kwargs["LeftInset"]
        self._top_inset = kwargs["TopInset"]
        self._right_inset = kwargs["RightInset"]
        self._bottom_inset = kwargs["BottomInset"]
        inst_keys = ('X', 'Y', 'Width', 'Height', 'LeftInset', 'TopInset', 'RightInset', 'BottomInset')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def X(self) -> int:
        """
        specifies the outer x position of the window.
        """
        return self._x

    @X.setter
    def X(self, value: int) -> None:
        self._x = value

    @property
    def Y(self) -> int:
        """
        specifies the outer y position of the window.
        """
        return self._y

    @Y.setter
    def Y(self, value: int) -> None:
        self._y = value

    @property
    def Width(self) -> int:
        """
        specifies the outer (total) width of the window.
        """
        return self._width

    @Width.setter
    def Width(self, value: int) -> None:
        self._width = value

    @property
    def Height(self) -> int:
        """
        specifies the outer (total) height of the window.
        """
        return self._height

    @Height.setter
    def Height(self, value: int) -> None:
        self._height = value

    @property
    def LeftInset(self) -> int:
        """
        specifies the inset from the left.
        
        The inset is the distance between the outer and the inner window, that means the left inset is the width of the left border.
        """
        return self._left_inset

    @LeftInset.setter
    def LeftInset(self, value: int) -> None:
        self._left_inset = value

    @property
    def TopInset(self) -> int:
        """
        specifies the inset from the top.
        
        The inset is the distance between the outer and the inner window, that means the top inset is the height of the top border.
        """
        return self._top_inset

    @TopInset.setter
    def TopInset(self, value: int) -> None:
        self._top_inset = value

    @property
    def RightInset(self) -> int:
        """
        specifies the inset from the right.
        
        The inset is the distance between the outer and the inner window, that means the right inset is the width of the right border.
        """
        return self._right_inset

    @RightInset.setter
    def RightInset(self, value: int) -> None:
        self._right_inset = value

    @property
    def BottomInset(self) -> int:
        """
        specifies the inset from the bottom.
        
        The inset is the distance between the outer and the inner window, that means the bottom inset is the height of the bottom border.
        """
        return self._bottom_inset

    @BottomInset.setter
    def BottomInset(self, value: int) -> None:
        self._bottom_inset = value


__all__ = ['WindowEvent']
