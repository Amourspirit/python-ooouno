===============
Exception Class
===============

Exception classes represent a UNO Exception

Static
======

Exception classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

Example static:
    .. code-block:: python

        from ooo.lo.uno.exception import Exception
        ex = Exception(Message="I made an error")
        assert ex.Message == 'I made an error'
        assert type(ex).__name__ == 'Exception'
        assert ex.__module__ == 'ooo.lo.uno.exception'

Exception classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.lo.uno.exception import Exception as LoException
        from ooo.csslo.uno import Exception as CssException
        same = LoException is CssException
        assert same == True

Dynamic
=======


Exception classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime.

Example dynamic:
    .. code-block:: python

        from ooo.dyn.uno.exception import Exception
        ex = Exception(Message="I made an error")
        assert ex.Message == 'I made an error'
        assert type(ex).__name__ == 'com.sun.star.uno.Exception'
        assert ex.__module__ == 'uno'

Exception classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are the same classes.

.. note::

    Dynamic exception classes have a dynamic constructor.

    | This means ``ooo.cssdyn.uno.Exception`` is a function at runtime
    | whereas ``ex = Exception()`` is an instance of a class.
