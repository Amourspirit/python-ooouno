# coding: utf-8
from typing import TYPE_CHECKING
from abc import abstractmethod
from typing import Any, Iterable
from ..uno.x_interface import XInterface
if TYPE_CHECKING:
    from ..uno.x_component_context import XComponentContext

class XMultiComponentFactory(XInterface):
    """
    Factory interface for creating component instances giving a context from which to retrieve deployment values.

    See Also:
        `API XMultiComponentFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XMultiComponentFactory.html>`_
    """

    @abstractmethod
    def createInstanceWithArgumentsAndContext(self, ServiceSpecifier: str, Arguments: Iterable[Any], Context: 'XComponentContext') -> XInterface:
        """
        Creates an instance of a component which supports the services specified by the
        factory, and initializes the new instance with the given arguments and context.

        Args:
            ServiceSpecifier (str): service name
            Arguments (Iterable[Any]): arguments
            Context (Any): context the component instance gets its deployment values from

        Returns:
            object: component instance
        """

    @abstractmethod
    def createInstanceWithContext(self, aServiceSpecifier: str, Context: 'XComponentContext') -> XInterface:
        """
        Creates an instance of a component which supports the services specified by the factory.

        Args:
            aServiceSpecifier (str): service name
            Context (Any): 	context the component instance gets its deployment values from

        Returns:
            XInterface: component instance
        """

    @abstractmethod
    def getAvailableServiceNames(self) -> list:
        """
        Gets the names of all supported services.

        Returns:
            list: sequence of all service names
        """
