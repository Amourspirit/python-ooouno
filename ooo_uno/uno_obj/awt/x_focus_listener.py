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
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .focus_event import FocusEvent as FocusEvent_8ecf0a56

class XFocusListener(XEventListener_c7230c4a):
    """
    makes it possible to receive keyboard focus events.
    
    The window which has the keyboard focus is the window which gets the keyboard events.

    See Also:
        `API XFocusListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFocusListener.html>`_
    """

    @abstractmethod
    def focusGained(self, e: 'FocusEvent_8ecf0a56') -> None:
        """
        is invoked when a window gains the keyboard focus.
        """
    @abstractmethod
    def focusLost(self, e: 'FocusEvent_8ecf0a56') -> None:
        """
        is invoked when a window loses the keyboard focus.
        """

__all__ = ['XFocusListener']

