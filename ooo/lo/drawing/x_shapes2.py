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
# Namespace: com.sun.star.drawing
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_shape import XShape as XShape_8fd00a3d

class XShapes2(ABC):
    """
    Allows insertion of shapes at different positions.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API XShapes2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapes2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XShapes2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XShapes2'

    @abstractmethod
    def addBottom(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        Insert a new shape to the bottom of the stack.
        
        **since**
        
            LibreOffice 4.2
        """
    @abstractmethod
    def addTop(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        Insert a new shape to the top of the stack.
        
        **since**
        
            LibreOffice 4.2
        """

__all__ = ['XShapes2']

