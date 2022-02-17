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
# Namespace: com.sun.star.table
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from .border_line2 import BorderLine2 as BorderLine2_af200b28


class TableBorder2(object):
    """
    Struct Class

    contains the style settings of the border lines of all cells in a cell range.
    
    TableBorder2 is nearly identical to TableBorder, except that it has members of BorderLine2 instead of BorderLine.
    
    In a queried structure, the flags in TableBorder2.Is...LineValid indicate that not all lines of the boxes have the same values.
    
    In a structure which is used for setting, these flags determine if the corresponding line should be set or if the old value should be kept.
    
    **since**
    
        LibreOffice 3.6

    See Also:
        `API TableBorder2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1TableBorder2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.TableBorder2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.TableBorder2'
    """Literal Constant ``com.sun.star.table.TableBorder2``"""

    def __init__(self, TopLine: BorderLine2_af200b28 = UNO_NONE, IsTopLineValid: bool = False, BottomLine: BorderLine2_af200b28 = UNO_NONE, IsBottomLineValid: bool = False, LeftLine: BorderLine2_af200b28 = UNO_NONE, IsLeftLineValid: bool = False, RightLine: BorderLine2_af200b28 = UNO_NONE, IsRightLineValid: bool = False, HorizontalLine: BorderLine2_af200b28 = UNO_NONE, IsHorizontalLineValid: bool = False, VerticalLine: BorderLine2_af200b28 = UNO_NONE, IsVerticalLineValid: bool = False, Distance: int = 0, IsDistanceValid: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``TopLine`` can be another ``TableBorder2`` instance,
                in which case other named args are ignored.

        Arguments:
            TopLine (BorderLine2, optional): TopLine value
            IsTopLineValid (bool, optional): IsTopLineValid value
            BottomLine (BorderLine2, optional): BottomLine value
            IsBottomLineValid (bool, optional): IsBottomLineValid value
            LeftLine (BorderLine2, optional): LeftLine value
            IsLeftLineValid (bool, optional): IsLeftLineValid value
            RightLine (BorderLine2, optional): RightLine value
            IsRightLineValid (bool, optional): IsRightLineValid value
            HorizontalLine (BorderLine2, optional): HorizontalLine value
            IsHorizontalLineValid (bool, optional): IsHorizontalLineValid value
            VerticalLine (BorderLine2, optional): VerticalLine value
            IsVerticalLineValid (bool, optional): IsVerticalLineValid value
            Distance (int, optional): Distance value
            IsDistanceValid (bool, optional): IsDistanceValid value
        """
        if isinstance(TopLine, TableBorder2):
            oth: TableBorder2 = TopLine
            self._top_line = oth.TopLine
            self._is_top_line_valid = oth.IsTopLineValid
            self._bottom_line = oth.BottomLine
            self._is_bottom_line_valid = oth.IsBottomLineValid
            self._left_line = oth.LeftLine
            self._is_left_line_valid = oth.IsLeftLineValid
            self._right_line = oth.RightLine
            self._is_right_line_valid = oth.IsRightLineValid
            self._horizontal_line = oth.HorizontalLine
            self._is_horizontal_line_valid = oth.IsHorizontalLineValid
            self._vertical_line = oth.VerticalLine
            self._is_vertical_line_valid = oth.IsVerticalLineValid
            self._distance = oth.Distance
            self._is_distance_valid = oth.IsDistanceValid
            return
        else:
            if TopLine is UNO_NONE:
                self._top_line = BorderLine2_af200b28()
            else:
                self._top_line = TopLine
            self._is_top_line_valid = IsTopLineValid
            if BottomLine is UNO_NONE:
                self._bottom_line = BorderLine2_af200b28()
            else:
                self._bottom_line = BottomLine
            self._is_bottom_line_valid = IsBottomLineValid
            if LeftLine is UNO_NONE:
                self._left_line = BorderLine2_af200b28()
            else:
                self._left_line = LeftLine
            self._is_left_line_valid = IsLeftLineValid
            if RightLine is UNO_NONE:
                self._right_line = BorderLine2_af200b28()
            else:
                self._right_line = RightLine
            self._is_right_line_valid = IsRightLineValid
            if HorizontalLine is UNO_NONE:
                self._horizontal_line = BorderLine2_af200b28()
            else:
                self._horizontal_line = HorizontalLine
            self._is_horizontal_line_valid = IsHorizontalLineValid
            if VerticalLine is UNO_NONE:
                self._vertical_line = BorderLine2_af200b28()
            else:
                self._vertical_line = VerticalLine
            self._is_vertical_line_valid = IsVerticalLineValid
            self._distance = Distance
            self._is_distance_valid = IsDistanceValid



    @property
    def TopLine(self) -> BorderLine2_af200b28:
        """
        determines the line style at the top edge.
        """
        return self._top_line
    
    @TopLine.setter
    def TopLine(self, value: BorderLine2_af200b28) -> None:
        self._top_line = value

    @property
    def IsTopLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.TopLine is used.
        """
        return self._is_top_line_valid
    
    @IsTopLineValid.setter
    def IsTopLineValid(self, value: bool) -> None:
        self._is_top_line_valid = value

    @property
    def BottomLine(self) -> BorderLine2_af200b28:
        """
        determines the line style at the bottom edge.
        """
        return self._bottom_line
    
    @BottomLine.setter
    def BottomLine(self, value: BorderLine2_af200b28) -> None:
        self._bottom_line = value

    @property
    def IsBottomLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.BottomLine is used.
        """
        return self._is_bottom_line_valid
    
    @IsBottomLineValid.setter
    def IsBottomLineValid(self, value: bool) -> None:
        self._is_bottom_line_valid = value

    @property
    def LeftLine(self) -> BorderLine2_af200b28:
        """
        determines the line style at the left edge.
        """
        return self._left_line
    
    @LeftLine.setter
    def LeftLine(self, value: BorderLine2_af200b28) -> None:
        self._left_line = value

    @property
    def IsLeftLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.LeftLine is used.
        """
        return self._is_left_line_valid
    
    @IsLeftLineValid.setter
    def IsLeftLineValid(self, value: bool) -> None:
        self._is_left_line_valid = value

    @property
    def RightLine(self) -> BorderLine2_af200b28:
        """
        determines the line style at the right edge.
        """
        return self._right_line
    
    @RightLine.setter
    def RightLine(self, value: BorderLine2_af200b28) -> None:
        self._right_line = value

    @property
    def IsRightLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.RightLine is used.
        """
        return self._is_right_line_valid
    
    @IsRightLineValid.setter
    def IsRightLineValid(self, value: bool) -> None:
        self._is_right_line_valid = value

    @property
    def HorizontalLine(self) -> BorderLine2_af200b28:
        """
        determines the line style of horizontal lines for the inner part of a cell range.
        """
        return self._horizontal_line
    
    @HorizontalLine.setter
    def HorizontalLine(self, value: BorderLine2_af200b28) -> None:
        self._horizontal_line = value

    @property
    def IsHorizontalLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.HorizontalLine is used.
        """
        return self._is_horizontal_line_valid
    
    @IsHorizontalLineValid.setter
    def IsHorizontalLineValid(self, value: bool) -> None:
        self._is_horizontal_line_valid = value

    @property
    def VerticalLine(self) -> BorderLine2_af200b28:
        """
        determines the line style of vertical lines for the inner part of a cell range.
        """
        return self._vertical_line
    
    @VerticalLine.setter
    def VerticalLine(self, value: BorderLine2_af200b28) -> None:
        self._vertical_line = value

    @property
    def IsVerticalLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.VerticalLine is used.
        """
        return self._is_vertical_line_valid
    
    @IsVerticalLineValid.setter
    def IsVerticalLineValid(self, value: bool) -> None:
        self._is_vertical_line_valid = value

    @property
    def Distance(self) -> int:
        """
        contains the distance between the lines and other contents.
        """
        return self._distance
    
    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value

    @property
    def IsDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder2.Distance is used.
        """
        return self._is_distance_valid
    
    @IsDistanceValid.setter
    def IsDistanceValid(self, value: bool) -> None:
        self._is_distance_valid = value


__all__ = ['TableBorder2']
