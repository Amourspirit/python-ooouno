# coding: utf-8
from __future__ import annotations
from typing import Any
import sys
import uno
from enum import Enum, EnumMeta, _EnumDict

# coding: utf-8


def uno_enum_class_new(cls, value):
    """
    New (__new__) method for dynamically created uno.enum classes

    Args:
        value (object): Can be Uno.Enum, uno.Enum.value, str

    Raises:
        ValueError: if unable to match enum instance

    Returns:
        [uno.Enum]: Enum Instance

    Example:
        ..code-block:: python

            >>> e = HorizontalAlignment("RIGHT")
            >>> print(e.value)
            RIGHT
            >>> e = HorizontalAlignment(HorizontalAlignment.LEFT)
            >>> print(e.value)
            LEFT
            >>> e = HorizontalAlignment(HorizontalAlignment.CENTER.value)
            >>> print(e.value)
            CENTER
    """
    if isinstance(value, str):
        if hasattr(cls, value):
            return getattr(cls, value)
    _type = type(value)
    if _type is uno.Enum:
        return value
    if _type is cls:
        return value
    raise ValueError("%r is not a valid %s" % (value, cls.__name__))


def uno_enum_class_ne(self, other):
    return not self.__eq__(other)


class UnoEnumMeta(type):
    """
    Get access to Uno Enum values without having to directly import them.

    This is a meta class.

    Example:

        .. code-block:: python

            class FillMode(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FillMode", name_space="com.sun.star.sheet"):
                pass

    Note:
        Uno enums can not be imported directly in python.

        ``from com.sun.star.sheet import FillMode`` is not a valid import
        and results in an import error.

        ``from com.sun.star.sheet.FillMode import LINEAR, SIMPLE, GROWTH`` is valid import but cumbersome.

        This metaclass use a just in time approach. If the enum is not yet an attribute it is automatiacally added dynamically.
        All subsequent calls automatically use the dynamically added attribute.
    """
    _initialized = False  # This class var is important. It is always False.
    # The instances will override this with their own,
    # set to True.
    typeName = None
    __ooo_type_name__ = "enum"
    __ooo_full_ns__ = None
    __ooo_ns__ = None

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __new__(metacls, name, bases, namespace, **kwargs):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, type_name, name_space, **kwargs):
        super().__init__(name, bases, namespace)
        cls.typeName = type_name
        cls.__ooo_full_ns__ = type_name
        cls.__ooo_ns__ = name_space
        cls._initialized = True

    def __call__(cls, value) -> uno.Enum:
        """
        New (__new__) method for dynamically created uno.enum classes

        Args:
            value (object): Can be Uno.Enum, uno.Enum.value, str

        Raises:
            TypeError: if unable to match enum instance

        Returns:
            [uno.Enum]: Enum Instance

        Example:
            ..code-block:: python

                >>> e = HorizontalAlignment("RIGHT")
                >>> print(e.value)
                RIGHT
                >>> e = HorizontalAlignment(HorizontalAlignment.LEFT)
                >>> print(e.value)
                LEFT
                >>> e = HorizontalAlignment(HorizontalAlignment.CENTER.value)
                >>> print(e.value)
                CENTER
        """
        if isinstance(value, str):
            if hasattr(cls, value):
                return getattr(cls, value)
        _type = type(value)
        if _type is uno.Enum:
            return value
        if _type is cls:
            return value
        raise TypeError("%r is not a valid %s" % (value, cls.__name__))

    def __getattr__(cls, __name: str) -> uno.Enum | Any:
        if cls._initialized:
            # Provide the caller attributes in whatever ways interest you.
            try:
                key = __name
                e = uno.Enum(cls.typeName, __name)
                # metaclass __dict__ is a mappingproxy
                # the only way to set attribue is to call super
                super().__setattr__(key, e)
                return cls.__dict__[key]
            except Exception:
                raise AttributeError(
                    f"Enum {cls.typeName} has no attribute {__name}")
        else:
            try:
                # Transparent access to instance vars.
                return cls.__dict__[__name]
            except KeyError:
                raise AttributeError(__name)

    def __setattr__(cls, key, value):
        if cls._initialized:
            pass
        else:
            # metaclass __dict__ is a mappingproxy
            # the only way to set attribue is to call super
            super().__setattr__(key, value)  # Transparent access.


class ConstEnumMeta(EnumMeta):
    """
    Dynamic Enum for Constants

    Enums that use this metaclass will automatically look up const values from uno and assign enums on the fly.

    :example:
        .. code-block:: python

            class AccessibleRelationTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.accessibility.AccessibleRelationType", name_space="com.sun.star.accessibility"):
                pass

            # INVALID is lookup up automatically and added to enum
            assert AccessibleRelationTypeEnum.INVALID.value == 0

    """
    _initialized = False  # This class var is important. It is always False.
    # The instances will override this with their own,
    # set to True.
    __ooo_type_name__ = "const"
    __ooo_full_ns__ = None
    __ooo_ns__ = None

    @classmethod
    def __prepare__(metacls, cls, bases, **kwds):
        return super().__prepare__(cls, bases)

    def __new__(metacls, cls, bases, classdict, **kwds):
        return super().__new__(metacls, cls, bases, classdict)

    def __init__(cls, name, bases, namespace, **kwds):
        super().__init__(name, bases, namespace)
        type_name = kwds["type_name"]
        name_space = kwds["name_space"]
        cls.__ooo_full_ns__ = type_name
        cls.__ooo_ns__ = name_space
        cls._initialized = True

    def __getattr__(cls, name: str) -> uno.Enum | Any:
        if cls._initialized:
            # Provide the caller attributes in whatever ways interest you.
            try:
                if name.startswith('_'):
                    try:
                        super().__setattr__("_initialized", False)
                        return super().__getattr__(name)
                    finally:
                        super().__setattr__("_initialized", True)
                member = cls._member_map_.get(name, None)
                if member is None:
                    try:
                        super().__setattr__("_initialized", False)
                        member = cls._create_const_member_(name)
                    finally:
                        super().__setattr__("_initialized", True)
                return member
            except Exception as e:
                raise AttributeError(
                    f"Enum {cls.__ooo_full_ns__} has no attribute {name}") from e
        else:
            try:
                # Transparent access to instance vars.
                return super().__getattr__(name)
            except KeyError:
                raise AttributeError(name)

    def _create_const_member_(cls, name):
        const = uno.getConstantByName(f"{cls.__ooo_full_ns__}.{name}")
        sup = super(cls)

        # new_enum = sup.__thisclass__(
        #     sup.__thisclass__.__name__, [(name, const)])
        enum_dict = _EnumDict()
        enum_dict._cls_name = cls.__name__
        enum_dict['_generate_next_value_'] = None
        enum_dict[name] = const
        new_enum = cls(
            sup.__thisclass__.__name__, enum_dict)
        new_member: Enum = getattr(new_enum, name)
        # assigning new_member.__classs__ is essential.
        # Otherwise it will point to the enum in memory just created.
        # this would lead to other issues as each enum value depends on
        # having the same class for Flags and other operations.
        setattr(new_member, "__class__", cls)
        cls._value2member_map_[new_member.value] = new_member
        cls._member_map_[new_member.name] = new_member

        cls._member_names_.append(new_member.name)
        return cls._member_map_[new_member.name]

    if sys.version_info < (3, 8, 0):
        @staticmethod
        def _get_mixins_(bases):
            """Returns the type for creating enum members, and the first inherited
            enum class.

            bases: the tuple of bases that was given to __new__

            """
            if not bases:
                return object, Enum

            def _find_data_type(bases):
                for chain in bases:
                    for base in chain.__mro__:
                        if base is object:
                            continue
                        elif '__new__' in base.__dict__:
                            if issubclass(base, Enum):
                                continue
                            return base

            # ensure final parent class is an Enum derivative, find any concrete
            # data type, and check that Enum has no members
            first_enum = bases[-1]
            if not issubclass(first_enum, Enum):
                raise TypeError("new enumerations should be created as "
                                "`EnumName([mixin_type, ...] [data_type,] enum_type)`")
            member_type = _find_data_type(bases) or object
            return member_type, first_enum

    else:
        @staticmethod
        def _get_mixins_(class_name, bases):
            """
            Returns the type for creating enum members, and the first inherited
            enum class.

            bases: the tuple of bases that was given to __new__
            """
            if not bases:
                return object, Enum

            def _find_data_type(bases):
                data_types = set()
                for chain in bases:
                    candidate = None
                    for base in chain.__mro__:
                        if base is object:
                            continue
                        elif issubclass(base, Enum):
                            if base._member_type_ is not object:
                                data_types.add(base._member_type_)
                                break
                        elif '__new__' in base.__dict__:
                            if issubclass(base, Enum):
                                continue
                            data_types.add(candidate or base)
                            break
                        else:
                            candidate = candidate or base
                if len(data_types) > 1:
                    raise TypeError('%r: too many data types: %r' %
                                    (class_name, data_types))
                elif data_types:
                    return data_types.pop()
                else:
                    return None

            # ensure final parent class is an Enum derivative, find any concrete
            # data type, and check that Enum has no members
            first_enum = bases[-1]
            if not issubclass(first_enum, Enum):
                raise TypeError("new enumerations should be created as "
                                "`EnumName([mixin_type, ...] [data_type,] enum_type)`")
            member_type = _find_data_type(bases) or object
            return member_type, first_enum

    @classmethod
    def _check_for_existing_members(cls, class_name, bases):
        if cls._initialized is False:
            return
        for chain in bases:
            for base in chain.__mro__:
                if issubclass(base, Enum) and base._member_names_:
                    raise TypeError(
                        "%s: cannot extend enumeration %r"
                        % (class_name, base.__name__)
                    )

    def __setattr__(cls, key, value):
        if cls._initialized:
            pass
        else:
            # metaclass __dict__ is a mappingproxy
            # the only way to set attribue is to call super
            super().__setattr__(key, value)  # Transparent access.


class UnoConstMeta(type):
    """
    Get access to Uno Enum values without having to directly import them.

    This is a meta class.

    Example:

        .. code-block:: python

            class FillMode(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FillMode", name_space="com.sun.star.sheet"):
                pass

    Note:
        Uno enums can not be imported directly in python.

        ``from com.sun.star.sheet import FillMode`` is not a valid import
        and results in an import error.

        ``from com.sun.star.sheet.FillMode import LINEAR, SIMPLE, GROWTH`` is valid import but cumbersome.

        This metaclass use a just in time approach. If the enum is not yet an attribute it is automatiacally added dynamically.
        All subsequent calls automatically use the dynamically added attribute.
    """
    _initialized = False  # This class var is important. It is always False.
    # The instances will override this with their own,
    # set to True.
    __ooo_type_name__ = "const"
    __ooo_full_ns__ = None
    __ooo_ns__ = None

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __new__(metacls, name, bases, namespace, **kwargs):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, type_name, name_space, **kwargs):
        super().__init__(name, bases, namespace)
        cls.__ooo_full_ns__ = type_name
        cls.__ooo_ns__ = name_space
        cls._initialized = True

    def __getattr__(cls, name: str) -> uno.Enum | Any:
        if cls._initialized:
            # Provide the caller attributes in whatever ways interest you.
            try:
                const = uno.getConstantByName(f"{cls.__ooo_full_ns__}.{name}")
                # metaclass __dict__ is a mappingproxy
                # the only way to set attribue is to call super
                super().__setattr__(name, const)
                return cls.__dict__[name]
            except Exception:
                raise AttributeError(
                    f"Enum {cls.__ooo_full_ns__} has no attribute {name}")
        else:
            try:
                # Transparent access to instance vars.
                return cls.__dict__[name]
            except KeyError:
                raise AttributeError(name)

    def __setattr__(cls, key, value):
        if cls._initialized:
            pass
        else:
            # metaclass __dict__ is a mappingproxy
            # the only way to set attribue is to call super
            super().__setattr__(key, value)  # Transparent access.
