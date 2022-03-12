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
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class HoriOrientationFormat(object):
    """
    Struct Class

    describes the horizontal orientation of an object.
    
    If HorizontalOrientation == HORI_NONE, then the value \"XPos\" describes the distance from the left border of the context. Otherwise \"XPos\" is ignored.
    
    The following flags are used to adapt the position of the object to odd and even pages. If \"PositionToggle\" is set, then the horizontal position is mirrored.

    See Also:
        `API HoriOrientationFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1HoriOrientationFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.HoriOrientationFormat'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.text.HoriOrientationFormat'
    """Literal Constant ``com.sun.star.text.HoriOrientationFormat``"""

    def __init__(self, XPos: typing.Optional[int] = 0, HorizontalOrientation: typing.Optional[int] = 0, HorizontalRelation: typing.Optional[int] = 0, PositionToggle: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            XPos (int, optional): XPos value.
            HorizontalOrientation (int, optional): HorizontalOrientation value.
            HorizontalRelation (int, optional): HorizontalRelation value.
            PositionToggle (bool, optional): PositionToggle value.
        """
        super().__init__()
        kargs = {
            "XPos": XPos,
            "HorizontalOrientation": HorizontalOrientation,
            "HorizontalRelation": HorizontalRelation,
            "PositionToggle": PositionToggle,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._x_pos = kwargs["XPos"]
        self._horizontal_orientation = kwargs["HorizontalOrientation"]
        self._horizontal_relation = kwargs["HorizontalRelation"]
        self._position_toggle = kwargs["PositionToggle"]


    @property
    def XPos(self) -> int:
        """
        contains the distance from the left border.
        
        Only valid if the property HorizontalOrientation contains the value HORI_NONE.
        """
        return self._x_pos
    
    @XPos.setter
    def XPos(self, value: int) -> None:
        self._x_pos = value

    @property
    def HorizontalOrientation(self) -> int:
        """
        determines the horizontal alignment of an object.
        
        The values refer to com.sun.star.HoriOrientation.
        """
        return self._horizontal_orientation
    
    @HorizontalOrientation.setter
    def HorizontalOrientation(self, value: int) -> None:
        self._horizontal_orientation = value

    @property
    def HorizontalRelation(self) -> int:
        """
        determines the reference position of the horizontal alignment.
        """
        return self._horizontal_relation
    
    @HorizontalRelation.setter
    def HorizontalRelation(self, value: int) -> None:
        self._horizontal_relation = value

    @property
    def PositionToggle(self) -> bool:
        """
        determines if the orientation toggles between left and right pages.
        """
        return self._position_toggle
    
    @PositionToggle.setter
    def PositionToggle(self, value: bool) -> None:
        self._position_toggle = value


__all__ = ['HoriOrientationFormat']
