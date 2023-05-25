==========
Enum Class
==========

.. contents:: Table of Contents
    :local:
    :backlinks: top
    :depth: 2


Enum classes represent an enumeration

Overview
========

It is not possible to import a ``uno.Enum`` in the same way as a python enum.
``from com.sun.star.sheet import FillDateMode`` would result in an import error.

However ``uno.Enum`` attributes can be imported.

.. code-block:: python

    >>> from com.sun.star.sheet.FillDateMode import FILL_DATE_DAY
    >>> print(FILL_DATE_DAY)
    <Enum instance com.sun.star.sheet.FillDateMode ('FILL_DATE_DAY')>

Also ``uno.Enum`` attributes instance of the ``uno.Enum`` class behave similar to  python Enum values.

Example: In this example the value is a string containing ``"FILL_DATE_DAY"`` .

.. code-block:: python

    >>> from com.sun.star.sheet.FillDateMode import FILL_DATE_DAY
    >>> print(FILL_DATE_DAY.value)
    FILL_DATE_DAY

OOOUNO Dynamic Enums
====================

Overview
--------

``ooouno`` has python enums for each ``uno.Enum``. At runtime the values of ``ooouno`` enum are actual ``uno.Enum`` values.
This gives the best of both worlds when working with enums in the LibreOffice API.

.. code-block:: python

    import uno
    from ooo.dyn.sheet.solver_constraint_operator import SolverConstraintOperator
    from com.sun.star.sheet.SolverConstraintOperator import (
        BINARY, EQUAL, GREATER_EQUAL, INTEGER, LESS_EQUAL
    )

    def main() -> None:
        print(com.sun.star.sheet.SolverConstraintOperator.BINARY == BINARY) # True

Typing Support
--------------

In many cases is it much more desirable to import ``uno.Enum`` as if it is a python enum.
This especially valuable when a method takes a ``uno:Enum`` type.

Dynamic Enum
^^^^^^^^^^^^

In the following example type checkers have something to work with.
If the underlying value are changed in a different version of LibreOffice it will not break the function as ``ooouno`` loads the enum values dynamically.

Example: Normal python behavior using ``ooouno``.

.. code-block:: python

    import uno
    from ooo.dyn.sheet.solver_constraint_operator import SolverConstraintOperator

    def solve_operation(value: int, x: SolverConstraintOperator) -> int:
        # do some work
        if x == SolverConstraintOperator.BINARY:
            ...
        elif x == SolverConstraintOperator.EQUAL:
            ...
        elif x == SolverConstraintOperator.GREATER_EQUAL:
            ...
        elif x == SolverConstraintOperator.INTEGER:
            ...
        elif x == SolverConstraintOperator.LESS_EQUAL:
            ...
        else:
            # future proofing
            raise ValueError(f"x value is unknown: {x.value}")
        ...

    def main() -> None:
        y = solve_operation(13, SolverConstraintOperator.BINARY)
        y = solve_operation(101, SolverConstraintOperator.EQUAL)


Standard LibreOffice API Enum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, each enum value as to be imported separately.
The ``solve_operation()`` has limited type information as ``uno:Enum`` only exposes ``typeName`` and ``value``.

The method has to ensure the proper type has been passed in. Conditions have to be checked against the ``x.value`` to find a match.

Example: Have to import each enum value separately and use values for checking.

.. code-block:: python

    import uno
    from typing import cast
    from com.sun.star.sheet.SolverConstraintOperator import (
        BINARY, EQUAL, GREATER_EQUAL, INTEGER, LESS_EQUAL
    )

    def solve_operation(value: int, x: uno.Enum) -> int:
        # risky if SolverConstraintOperator values change in the future
        # then this function will break.
        if x.typeName != "com.sun.star.sheet.SolverConstraintOperator":
            raise TypeError("x is not a SolverConstraintOperator")

        if x.value == "BINARY":
            ...
        elif x.value == "EQUAL":
            ...
        elif x.value == "GREATER_EQUAL":
            ...
        elif x.value == "INTEGER":
            ...
        elif x.value == "LESS_EQUAL":
            ...
        else:
            # future proofing
            raise ValueError(f"x value is unknown: {x.value}")

    def main() -> None:
        # cast so type checkers like mypy and pyright will pass
        y = solve_operation(13, cast(uno.Enum, BINARY))
        y = solve_operation(101, cast(uno.Enum, EQUAL))

Enum Protocol
-------------

``ooouno`` uses `types-unopy <https://pypi.org/project/types-unopy/>`__ for type support.

``types-unopy`` handles typing for ``uno.Enum`` groups by using a protocol for each enum.

A protocol for ``com.sun.star.sheet.SolverConstraintOperator`` would look something like this.

.. code-block:: python

    class SolverConstraintOperatorProto(Protocol):
        @property
        def typeName(self) -> Literal["com.sun.star.sheet.SolverConstraintOperator"]:
            ... 
        value: Any
        BINARY: SolverConstraintOperatorProto
        EQUAL: SolverConstraintOperatorProto
        GREATER_EQUAL: SolverConstraintOperatorProto
        INTEGER: SolverConstraintOperatorProto
        LESS_EQUAL: SolverConstraintOperatorProto

Each value in the ``com.sun.star.sheet.SolverConstraintOperator`` namespace when imported is now considered to be a protocol.

Type Guarding Protocol
^^^^^^^^^^^^^^^^^^^^^^

The Enum Protocols in ``ooouno`` are a special case and do not exist at runtime.
For this reason it is necessary to guard the import. Since ``typing.TYPE_CHECKING`` is always ``False`` at runtime we can use it.

There are two way to handle importing a protocol class.
The first way is by importing ``annotations``.

.. code-block:: python

    from __future__ import annotations
    import uno
    from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto
    # ...

    def solve_operation(value: int, x: SolverConstraintOperatorProto) -> int:
        ...

Note when using ``annotations`` the ``cast`` to protocol must be wrapped in a string.

.. code-block:: python

    from typing import cast
    from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto
    from ooo.dyn.sheet.solver_constraint_operator import SolverConstraintOperator
    # ...

    # SolverConstraintOperatorProto must be wrapped in a string
    # if it has not been assigned to object at runtime.
    solve_operation(
        11, cast("SolverConstraintOperatorProto", SolverConstraintOperator.BINARY)
    )


The other way is to assign the protocol class as an object at runtime.

.. code-block:: python

    from typing import TYPE_CHECKING
    import uno
    from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto

    if TYPE_CHECKING:
        # While writing code we have the advantages of protocol
        from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto
    else:
        # code is executing. Now protocol is an object and basically ignored
        SolverConstraintOperatorProto = object

Examples
--------

Taking advantage of type support.

``ooouno`` assigns standard Enum constants type as a protocol.
Standard Enum constants are now imported and the type is reported as a Protocol.

.. code-block:: python

    import uno
    from typing import TYPE_CHECKING
    from ooo.dyn.sheet.solver_constraint_operator import SolverConstraintOperator
    from com.sun.star.sheet.SolverConstraintOperator import (
        BINARY, EQUAL, GREATER_EQUAL, INTEGER, LESS_EQUAL
    )   

    if TYPE_CHECKING:
        from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto
    else:
        SolverConstraintOperatorProto = object

    def solve_operation(value: int, x: SolverConstraintOperatorProto) -> int:
        # at runtime x and SolverConstraintOperator enum values are identical
        if x == SolverConstraintOperator.BINARY:
            ...
        elif x == SolverConstraintOperator.EQUAL:
            ...
        elif x == SolverConstraintOperator.GREATER_EQUAL:
            ...
        elif x == SolverConstraintOperator.INTEGER:
            ...
        elif x == SolverConstraintOperator.LESS_EQUAL:
            ...
        else:
            # future proofing
            raise ValueError(f"x value is unknown: {x.value}")

    def main() -> None:
        # cast is not needed because types-unopy imports the constants
        # as SolverConstraintOperatorProto automatically
        y = solve_operation(13, BINARY)
        y = solve_operation(101, EQUAL)

Passing incorrect type will result in a typing error for type checkers such as ``mypy`` and ``pyright``.

.. code-block:: python

    from com.sun.star.sheet.FillDateMode import FILL_DATE_DAY

    # ...
    # Fails type checking because FILL_DATE_DAY is not SolverConstraintOperatorProto
    solve_operation(3, FILL_DATE_DAY)

`Screenshot <https://github.com/Amourspirit/python-ooouno/assets/4193389/2fe7e4cb-e952-4fca-b74c-85a45324d7dc>`__ of type error.

.. figure:: https://github.com/Amourspirit/python-ooouno/assets/4193389/2fe7e4cb-e952-4fca-b74c-85a45324d7dc
    :alt: Enum protocol error

    Enum protocol error


Using Dynamic Enums with a method that expects a Protocol will need a casting.
This is perfectly fine as Dynamic Enum values are identical to their ``uno.Enum`` constant counterparts.

.. code-block:: python

    import uno
    from typing import TYPE_CHECKING
    from ooo.dyn.sheet.solver_constraint_operator import SolverConstraintOperator
    from com.sun.star.sheet.SolverConstraintOperator import (
        BINARY, EQUAL, GREATER_EQUAL, INTEGER, LESS_EQUAL
    )

    if TYPE_CHECKING:
        from com.sun.star.sheet.SolverConstraintOperator import SolverConstraintOperatorProto
    else:
        SolverConstraintOperatorProto = object

    def solve_operation(value: int, x: SolverConstraintOperatorProto) -> int:
        # at runtime x and SolverConstraintOperator enum values are identical
        if x == SolverConstraintOperator.BINARY:
            ...
        elif x == SolverConstraintOperator.EQUAL:
            ...
        elif x == SolverConstraintOperator.GREATER_EQUAL:
            ...
        elif x == SolverConstraintOperator.INTEGER:
            ...
        elif x == SolverConstraintOperator.LESS_EQUAL:
            ...
        else:
            # future proofing
            raise ValueError(f"x value is unknown: {x.value}")

    def main() -> None:
        # cast is not needed becuase types-unopy imports the constants
        # as SolverConstraintOperatorProto automatically
        y = solve_operation(
            3,
            cast(SolverConstraintOperatorProto, SolverConstraintOperator.GREATER_EQUAL)
        )
        y = solve_operation(
        101,
        cast(SolverConstraintOperatorProto, SolverConstraintOperator.EQUAL)
        )

Static
======

Enum classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

As of version ``2.0.0`` the ``ooo.csslo`` namespace is deprecated. Use the ``ooo.lo`` namespace instead.

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

As of version ``2.0.0`` the ``ooo.cssdyn`` namespace is deprecated. Use the ``ooo.dyn`` namespace instead.

Example dynamic:
    .. code-block:: python

        from ooo.cssdyn.awt import FontSlant

        e = FontSlant('OBLIQUE')
        assert e == FontSlant.OBLIQUE
        assert e.value == FontSlant.OBLIQUE.value

        e = FontSlant(FontSlant.OBLIQUE)
        assert e == FontSlant.OBLIQUE

At runtime dynamic enum are the same as UNO enum.

.. code-block:: python

    from ooo.cssdyn.awt import FontSlant
    from com.sun.star.awt.FontSlant import ITALIC
    same = FontSlant.ITALIC is ITALIC
    assert same

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