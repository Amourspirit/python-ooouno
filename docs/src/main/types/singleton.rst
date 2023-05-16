===============
Singleton Class
===============

Singleton classes represent a UNO singleton.


Static
======

Singleton classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static abstract classes.
As of version ``2.0.0`` the ``ooo.csslo`` namespace is deprecated. Use the ``ooo.lo`` namespace instead.

Singleton classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are the same classes.
As of version ``2.0.0`` the ``ooo.cssdyn`` namespace is deprecated. Use the ``ooo.dyn`` namespace instead.

Example:
    .. code-block:: python

        from ooo.lo.beans.the_introspection import theIntrospection as LotheIntrospection
        from ooo.csslo.beans import theIntrospection as CsstheIntrospection
        same = LotheIntrospection is CsstheIntrospection
        assert same == True

Dynamic
=======

Singleton classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime.

Example dynamic:
    .. code-block:: python

        from ooo.cssdyn.beans import theIntrospection
        singleton = theIntrospection()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.stoc.Introspection"
        assert singleton.getImplementationName() == im_name

Singleton classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime

.. note::

    Dynamic singleton classes have a dynamic constructor.

    | This means ``ooo.cssdyn.beans.theIntrospection`` is a function at runtime
    | whereas ``singleton = theIntrospection()`` is an instance of a UNO class.