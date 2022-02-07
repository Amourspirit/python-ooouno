# coding: utf-8
import pytest

if __name__ == "__main__":
    pytest.main([__file__])


def test_service():
    from ooo.dyn.accessibility.accessible_context import AccessibleContext
    assert type(AccessibleContext).__name__ == 'ABCMeta'
    assert AccessibleContext.__ooo_full_ns__ == 'com.sun.star.accessibility.AccessibleContext'


def test_struct():
    from ooo.dyn.accessibility.accessible_event_object import AccessibleEventObject
    ev = AccessibleEventObject(EventId=2, NewValue=4, OldValue=3)
    assert ev.EventId == 2
    assert ev.NewValue == 4
    assert ev.OldValue == 3
    assert AccessibleEventObject.__qualname__ == '_dynamic_struct.<locals>._struct_init'


def test_enum():
    from ooo.dyn.awt.font_slant import FontSlant
    a = FontSlant.ITALIC
    b = FontSlant.ITALIC
    assert a == b
    insta = FontSlant(FontSlant.ITALIC)
    assert insta == b
    instb = FontSlant('ITALIC')
    assert insta == instb

def test_uno_obj_enum():
    from ooo.lo.awt.font_slant import FontSlant
    a = FontSlant.ITALIC
    b = FontSlant.ITALIC
    assert a == b
    insta = FontSlant(FontSlant.ITALIC)
    assert insta == b
    instb = FontSlant('ITALIC')
    assert insta == instb

def test_interface():
    from ooo.dyn.accessibility.x_accessible_action import XAccessibleAction
    assert XAccessibleAction.__pyunointerface__ == 'com.sun.star.accessibility.XAccessibleAction'


def test_exception():
    from ooo.dyn.uno.exception import Exception
    ex = Exception()
    ex.Message = "Hello World"
    assert ex.Message == 'Hello World'
    assert Exception.typeName == 'com.sun.star.uno.Exception'
    assert ex.__pyunointerface__ == Exception.typeName
    assert ex.__pyunostruct__ == Exception.typeName
    


def test_exception_oth():
    from ooo.dyn.accessibility.illegal_accessible_component_state_exception import IllegalAccessibleComponentStateException
    ex = IllegalAccessibleComponentStateException()
    assert IllegalAccessibleComponentStateException.__pyunointerface__ == 'com.sun.star.accessibility.IllegalAccessibleComponentStateException'


def test_exception_prop():
    from ooo.dyn.configuration.backend.malformed_data_exception import MalformedDataException
    ex = MalformedDataException()
    ex.ErrorDetails = 'ERROR DETALL'
    assert ex.ErrorDetails == 'ERROR DETALL'


def test_singleton():
    from ooo.dyn.beans.the_introspection import theIntrospection as theIntrospection
    singleton = theIntrospection()
    assert type(singleton).__name__ == 'pyuno'

def test_rectangle():
    # https://github.com/hanya/pyuno3/blob/master/test/test.py
    import uno
    from ooo.dyn.awt.rectangle import Rectangle
    from com.sun.star.awt import Rectangle as URectangle
    rect1 = Rectangle()
    assert rect1.typeName == 'com.sun.star.awt.Rectangle'
    assert isinstance(rect1, URectangle)
    rect2 = Rectangle(X=100, Y=200, Width=50, Height=1)
    assert isinstance(rect2, URectangle)
    assert rect2.X == 100
    rect3 = uno.createUnoStruct("com.sun.star.awt.Rectangle", rect2)
    assert rect3.X == 100
    rect4 = Rectangle(rect2)
    assert rect4.X == 100

def test_uno_obj_rectangle():
    from ooo.lo.awt.rectangle import Rectangle
    rect1 = Rectangle()
    assert rect1.typeName == 'com.sun.star.awt.Rectangle'
    assert isinstance(rect1, Rectangle)
    rect2 = Rectangle(100, 200, 50, 1)
    assert rect2.X == 100
    rect3 = Rectangle(rect2)
    assert rect3.X == 100

