# coding: utf-8
from __future__ import annotations
from typing import Any
import uno
from enum import Enum, EnumMeta, _EnumDict


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
        cls.__ooo_enum_name__: str = cls.__get_enum_name()
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
                # the only way to set attribute is to call super
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
            # the only way to set attribute is to call super
            super().__setattr__(key, value)  # Transparent access.

    def __get_enum_name(cls) -> str:
        return cls.__ooo_full_ns__.rsplit(sep=".", maxsplit=1)[1]


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
        def set_enum_values(name: str, ns: str, dic: _EnumDict) -> None:
            m_obj = __import__(name=ns, fromlist=[name])
            const = getattr(m_obj, name)
            attrs = [a for a in dir(const) if not a.startswith('__')]
            for attr in attrs:
                val = getattr(const, attr, None)
                if val is not None:
                    dic[attr] = val

        type_name: str = kwds["type_name"]
        name_space: str = kwds["name_space"]
        enum_name = type_name.rsplit(sep=".", maxsplit=1)[1]
        set_enum_values(enum_name, name_space, classdict)
        return super().__new__(metacls, cls, bases, classdict)

    def __init__(cls, name, bases, namespace, **kwds):
        super().__init__(name, bases, namespace)
        type_name = kwds["type_name"]
        name_space = kwds["name_space"]
        cls.__ooo_full_ns__: str = type_name
        cls.__ooo_ns__: str = name_space
        cls.__ooo_name__: str = cls.__get_enum_name()
        cls.__ooo_enum_name__: str = cls.__ooo_name__ + "Enum"
        cls._initialized = True

    def __call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1):
        if isinstance(value, str) and value != cls.__ooo_enum_name__:
            return cls.__get_enum_from_str(value)
        return super().__call__(value=value, names=names, module=module, qualname=qualname, type=type, start=start)

    def __get_enum_name(cls) -> str:
        return cls.__ooo_full_ns__.rsplit(sep=".", maxsplit=1)[1]

    def __get_enum_from_str(cls, value: str) -> Enum:
        if not value:
            return None
        val = getattr(cls, value, None)
        return val

    def __setattr__(cls, key, value):
        if cls._initialized:
            pass
        else:
            # metaclass __dict__ is a mappingproxy
            # the only way to set attribute is to call super
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
                # the only way to set attribute is to call super
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
            # the only way to set attribute is to call super
            super().__setattr__(key, value)  # Transparent access.
