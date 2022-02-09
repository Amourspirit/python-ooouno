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
# Libre Office Version: 7.2
# Namespace: com.sun.star.view
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XRenderable(XInterface_8f010a43):
    """
    represents something that can be rendered.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XRenderable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XRenderable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.XRenderable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.view.XRenderable'

    @abstractmethod
    def getRenderer(self, nRenderer: int, aSelection: object, xOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        returns the specific renderer properties based on the given selection.
        
        If the selection contains a valid XModel interface, it is assumed that the whole document should be rendered. If the selection is empty, nothing should be rendered.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getRendererCount(self, aSelection: object, xOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> int:
        """
        If a selection is given, the count has to be calculated based on this selection. The other methods of this interface will rely on this value if called.
        
        If the selection contains a valid XModel interface, it is assumed that the whole document should be rendered. If the selection is empty, nothing should be rendered.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def render(self, nRenderer: int, aSelection: object, xOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        renders the object.
        
        renders the object with the specific renderer based on the given selection.
        
        If the selection contains a valid XModel interface, it is assumed that the whole document should be rendered. If the selection is empty, nothing should be rendered.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


__all__ = ['XRenderable']

