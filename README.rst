=========================
Welcome to ooouno's docs!
=========================

|lic| |pver| |pwheel| |github|

ooouno
======

**ooouno** is a library of all *(more than 4300)* classes, typings and types for the LibreOffice `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_.

**ooouno** is for version ``7.4`` of LibreOffice `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_.

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

    $ conda install -c conda-forge ooouno


For LibreOffice <= ``7.3``
    ``$ conda install -c conda-forge "ooouno>=0.2.5, <1.0"``


For LibreOffice <= ``7.2``
    ``$ conda install -c conda-forge "ooouno<0.2"``

PIP
---

**ooouno** `PyPI <https://pypi.org/project/ooouno/>`_

.. code-block:: bash

    $ pip install ooouno

For LibreOffice <= ``7.3``
    ``pip install "ooouno>= 0.2.5, < 1.0"``

For LibreOffice <= ``7.2``
    ``pip install "ooouno<0.2"``


Usage
=====

All class found in LO `API <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html>`_ are recreated in this library.

For instance:
    | ``from ooo.dyn.style.line_spacing import LineSpacing`` is equivalent to
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

As of version ``2.0.0`` the ``ooo.csslo`` namespace is deprecated. Use the ``ooo.lo`` namespace instead.

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

As of version ``2.0.0`` the ``ooo.cssdyn`` namespace is deprecated. Use the ``ooo.dyn`` namespace instead.

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

When using ooo interactively such as creating struts, enums, singletons, const classes then
import from ``ooo.dyn`` or ``ooo.cssdyn``.

Development
-----------

Development environment is configured using `poetry <https://python-poetry.org/>`__.

It is recommended to install virtual environment locally.

To Configure poetry to install virtual environment in local folder:

.. code-block::

    poetry config virtualenvs.in-project true

After virtual environment has been set up.

Linux/Mac
+++++++++

Link UNO files into virtual environment.

.. code-block::

    oooenv cmd-link -a

Windows
+++++++

Run toggle command to set virtual environment.

.. code-block::

    oooenv env -t

See Also
++++++++

- `oooenv <https://pypi.org/project/oooenv/>`__
- `OOO Development Tools - Develop Docs <https://python-ooo-dev-tools.readthedocs.io/en/latest/dev_docs/dev_notes.html>`__

Related Projects
----------------

* `OOO Development Tools <https://github.com/Amourspirit/python_ooo_dev_tools>`__
* `LibreOffice API Typings <https://github.com/Amourspirit/python-types-unopy>`__
* `ScriptForge Typings <https://github.com/Amourspirit/python-types-scriptforge>`__
* `Access2base Typings <https://github.com/Amourspirit/python-types-access2base>`__
* `LibreOffice Python UNO Examples <https://github.com/Amourspirit/python-ooouno-ex>`__
* `LibreOffice Developer Search <https://github.com/Amourspirit/python_lo_dev_search>`__
* `LibreOffice UNO Typings <https://github.com/Amourspirit/python-types-uno-script>`__
* `OOO UNO TEMPLATE <https://github.com/Amourspirit/ooo_uno_tmpl>`__

.. |lic| image:: https://img.shields.io/github/license/Amourspirit/python-ooouno
    :alt: License Apache

.. |pver| image:: https://img.shields.io/pypi/pyversions/ooouno
    :alt: PyPI - Python Version

.. |pwheel| image:: https://img.shields.io/pypi/wheel/ooouno
    :alt: PyPI - Wheel

.. |github| image:: https://img.shields.io/badge/GitHub-100000?style=plastic&logo=github&logoColor=white
    :target: https://github.com/Amourspirit/python-ooouno
    :alt: Github
