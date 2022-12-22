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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class EnhancedCustomShapeParameterType(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeParameterType", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeParameterType``"""
        pass

    class EnhancedCustomShapeParameterTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeParameterType", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeParameterType`` as Enum values"""
        pass

else:
    from ...lo.drawing.enhanced_custom_shape_parameter_type import EnhancedCustomShapeParameterType as EnhancedCustomShapeParameterType

    class EnhancedCustomShapeParameterTypeEnum(IntEnum):
        """
        Enum of Const Class EnhancedCustomShapeParameterType

        defines how an EnhancedCustomShapeParameter has to be interpreted
        """
        NORMAL = EnhancedCustomShapeParameterType.NORMAL
        """
        the value of the point component is normal, the Coordinate is taken as it is
        """
        EQUATION = EnhancedCustomShapeParameterType.EQUATION
        """
        the value of the point component has to be interpreted as index to an Equation
        """
        ADJUSTMENT = EnhancedCustomShapeParameterType.ADJUSTMENT
        """
        the value of the point component has to be interpreted as index into the list of AdjustmentValues
        """
        LEFT = EnhancedCustomShapeParameterType.LEFT
        """
        the logical left border of the CustomShape is used
        """
        TOP = EnhancedCustomShapeParameterType.TOP
        """
        the logical top border of the CustomShape is used
        """
        RIGHT = EnhancedCustomShapeParameterType.RIGHT
        """
        the logical right border of the CustomShape is used
        """
        BOTTOM = EnhancedCustomShapeParameterType.BOTTOM
        """
        the logical bottom border of the CustomShape is used
        """
        XSTRETCH = EnhancedCustomShapeParameterType.XSTRETCH
        """
        the x value of the stretch point is used
        """
        YSTRETCH = EnhancedCustomShapeParameterType.YSTRETCH
        """
        the y value of the stretch point is used
        """
        HASSTROKE = EnhancedCustomShapeParameterType.HASSTROKE
        """
        If the shape has a line style, a value of 1 is used.
        """
        HASFILL = EnhancedCustomShapeParameterType.HASFILL
        """
        If the shape has a fill style, a value of 1 is used.
        """
        WIDTH = EnhancedCustomShapeParameterType.WIDTH
        """
        The width of the svg:viewBox is used.
        """
        HEIGHT = EnhancedCustomShapeParameterType.HEIGHT
        """
        The height of the svg:viewBox is used.
        """
        LOGWIDTH = EnhancedCustomShapeParameterType.LOGWIDTH
        """
        The logical width of the shape is used.
        """
        LOGHEIGHT = EnhancedCustomShapeParameterType.LOGHEIGHT
        """
        The logical height of the shape is used.
        """

__all__ = ['EnhancedCustomShapeParameterType', 'EnhancedCustomShapeParameterTypeEnum']
