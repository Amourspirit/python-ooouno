# coding: utf-8
import pytest
if __name__ == "__main__":
    pytest.main([__file__])

from ooo.helper import uno_helper


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
    assert AccessibleEventObject.__qualname__ == 'com.sun.star.accessibility.AccessibleEventObject'


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
    assert XAccessibleAction.__ooo_ns__ == 'com.sun.star.accessibility'
    assert XAccessibleAction.__ooo_full_ns__ == 'com.sun.star.accessibility.XAccessibleAction'
    assert XAccessibleAction.__ooo_type_name__ == 'interface'


def test_exception_uno():
    from ooo.dyn.uno.exception import Exception
    ex = Exception()
    assert id(ex) != id(Exception)
    ex.Message = "Hello World"
    assert ex.Message == 'Hello World'
    assert Exception.typeName == 'com.sun.star.uno.Exception'
    assert ex.__pyunointerface__ == Exception.typeName
    assert ex.__pyunostruct__ == 'com.sun.star.uno.Exception'
    assert ex.__ooo_ns__ == 'com.sun.star.uno'
    assert ex.__ooo_full_ns__ == 'com.sun.star.uno.Exception'
    assert ex.__ooo_type_name__ == 'exception'
    assert type(ex).__name__ == 'com.sun.star.uno.Exception'
    assert ex.__module__ == 'uno'
    ex = Exception(Message="I made an error")
    assert ex.Message == 'I made an error'

def test_exception():
    from ooo.lo.uno.exception import Exception
    ex = Exception()
    assert id(ex) != id(Exception)
    ex.Message = "Hello World"
    assert ex.Message == 'Hello World'
    assert type(ex).__name__ == 'Exception'
    assert ex.__module__ == 'ooo.lo.uno.exception'
    


def test_exception_oth():
    from ooo.dyn.accessibility.illegal_accessible_component_state_exception import IllegalAccessibleComponentStateException
    ex = IllegalAccessibleComponentStateException()
    assert IllegalAccessibleComponentStateException.typeName == 'com.sun.star.accessibility.IllegalAccessibleComponentStateException'
    assert ex.__ooo_ns__ == 'com.sun.star.accessibility'
    assert ex.__ooo_full_ns__ == 'com.sun.star.accessibility.IllegalAccessibleComponentStateException'
    assert ex.__ooo_type_name__ == 'exception'


def test_exception_prop():
    from ooo.dyn.configuration.backend.malformed_data_exception import MalformedDataException
    ex = MalformedDataException()
    ex.ErrorDetails = 'ERROR DETALL'
    assert ex.ErrorDetails == 'ERROR DETALL'


def test_singleton():
    from ooo.dyn.beans.the_introspection import theIntrospection as theIntrospection
    from ooo.lo.beans.introspection import Introspection as LoIntrospection
    from ooo.dyn.beans.introspection import Introspection as DynIntrospection
    singleton = theIntrospection()
    assert type(singleton).__name__ == 'pyuno'
    im_name = "com.sun.star.comp.stoc.Introspection"
    assert singleton.getImplementationName() == im_name
    assert uno_helper.supports_service(singleton, 'com.sun.star.beans.Introspection')
    assert uno_helper.supports_service(singleton, LoIntrospection)
    assert uno_helper.supports_service(singleton, DynIntrospection)

def test_rectangle():
    # https://github.com/hanya/pyuno3/blob/master/test/test.py
    import uno
    from ooo.dyn.awt.rectangle import Rectangle
    assert Rectangle.typeName == 'com.sun.star.awt.Rectangle'
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

def test_property_value():
    from ooo.dyn.beans.property_value import PropertyValue
    p = PropertyValue(Name='MyProperty', Value=101)
    assert p.Name == 'MyProperty'
    assert p.Value == 101
    assert type(p).__name__ == 'com.sun.star.beans.PropertyValue'
    
def test_uno_obj_rectangle():
    from ooo.lo.awt.rectangle import Rectangle
    rect1 = Rectangle()
    assert rect1.typeName == 'com.sun.star.awt.Rectangle'
    assert isinstance(rect1, Rectangle)
    rect2 = Rectangle(100, 200, 50, 1)
    assert rect2.X == 100
    rect3 = Rectangle(rect2)
    assert rect3.X == 100

def test_const():
    from ooo.dyn.awt.device_capability import DeviceCapability, DeviceCapabilityEnum
    assert DeviceCapability.GETBITS == DeviceCapabilityEnum.GETBITS
    assert DeviceCapability.RASTEROPERATIONS == DeviceCapabilityEnum.RASTEROPERATIONS
    assert DeviceCapability.GETBITS == DeviceCapabilityEnum.GETBITS.value
    assert DeviceCapability.RASTEROPERATIONS == DeviceCapabilityEnum.RASTEROPERATIONS.value
    assert DeviceCapability.__module__ == 'ooo.dyn.awt.device_capability'

def test_excpetion_createUnoStruct():
    from ooo.dyn.ucb.missing_properties_exception import MissingPropertiesException
    prop = ("hello", "world")
    ex: MissingPropertiesException = MissingPropertiesException(Properties=prop)
    assert ex.Properties == ("hello", "world")

def test_color():
    from ooo.dyn.util.color import Color
    c1 = Color(234)
    c2 = Color(6)
    assert isinstance(c1, int)
    result = c1 + c2
    assert result == 240
    