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


class BezierPoint(object):
    """
    Struct Class

    This is a point on a Bezier curve.
    
    The two control points specify how the Bezier curve goes through the given position.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API BezierPoint <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1BezierPoint.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.BezierPoint'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.BezierPoint'
    """Literal Constant ``com.sun.star.drawing.BezierPoint``"""

    def __init__(self, Position: Point_5fb2085e = UNO_NONE, ControlPoint1: Point_5fb2085e = UNO_NONE, ControlPoint2: Point_5fb2085e = UNO_NONE) -> None:
        """
        Constructor

        Other Arguments:
            ``Position`` can be another ``BezierPoint`` instance,
                in which case other named args are ignored.

        Arguments:
            Position (Point, optional): Position value
            ControlPoint1 (Point, optional): ControlPoint1 value
            ControlPoint2 (Point, optional): ControlPoint2 value
        """
        if isinstance(Position, BezierPoint):
            oth: BezierPoint = Position
            self._position = oth.Position
            self._control_point1 = oth.ControlPoint1
            self._control_point2 = oth.ControlPoint2
            return
        else:
            if Position is UNO_NONE:
                self._position = Point_5fb2085e()
            else:
                self._position = Position
            if ControlPoint1 is UNO_NONE:
                self._control_point1 = Point_5fb2085e()
            else:
                self._control_point1 = ControlPoint1
            if ControlPoint2 is UNO_NONE:
                self._control_point2 = Point_5fb2085e()
            else:
                self._control_point2 = ControlPoint2



    @property
    def Position(self) -> Point_5fb2085e:
        """
        This is the position of this point.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: Point_5fb2085e) -> None:
        self._position = value

    @property
    def ControlPoint1(self) -> Point_5fb2085e:
        """
        This is the position of the first control point.
        """
        return self._control_point1
    
    @ControlPoint1.setter
    def ControlPoint1(self, value: Point_5fb2085e) -> None:
        self._control_point1 = value

    @property
    def ControlPoint2(self) -> Point_5fb2085e:
        """
        This is the position of the second control point.
        """
        return self._control_point2
    
    @ControlPoint2.setter
    def ControlPoint2(self, value: Point_5fb2085e) -> None:
        self._control_point2 = value


__all__ = ['BezierPoint']