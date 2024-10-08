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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.graphic
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..geometry.real_rectangle2_d import RealRectangle2D as RealRectangle2D_d9b0e03

class XPrimitive2D(XInterface_8f010a43):
    """
    XPrimitive2D interface.
    
    This is the basic interface for 2D graphic primitives. They need to be able

    See Also:
        `API XPrimitive2D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XPrimitive2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XPrimitive2D'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XPrimitive2D'

    @abstractmethod
    def getDecomposition(self, aViewParameters: typing.Tuple[PropertyValue_c9610c73, ...]) -> typing.Tuple[XPrimitive2D, ...]:
        """
        Retrieve decomposed list of simpler primitives.
        
        com.sun.star.geometry.AffineMatrix2D Transformation
        
        A transformation matrix which maps between world coordinates (which is equal to object's local coordinates) to view coordinates. If not defined, an empty transformation is implied.
        
        com.sun.star.geometry.RealRectangle2D Viewport
        
        Defines the visible part of the view in world coordinates. May be used to optimize decompositions, e.g. for 3D scenes only the visible part needs to be created. If not given, an empty Viewport is implied which means all is visible.
        
        double Time
        
        Defines the point in time for which the geometry is defined. This may lead to varied results for animated objects. This value is defined in the range [0.0 .. n[, negative values are not allowed. If not given, a value of 0.0 is implied.
        """
        ...
    @abstractmethod
    def getRange(self, aViewParameters: typing.Tuple[PropertyValue_c9610c73, ...]) -> RealRectangle2D_d9b0e03:
        """
        Retrieve bound rect of primitive.
        
        This method calculates the actual bound rect of the area in world coordinates. Note that for view-dependent primitives, the necessary pixel adjustments are taken into account. For that reason the ViewParameters need to be given.
        """
        ...

__all__ = ['XPrimitive2D']

