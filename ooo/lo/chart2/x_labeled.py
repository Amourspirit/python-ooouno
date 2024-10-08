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
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_title import XTitle as XTitle_833f09a6
    from com.sun.star.drawing.RectanglePoint import RectanglePointProto  # type: ignore

class XLabeled(ABC):
    """

    See Also:
        `API XLabeled <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XLabeled.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XLabeled'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XLabeled'

    @abstractmethod
    def getLabel(self) -> XTitle_833f09a6:
        """
        """
        ...
    @abstractmethod
    def getLabelAnchor(self) -> RectanglePointProto:
        """
        """
        ...
    @abstractmethod
    def getOffset(self) -> typing.Tuple[float, ...]:
        """
        """
        ...
    @abstractmethod
    def getOwnAnchor(self) -> RectanglePointProto:
        """
        """
        ...
    @abstractmethod
    def setLabel(self, xTitle: XTitle_833f09a6) -> None:
        """
        """
        ...
    @abstractmethod
    def setLabelAnchor(self, aAnchorPoint: RectanglePointProto) -> None:
        """
        """
        ...
    @abstractmethod
    def setOffset(self, aOffsetVector: typing.Tuple[float, ...]) -> None:
        """
        """
        ...
    @abstractmethod
    def setOwnAnchor(self, aAnchorPoint: RectanglePointProto) -> None:
        """
        """
        ...

__all__ = ['XLabeled']