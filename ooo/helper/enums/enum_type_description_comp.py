from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum, EnumMeta
import uno
from ..component.component_prop import ComponentProp
from .enum_type_description_partial import EnumTypeDescriptionPartial

if TYPE_CHECKING:
    from com.sun.star.reflection import XEnumTypeDescription

class EnumMetaType(EnumMeta):
    """
    Metaclass for EnumTypeDescriptionComp.

    This metaclass is used to create a dynamic enum from the enum names and values.
    """

    # def __new__(mcs, name, bases, namespace, **kwargs):
    #     """
    #     Creates a new Enum class.

    #     Args:
    #         name (str): The name of the class.
    #         bases (tuple): The base classes.
    #         namespace (dict): The class namespace.
    #         **kwargs: Additional keyword arguments.

    #     Returns:
    #         Enum: The new Enum class.
    #     """
    #     if "EnumTypeDescriptionComp" in namespace:
    #         enum_info = namespace["EnumTypeDescriptionComp"]
    #         if isinstance(enum_info, EnumTypeDescriptionComp):
    #             enum_info = cast(EnumTypeDescriptionComp, enum_info)
    #             namespace["EnumTypeDescriptionComp"] = enum_info.create_dynamic_enum(name)
    #     return super().__new__(mcs, name, bases, namespace, **kwargs)
    
    def __instancecheck__(cls, inst):
        """Implement isinstance(inst, cls)."""
        return any(cls.__subclasscheck__(c)
                   for c in {type(inst), inst.__class__})

    def __subclasscheck__(cls, sub):
        """Implement issubclass(sub, cls)."""
        candidates = cls.__dict__.get("__subclass__", set()) | {cls}
        return any(c in candidates for c in sub.mro())

class DynamicEnum(Enum, metaclass=EnumMetaType):
    """
    Base class for dynamic
    """
    pass

class EnumTypeDescriptionComp(ComponentProp, EnumTypeDescriptionPartial):
    """
    Class for managing XEnumTypeDescription.
    """

    # pylint: disable=unused-argument

    def __init__(self, component: XEnumTypeDescription) -> None:
        """
        Constructor

        Args:
            component (XEnumTypeDescription): UNO Component that implements ``com.sun.star.reflection.XEnumTypeDescription`` interface.
        """
        ComponentProp.__init__(self, component)
        EnumTypeDescriptionPartial.__init__(self, component=component)

    # region Overrides
    def _ComponentBase__get_supported_service_names(self) -> tuple[str, ...]:
        """Returns a tuple of supported service names."""
        # validated by TypeDescriptionEnumerationPartial
        return ()

    # endregion Overrides

    def get_name_value_dict(self) -> dict[str, int]:
        """
        Returns the enum member names and values as a dictionary.
        """
        names = self.get_enum_names()
        values = self.get_enum_values()
        return dict(zip(names, values))

    def get_value_name_dict(self) -> dict[int, str]:
        """
        Returns the enum member values and names as a dictionary.
        """
        names = self.get_enum_names()
        values = self.get_enum_values()
        return dict(zip(values, names))

    def get_name_from_value(self, value: int) -> str:
        """
        Returns the enum member name from the value.

        Args:
            value (int): The enum member value.

        Returns:
            str: The enum member name, or an empty string if not found.
        """
        vn = self.get_value_name_dict()
        return vn[value] if value in vn else ""

    def create_dynamic_enum(self, name: str) -> Enum:
        """
        Returns a dynamic python enum from the current enum names and values.

        Args:
            name (str): The name of the dynamic enum.

        Returns:
            Enum: The dynamic python enum.

        Example:
            This example is when the enum is info is for ``com.sun.star.awt.FontSlant``.
            Any valid code name can be used for the dynamic enum.

            .. code-block:: python

                >>> my_enum = info.create_dynamic_enum("com.sun.star.awt.FontSlant")
                >>> print(my_enum)
                <enum 'com.sun.star.awt.FontSlant'>
                >>> for e in my_enum:
                ...    print(e.name, e.value)
                NONE NONE
                OBLIQUE OBLIQUE
                ITALIC ITALIC
                DONTKNOW DONTKNOW
                REVERSE_OBLIQUE REVERSE_OBLIQUE
                REVERSE_ITALIC REVERSE_ITALIC

        """
        # names = self.get_enum_names()
        # enum_dict = dict(zip(names, names))
        # enum_dict["_member_names"] = names

        # # Create a new dynamic enum class
        # DynamicEnum = type(name, (Enum,), enum_dict)

        # # Register the new dynamic enum class
        # DynamicEnum.register(uno.Enum)
        
        # return DynamicEnum

        names = self.get_enum_names()

        result = DynamicEnum(name, dict(zip(names, names)))
        # result.register(uno.Enum)
        return result

    def create_dynamic_name_value_enum(self, name: str) -> Enum:
        """
        Returns a dynamic python enum from the current enum names and values.

        Args:
            name (str): The name of the dynamic enum.

        Returns:
            Enum: The dynamic python enum.

        Example:
            This example is when the enum is info is for ``com.sun.star.awt.FontSlant``.
            Any valid code name can be used for the dynamic enum.

            .. code-block:: python

                >>> my_enum = inst.create_dynamic_enum("com.sun.star.awt.FontSlant")
                >>> print(my_enum)
                <enum 'com.sun.star.awt.FontSlant'>
                >>> for e in my_enum:
                ...    print(e.name, e.value)
                NONE 0
                OBLIQUE 1
                ITALIC 2
                DONTKNOW 3
                REVERSE_OBLIQUE 4
                REVERSE_ITALIC 5
        """
        return DynamicEnum(name, self.get_name_value_dict())

    # region Properties
    @property
    def component(self) -> XEnumTypeDescription:
        """XEnumTypeDescription Component"""
        # pylint: disable=no-member
        return cast("XEnumTypeDescription", self._ComponentBase__get_component())  # type: ignore

    # endregion Properties
