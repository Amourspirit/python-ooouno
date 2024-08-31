from __future__ import annotations
from typing import Any
from abc import ABC

import uno  # pylint: disable=unused-import
from ..ex import NotSupportedServiceError

# https://github.com/Amourspirit/python_ooo_dev_tools/blob/e17ca074f19980b021631c949e816f956d12441b/ooodev/adapter/component_base.py


class ComponentBase(ABC):
    """
    Base Class for Components in the ``component`` name space.
    """

    def __init__(self, component: Any) -> None:
        self.__set_component(component)

    def __set_component(self, component: Any) -> None:
        """
        Sets the component.

        Args:
            component (Any): UNO Object

        Raises:
            NotSupportedServiceError: If the component does not support the required service.
        """
        if not self.__get_is_supported(component):
            services = self.__get_supported_service_names()
            if services:
                raise NotSupportedServiceError(*services)
            else:
                raise NotSupportedServiceError("No service name specified.")
        self.__component = component

    def __get_component(self) -> Any:
        return self.__component

    def __get_supported_service_names(self) -> tuple[str, ...]:
        """Returns a tuple of supported service names."""
        return ()

    def __get_is_supported(self, component: Any) -> bool:
        """
        Gets whether the component supports a service.

        Args:
            component (component): UNO Object

        Returns:
            bool: True if the component supports the service, otherwise False.
        """

        if component is None:
            return False
        srv_name = self.__get_supported_service_names()
        if not srv_name:
            return True
        # return mInfo.Info.support_service(component, *srv_name)

        result = False
        try:
            if not hasattr(component, "supportsService"):
                return False

            for srv in srv_name:
                result = component.supportsService(srv)  # type: ignore
                if result:
                    break
        except Exception:
            # mLo.Lo.print("Errors ocurred in support_service(). Returning False")
            # mLo.Lo.print(f"    {e}")
            pass
        return result
