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
    from ..awt.point import Point as Point_5fb2085e
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class GluePoint(object):
    """
    Struct Class

    A GluePoint could be attached to a shape or to a page.
    
    If a GluePoint is attached to a shape, it is moved when the shape moves. The ends of connectors can be attached to GluePoint.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API GluePoint <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1GluePoint.html>`_


    Note:
        | At runtime GluePoint will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | GluePoint is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Alignment: typing.Optional[int] = None, EscapeDirection: typing.Optional[int] = None, Position: 'typing.Optional[Point_5fb2085e]' = None, PositionAbsolute: typing.Optional[bool] = None):
        self._alignment = Alignment
        self._escape_direction = EscapeDirection
        self._position = Position
        self._position_absolute = PositionAbsolute

    @property
    def Alignment(self) -> int:
        """
        The alignment of a GluePoint defines how the position of the point is affected by resizing the parent Shape.
        """
        return self._alignment
    
    @Alignment.setter
    def Alignment(self, value: int) -> None:
        self._alignment = value

    @property
    def EscapeDirection(self) -> int:
        """
        This is the direction in which the connector line leaves the GluePoint.
        """
        return self._escape_direction
    
    @EscapeDirection.setter
    def EscapeDirection(self, value: int) -> None:
        self._escape_direction = value

    @property
    def Position(self) -> 'Point_5fb2085e':
        """
        This is the position of this GluePoint.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: 'Point_5fb2085e') -> None:
        self._position = value

    @property
    def PositionAbsolute(self) -> bool:
        """
        If this is TRUE, then the position of this GluePoint is absolute on a page and is not relative to a shape.
        """
        return self._position_absolute
    
    @PositionAbsolute.setter
    def PositionAbsolute(self, value: bool) -> None:
        self._position_absolute = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global GluePoint
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Alignment', 'EscapeDirection', 'Position', 'PositionAbsolute')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.drawing.GluePoint')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        GluePoint = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['GluePoint']
