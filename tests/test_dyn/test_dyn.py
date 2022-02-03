# coding: utf-8
import pytest

if __name__ == "__main__":
    pytest.main([__file__])


def test_service():
    from ooo_uno.dyn.accessibility.accessible_context import AccessibleContext
    assert type(AccessibleContext).__name__ == 'ABCMeta'


def test_struct():
    from ooo_uno.dyn.accessibility.accessible_event_object import AccessibleEventObject
    ev = AccessibleEventObject(EventId=2, NewValue=4, OldValue=3)
    assert ev.EventId == 2
    assert ev.NewValue == 4
    assert ev.OldValue == 3
    assert AccessibleEventObject.__qualname__ == '_dynamic_struct.<locals>._struct_init'

def test_enum():
    from ooo_uno.dyn.awt.font_slant import FontSlant
    a = FontSlant.ITALIC
    b = FontSlant.ITALIC
    assert a == b

def test_interface():
    from ooo_uno.dyn.accessibility.x_accessible_action import XAccessibleAction
    assert XAccessibleAction.__pyunointerface__ == 'com.sun.star.accessibility.XAccessibleAction'


def test_exception():
    from ooo_uno.dyn.uno.exception import Exception
    ex = Exception()
    ex.Message = "Hello World"
    assert ex.Message == 'Hello World'
    assert Exception.__pyunointerface__ == 'com.sun.star.uno.Exception'

def test_exception_oth():
    from ooo_uno.dyn.accessibility.illegal_accessible_component_state_exception import IllegalAccessibleComponentStateException
    ex = IllegalAccessibleComponentStateException()
    assert IllegalAccessibleComponentStateException.__pyunointerface__ == 'com.sun.star.accessibility.IllegalAccessibleComponentStateException'


def test_exception_prop():
    from ooo_uno.dyn.configuration.backend.malformed_data_exception import MalformedDataException
    ex = MalformedDataException()
    ex.ErrorDetails = 'ERROR DETALL'
    assert ex.ErrorDetails == 'ERROR DETALL'
def test_singleton():
    from ooo_uno.dyn.beans.the_introspection import theIntrospection as theIntrospection
    singleton = theIntrospection()
    assert type(singleton).__name__ == 'pyuno'
