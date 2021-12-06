# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
import uno
from ooo_uno.uno_obj.style.tab_stop import TabStop
from ooo_uno.uno_obj.style.tab_align import TabAlign
from enum import Enum


def test_TabStop():
    tab = TabStop(TabAlign.CENTER, 'd', 'f', 1)

    assert len(tab) == 4
    assert isinstance(tab.Alignment, Enum) == False
    assert tab.Alignment.value == TabAlign.CENTER.value
    assert tab.Alignment == TabAlign.CENTER
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1
    assert tab[0].value == TabAlign.CENTER.value
    assert tab[1] == 'd'
    assert tab[2] == 'f'
    assert tab[3] == 1


if __name__ == "__main__":
    pytest.main([__file__])
