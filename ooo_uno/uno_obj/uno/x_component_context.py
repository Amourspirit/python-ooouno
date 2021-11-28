# coding: utf-8
from typing import TYPE_CHECKING

from abc import abstractmethod
from typing import Any
# from com.sun.star.lang import XEventListener
if TYPE_CHECKING:
    from ..lang.x_multi_component_factory import XMultiComponentFactory
    # https://stackoverflow.com/questions/70117038/getting-circular-import-while-trying-hinting-python
    # Note that it is important to wrap Type in quotes when importing this way.
    # This solves circular refrences at runtime as TYPE_CHECKING is always False at runtime
from .x_interface import XInterface


class XComponentContext(XInterface):
    """
    Component context to be passed to a component via com.sun.star.lang.XSingleComponentFactory.
    
    See Also:
        `API XComponentContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XComponentContext.html>`_
    """

    @abstractmethod
    def getServiceManager() -> 'XMultiComponentFactory':
        """
        Gets the service manager instance to be used from key /singletons/com.sun.star.lang.theServiceManager.

        This method has been added for convenience, because the service manager is used very often.

        Returns:
            XMultiComponentFactory: service manager
        """

    @abstractmethod
    def getValueByName(Name: str) -> Any:
        """
        Gets a value from the context.

        Args:
            Name (str): name of value

        Returns:
            Any: [description]value
        """
