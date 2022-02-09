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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .frame_action_event import FrameActionEvent as FrameActionEvent_ed700d5e

class XFrameActionListener(XEventListener_c7230c4a):
    """
    has to be provided if an object wants to receive events when several things happen to components within frames of the desktop frame tree.
    
    E.g., you can receive events of instantiation/destruction and activation/deactivation of components.

    See Also:
        `API XFrameActionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrameActionListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XFrameActionListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XFrameActionListener'

    @abstractmethod
    def frameAction(self, Action: 'FrameActionEvent_ed700d5e') -> None:
        """
        is called whenever any action occurs to a component within a frame.
        """


__all__ = ['XFrameActionListener']

