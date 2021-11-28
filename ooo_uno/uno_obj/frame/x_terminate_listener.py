# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from ..lang.x_event_listener import XEventListener
if TYPE_CHECKING:
    from ..lang.event_object import IEventObject

class XTerminateListener(XEventListener):
    """has to be provided if an object wants to receive an event when the master environment (e.g., desktop) is terminated."""

    @abstractmethod
    def notifyTermination(self, Event: 'IEventObject'):
        """
        is called when the master environment is finally terminated.

        No veto will be accepted then.

        Args:
            Event (EventObject): describe the source of the event (e.g., the desktop)
        """

    @abstractmethod
    def queryTermination(self, Event: 'IEventObject'):
        """
        is called when the master environment (e.g., desktop) is about to terminate.

        Termination can be intercepted by throwing TerminationVetoException.
        Interceptor will be the new owner of desktop and should call
        XDesktop.terminate() after finishing his own operations.

        Args:
            Event (EventObject): describe the source of the event (e.g., the desktop)
        """
