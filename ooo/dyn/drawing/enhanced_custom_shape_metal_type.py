# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class EnhancedCustomShapeMetalType(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeMetalType", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeMetalType``"""
        pass

    class EnhancedCustomShapeMetalTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeMetalType", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeMetalType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.drawing import EnhancedCustomShapeMetalType as EnhancedCustomShapeMetalType
    else:
        # keep document generators happy
        from ...lo.drawing.enhanced_custom_shape_metal_type import EnhancedCustomShapeMetalType as EnhancedCustomShapeMetalType

    class EnhancedCustomShapeMetalTypeEnum(IntEnum):
        """
        Enum of Const Class EnhancedCustomShapeMetalType

        These constants define the way the attribute Metal of service EnhancedCustomShapeExtrusion is interpreted for rendering the shape.
        
        **since**
        
            LibreOffice 7.4
        """
        MetalODF = EnhancedCustomShapeMetalType.MetalODF
        """
        The rendering of the shape is modified as specified in the ODF standard.
        """
        MetalMSCompatible = EnhancedCustomShapeMetalType.MetalMSCompatible
        """
        The rendering of the shape is modified to get a similar rendering as in Microsoft Office for objects, which have the fc3DMetallic flag in Rich Text Format or binary MS Office format set.
        """

__all__ = ['EnhancedCustomShapeMetalType', 'EnhancedCustomShapeMetalTypeEnum']
