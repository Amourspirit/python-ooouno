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

class XShapes3(ABC):
    """
    Yet another XShapes interface, enables sorting shapes with some extra attention paid to shapes with textboxes and overall performance.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API XShapes3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapes3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XShapes3'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XShapes3'

    @abstractmethod
    def sort(self, sortOrder: 'typing.Tuple[int, ...]') -> None:
        """
        Sort shapes according to given sort order, for perf reason just rearrange and don't broadcast.
        
        **since**
        
            LibreOffice 6.4

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XShapes3']

