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
import typing
if typing.TYPE_CHECKING:
    from .shadow_location import ShadowLocation as ShadowLocation_d4530caf
    from ..util.color import Color as Color_68e908c5
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class ShadowFormat(object):
        """
        Struct Class

        describes the settings of a cell shadow.

        See Also:
            `API ShadowFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1ShadowFormat.html>`_


        Note:
            | At runtime ShadowFormat will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | ShadowFormat is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Color: 'typing.Optional[Color_68e908c5]' = None, IsTransparent: typing.Optional[bool] = None, Location: 'typing.Optional[ShadowLocation_d4530caf]' = None, ShadowWidth: typing.Optional[int] = None):
            self._color = Color
            self._is_transparent = IsTransparent
            self._location = Location
            self._shadow_width = ShadowWidth

        @property
        def Color(self) -> 'Color_68e908c5':
            """
            contains the color value of the shadow.
            """
            return self._color
        
        @Color.setter
        def Color(self, value: 'Color_68e908c5') -> None:
            self._color = value

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
        def Location(self) -> 'ShadowLocation_d4530caf':
            """
            contains the location of the shadow.
            """
            return self._location
        
        @Location.setter
        def Location(self, value: 'ShadowLocation_d4530caf') -> None:
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

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global ShadowFormat
        order = ('Color', 'IsTransparent', 'Location', 'ShadowWidth')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.table.ShadowFormat')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ShadowFormat = _struct_init

    _dynamic_struct()

__all__ = ['ShadowFormat']
