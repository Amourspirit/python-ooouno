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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2


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

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``LeftRightMarginScale`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``LeftRightMarginScale``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            TextLeft (int, optional): TextLeft value
            Left (int, optional): Left value
            Right (int, optional): Right value
            FirstLine (int, optional): FirstLine value
            ScaleLeft (int, optional): ScaleLeft value
            ScaleRight (int, optional): ScaleRight value
            ScaleFirstLine (int, optional): ScaleFirstLine value
            AutoFirstLine (bool, optional): AutoFirstLine value
        """
        self._text_left = None
        self._left = None
        self._right = None
        self._first_line = None
        self._scale_left = None
        self._scale_right = None
        self._scale_first_line = None
        self._auto_first_line = None

        key_order = ('TextLeft', 'Left', 'Right', 'FirstLine', 'ScaleLeft', 'ScaleRight', 'ScaleFirstLine', 'AutoFirstLine')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], LeftRightMarginScale):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("LeftRightMarginScale.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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
