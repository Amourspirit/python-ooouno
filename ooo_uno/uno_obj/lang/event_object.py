# coding: utf-8
# from com.sun.star.lang import EventObject
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..uno.x_interface import XInterface


class IEventObject(ABC):
    """
    specifies the base for all event objects and identifies the source of the event.

    See Also:
        `API EventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1lang_1_1EventObject.html>`_
    """
    @abstractmethod
    def Source(self) -> 'XInterface':
        """
        refers to the object that fired the event.

        Returns:
            XInterface: interface
        """
