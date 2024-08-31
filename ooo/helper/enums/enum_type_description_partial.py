from __future__ import annotations
from typing import Any, Tuple
import uno

from com.sun.star.reflection import XEnumTypeDescription

from .type_description_partial import TypeDescriptionPartial



class EnumTypeDescriptionPartial(TypeDescriptionPartial):
    """
    Partial class for XEnumTypeDescription.
    """

    def __init__(
        self,
        component: XEnumTypeDescription,
        interface: Any = XEnumTypeDescription,
    ) -> None:
        """
        Constructor

        Args:
            component (XEnumTypeDescription): UNO Component that implements ``com.sun.star.reflection.XEnumTypeDescription`` interface.
            interface (Any, optional): The interface to be validated. Defaults to ``XEnumTypeDescription``.
        """
        TypeDescriptionPartial.__init__(self, component=component, interface=interface)
        self.__component = component

    # region XEnumTypeDescription
    def get_default_enum_value(self) -> int:
        """
        Returns the default enum value.
        """
        return self.__component.getDefaultEnumValue()

    def get_enum_names(self) -> Tuple[str, ...]:
        """
        Returns the enum member values.
        """
        return self.__component.getEnumNames()

    def get_enum_values(self) -> Tuple[int, ...]:
        """
        Returns the enum member names.
        """
        return self.__component.getEnumValues()  # type: ignore

    # endregion XEnumTypeDescription