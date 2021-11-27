# coding: utf-8
from abc import abstractmethod
from .x_element_access import XElementAccess
from .x_enumeration import XEnumeration


class XEnumerationAccess(XElementAccess):
    """
    used to enumerate objects in a container which contains objects.

    See Also:
        `API  XEnumerationAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XEnumerationAccess.html>`_
    """

    @abstractmethod
    def createEnumeration(self) -> XEnumeration:
        """
        create enumeration

        Returns:
            XEnumeration: a new enumeration object for this container.
            It returns ``None`` if there are no objects in this container.
        """
