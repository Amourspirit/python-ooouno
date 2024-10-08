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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .enhanced_custom_shape_parameter_pair import EnhancedCustomShapeParameterPair as EnhancedCustomShapeParameterPair_262914a3
    from .enhanced_custom_shape_segment import EnhancedCustomShapeSegment as EnhancedCustomShapeSegment_b07b1249
    from .enhanced_custom_shape_text_frame import EnhancedCustomShapeTextFrame as EnhancedCustomShapeTextFrame_d6321306

class EnhancedCustomShapePath(ABC):
    """
    Service Class

    This service may be represented by a com.sun.star.beans.PropertyValue [].

    See Also:
        `API EnhancedCustomShapePath <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapePath.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapePath'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ConcentricGradientFillAllowed(self) -> bool:
        """
        This property specifies if this shape supports concentric gradient fill.
        
        The default is false.
        """
        ...

    @property
    @abstractmethod
    def Coordinates(self) -> typing.Tuple[EnhancedCustomShapeParameterPair_262914a3, ...]:
        """
        This property is specifying the points that makes the geometry of the shape.
        """
        ...

    @property
    @abstractmethod
    def ExtrusionAllowed(self) -> bool:
        """
        This property specifies if this shape supports the EnhancedCustomShapeExtrusion properties.
        
        The default is true.
        """
        ...

    @property
    @abstractmethod
    def GluePointLeavingDirections(self) -> typing.Tuple[float, ...]:
        """
        This property specifies GluePoint leaving directions.
        """
        ...

    @property
    @abstractmethod
    def GluePointType(self) -> int:
        """
        This property defines the GluePoint type.
        
        The values that can be used are specified in com.sun.star.drawing.EnhancedCustomShapeGluePointType
        """
        ...

    @property
    @abstractmethod
    def GluePoints(self) -> typing.Tuple[EnhancedCustomShapeParameterPair_262914a3, ...]:
        """
        This property specifies custom gluepoints.
        """
        ...

    @property
    @abstractmethod
    def Segments(self) -> typing.Tuple[EnhancedCustomShapeSegment_b07b1249, ...]:
        """
        This property specifies the commands and the way the Coordinates have to be interpreted.
        """
        ...

    @property
    @abstractmethod
    def StretchX(self) -> int:
        """
        This property specifies the horizontal StretchPoint that has to be used.
        
        No stretching is used if this property is omitted.
        """
        ...

    @property
    @abstractmethod
    def StretchY(self) -> int:
        """
        This property specifies the vertical StretchPoint that has to be used.
        
        No stretching is used if this property is omitted.
        """
        ...

    @property
    @abstractmethod
    def SubViewSize(self) -> typing.Tuple[Size_576707ef, ...]:
        """
        This property specifies view size per sub path.
        """
        ...

    @property
    @abstractmethod
    def TextFrames(self) -> typing.Tuple[EnhancedCustomShapeTextFrame_d6321306, ...]:
        """
        This property specifies the text frames that can be used with the shape.
        
        In general the first text frame is used, except the shape is containing vertical text, then the object tries to use the second text frame. The default text frame will be as big as the shape.
        """
        ...

    @property
    @abstractmethod
    def TextPathAllowed(self) -> bool:
        """
        This property specifies if this shape supports concentric gradient fill.
        
        The default is false;
        """
        ...


__all__ = ['EnhancedCustomShapePath']

