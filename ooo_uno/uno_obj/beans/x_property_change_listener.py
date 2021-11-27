# coding: utf-8
from ..lang.x_event_listener import XEventListener
from .property_change_event import IPropertyChangeEvent
# from com.sun.star.beans import XPropertyChangeListener
from abc import abstractmethod


class XPropertyChangeListener(XEventListener):
    """
    is used to receive PropertyChangeEvents whenever a bound property is changed.

    See Also:
        `API XPropertyChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyChangeListener.html>`_
    """

    @abstractmethod
    def propertyChange(self, evt: IPropertyChangeEvent):
        """is called when a bound property is changed."""
