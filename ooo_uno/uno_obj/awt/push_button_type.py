# coding: utf-8
from typing import TYPE_CHECKING
from enum import Enum
from ...env import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    # PushButtonType is string enum
    from com.sun.star.awt.PushButtonType import STANDARD, OK, CANCEL, HELP


class PushButtonType(str, Enum):
    """
    specifies the default actions of a button.

    See Also:
        `API PushButtonType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa4e49c7e6c5bf2b4d010ad4a50b90ec0>`_
    """
    STANDARD = 'STANDARD'
    """acts like a standard push button."""
    OK = 'OK'
    """acts like an OK button."""
    CANCEL = 'CANCEL'
    """acts like a cancel button."""
    HELP = 'HELP'
    """acts like a help button."""

    def __str__(self) -> str:
        return str(self._value_)


def _dynamic_enum():
    '''
    Dynamically add Enum names and value for enum

    It is possible that enum values could change, therefore dynamically create enum
    '''
    global PushButtonType
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
        PushButtonType = Enum('PushButtonType', {
            "STANDARD": STANDARD.value,
            "OK": OK.value,
            "CANCEL": CANCEL.value,
            "HELP": HELP.value
        })
        PushButtonType.__str__ = lambda self: self._value_


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['PushButtonType']
