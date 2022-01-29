# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
import uno
from ooo_uno.uno_obj.style.tab_stop import TabStop
from ooo_uno.uno_obj.style.tab_align import TabAlign
from ooo_uno.uno_obj.style.line_spacing import LineSpacing
from ooo_uno.uno_obj.i18n.number_format_code import NumberFormatCode
from enum import Enum


def test_TabStop():
    tab = TabStop(TabAlign.CENTER, 'd', 'f', 1)

    assert isinstance(tab.Alignment, Enum) == False
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


def test_LineSpacing():
    lns = LineSpacing()
    lns.Height = 10
    lns.Mode = 3
    assert lns.Height == 10
    assert lns.Mode == 3
    
    lns = LineSpacing(10, 3)
    assert lns.Height == 10
    assert lns.Mode == 3

    lns = LineSpacing(10, Mode=3)
    assert lns.Height == 10
    assert lns.Mode == 3

    lns = LineSpacing(Height=10, Mode=3)
    assert lns.Height == 10
    assert lns.Mode == 3
    
    lns.Height = 34
    lns.Mode = 12
    assert lns.Height == 34
    assert lns.Mode == 12

def test_NumberFormatCode():
    nfc = NumberFormatCode()
    nfc.Code = 'YYYY-MM-DD'
    nfc.Default = True
    nfc.DefaultName = 'MyFormat'
    assert nfc.Code == 'YYYY-MM-DD'
    assert nfc.Default
    assert nfc.DefaultName == 'MyFormat'
    
    nfc = NumberFormatCode('YYYY-MM-DD', False, 'MyFormat', 12, Usage=5, Type=7)
    assert nfc.Code == 'YYYY-MM-DD'
    assert nfc.Default == False
    assert nfc.DefaultName == 'MyFormat'
    assert nfc.Index == 12
    assert nfc.Type == 7
    assert nfc.Usage == 5

if __name__ == "__main__":
    pytest.main([__file__])
