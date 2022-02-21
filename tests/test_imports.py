# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])

def test_lo_css_lo():
    from ooo.lo.style.line_spacing import LineSpacing as LoLineSpacing
    from ooo.csslo.style import LineSpacing as CssLineSpacing
    result = LoLineSpacing is CssLineSpacing
    assert result
    ls = LoLineSpacing()
    assert type(ls).__name__ == 'LineSpacing'
    

def test_dyn_css_dyn():
    from ooo.dyn.style.line_spacing import LineSpacing as DynLineSpacing
    from ooo.cssdyn.style import LineSpacing as CssLineSpacing
    result = DynLineSpacing is CssLineSpacing
    assert result
    ls = DynLineSpacing()
    assert type(ls).__name__ == 'com.sun.star.style.LineSpacing'

def test_uno_xinterface():
    from ooo.csslo.uno import XInterface as LoXInterface
    from ooo.cssdyn.uno import XInterface as DynXInterface
    assert LoXInterface != DynXInterface
    assert LoXInterface.__name__ == 'XInterface'
    assert LoXInterface.__module__ == 'ooo.lo.uno.x_interface'
    assert DynXInterface.__name__ == 'com.sun.star.uno.XInterface'
    assert DynXInterface.__module__ == 'uno'

def test_awt_font_slant():
    from ooo.lo.awt.font_slant import FontSlant as LoFontSlant
    from ooo.csslo.awt import FontSlant as CssFontSlant
    from ooo.dyn.awt.font_slant import FontSlant as DynFontSlant
    same = LoFontSlant is CssFontSlant
    assert same == True
    same = LoFontSlant is DynFontSlant
    assert same == False

def test_awt_font_slant_uno():
    from ooo.dyn.awt.font_slant import FontSlant as DynFontSlant
    from ooo.cssdyn.awt import FontSlant as CssFontSlant
    from ooo.lo.awt.font_slant import FontSlant as LoFontSlant
    same = DynFontSlant is CssFontSlant
    assert same == True
    same = DynFontSlant is LoFontSlant
    assert same == False

def test_awt_rectangle():
    from ooo.lo.awt.rectangle import Rectangle as LoRectangle
    from ooo.csslo.awt import Rectangle as CssRectangle
    from ooo.cssdyn.awt import Rectangle as DynRectangle
    same = LoRectangle is CssRectangle
    assert same == True
    same = LoRectangle is DynRectangle
    assert same == False

def test_awt_rectangle_uno():
    from ooo.dyn.awt.rectangle import Rectangle as LoRectangle
    from ooo.cssdyn.awt import Rectangle as DynRectangle
    from ooo.csslo.awt import Rectangle as CssRectangle
    same = LoRectangle is DynRectangle
    assert same == True
    same = LoRectangle is CssRectangle
    assert same == False