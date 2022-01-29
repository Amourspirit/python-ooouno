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
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_document_event_listener import XDocumentEventListener as XDocumentEventListener_7db01146
    from ..frame.x_controller2 import XController2 as XController2_bbcf0bc1

class XDocumentEventBroadcaster(ABC):
    """
    allows to be notified of events happening in an OfficeDocument, and to cause notification of such events.
    
    This interface is the successor of the XEventBroadcaster interface, which should not be used anymore.
    
    **since**
    
        OOo 3.1

    See Also:
        `API XDocumentEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentEventBroadcaster.html>`_
    """

    @abstractmethod
    def addDocumentEventListener(self, Listener: 'XDocumentEventListener_7db01146') -> None:
        """
        registers a listener which is notified about document events
        """
    @abstractmethod
    def notifyDocumentEvent(self, EventName: str, ViewController: 'XController2_bbcf0bc1', Supplement: object) -> None:
        """
        causes the broadcaster to notify all registered listeners of the given event
        
        The method will create a DocumentEvent instance with the given parameters, and fill in the Source member (denoting the broadcaster) as appropriate.
        
        Whether the actual notification happens synchronously or asynchronously is up to the implementor of this method. However, implementations are encouraged to specify this, for the list of supported event types, in their service contract.
        
        Implementations might also decide to limit the list of allowed events (means event names) at their own discretion. Again, in this case they're encouraged to document this in their service contract.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    @abstractmethod
    def removeDocumentEventListener(self, Listener: 'XDocumentEventListener_7db01146') -> None:
        """
        revokes a listener which has previously been registered to be notified about document events.
        """

__all__ = ['XDocumentEventBroadcaster']

