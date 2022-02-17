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
from ooo.oenv import UNO_NONE
import typing
from ..awt.point import Point as Point_5fb2085e
from .alignment import Alignment as Alignment_b1400b93
from .escape_direction import EscapeDirection as EscapeDirection_fdc50de6


class GluePoint2(object):
    """
    Struct Class

    This struct defines the attributes of a glue point.
    
    A glue point is a position inside a drawing shape where an edge of a connector shape can be connected.

    See Also:
        `API GluePoint2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1GluePoint2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.GluePoint2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.GluePoint2'
    """Literal Constant ``com.sun.star.drawing.GluePoint2``"""

    def __init__(self, Position: Point_5fb2085e = UNO_NONE, IsRelative: bool = False, PositionAlignment: Alignment_b1400b93 = Alignment_b1400b93.TOP_LEFT, Escape: EscapeDirection_fdc50de6 = EscapeDirection_fdc50de6.SMART, IsUserDefined: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``Position`` can be another ``GluePoint2`` instance,
                in which case other named args are ignored.

        Arguments:
            Position (Point, optional): Position value
            IsRelative (bool, optional): IsRelative value
            PositionAlignment (Alignment, optional): PositionAlignment value
            Escape (EscapeDirection, optional): Escape value
            IsUserDefined (bool, optional): IsUserDefined value
        """
        if isinstance(Position, GluePoint2):
            oth: GluePoint2 = Position
            self._position = oth.Position
            self._is_relative = oth.IsRelative
            self._position_alignment = oth.PositionAlignment
            self._escape = oth.Escape
            self._is_user_defined = oth.IsUserDefined
            return
        else:
            if Position is UNO_NONE:
                self._position = Point_5fb2085e()
            else:
                self._position = Position
            self._is_relative = IsRelative
            self._position_alignment = PositionAlignment
            self._escape = Escape
            self._is_user_defined = IsUserDefined



    @property
    def Position(self) -> Point_5fb2085e:
        """
        This is the position of this glue point.
        
        Depending on the flag IsRelative, this is either in 1/100cm or in 1/100%.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: Point_5fb2085e) -> None:
        self._position = value

    @property
    def IsRelative(self) -> bool:
        """
        if this flag is set to true, the position of this glue point is given in 1/100% values instead of 1/100cm.
        """
        return self._is_relative
    
    @IsRelative.setter
    def IsRelative(self, value: bool) -> None:
        self._is_relative = value

    @property
    def PositionAlignment(self) -> Alignment_b1400b93:
        """
        if this glue points position is not relative, this enum specifies the vertical and horizontal alignment of this point.
        
        The alignment specifies how the glue point is moved if the shape is resized.
        """
        return self._position_alignment
    
    @PositionAlignment.setter
    def PositionAlignment(self, value: Alignment_b1400b93) -> None:
        self._position_alignment = value

    @property
    def Escape(self) -> EscapeDirection_fdc50de6:
        """
        this member specifies the escape direction for a glue point.
        
        The escape direction is the direction the connecting line escapes the shape.
        """
        return self._escape
    
    @Escape.setter
    def Escape(self, value: EscapeDirection_fdc50de6) -> None:
        self._escape = value

    @property
    def IsUserDefined(self) -> bool:
        """
        if this flag is set to false, this is a default glue point.
        
        Some shapes may have default glue points attached to them which cannot be altered or removed.
        """
        return self._is_user_defined
    
    @IsUserDefined.setter
    def IsUserDefined(self, value: bool) -> None:
        self._is_user_defined = value


__all__ = ['GluePoint2']
