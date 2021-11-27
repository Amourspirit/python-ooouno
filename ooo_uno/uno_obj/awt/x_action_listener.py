# coding: utf-8
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener


class XActionListener(XEventListener):
    """
    makes it possible to receive action events.
    
    See Also:
        `API  XActionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XActionListener.html>`_
    """

    @abstractmethod
    def actionPerformed(self, rEvent: object):
        """is invoked when an action is performed."""
