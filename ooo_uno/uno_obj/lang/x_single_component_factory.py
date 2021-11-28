# coding: utf-8
from abc import abstractmethod
from typing import Any, Iterable, TYPE_CHECKING
from ..uno.x_interface import XInterface
if TYPE_CHECKING:
    from ..uno.x_component_context import XComponentContext


class XSingleComponentFactory(XInterface):
    """
    Factory interface to create instances of an implementation of a service specification.

    See Also:
        `API XSingleComponentFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XSingleComponentFactory.html>`_
    """

    @abstractmethod
    def createInstanceWithArgumentsAndContext(self, Arguments: Iterable[Any], Context: 'XComponentContext') -> XInterface:
        """
        Creates an instance of a component and initializes the new instance with the given arguments and context.

        Args:
            Arguments (Iterable[Any]): arguments passed to implementation
            Context (XComponentContext): the instance gets its deployment values from this

        Returns:
            XInterface: [description]
        """

    @abstractmethod
    def createInstanceWithContext(self, Context: 'XComponentContext') -> XInterface:
        """
        Creates an instance of a service implementation.

        Args:
            Context (XComponentContext): the instance gets its deployment values from this

        Returns:
            XInterface: component instance
        """
