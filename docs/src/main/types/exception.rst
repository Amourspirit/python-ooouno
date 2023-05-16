===============
Exception Class
===============

Exception classes represent a UNO Exception

Static
======

Exception classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

As of version ``2.0.0`` the ``ooo.csslo`` namespace is deprecated. Use the ``ooo.lo`` namespace instead.

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

As of version ``2.0.0`` the ``ooo.cssdyn`` namespace is deprecated. Use the ``ooo.dyn`` namespace instead.

Example dynamic:
    .. code-block:: python

        from ooo.dyn.uno.runtime_exception import RuntimeException
        ex = RuntimeException("I made an error")
        assert ex.Message == 'I made an error'
        assert type(ex).__name__ == 'com.sun.star.uno.RuntimeException'
        assert ex.__module__ == 'uno'
    
Dynamic exceptions can be used in try block to catch UNO exceptions.

.. code-block:: python

    from ooo.dyn.uno.runtime_exception import RuntimeException

    def foo():
        try:
            # some uno operation
            ...
        except RuntimeException as e:
            # handle com.sun.star.uno.RuntimeException errors
            print(e)

Dynamic exception can be used to raise UNO exceptions.

.. code-block:: python

    from ooo.dyn.uno.exception import Exception as UnoException

    def foo(x):
        if not x:
            raise UnoException('Expected x to be something?')
        # some amazing stuff
    
    def bar(y):
        if not y:
            ex = UnoException()
            ex.Message='Expected y to be something?'
            raise ex
        # some amazing stuff
    
    def foobar(z):
        if not z:
            raise UnoException
        # some amazing stuff

Exception classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are the same classes.

.. note::

    Dynamic exception classes return equivalent UNO classes

    This means dynamic exceptions are interchangable with UNO classes.
