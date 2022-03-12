import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])
from ooo.helper import uno_helper as helper

def test_property_value():
    pv = helper.make_property_value(name='MyName', value="Hello World")
    assert pv.Name == 'MyName'
    assert pv.Value == 'Hello World'