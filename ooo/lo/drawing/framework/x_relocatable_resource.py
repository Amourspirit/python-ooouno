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
# Namespace: com.sun.star.drawing.framework
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_resource import XResource as XResource_3bcd0f90

class XRelocatableResource(ABC):
    """
    An optional interface that is implemented by resources that are relocatable to different anchors.

    See Also:
        `API XRelocatableResource <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XRelocatableResource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.XRelocatableResource'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XRelocatableResource'

    @abstractmethod
    def relocateToAnchor(self, xNewAnchor: XResource_3bcd0f90) -> bool:
        """
        Replace the current anchor of the called resource with the given one.
        """
        ...

__all__ = ['XRelocatableResource']

