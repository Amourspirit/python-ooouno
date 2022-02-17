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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .control_event import ControlEvent as ControlEvent_bc4b0bf6

class XControlNotificationListener(XInterface_8f010a43):
    """
    Must be implemented by dispatch objects which want to get notifications about control events.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XControlNotificationListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XControlNotificationListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XControlNotificationListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XControlNotificationListener'

    @abstractmethod
    def controlEvent(self, Event: 'ControlEvent_bc4b0bf6') -> None:
        """
        notifies that a control event has happened
        """

__all__ = ['XControlNotificationListener']

