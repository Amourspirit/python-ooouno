# coding: utf-8
from abc import ABC, abstractproperty


class IProperty(ABC):
    """
    This structure describes a property.

    There are three types of properties:

        * bound properties
        * constrained properties
        * free properties

    See Also:
        `API Property <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Property.html>`_
    """
    @abstractproperty
    def Attributes(self) -> int:
        """This field may contain zero or more constants of the PropertyAttribute constants group."""
    @abstractproperty
    def Handle(self) -> int:
        """
        contains an implementation-specific handle for the property.

        It may be -1 if the implementation has no handle.
        You can use this handle to get values from the :py:class:`~beans.XFastPropertySet`.
        """
    @abstractproperty
    def Name(self) -> str:
        """
        specifies the name of the property.

        The name is unique within an py:class:`~beans.XPropertySet`. Upper and lower case are distinguished.
        """
    @abstractproperty
    def Type(self) -> object:
        """
        contains an object that identifies the declared type for the property.

        If the property has multiple types or the type is not known, **but not an any**, then void must be returned.
        """
