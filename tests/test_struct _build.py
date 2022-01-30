# coding: utf-8
import pytest
import os
os.environ['ooouno_ignore_runtime'] = 'True'
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.realpath('.'))
import uno
from ooo_uno.uno_obj.style.tab_stop import TabStop
from ooo_uno.uno_obj.style.tab_align import TabAlign
from enum import Enum


def test_TabStop():
    tab = TabStop(TabAlign.CENTER, 'd', 'f', 1)

    assert isinstance(tab.Alignment, Enum) == True
    assert tab.Alignment.value == TabAlign.CENTER.value
    assert tab.Alignment == TabAlign.CENTER
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1

    tab = TabStop(
        Alignment=TabAlign.CENTER,
        DecimalChar='d',
        FillChar='f',
        Position=1
    )
    assert tab.Alignment == TabAlign.CENTER
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1

    tab = TabStop(
        TabAlign.DECIMAL, 'd',
        FillChar='f',
        Position=1
    )
    assert tab.Alignment == TabAlign.DECIMAL
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1


if __name__ == "__main__":
    pytest.main([__file__])
