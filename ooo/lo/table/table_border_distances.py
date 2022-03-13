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


class TableBorderDistances(object):
    """
    Struct Class

    contains the distance settings of the border lines of all cells in a cell range.
    
    In a queried structure, the flags in TableBorderDistances.Is...DistanceValid indicate that not all lines of the boxes have the same values.
    
    In a structure which is used for setting, these flags determine if the corresponding distance should be set or if the old value should be kept.

    See Also:
        `API TableBorderDistances <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1TableBorderDistances.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.TableBorderDistances'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.TableBorderDistances'
    """Literal Constant ``com.sun.star.table.TableBorderDistances``"""

    def __init__(self, TopDistance: typing.Optional[int] = 0, IsTopDistanceValid: typing.Optional[bool] = False, BottomDistance: typing.Optional[int] = 0, IsBottomDistanceValid: typing.Optional[bool] = False, LeftDistance: typing.Optional[int] = 0, IsLeftDistanceValid: typing.Optional[bool] = False, RightDistance: typing.Optional[int] = 0, IsRightDistanceValid: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            TopDistance (int, optional): TopDistance value.
            IsTopDistanceValid (bool, optional): IsTopDistanceValid value.
            BottomDistance (int, optional): BottomDistance value.
            IsBottomDistanceValid (bool, optional): IsBottomDistanceValid value.
            LeftDistance (int, optional): LeftDistance value.
            IsLeftDistanceValid (bool, optional): IsLeftDistanceValid value.
            RightDistance (int, optional): RightDistance value.
            IsRightDistanceValid (bool, optional): IsRightDistanceValid value.
        """
        super().__init__()

        if isinstance(TopDistance, TableBorderDistances):
            oth: TableBorderDistances = TopDistance
            self.TopDistance = oth.TopDistance
            self.IsTopDistanceValid = oth.IsTopDistanceValid
            self.BottomDistance = oth.BottomDistance
            self.IsBottomDistanceValid = oth.IsBottomDistanceValid
            self.LeftDistance = oth.LeftDistance
            self.IsLeftDistanceValid = oth.IsLeftDistanceValid
            self.RightDistance = oth.RightDistance
            self.IsRightDistanceValid = oth.IsRightDistanceValid
            return

        kargs = {
            "TopDistance": TopDistance,
            "IsTopDistanceValid": IsTopDistanceValid,
            "BottomDistance": BottomDistance,
            "IsBottomDistanceValid": IsBottomDistanceValid,
            "LeftDistance": LeftDistance,
            "IsLeftDistanceValid": IsLeftDistanceValid,
            "RightDistance": RightDistance,
            "IsRightDistanceValid": IsRightDistanceValid,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._top_distance = kwargs["TopDistance"]
        self._is_top_distance_valid = kwargs["IsTopDistanceValid"]
        self._bottom_distance = kwargs["BottomDistance"]
        self._is_bottom_distance_valid = kwargs["IsBottomDistanceValid"]
        self._left_distance = kwargs["LeftDistance"]
        self._is_left_distance_valid = kwargs["IsLeftDistanceValid"]
        self._right_distance = kwargs["RightDistance"]
        self._is_right_distance_valid = kwargs["IsRightDistanceValid"]


    @property
    def TopDistance(self) -> int:
        """
        contains the distance between the top lines and other contents.
        """
        return self._top_distance
    
    @TopDistance.setter
    def TopDistance(self, value: int) -> None:
        self._top_distance = value

    @property
    def IsTopDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.TopDistance is used.
        """
        return self._is_top_distance_valid
    
    @IsTopDistanceValid.setter
    def IsTopDistanceValid(self, value: bool) -> None:
        self._is_top_distance_valid = value

    @property
    def BottomDistance(self) -> int:
        """
        contains the distance between the bottom lines and other contents.
        """
        return self._bottom_distance
    
    @BottomDistance.setter
    def BottomDistance(self, value: int) -> None:
        self._bottom_distance = value

    @property
    def IsBottomDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.BottomDistance is used.
        """
        return self._is_bottom_distance_valid
    
    @IsBottomDistanceValid.setter
    def IsBottomDistanceValid(self, value: bool) -> None:
        self._is_bottom_distance_valid = value

    @property
    def LeftDistance(self) -> int:
        """
        contains the distance between the left lines and other contents.
        """
        return self._left_distance
    
    @LeftDistance.setter
    def LeftDistance(self, value: int) -> None:
        self._left_distance = value

    @property
    def IsLeftDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.LeftDistance is used.
        """
        return self._is_left_distance_valid
    
    @IsLeftDistanceValid.setter
    def IsLeftDistanceValid(self, value: bool) -> None:
        self._is_left_distance_valid = value

    @property
    def RightDistance(self) -> int:
        """
        contains the distance between the right lines and other contents.
        """
        return self._right_distance
    
    @RightDistance.setter
    def RightDistance(self, value: int) -> None:
        self._right_distance = value

    @property
    def IsRightDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.RightDistance is used.
        """
        return self._is_right_distance_valid
    
    @IsRightDistanceValid.setter
    def IsRightDistanceValid(self, value: bool) -> None:
        self._is_right_distance_valid = value


__all__ = ['TableBorderDistances']
