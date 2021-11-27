# coding: utf-8
from abc import abstractmethod
from ..uno.x_interface import XInterface
# https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XElementAccess.html

class XElementAccess(XInterface):
    """
    This is the base interface of all collection interfaces.
    
    See Also:
        `API XElementAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XElementAccess.html>`_
    """
    
    @abstractmethod
    def getElementType(self) -> object:
        """
        Get Element Type

        Returns:
            object: the type of the elements. void means that it is a multi-type container and you cannot determine the exact types with this interface.
        """
    @abstractmethod
    def hasElements(self) -> bool:
        """
        Has Element

        Returns:
            bool: ``True`` if the object contain elements; Otherwise, ``False``.
        """
