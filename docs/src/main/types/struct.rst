============
Struct Class
============

Struct classes represent a UNO structure.

Static
======

Struct classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

Example static:
    .. code-block:: python

        from ooo.csslo.awt import Rectangle
        rect1 = Rectangle(X=100, Y=200, Width=50, Height=1)
        assert rect1.X == 100
        assert rect1.Height == 1
        rect1.Width == 250
        assert rect1.Width == 250
        rect2 = Rectangle()
        rect2.X = 122
        rect2.Y = 240
        assert rect2.X == 122
        assert rect2.Y == 240

Struct classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.lo.awt.rectangle import Rectangle as LoRectangle
        from ooo.csslo.awt import Rectangle as CssRectangle
        from ooo.cssdyn.awt import Rectangle as DynRectangle
        same = LoRectangle is CssRectangle
        assert same == True
        same = LoRectangle is DynRectangle
        assert same == False

Dynamic
=======


Struct classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime.

Example dynamic:
    .. code-block:: python

        from ooo.cssdyn.awt import Rectangle
        from com.sun.star.awt import Rectangle as URectangle
        rect1 = Rectangle(X=100, Y=200, Width=50, Height=1)
        assert isinstance(rect1, URectangle)
        assert rect1.X == 100
        assert rect1.Height == 1
        rect1.Width == 250
        assert rect1.Width == 250
        rect2 = Rectangle()
        rect2.X = 122
        rect2.Y = 240
        assert rect2.X == 122
        assert rect2.Y == 240

Struct classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.dyn.awt.rectangle import Rectangle as LoRectangle
        from ooo.cssdyn.awt import Rectangle as DynRectangle
        from ooo.csslo.awt import Rectangle as CssRectangle
        same = LoRectangle is DynRectangle
        assert same == True
        same = LoRectangle is CssRectangle
        assert same == False