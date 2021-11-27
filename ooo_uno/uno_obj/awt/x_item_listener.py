# coding: utf-8
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener
# from com.sun.star.awt import XItemListener

# https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListener.html


class XItemListener(XEventListener):
    """
    makes it possible to receive action events.
    
    See Also:
        `API XItemListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListener.html>`_
    """

    @abstractmethod
    def itemStateChanged(self, rEvent: object):
        """is invoked when an item changes its state."""
