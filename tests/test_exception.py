# coding: utf-8
import pytest
if __name__ == "__main__":
    pytest.main([__file__])

def test_raise_uno_ex():
    import uno
    from ooo.dyn.uno.exception import Exception as EX
    UnoEx = uno.getClass("com.sun.star.uno.Exception")
    from com.sun.star.uno import Exception as UnoException
    assert (True if EX is UnoEx else False)
    assert (True if EX is UnoException else False)
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

    is_uno_ex = False
    try:
        err = EX()
        err.Message = "Hello World"
        raise err
    except EX as e:
        assert e.Message == 'Hello World'
        is_uno_ex = True
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
        x = EX('Hello World')
        raise x
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
    is_uno_ex = False
    try:
        raise UnoEx('Hello World')
    except EX as e:
        is_uno_ex = True
        assert e.Message == 'Hello World'
    assert is_uno_ex == True

    with pytest.raises(EX):
        raise UnoEx(Message='Hello World')

def test_no_connect_exception():
    import uno
    from ooo.dyn.connection.no_connect_exception import NoConnectException as EX
    from com.sun.star.connection import NoConnectException as UnoEx
    try:
        err = EX(Message='No Connect')
        raise err
    except EX as e:
        assert e.Message == 'No Connect'
    
    try:
        err = EX('No Connect', None)
        raise err
    except EX as e:
        assert e.Message == 'No Connect'

    with pytest.raises(EX):
        raise UnoEx(Message='Hello World')

def test_classified_interaction_request():
    from ooo.dyn.task.interaction_classification import InteractionClassification as IcEnum
    from ooo.dyn.task.classified_interaction_request import ClassifiedInteractionRequest
    is_uno_ex = False
    try:
        raise ClassifiedInteractionRequest
    except ClassifiedInteractionRequest:
        is_uno_ex = True
    assert is_uno_ex == True
    
    is_uno_ex = False
    try:
        err = ClassifiedInteractionRequest()
        raise err
    except ClassifiedInteractionRequest as e:
        is_uno_ex = True
        assert e.Classification == IcEnum.ERROR
    assert is_uno_ex == True
    
    is_uno_ex = False
    try:
        err = ClassifiedInteractionRequest(Classification=IcEnum.INFO)
        err.Message = 'Classified Error'
        raise err
    except ClassifiedInteractionRequest as e:
        is_uno_ex = True
        assert e.Message == 'Classified Error'
        assert e.Classification == IcEnum.INFO
    assert is_uno_ex == True
    
    is_uno_ex = False
    try:
        err = ClassifiedInteractionRequest(Classification=IcEnum.INFO, Message='Classified Error')
        raise err
    except ClassifiedInteractionRequest as e:
        is_uno_ex = True
        assert e.Message == 'Classified Error'
        assert e.Classification == IcEnum.INFO
    assert is_uno_ex == True
    
    is_uno_ex = False
    try:
        err = ClassifiedInteractionRequest(Message='Classified Error', Classification=IcEnum.WARNING)
        raise err
    except ClassifiedInteractionRequest as e:
        is_uno_ex = True
        assert e.Message == 'Classified Error'
        assert e.Classification == IcEnum.WARNING
    assert is_uno_ex == True
    
    is_uno_ex = False
    try:
        err = ClassifiedInteractionRequest('Classified Error', None, IcEnum.INFO)
        raise err
    except ClassifiedInteractionRequest as e:
        is_uno_ex = True
        assert e.Message == 'Classified Error'
        assert e.Classification == IcEnum.INFO
    assert is_uno_ex == True