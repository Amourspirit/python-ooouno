# coding: utf-8
from typing import Union
from ..uno.x_interface import XInterface
from ..beans.x_vetoable_change_listener import XVetoableChangeListener
from ..beans.x_property_change_listener import XPropertyChangeListener
from ..beans.x_property_set_info import XPropertySetInfo
from abc import abstractmethod


class XPropertySet(XInterface):
    """
    provides information about and access to the properties from an implementation.

    There are three types of properties:

        * bound properties
        * constrained properties
        * free properties

    See Also:
        `API PropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySet.html>`_
    """
    @abstractmethod
    def addPropertyChangeListener(self, aPropertyName: str, xListener: XPropertyChangeListener):
        """
        adds an XPropertyChangeListener to the specified property.

        An empty name ("") registers the listener to all bound properties.
        If the property is not bound, the behavior is not specified.

        It is suggested to allow multiple registration of the same listener,
        thus for each time a listener is added, it has to be removed.

        Args:
            aPropertyName (str): Property Name
            xListener (XPropertyChangeListener): listener
        """

    @abstractmethod
    def addVetoableChangeListener(self, PropertyName: str, aListener: XVetoableChangeListener):
        """
        adds an ``XVetoableChangeListener`` to the specified property with the name PropertyName.

        An empty name ("") registers the listener to all constrained properties. If the property is not constrained, the behavior is not specified.

        Args:
            PropertyName (str): Propery name
            aListener (XVetoableChangeListener): listener
        """

    @abstractmethod
    def getPropertySetInfo(self) -> Union[XPropertySetInfo, None]:
        """
        [summary]

        Returns:
            XPropertySetInfo: the XPropertySetInfo interface, which describes all properties of the object which supplies this interface.
            ``None`` if the implementation cannot or will not provide information about the properties; otherwise the interface XPropertySetInfo is returned.
        """

    @abstractmethod
    def getPropertyValue(self, PropertyName: str) -> object:
        """
        Gets a property value

        Args:
            PropertyName (str): This parameter specifies the name of the property.

        Returns:
            object: the value of the property with the specified name.

        Raises:
            UnknownPropertyException: if the property does not exist.
            com.sun.star.lang.WrappedTargetException: if the implementation has an internal reason for the exception.
                In this case the original exception is wrapped into that ``com.sun.star.lang.WrappedTargetException``.
        """

    @abstractmethod
    def removePropertyChangeListener(self, aPropertyName: str, aListener: XPropertyChangeListener):
        """
        removes an XPropertyChangeListener from the listener list.

        It is a "noop" if the listener is not registered.

        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.

        Args:
            aPropertyName (str): name of propety
            aListener (XPropertyChangeListener): listener

        Raises:
            com.sun.star.beans.UnknownPropertyException:
            com.sun.star.lang.WrappedTargetException:
        """

    @abstractmethod
    def removeVetoableChangeListener(self, PropertyName: str, aListener: XVetoableChangeListener):
        """
        Removes an XVetoableChangeListener from the listener list.

        It is a "noop" if the listener is not registered.

        Args:
            PropertyName (str): [description]
            aListener (XVetoableChangeListener): [description]

        Raises:
            com.sun.star.beans.UnknownPropertyException:
            com.sun.star.lang.WrappedTargetException:
        """

    @abstractmethod
    def setPropertyValue(self, aPropertyName: str, aValue: object):
        """
        sets the value of the property with the specified name.
        
        If it is a bound property the value will be changed before the change event is fired.
        If it is a constrained property a vetoable event is fired before the property value can be changed.

        Args:
            aPropertyName (str): property name
            aValue (object): value
        
        Raises:
            com.sun.star.beans.PropertyVetoException: if the property is read-only or vetoable and one of the
                listeners throws this exception because of an unaccepted new value.
            com.sun.star.beans.UnknownPropertyException:
            com.sun.star.lang.IllegalArgumentException:
            com.sun.star.lang.WrappedTargetException:
        """
    
