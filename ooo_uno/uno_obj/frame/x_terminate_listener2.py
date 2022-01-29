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
from .x_terminate_listener import XTerminateListener as XTerminateListener_b760e5a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XTerminateListener2(XTerminateListener_b760e5a):
    """
    extend interface XTerminateListener so a listener will be informed in case termination process was canceled by other reasons.

    See Also:
        `API XTerminateListener2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XTerminateListener2.html>`_
    """

    @abstractmethod
    def cancelTermination(self, Event: 'EventObject_a3d70b03') -> None:
        """
        is called when the master environment (e.g., desktop) was canceled in it's terminate request.
        
        Termination can be intercepted by throwing TerminationVetoException. But if a listener was queried for termination .. doesn't throw a veto exception ... it doesn't know if termination will be real next time. Because any other listener can throw those exception too ... and so it can happen that after queryTermination() no notifyTermination() will occur. But these listener don't know if it's allowed to start new processes then. Using this optional(!) interface will make it possible to be informed about canceled termination requests also.
        """

__all__ = ['XTerminateListener2']

