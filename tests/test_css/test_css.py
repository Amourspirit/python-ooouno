# coding: utf-8
import pytest
if __name__ == "__main__":
    pytest.main([__file__])
from ooo.csslo.beans import PropertyValues
from ooo.csslo.beans import PropertyValue
from ooo.csslo.beans import PropertyState


def test_property_values():
    pv1 = PropertyValue(
        Handle=-1,
        Name='one',
        State=PropertyState.DIRECT_VALUE,
        Value=10
    )
    pv2 = PropertyValue(
        Handle=-1,
        Name='two',
        State=PropertyState.DEFAULT_VALUE,
        Value=10
    )
    lst: PropertyValues = []
    lst.append(pv1)
    lst.append(pv2)
    assert isinstance(lst, list)
