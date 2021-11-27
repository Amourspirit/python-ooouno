# coding: utf-8
from ..uno.x_interface import XInterface
# from com.sun.star.beans import XFastPropertySet
from abc import abstractmethod


class XFastPropertySet(XInterface):
    """
    provides a fast way of accessing and changing property values.

    This interface is an extension to the IPropertySet interface.
    The get and set methods use handles to access the property values instead of character strings.

    See Also:
        `API PropertyChangeEvent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XFastPropertySet.html>`_
    """
    @abstractmethod
    def getFastPropertyValue(self, nHandle: int) -> object:
        """
        Gets Property Value

        Args:
            nHandle (int): contains the implementation handle of the implementation for the property.

        Raises:
            UnknownPropertyException: if the property does not exist.
            com.sun.star.lang.WrappedTargetException: if the implementation has an internal reason
                for the exception. In this case the original exception is wrapped into that com.sun.star.lang.WrappedTargetException.

        Returns:
            object: the value of the property with the name PropertyName.

        """

    @abstractmethod
    def setFastPropertyValue(self, 	nHandle: int, aValue: object):
        """
        sets the value to the property with the specified name.

        Args:
            nHandle (int): contains the implementation handle of the implementation for the property.
            aValue (object): contains the new value of the property.

        Raises:
            UnknownPropertyException: if the property does not exist.
            PropertyVetoException: if a vetoable listener does not approve the change of a property value.
            IllegalArgumentException: 	if the new value cannot be converted to the type of the underlying
                property by an identity or widening conversion.
            com.sun.star.lang.WrappedTargetException: if the implementation has an internal reason for the exception.
                In this case the original exception is wrapped into this com.sun.star.lang.WrappedTargetException.
        """
