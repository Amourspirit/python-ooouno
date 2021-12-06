# coding: utf-8
import pytest
from typing import TYPE_CHECKING
from enum import Enum
import uno
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))

import ooo_uno.oenv as env

if (not TYPE_CHECKING) and env.UNO_ENVIRONMENT:
    # PushButtonType is string enum
    from com.sun.star.awt.PushButtonType import STANDARD, OK, CANCEL, HELP


def test_enum_no_uno(monkeypatch):

    monkeypatch.setattr(env, 'UNO_ENVIRONMENT', False)

    class PushButtonTypeCls(str, Enum):
        STANDARD = '__standard'
        OK = '__ok'
        CANCEL = '__cancel'
        HELP = '__help'

        def __str__(self) -> str:
            return str(self._value_)
    PushButtonType = PushButtonTypeCls

    def _set_push_button_type():
        '''
        Dynamically add Enum names and value for enum
        '''
        nonlocal PushButtonType
        # if statment is to stop VS Code from reporting errors
        if (not TYPE_CHECKING) and env.UNO_ENVIRONMENT:
            PushButtonType = Enum('PushButtonType', {
                "STANDARD": STANDARD.value,
                "OK": OK.value,
                "CANCEL": CANCEL.value,
                "HELP": HELP.value
            })
            PushButtonType.__str__ = lambda self: self._value_

    if env.UNO_ENVIRONMENT:
        _set_push_button_type()
    assert str(PushButtonType.STANDARD) == '__standard'
    assert str(PushButtonType.OK) == '__ok'
    assert str(PushButtonType.CANCEL) == '__cancel'
    assert str(PushButtonType.HELP) == '__help'


def test_enum_uno():
    # does not need fixtures in this case
    class PushButtonTypeCls(str, Enum):
        STANDARD = '__standard'
        OK = '__ok'
        CANCEL = '__cancel'
        HELP = '__help'

        def __str__(self) -> str:
            return str(self._value_)
    PushButtonType = PushButtonTypeCls

    def _set_push_button_type():
        '''
        Dynamically add Enum names and value for enum
        '''
        nonlocal PushButtonType
        # if statment is to stop VS Code from reporting errors
        if (not TYPE_CHECKING) and env.UNO_ENVIRONMENT:
            PushButtonType = Enum('PushButtonType', {
                "STANDARD": STANDARD.value,
                "OK": OK.value,
                "CANCEL": CANCEL.value,
                "HELP": HELP.value
            })
            PushButtonType.__str__ = lambda self: self._value_

    if env.UNO_ENVIRONMENT:
        _set_push_button_type()
    assert str(PushButtonType.STANDARD) == STANDARD.value
    assert str(PushButtonType.OK) == OK.value
    assert str(PushButtonType.CANCEL) == CANCEL.value
    assert str(PushButtonType.HELP) == HELP.value


def test_enum_uno_cls():
    # does not need fixtures in this case
    class PushButtonTypeCls(str, Enum):
        STANDARD = '__standard'
        OK = '__ok'
        CANCEL = '__cancel'
        HELP = '__help'

        def __str__(self) -> str:
            return str(self._value_)
    PushButtonType = PushButtonTypeCls

    def _set_push_button_type():
        '''
        Dynamically add Enum names and value for enum
        '''
        nonlocal PushButtonType
        # constructor

        def constructor(self_, **kwargs):
            for k, v in kwargs.items():
                self_.__dict__[k] = v

        # if statment is to stop VS Code from reporting errors
        if (not TYPE_CHECKING) and env.UNO_ENVIRONMENT:
            _dict = {
                "STANDARD": STANDARD,
                "OK": OK,
                "CANCEL": CANCEL,
                "HELP": HELP
            }

            # creating class dynamically
            push_button_type = type("PushButtonType", (object, ), {
                # constructor
                "__init__": constructor,
            })
            PushButtonType = push_button_type(**_dict)
            # PushButtonType.__str__ = lambda self: self._value_

    if env.UNO_ENVIRONMENT:
        _set_push_button_type()
    assert PushButtonType.STANDARD == STANDARD
    assert PushButtonType.OK == OK
    assert PushButtonType.CANCEL == CANCEL
    assert PushButtonType.HELP == HELP


if __name__ == "__main__":
    pytest.main([__file__])
