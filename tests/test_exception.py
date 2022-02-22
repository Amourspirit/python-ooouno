# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])

def test_raise_uno_ex():
    import uno
    from ooo.dyn.uno.exception import Exception as EX
    UnoEx = uno.getClass("com.sun.star.uno.Exception")
    assert (True if EX is UnoEx else False)
    is_uno_ex = False
    try:
        raise EX
    except EX:
        is_uno_ex = True
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        raise EX('Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        raise EX(Message='Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        raise UnoEx(Message='Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True

    with pytest.raises(EX):
        raise UnoEx(Message='Hello World')

def test_raise_uno_runtime_ex():
    import uno
    from ooo.dyn.uno.runtime_exception import RuntimeException as EX
    UnoEx = uno.getClass("com.sun.star.uno.RuntimeException")
    assert (True if EX is UnoEx else False)
    is_uno_ex = False
    try:
        raise EX
    except EX:
        is_uno_ex = True
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        raise EX(Message='Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        err = EX()
        err.Message = "I am in error"
        raise err
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'I am in error'
    assert is_uno_ex == True
    is_uno_ex = False
    try:
        raise UnoEx(Message='Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True

    with pytest.raises(EX):
        raise UnoEx(Message='Hello World')