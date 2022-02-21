==========
Enum Class
==========

Enum classes represent an enumeration

Static
======

Enum classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

Example static:
    .. code-block:: python

        from ooo.csslo.awt import FontSlant
        assert FontSlant.ITALIC.__module__ == 'ooo.lo.awt.font_slant'
        assert FontSlant.NONE.__module__ == 'ooo.lo.awt.font_slant'
        e = FontSlant('OBLIQUE')
        assert e == FontSlant.OBLIQUE
        assert e.value == FontSlant.OBLIQUE.value
        assert e.__module__ == 'ooo.lo.awt.font_slant'
        e = FontSlant(FontSlant.OBLIQUE)
        assert e == FontSlant.OBLIQUE
        assert e.__module__ == 'ooo.lo.awt.font_slant'

Enum classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.lo.awt.font_slant import FontSlant as LoFontSlant
        from ooo.csslo.awt import FontSlant as CssFontSlant
        from ooo.dyn.awt.font_slant import FontSlant as DynFontSlant
        same = LoFontSlant is CssFontSlant
        assert same == True
        same = LoFontSlant is DynFontSlant
        assert same == False

Dynamic
=======

Enum classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime. All enumeration values are UNO equivalent.



Example dynamic:
    .. code-block:: python

        from ooo.cssdyn.awt import FontSlant
        from com.sun.star.awt.FontSlant import ITALIC, NONE
        assert FontSlant.ITALIC.__module__ == 'uno'
        assert FontSlant.NONE.__module__ == 'uno'
        assert FontSlant.ITALIC == ITALIC
        assert FontSlant.NONE == NONE
        e = FontSlant('OBLIQUE')
        assert e == FontSlant.OBLIQUE
        assert e.value == FontSlant.OBLIQUE.value
        assert e.__module__ == 'uno'
        e = FontSlant(FontSlant.OBLIQUE)
        assert e == FontSlant.OBLIQUE
        assert e.__module__ == 'uno'

Enum classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.dyn.awt.font_slant import FontSlant as DynFontSlant
        from ooo.cssdyn.awt import FontSlant as CssFontSlant
        from ooo.lo.awt.font_slant import FontSlant as LoFontSlant
        same = DynFontSlant is CssFontSlant
        assert same == True
        same = DynFontSlant is LoFontSlant
        assert same == False