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