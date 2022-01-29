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
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a

class XSessionManagerListener(XEventListener_c7230c4a):
    """

    See Also:
        `API XSessionManagerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XSessionManagerListener.html>`_
    """

    @abstractmethod
    def approveInteraction(self, bInteractionGranted: bool) -> None:
        """
        approveInteraction is called when an outstanding interaction request was processed by the session manager
        """
    @abstractmethod
    def doRestore(self) -> bool:
        """
        returns true, if a session was restored
        """
    @abstractmethod
    def doSave(self, bShutdown: bool, bCancelable: bool) -> None:
        """
        doSave gets called when a save event was issued by the session manager the listener should do what is necessary to restore the current state of the application
        
        If the listener desires to interact with the user it must first issue a user interaction request and only do so if interaction was granted
        
        When the save request is processed (with or without user interaction) the listener must call XSessionManagerClient.saveDone() on the session manager client service object.
        
        the listener may choose to ignore the saveDone() event in case no real shutdown is in progress. He still has to call XSessionManagerClient.saveDone() in that case.
        """
    @abstractmethod
    def shutdownCanceled(self) -> None:
        """
        shutdownCanceled is called when a shutdown was canceled by the user The listener can cancel his saving operations.
        
        No further interaction is necessary and further calls on the session manager client service object will be ignored.
        """

__all__ = ['XSessionManagerListener']

