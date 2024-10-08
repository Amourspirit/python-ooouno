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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class LeftRightMarginScale(object):
    """
    Struct Class

    specifies a left and right margin.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API LeftRightMarginScale <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1LeftRightMarginScale.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.LeftRightMarginScale'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.LeftRightMarginScale'
    """Literal Constant ``com.sun.star.frame.status.LeftRightMarginScale``"""

    def __init__(self, TextLeft: typing.Optional[int] = 0, Left: typing.Optional[int] = 0, Right: typing.Optional[int] = 0, FirstLine: typing.Optional[int] = 0, ScaleLeft: typing.Optional[int] = 0, ScaleRight: typing.Optional[int] = 0, ScaleFirstLine: typing.Optional[int] = 0, AutoFirstLine: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            TextLeft (int, optional): TextLeft value.
            Left (int, optional): Left value.
            Right (int, optional): Right value.
            FirstLine (int, optional): FirstLine value.
            ScaleLeft (int, optional): ScaleLeft value.
            ScaleRight (int, optional): ScaleRight value.
            ScaleFirstLine (int, optional): ScaleFirstLine value.
            AutoFirstLine (bool, optional): AutoFirstLine value.
        """
        super().__init__()

        if isinstance(TextLeft, LeftRightMarginScale):
            oth: LeftRightMarginScale = TextLeft
            self.TextLeft = oth.TextLeft
            self.Left = oth.Left
            self.Right = oth.Right
            self.FirstLine = oth.FirstLine
            self.ScaleLeft = oth.ScaleLeft
            self.ScaleRight = oth.ScaleRight
            self.ScaleFirstLine = oth.ScaleFirstLine
            self.AutoFirstLine = oth.AutoFirstLine
            return

        kargs = {
            "TextLeft": TextLeft,
            "Left": Left,
            "Right": Right,
            "FirstLine": FirstLine,
            "ScaleLeft": ScaleLeft,
            "ScaleRight": ScaleRight,
            "ScaleFirstLine": ScaleFirstLine,
            "AutoFirstLine": AutoFirstLine,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._text_left = kwargs["TextLeft"]
        self._left = kwargs["Left"]
        self._right = kwargs["Right"]
        self._first_line = kwargs["FirstLine"]
        self._scale_left = kwargs["ScaleLeft"]
        self._scale_right = kwargs["ScaleRight"]
        self._scale_first_line = kwargs["ScaleFirstLine"]
        self._auto_first_line = kwargs["AutoFirstLine"]


    @property
    def TextLeft(self) -> int:
        """
        specifies a left text margin in 1/100th mm.
        """
        return self._text_left

    @TextLeft.setter
    def TextLeft(self, value: int) -> None:
        self._text_left = value

    @property
    def Left(self) -> int:
        """
        specifies a left margin in 1/100th mm.
        """
        return self._left

    @Left.setter
    def Left(self, value: int) -> None:
        self._left = value

    @property
    def Right(self) -> int:
        """
        specifies a right margin in 1/100th mm.
        """
        return self._right

    @Right.setter
    def Right(self, value: int) -> None:
        self._right = value

    @property
    def FirstLine(self) -> int:
        """
        specifies a first line indent relative to TextLeft in 1/100th mm.
        """
        return self._first_line

    @FirstLine.setter
    def FirstLine(self, value: int) -> None:
        self._first_line = value

    @property
    def ScaleLeft(self) -> int:
        """
        specifies a scale value for the left margin in percent.
        """
        return self._scale_left

    @ScaleLeft.setter
    def ScaleLeft(self, value: int) -> None:
        self._scale_left = value

    @property
    def ScaleRight(self) -> int:
        """
        specifies a scale value for the right margin in percent.
        """
        return self._scale_right

    @ScaleRight.setter
    def ScaleRight(self, value: int) -> None:
        self._scale_right = value

    @property
    def ScaleFirstLine(self) -> int:
        """
        specifies a scale value for the first line margin in percent.
        """
        return self._scale_first_line

    @ScaleFirstLine.setter
    def ScaleFirstLine(self, value: int) -> None:
        self._scale_first_line = value

    @property
    def AutoFirstLine(self) -> bool:
        """
        specifies if the automatic calculation of the first line indent occurs.
        """
        return self._auto_first_line

    @AutoFirstLine.setter
    def AutoFirstLine(self, value: bool) -> None:
        self._auto_first_line = value


__all__ = ['LeftRightMarginScale']
