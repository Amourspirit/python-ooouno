# coding: utf-8
import pytest
if __name__ == "__main__":
    pytest.main([__file__])

import uno

def test_font_slant_dyn():
    from ooo.cssdyn.awt import FontSlant
    from com.sun.star.awt.FontSlant import (
        DONTKNOW, ITALIC, NONE, OBLIQUE, REVERSE_ITALIC, REVERSE_OBLIQUE)
    assert FontSlant.ITALIC.__module__ == 'uno'
    assert FontSlant.DONTKNOW.__module__ == 'uno'
    assert FontSlant.NONE.__module__ == 'uno'
    assert FontSlant.OBLIQUE.__module__ == 'uno'
    assert FontSlant.REVERSE_ITALIC.__module__ == 'uno'
    assert FontSlant.REVERSE_OBLIQUE.__module__ == 'uno'
    assert FontSlant.ITALIC == ITALIC
    assert FontSlant.DONTKNOW == DONTKNOW
    assert FontSlant.NONE == NONE
    assert FontSlant.OBLIQUE == OBLIQUE
    assert FontSlant.REVERSE_ITALIC == REVERSE_ITALIC
    assert FontSlant.REVERSE_OBLIQUE == REVERSE_OBLIQUE
    e = FontSlant('OBLIQUE')
    assert e == FontSlant.OBLIQUE
    assert e.value == FontSlant.OBLIQUE.value
    assert e.__module__ == 'uno'
    e = FontSlant(FontSlant.OBLIQUE)
    assert e == FontSlant.OBLIQUE
    assert e.value == FontSlant.OBLIQUE.value
    assert e.__module__ == 'uno'
    

def test_font_slant():
    from ooo.csslo.awt import FontSlant
    assert FontSlant.ITALIC.__module__ == 'ooo.lo.awt.font_slant'
    assert FontSlant.DONTKNOW.__module__ == 'ooo.lo.awt.font_slant'
    assert FontSlant.NONE.__module__ == 'ooo.lo.awt.font_slant'
    assert FontSlant.OBLIQUE.__module__ == 'ooo.lo.awt.font_slant'
    assert FontSlant.REVERSE_ITALIC.__module__ == 'ooo.lo.awt.font_slant'
    assert FontSlant.REVERSE_OBLIQUE.__module__ == 'ooo.lo.awt.font_slant'
    e = FontSlant('OBLIQUE')
    assert e == FontSlant.OBLIQUE
    assert e.__module__ == 'ooo.lo.awt.font_slant'
    e = FontSlant(FontSlant.OBLIQUE)
    assert e == FontSlant.OBLIQUE
    assert e.value == FontSlant.OBLIQUE.value
    assert e.__module__ == 'ooo.lo.awt.font_slant'