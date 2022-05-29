=========================
Welcome to ooouno's docs!
=========================

|lic| |pver| |pwheel| |github|

ooouno
======

**ooouno** is a library of all *(more than 4300)* classes, typings and types for the LibreOffice `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_.

**ooouno** is for version 6.4 to 7.2 of LibreOffice `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_.
**ooouno** may work in older versions of API but has not been tested.

More about `LibreOffice <https://www.libreoffice.org/>`_.

Docs
====

Read the docs `here <https://python-ooouno.readthedocs.io/>`_

Installation
============

CONDA
-----

**ooouno** on `Anaconda <https://anaconda.org/conda-forge/ooouno>`_

.. code-block:: bash

    $ conda install -c conda-forge "ooouno<0.2"


PIP
---

**ooouno** `PyPI <https://pypi.org/project/ooouno/>`_

.. code-block:: bash

    $ pip install "ooouno<0.2"




Usage
=====

All class found in LO `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_ are recreated in this library.

For instance:
    | ``from ooo.dyn.style.line_spacing import LineSpacing`` is equivalent to
    | ``from com.sun.star.style import LineSpacing``

    | ``from ooo.cssdyn.style import LineSpacing`` is equivalent to
    | ``from com.sun.star.style import LineSpacing``


Namespace
---------

There are four namespaces representing LO `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_ in this library.

ooo.lo
++++++

| Namespace ``ooo.lo`` contains all static python classes. The format is
| ``ooo.lo.<ns>.<snake_case_name>.<PascalCaseName>``

.. code-block:: python

    from ooo.lo.uno.x_interface import XInterface

    def foo(input:str) -> XInterface: ...

ooo.dyn
+++++++

Namespace ``ooo.dyn`` contains static and dynamic classes depending on class type.
The format is ``ooo.dyn.<ns>.<snake_case_name>.<PascalCaseName>``

This namespace has dynamic classes that are changed at runtime.
For classes that are dynamic are fully or partially replaced by UNO version at runtime.

This allows for typings while in design time (working in IDE) and at runtime UNO classes are created instead.

.. code-block:: python

    >>> from ooo.dyn.style.line_spacing import LineSpacing as DynLineSpacing
    >>> from ooo.lo.style.line_spacing import LineSpacing as LoLineSpacing
    >>> dyn_lns = DynLineSpacing(Height=10, Mode=3)
    >>> lo_lns = LoLineSpacing(Height=10, Mode=3)
    >>> assert dyn_lns.Height == 10
    >>> assert dyn_lns.Mode == 3
    >>> type(dyn_lns).__name__
    'com.sun.star.style.LineSpacing'
    >>> type(lo_lns).__name__
    'LineSpacing'
    

ooo.csslo
+++++++++

| Namespace ``ooo.csslo`` contains static classes as LO `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_ style imports.
| The format is ``ooo.csslo.<ns>.<PascalCaseName>``

When importing from ``ooo.csslo`` all classes in that namespace are also loaded.
Under some circumstances this may not be desired. Such as packaging with `stickytape <https://pypi.org/project/stickytape/>`_.

.. code-block:: python

    >>> from ooo.lo.style.line_spacing import LineSpacing as LoLineSpacing
    >>> from ooo.csslo.style import LineSpacing as CssLineSpacing
    >>> LoLineSpacing is CssLineSpacing
    True
    >>> ls = CssLineSpacing()
    >>> type(ls).__name__
    'LineSpacing'

ooo.cssdyn
++++++++++

Namespace ``ooo.cssdyn`` contains static and dynamic classes depending on class type as LO `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_ style imports.

When importing from ``ooo.cssdyn`` all classes in that namespace are also loaded.
Under some circumstances this may not be desired. Such as packaging with `stickytape <https://pypi.org/project/stickytape/>`_.

.. code-block:: python

    >>> from ooo.dyn.style.line_spacing import LineSpacing as DynLineSpacing
    >>> from ooo.cssdyn.style import LineSpacing as CssLineSpacing
    >>> DynLineSpacing is CssLineSpacing
    True
    >>> ls = CssLineSpacing()
    >>> type(ls).__name__
    'com.sun.star.style.LineSpacing'


Generally speaking
------------------

When using ooo as typings then import from ``ooo.lo`` or ``ooo.csslo``.

When using ooo interactivly such as creating structs, enums, singletons, const classes then
import from ``ooo.dyn`` or ``ooo.cssdyn``.

Related Projects
----------------

* `LibreOffice API Typings <https://github.com/Amourspirit/python-types-unopy>`_
* `ScriptForge Typings <https://github.com/Amourspirit/python-types-scriptforge>`_
* `Access2base Typings <https://github.com/Amourspirit/python-types-access2base>`_
* `LibreOffice Python UNO Examples <https://github.com/Amourspirit/python-ooouno-ex>`_
* `LibreOffice Developer Search <https://github.com/Amourspirit/python_lo_dev_search>`_
* `LibreOffice UNO Typings <https://github.com/Amourspirit/python-types-uno-script>`_
* `LibreOffice Developer Search <https://github.com/Amourspirit/python_lo_dev_search>`_
* `OOO UNO TEMPLATE <https://github.com/Amourspirit/ooo_uno_tmpl>`_

.. |lic| image:: https://img.shields.io/github/license/Amourspirit/python-ooouno
    :alt: License Apache

.. |pver| image:: https://img.shields.io/pypi/pyversions/ooouno
    :alt: PyPI - Python Version

.. |pwheel| image:: https://img.shields.io/pypi/wheel/ooouno
    :alt: PyPI - Wheel

.. |github| image:: https://img.shields.io/badge/GitHub-100000?style=plastic&logo=github&logoColor=white
    :target: https://github.com/Amourspirit/python-ooouno
    :alt: Github
