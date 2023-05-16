===============
Interface Class
===============

An interface defines how something interacts with its environment.
A UNO interface resembles a group of subroutine and function declarations; arguments and return types are specified along with functionality.
The interface indicates how an object can be used, but it says nothing about the implementation.

In ``ooo`` all interface classes are abstract classes.

Tip:
    UNO interface names start with the capital letter X.

Interface classes imported from ``ooo.lo`` and ``ooo.csslo`` namespaces are static and not changed during runtime.

As of version ``2.0.0`` the ``ooo.csslo`` namespace is deprecated. Use the ``ooo.lo`` namespace instead.

Interface classes imported from ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic and are changed
to UNO classes at runtime.

As of version ``2.0.0`` the ``ooo.cssdyn`` namespace is deprecated. Use the ``ooo.dyn`` namespace instead.

Example:

    .. code-block:: python

        from ooo.csslo.uno import XInterface as LoXInterface
        from ooo.cssdyn.uno import XInterface as DynXInterface
        assert LoXInterface != DynXInterface
        assert LoXInterface.__name__ == 'XInterface'
        assert LoXInterface.__module__ == 'ooo.lo.uno.x_interface'
        assert DynXInterface.__name__ == 'com.sun.star.uno.XInterface'
        assert DynXInterface.__module__ == 'uno'