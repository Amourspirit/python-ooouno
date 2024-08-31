from __future__ import annotations
from typing import Any
import uno

from com.sun.star.reflection import XTypeDescription


class TypeDescriptionPartial:
    """
    Partial class for XTypeDescription.
    """

    def __init__(
        self,
        component: XTypeDescription,
        interface: Any = XTypeDescription,
    ) -> None:
        """
        Constructor

        Args:
            component (XTypeDescription): UNO Component that implements ``com.sun.star.reflection.XTypeDescription`` interface.
            interface (Any, optional): The interface to be validated. Defaults to ``XTypeDescription``.
        """
        self.__component = component

    # region XTypeDescription
    def get_name(self) -> str:
        """
        Returns the fully qualified name of the UNOIDL entity.
        """
        return self.__component.getName()

    def get_type_class(self) -> Any:
        """
        Returns the type class of the reflected UNOIDL entity.

        Returns:
            TypeClass: The type class of the reflected UNOIDL entity.
        """
        return self.__component.getTypeClass()  # type: ignore

    # endregion XTypeDescription