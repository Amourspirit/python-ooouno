# coding: utf-8
from abc import abstractmethod
from .x_element_access import XElementAccess


class XIndexAccess(XElementAccess):
    """
    provides access to the elements of a collection through an index.
    This interface should only be used if the data structure, itself, is indexed.

    See Also:
        `API XIndexAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XIndexAccess.html>`_
    """

    @abstractmethod
    def getByIndex(self, Index: int) -> object:
        """
        [summary]

        Args:
            Index (int): specifies the position in the array. The first index is ``0``.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: if the index is not valid.
            com.sun.star.lang.WrappedTargetException: If the implementation has internal reasons
                for exceptions, then wrap these in a ``com.sun.star.lang.WrappedTargetException`` exception.
        Returns:
            object: the element at the specified index.
        """

    @abstractmethod
    def getCount(self) -> int:
        """
        Get Count

        Returns:
            int: the number of elements in this container.
        """
