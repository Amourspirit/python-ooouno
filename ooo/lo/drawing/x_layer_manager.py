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
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_layer import XLayer as XLayer_8fd00a49
    from .x_shape import XShape as XShape_8fd00a3d

class XLayerManager(XIndexAccess_f0910d6d):
    """
    This interface makes it possible to access and manage the Layers of a document.

    See Also:
        `API XLayerManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XLayerManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XLayerManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XLayerManager'

    @abstractmethod
    def attachShapeToLayer(self, xShape: 'XShape_8fd00a3d', xLayer: 'XLayer_8fd00a49') -> None:
        """
        attaches a Shape to the given Layer.
        """
        ...
    @abstractmethod
    def getLayerForShape(self, xShape: 'XShape_8fd00a3d') -> 'XLayer_8fd00a49':
        """
        queries the Layer that a Shape is attached to
        """
        ...
    @abstractmethod
    def insertNewByIndex(self, nIndex: int) -> 'XLayer_8fd00a49':
        """
        creates a new Layer
        """
        ...
    @abstractmethod
    def remove(self, xLayer: 'XLayer_8fd00a49') -> None:
        """
        removes a Layer and all Shapes on this Layer.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XLayerManager']

