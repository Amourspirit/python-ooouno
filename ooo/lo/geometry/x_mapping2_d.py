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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.geometry
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .real_point2_d import RealPoint2D as RealPoint2D_d6e70c78

class XMapping2D(XInterface_8f010a43):
    """
    Interface defining an arbitrary bijective mapping from R^2 to R^2.
    
    This interface provides methods to define an arbitrary bijective mapping from R^2 to R^2, i.e. from the two-dimensional space of real numbers onto itself, as is representable by the double floating point type. The mapping must be bijective, i.e. map a pair of real numbers to exactly one other pair of real numbers and vice versa, to facilitate a working inverse. Bijectiveness also implies completeness, i.e. for every pair of real numbers there must be another pair that is mapped upon them.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XMapping2D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1geometry_1_1XMapping2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.XMapping2D'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.geometry.XMapping2D'

    @abstractmethod
    def map(self, aPoint: 'RealPoint2D_d6e70c78') -> 'RealPoint2D_d6e70c78':
        """
        Forward 2D mapping function.
        """
    @abstractmethod
    def mapInverse(self, aPoint: 'RealPoint2D_d6e70c78') -> 'RealPoint2D_d6e70c78':
        """
        Inverse 2D mapping function.
        
        The following invariant must hold: map(mapInverse(p))=p. This effectively rules out non-bijective mappings.
        """

__all__ = ['XMapping2D']

