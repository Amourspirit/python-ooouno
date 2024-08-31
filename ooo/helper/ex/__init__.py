from __future__ import annotations
from typing import Any

class NotSupportedError(Exception):
    """Generic Not Supported Error"""

    pass

class NotFoundError(Exception):
    """Generic Not Found Error"""

    pass


class NotSupportedServiceError(NotSupportedError):
    """
    Handles errors of service not being supported.
    """

    def __init__(self, service_name: str, *args: object) -> None:
        """
        NotSupportedServiceError Constructor

        Args:
            service_name (str): Service name
        """
        super().__init__(service_name, *args)

    def __str__(self) -> str:
        return repr(f"Service not supported: '{self.args[0]}'")


class MissingInterfaceError(NotFoundError):
    """Error when a interface is not found for a uno object"""

    def __init__(self, interface: Any, message: Any = None, *args) -> None:
        """
        MissingInterfaceError constructor

        Args:
            interface (Any): Missing Interface that caused error
            message (Any, optional): Message of error
        """
        if message is None:
            try:
                message = f"Missing interface {interface.__pyunointerface__}"
            except AttributeError:
                message = "Missing Uno Interface Error"
        super().__init__(interface, message, *args)

    def __str__(self) -> str:
        return repr(self.args[1])