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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..drawing.shape import Shape as Shape_85cc09e5
if typing.TYPE_CHECKING:
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class Shape(Shape_85cc09e5):
    """
    Service Class

    specifies the service of shapes in a spreadsheet document
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1Shape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.Shape'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Anchor(self) -> XInterface_8f010a43:
        """
        contains the object where this shape is anchored on.
        
        Possible objects are XSpreadsheet and XCell.
        """
        ...

    @property
    @abstractmethod
    def HoriOrientPosition(self) -> int:
        """
        contains the horizontal position of the object (1/100 mm).
        
        The position is relative to the anchor object.
        
        If the underlying table layout direction is left to right the position is the difference of the left top edge of the anchor object and the left top edge of the drawing object.
        
        If the underlying table layout direction is right to left the position is the difference of the right top edge of the anchor object and the right top edge of the drawing object.
        """
        ...

    @property
    @abstractmethod
    def ResizeWithCell(self) -> bool:
        """
        If set, the shape will resize with the cell.
        
        Only works when shape is anchored to a cell.
        
        **since**
        
            LibreOffice 6.3
        """
        ...

    @property
    @abstractmethod
    def VertOrientPosition(self) -> int:
        """
        contains the vertical position of the object (1/100 mm).
        
        The position is relative to the anchor object.
        
        If the underlying table layout direction is left to right the position is the difference of the left top edge of the anchor object and the left top edge of the drawing object.
        
        If the underlying table layout direction is right to left the position is the difference of the right top edge of the anchor object and the right top edge of the drawing object.
        """
        ...


__all__ = ['Shape']

