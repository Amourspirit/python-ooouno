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
# Namespace: com.sun.star.style
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from .tab_align import TabAlign as TabAlign_8fc90a3b


class TabStop(object):
    """
    Struct Class

    This structure is used to specify a single tabulator stop.

    See Also:
        `API TabStop <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1style_1_1TabStop.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.TabStop'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.style.TabStop'
    """Literal Constant ``com.sun.star.style.TabStop``"""

    def __init__(self, Position: int = 0, Alignment: TabAlign_8fc90a3b = TabAlign_8fc90a3b.LEFT, DecimalChar: str = '\u0000', FillChar: str = '\u0000') -> None:
        """
        Constructor

        Other Arguments:
            ``Position`` can be another ``TabStop`` instance,
                in which case other named args are ignored.

        Arguments:
            Position (int, optional): Position value
            Alignment (TabAlign, optional): Alignment value
            DecimalChar (str, optional): DecimalChar value
            FillChar (str, optional): FillChar value
        """
        if isinstance(Position, TabStop):
            oth: TabStop = Position
            self._position = oth.Position
            self._alignment = oth.Alignment
            self._decimal_char = oth.DecimalChar
            self._fill_char = oth.FillChar
            return
        else:
            self._position = Position
            self._alignment = Alignment
            self._decimal_char = DecimalChar
            self._fill_char = FillChar



    @property
    def Position(self) -> int:
        """
        This field specifies the position of the tabulator in relation to the left border.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: int) -> None:
        self._position = value

    @property
    def Alignment(self) -> TabAlign_8fc90a3b:
        """
        This field specifies the alignment of the text range before the tabulator.
        """
        return self._alignment
    
    @Alignment.setter
    def Alignment(self, value: TabAlign_8fc90a3b) -> None:
        self._alignment = value

    @property
    def DecimalChar(self) -> str:
        """
        This field specifies which delimiter is used for the decimal.
        """
        return self._decimal_char
    
    @DecimalChar.setter
    def DecimalChar(self, value: str) -> None:
        self._decimal_char = value

    @property
    def FillChar(self) -> str:
        """
        This field specifies the character that is used to fill up the space between the text in the text range and the tabulators.
        """
        return self._fill_char
    
    @FillChar.setter
    def FillChar(self, value: str) -> None:
        self._fill_char = value


__all__ = ['TabStop']