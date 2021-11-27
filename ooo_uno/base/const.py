# coding: utf-8
from inspect import getattr_static
from enum import IntEnum, IntFlag
from typing import Union


class ConstBase(object):
    """Base class for Constant classes"""
    @classmethod
    def _get_constants(cls) -> dict:
        return {name: value for (name, value) in vars(cls).items() if not name.startswith('_')}


class ConstIntBase(ConstBase):
    """Base class for Constant classes of which all values are enum"""

    @classmethod
    def _get_enum(cls, flags: bool = False) -> Union[IntFlag, IntEnum]:

        key = '_enum_cache'
        try:
            return getattr_static(cls, key)
        except AttributeError:
            d = cls._get_constants()
            name = cls.__name__ + "Enum"
            if not flags:
                e = IntEnum(name, d)
            else:
                e = IntFlag(name, d)
            e.__doc__ = cls.__doc__
            for n in d.keys():
                e.__dict__[n].__doc__ = cls.__dict__[n].__doc__
            setattr(cls, key, e)
        return e

    @classmethod
    def get_enum(cls) -> IntEnum:
        """
        Gets an ``IntEnum`` class from class constants.

        Returns:
            IntEnum: Enum

        Note:
            Enum name will be the class name + Enum

            All doc strings are copied to the enum as well.

            Result of get_enum are cached. This means that
            after the first call the same enum is always returned.
        """
        return cls._get_enum(flags=False)


class ConstIntFlagsBase(ConstIntBase):
    """Base class for Constant classes of which all values are enum"""

    @classmethod
    def get_enum(cls) -> IntFlag:
        """
        Gets an ``IntFlag`` class from class constants.

        Returns:
            IntFlag: Enum

        Note:
            Enum name will be the class name + Enum

            All doc strings are copied to the enum as well.

            Result of get_enum are cached. This means that
            after the first call the same enum is always returned.
        """
        return cls._get_enum(flags=True)
