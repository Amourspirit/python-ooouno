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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
import os
import typing
if typing.TYPE_CHECKING:
    from .dash_style import DashStyle as DashStyle_b10d0b85
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class LineDash(object):
    """
    Struct Class

    A LineDash defines a non-continuous line.

    See Also:
        `API LineDash <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1LineDash.html>`_


    Note:
        | At runtime LineDash will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | LineDash is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, DashLen: typing.Optional[int] = None, Dashes: typing.Optional[int] = None, Distance: typing.Optional[int] = None, DotLen: typing.Optional[int] = None, Dots: typing.Optional[int] = None, Style: 'typing.Optional[DashStyle_b10d0b85]' = None):
        self._dash_len = DashLen
        self._dashes = Dashes
        self._distance = Distance
        self._dot_len = DotLen
        self._dots = Dots
        self._style = Style

    @property
    def DashLen(self) -> int:
        """
        This is the length of a single dash.
        """
        return self._dash_len
    
    @DashLen.setter
    def DashLen(self, value: int) -> None:
        self._dash_len = value

    @property
    def Dashes(self) -> int:
        """
        This is the number of dashes.
        """
        return self._dashes
    
    @Dashes.setter
    def Dashes(self, value: int) -> None:
        self._dashes = value

    @property
    def Distance(self) -> int:
        """
        This is the distance between the dots.
        """
        return self._distance
    
    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value

    @property
    def DotLen(self) -> int:
        """
        This is the length of a dot.
        """
        return self._dot_len
    
    @DotLen.setter
    def DotLen(self, value: int) -> None:
        self._dot_len = value

    @property
    def Dots(self) -> int:
        """
        This is the number of dots in this LineDash.
        """
        return self._dots
    
    @Dots.setter
    def Dots(self, value: int) -> None:
        self._dots = value

    @property
    def Style(self) -> 'DashStyle_b10d0b85':
        """
        This sets the style of this LineDash.
        """
        return self._style
    
    @Style.setter
    def Style(self, value: 'DashStyle_b10d0b85') -> None:
        self._style = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global LineDash
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('DashLen', 'Dashes', 'Distance', 'DotLen', 'Dots', 'Style')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.drawing.LineDash')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        LineDash = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['LineDash']
