# coding: utf-8
from abc import abstractmethod
from ..uno.x_interface import XInterface


class XEnumeration(XInterface):
    """
    provides functionality to enumerate the contents of a container.

    An object that implements the XEnumeration interface generates a series of elements,
    one at a time. Successive calls to the XEnumeration.nextElement method return
    successive elements of the series.

    If the object changed, the behavior of the enumeration is not specified. This is not a remote interface.

    See Also:
        `API XEnumeration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XEnumeration.html>`_
    """

    @abstractmethod
    def hasMoreElements(self) -> bool:
        """
        tests whether this enumeration contains more elements.

        Returns:
            bool: ``True`` if there are more elements; Otherwise, ``False``.
        """

    @abstractmethod
    def nextElement(self) -> object:
        """
        Next element

        Returns:
            object: the next element of this enumeration.
        """
