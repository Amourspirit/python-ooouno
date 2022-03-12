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
from .shadow_location import ShadowLocation as ShadowLocation_d4530caf
from ..util.color import Color as Color_68e908c5


class ShadowFormat(object):
    """
    Struct Class

    describes the settings of a cell shadow.

    See Also:
        `API ShadowFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1ShadowFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.ShadowFormat'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.table.ShadowFormat'
    """Literal Constant ``com.sun.star.table.ShadowFormat``"""

    def __init__(self, Location: typing.Optional[ShadowLocation_d4530caf] = ShadowLocation_d4530caf.NONE, ShadowWidth: typing.Optional[int] = 0, IsTransparent: typing.Optional[bool] = False, Color: typing.Optional[Color_68e908c5] = Color_68e908c5(0)) -> None:
        """
        Constructor

        Arguments:
            Location (ShadowLocation, optional): Location value.
            ShadowWidth (int, optional): ShadowWidth value.
            IsTransparent (bool, optional): IsTransparent value.
            Color (Color, optional): Color value.
        """
        super().__init__()
        kargs = {
            "Location": Location,
            "ShadowWidth": ShadowWidth,
            "IsTransparent": IsTransparent,
            "Color": Color,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._location = kwargs["Location"]
        self._shadow_width = kwargs["ShadowWidth"]
        self._is_transparent = kwargs["IsTransparent"]
        self._color = kwargs["Color"]


    @property
    def Location(self) -> ShadowLocation_d4530caf:
        """
        contains the location of the shadow.
        """
        return self._location
    
    @Location.setter
    def Location(self, value: ShadowLocation_d4530caf) -> None:
        self._location = value

    @property
    def ShadowWidth(self) -> int:
        """
        contains the size of the shadow.
        """
        return self._shadow_width
    
    @ShadowWidth.setter
    def ShadowWidth(self, value: int) -> None:
        self._shadow_width = value

    @property
    def IsTransparent(self) -> bool:
        """
        is TRUE, if shadow is transparent.
        """
        return self._is_transparent
    
    @IsTransparent.setter
    def IsTransparent(self, value: bool) -> None:
        self._is_transparent = value

    @property
    def Color(self) -> Color_68e908c5:
        """
        contains the color value of the shadow.
        """
        return self._color
    
    @Color.setter
    def Color(self, value: Color_68e908c5) -> None:
        self._color = value


__all__ = ['ShadowFormat']
