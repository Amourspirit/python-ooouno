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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
import os
import typing
if typing.TYPE_CHECKING:
    from .color_component import ColorComponent as ColorComponent_e4c0e78
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class RGBColor(object):
    """
    Struct Class

    RGB color triplet.

    See Also:
        `API RGBColor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1RGBColor.html>`_


    Note:
        | At runtime RGBColor will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | RGBColor is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Blue: 'typing.Optional[ColorComponent_e4c0e78]' = None, Green: 'typing.Optional[ColorComponent_e4c0e78]' = None, Red: 'typing.Optional[ColorComponent_e4c0e78]' = None):
        self._blue = Blue
        self._green = Green
        self._red = Red

    @property
    def Blue(self) -> 'ColorComponent_e4c0e78':
        """
        Blue component. Valid range is [0,1.0].
        """
        return self._blue
    
    @Blue.setter
    def Blue(self, value: 'ColorComponent_e4c0e78') -> None:
        self._blue = value

    @property
    def Green(self) -> 'ColorComponent_e4c0e78':
        """
        Green component. Valid range is [0,1.0].
        """
        return self._green
    
    @Green.setter
    def Green(self, value: 'ColorComponent_e4c0e78') -> None:
        self._green = value

    @property
    def Red(self) -> 'ColorComponent_e4c0e78':
        """
        Red component. Valid range is [0,1.0].
        """
        return self._red
    
    @Red.setter
    def Red(self, value: 'ColorComponent_e4c0e78') -> None:
        self._red = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global RGBColor
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Blue', 'Green', 'Red')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.rendering.RGBColor')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        RGBColor = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['RGBColor']
