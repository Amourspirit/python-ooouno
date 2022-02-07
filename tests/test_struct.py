# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])
import uno


from enum import Enum


def test_TabStop():
    from ooo.dyn.style.tab_stop import TabStop
    from ooo.dyn.style.tab_align import TabAlign
    tab = TabStop(1, TabAlign.CENTER, 'd', 'f')

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
        1,
        TabAlign.DECIMAL, 'd',
        FillChar='f'
    )
    assert tab.Alignment == TabAlign.DECIMAL
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1
    
    tab = TabStop(1, TabAlign.DECIMAL, 'd', 'f')
    assert tab.Alignment == TabAlign.DECIMAL
    assert tab.DecimalChar == 'd'
    assert tab.FillChar == 'f'
    assert tab.Position == 1


def test_LineSpacing():
    from ooo.dyn.style.line_spacing import LineSpacing
    lns = LineSpacing()
    lns.Height = 10
    lns.Mode = 3
    assert lns.Height == 10
    assert lns.Mode == 3
    
    lns = LineSpacing(3, 10)
    assert lns.Mode == 3
    assert lns.Height == 10

    lns = LineSpacing(3, Height=10)
    assert lns.Height == 10
    assert lns.Mode == 3

    lns = LineSpacing(Height=10, Mode=3)
    assert lns.Height == 10
    assert lns.Mode == 3
    
    lns.Height = 34
    lns.Mode = 12
    assert lns.Height == 34
    assert lns.Mode == 12
    assert lns.__ooo_ns__ == 'com.sun.star.style'
    assert lns.__ooo_full_ns__ == 'com.sun.star.style.LineSpacing'
    assert lns.__ooo_type_name__ == 'struct'

def test_NumberFormatCode():
    from ooo.dyn.i18n.number_format_code import NumberFormatCode
    nfc = NumberFormatCode()
    nfc.Code = 'YYYY-MM-DD'
    nfc.Default = True
    nfc.DefaultName = 'MyFormat'
    assert nfc.Code == 'YYYY-MM-DD'
    assert nfc.Default
    assert nfc.DefaultName == 'MyFormat'
    
    nfc = NumberFormatCode(7, 5, 'YYYY-MM-DD', 'MyFormat',"ID", 12, False)
    assert nfc.Code == 'YYYY-MM-DD'
    assert nfc.Default == False
    assert nfc.DefaultName == 'MyFormat'
    assert nfc.Index == 12
    assert nfc.Type == 7
    assert nfc.Usage == 5
    assert nfc.NameID == 'ID'
    assert nfc.__ooo_ns__ == 'com.sun.star.i18n'
    assert nfc.__ooo_full_ns__ == 'com.sun.star.i18n.NumberFormatCode'
    assert nfc.__ooo_type_name__ == 'struct'
    
    nfc3 = NumberFormatCode(nfc)
    assert nfc3.Code == 'YYYY-MM-DD'
    assert nfc3.Default == False
    assert nfc3.DefaultName == 'MyFormat'
    assert nfc3.Index == 12
    assert nfc3.Type == 7
    assert nfc3.Usage == 5
    assert nfc3.NameID == 'ID'
    assert nfc3.__ooo_ns__ == 'com.sun.star.i18n'
    assert nfc3.__ooo_full_ns__ == 'com.sun.star.i18n.NumberFormatCode'
    assert nfc3.__ooo_type_name__ == 'struct'