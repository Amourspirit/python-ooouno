# coding: utf-8
from abc import abstractmethod
from typing import Iterable
from ..uno.x_interface import XInterface
from .property import IProperty


class XPropertySetInfo(XInterface):
    """
    specifies a set of properties.

    There are three kinds of properties:

        * bound properties
        * constrained properties
        * free properties

    The specification only describes the properties, it does not contain any values.

    See Also:
        `API XPropertySetInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySetInfo.html>`_
    """
    @abstractmethod
    def getProperties(self) -> Iterable[IProperty]:
        """
        Gets properties

        Returns:
            Iterable[IProperty]: a sequence with all property descriptors which are specified within this XPropertySetInfo.
        """
    @abstractmethod
    def getPropertyByName(self, aName: str) -> IProperty:
        """
        Get property by name

        Args:
            aName (str): specifies the name of the property.

        Returns:
            IProperty: the property with the specified name from the object.

        Raises:
            UnknownPropertyException: if the property does not exist.
        """

    @abstractmethod
    def hasPropertyByName(self, Name: str) -> bool:
        """
        [summary]

        Args:
            Name (str): specifies the name of the property.

        Returns:
            bool: ``True`` if a property with the specified name exist; Otherwise, ``False``.
        """
