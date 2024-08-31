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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .command_info_change_event import CommandInfoChangeEvent as CommandInfoChangeEvent_25100ed5

class XCommandInfoChangeListener(XEventListener_c7230c4a):
    """
    a listener for events related to changing XCommandInfos.

    See Also:
        `API XCommandInfoChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCommandInfoChangeListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XCommandInfoChangeListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XCommandInfoChangeListener'

    @abstractmethod
    def commandInfoChange(self, evt: CommandInfoChangeEvent_25100ed5) -> None:
        """
        gets called whenever changes of a XCommandInfo shall be propagated.
        """
        ...

__all__ = ['XCommandInfoChangeListener']

