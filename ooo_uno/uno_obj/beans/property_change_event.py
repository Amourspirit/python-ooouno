# coding: utf-8
from ..lang.event_object_struct import IEventObject
from abc import abstractproperty


class IPropertyChangeEvent(IEventObject):
    """
    gets delivered whenever a "bound" or "constrained" property is changed.

    A PropertyChangeEvent object is sent as an argument to the methods of
    XPropertyChangeListener and XVetoableChangeListener.

    Normally such events contain the name and the old and new value of the changed property.

    Void values may be provided for the old and new values if their true values are not known.

    See Also:
        `API PropertyChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyChangeEvent.html>`_
    """
    @abstractproperty
    def Further(self) -> bool:
        """contains ``True`` if further events in the same transaction occur."""

    @abstractproperty
    def NewValue(self) -> object:
        """contains the new value of the property"""
    @abstractproperty
    def OldValue(self) -> object:
        """contains the old value of the property."""

    @abstractproperty
    def PropertyHandle(self) -> int:
        """
        contains the implementation handle for the property.

        May be -1 if the implementation has no handle.
        You can use this handle to get values from the XFastPropertySet.
        """
    @abstractproperty
    def PropertyName(self) -> str:
        """contains the unique name of the property which changes its value."""
