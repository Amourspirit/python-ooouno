=============
Service Class
=============

A service abstractly defines an object by combining interfaces and properties to encapsulate some useful functionality.
A UNO interface defines how an object interacts with the outside world.
A UNO structure defines a collection of data; and a UNO service combines them together.
Like a UNO interface, a UNO service does not specify the implementation.
It only specifies how to interact with the object.

A service may include multiple services and interfaces.
An interface usually defines a single aspect of a service and therefore is usually smaller in scope.

Example creating service using :doc:`../../helper/uno_helper`.

.. code-block:: python

    from ooo.helper import uno_helper
    from ooo.csslo.ucb import SimpleFileAccess
    file_access: SimpleFileAccess = uno_helper.create_uno_service(
        'com.sun.star.ucb.SimpleFileAccess')
    s = file_access.getContentType(
        'https://raw.githubusercontent.com/Amourspirit/python-ooouno/main/README.rst')
    assert s == 'application/http-content'


Service class in ``ooo`` are the same across all namespaces and do not have any dynamic generation.

.. code-block:: python

    >>> from ooo.lo.ucb.simple_file_access import SimpleFileAccess as LoSimpleFileAccess
    >>> from ooo.dyn.ucb.simple_file_access import SimpleFileAccess as DynSimpleFileAccess
    >>> from ooo.csslo.ucb import SimpleFileAccess as CssLoSimpleFileAccess
    >>> from ooo.cssdyn.ucb import SimpleFileAccess as CssDynSimpleFileAccess
    >>> LoSimpleFileAccess is DynSimpleFileAccess
    True
    >>> LoSimpleFileAccess is CssLoSimpleFileAccess
    True
    >>> LoSimpleFileAccess is CssDynSimpleFileAccess
    True
