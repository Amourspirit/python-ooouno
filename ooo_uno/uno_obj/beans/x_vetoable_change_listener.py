# coding: utf-8
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener
from .property_change_event import IPropertyChangeEvent


class XVetoableChangeListener(XEventListener):
    """
    is used to receive PropertyChangeEvents whenever a "constrained" property is changed.

    See Also:
        `API XVetoableChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XVetoableChangeListener.html>`_
    """
    @abstractmethod
    def vetoableChange(self, aEvent: IPropertyChangeEvent):
        """
        gets called when a constrained property is changed.

        Args:
            aEvent (IPropertyChangeEvent): event
        """
