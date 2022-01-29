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
    class PushButtonTypeCls(Enum):
        STANDARD = '__standard'
        OK = '__ok'
        CANCEL = '__cancel'
        HELP = '__help'

        def __str__(self) -> str:
            return str(self._value_)
    # PushButtonType = PushButtonTypeCls

    def _set_push_button_type():
        '''
        Dynamically add Enum names and value for enum
        '''
        nonlocal PushButtonTypeCls
        # constructor

        # if statment is to stop VS Code from reporting errors
        if (not TYPE_CHECKING) and env.UNO_ENVIRONMENT:
            def uno_enum_class_new(cls, value):
                if isinstance(value, str):
                    if hasattr(cls, value):
                        return getattr(cls, value)
                _type = type(value)
                if _type is uno.Enum:
                    return value
                if _type is cls:
                    return value
                raise ValueError("%r is not a valid %s" % (value, cls.__name__))


            _dict = {
                "STANDARD": STANDARD,
                "OK": OK,
                "CANCEL": CANCEL,
                "HELP": HELP
            }

            # creating class dynamically
            PushButtonTypeCls = type("PushButtonTypeCls", (object, ), {
                "__new__": uno_enum_class_new
            })
            for k, v in _dict.items():
                setattr(PushButtonTypeCls, k, v)

    if env.UNO_ENVIRONMENT:
        _set_push_button_type()
    
    assert PushButtonTypeCls.STANDARD == STANDARD
    assert PushButtonTypeCls.OK == OK
    assert PushButtonTypeCls.CANCEL == CANCEL
    assert PushButtonTypeCls.HELP == HELP
    p1 = PushButtonTypeCls.HELP
    p2 = PushButtonTypeCls.HELP
    assert p1 == p2
    assert p1.value == p2.value
    assert p1.__repr__() == "<Enum instance com.sun.star.awt.PushButtonType ('HELP')>"
    p1 = PushButtonTypeCls('HELP')
    assert p1 == p2




if __name__ == "__main__":
    pytest.main([__file__])
