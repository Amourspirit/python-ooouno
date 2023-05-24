# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .view_state import ViewState as ViewState_cab30c62

class XCachedPrimitive(XInterface_8f010a43):
    """
    Interface for cached repaint of already drawn XCanvas primitives.
    
    This interface provides a method to quickly redraw some XCanvas primitives, using cached data.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XCachedPrimitive <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XCachedPrimitive.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XCachedPrimitive'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XCachedPrimitive'

    @abstractmethod
    def redraw(self, aState: ViewState_cab30c62) -> int:
        """
        Redraw the cached primitive.
        
        Redraw the cached primitive, with a possibly new view state.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XCachedPrimitive']

