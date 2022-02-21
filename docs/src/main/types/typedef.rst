=======
Typedef
=======

typedef objects define a type using `NewType <https://docs.python.org/3.7/library/typing.html#newtype>`_ similar to type alias.

Static type checker will treat the new type as if it were a subclass of the original type. This is useful in helping catch logical errors:

In the following example Color is a NewType of int ``Color = typing.NewType('Color', int)``

Example:
    .. code-block:: python

        from ooo.dyn.util.color import Color
        c1 = Color(234)
        c2 = Color(6)
        assert isinstance(c1, int)
        result = c1 + c2
        assert result == 240

Typedef's in ``ooo`` are the same accross all namespaces and do not have any dynamic generation.

.. code-block:: python

    >>> from ooo.lo.util.color import Color as LoColor
    >>> from ooo.dyn.util.color import Color as DynColor
    >>> from ooo.csslo.util import Color as CssLoColor
    >>> from ooo.cssdyn.util import Color as CssDynColor
    >>> LoColor is DynColor
    True
    >>> LoColor is CssLoColor
    True
    >>> LoColor is CssDynColor
    True

.. note::

    Checks for **NewType** are enforced only by the static type checker.
    At runtime the statement Color = NewType('Color', int) will make Color a function that
    immediately returns whatever parameter you pass it.
    That means the expression Color(some_value) does not create a new class or introduce any overhead beyond that of a regular function call.