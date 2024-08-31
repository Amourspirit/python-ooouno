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
# Namespace: com.sun.star.media
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_player import XPlayer as XPlayer_83f509cd

class XManager(ABC):
    """
    the com.sun.star.media.XPlayer factory interface

    See Also:
        `API XManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1media_1_1XManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.media'
    __ooo_full_ns__: str = 'com.sun.star.media.XManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.media.XManager'

    @abstractmethod
    def createPlayer(self, aURL: str) -> XPlayer_83f509cd:
        """
        creates a new media player
        """
        ...

__all__ = ['XManager']

