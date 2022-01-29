from ooo_uno.helper import uno_helper as helper

def test_property_value():
    pv = helper.make_property_value(cName='MyName', uValue="Hello World")
    assert pv.Name == 'MyName'
    assert pv.Value == 'Hello World'