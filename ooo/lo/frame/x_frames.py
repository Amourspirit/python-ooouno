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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_frame import XFrame as XFrame_7a570956

class XFrames(XIndexAccess_f0910d6d):
    """
    manages and creates frames.
    
    Frames may contain other frames (by implementing an XFrames interface) and may be contained in other frames.

    See Also:
        `API XFrames <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrames.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XFrames'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XFrames'

    @abstractmethod
    def append(self, xFrame: XFrame_7a570956) -> None:
        """
        appends the specified Frame to the list of sub-frames.
        """
        ...
    @abstractmethod
    def queryFrames(self, nSearchFlags: int) -> typing.Tuple[XFrame_7a570956, ...]:
        """
        provides access to the list of all currently existing frames inside this container and her sub frames
        """
        ...
    @abstractmethod
    def remove(self, xFrame: XFrame_7a570956) -> None:
        """
        removes the frame from its container.
        
        Note:
        """
        ...

__all__ = ['XFrames']

