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
# Namespace: com.sun.star.drawing
import typing
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_shape import XShape as XShape_8fd00a3d

class XShapes(XIndexAccess_f0910d6d):
    """
    makes it possible to access, add, and remove the Shapes in a collection.

    See Also:
        `API XShapes <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapes.html>`_
    """

    @abstractmethod
    def add(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        inserts a Shape into this collection.
        """
    @abstractmethod
    def remove(self, xShape: 'XShape_8fd00a3d') -> None:
        """
        removes a Shape from this collection.
        """

__all__ = ['XShapes']

