.. conditional documentation master file, created by
   sphinx-quickstart on Thu May 10 17:11:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================================
conditional |version| -- Conditional Context
====================================================

.. toctree::
   :maxdepth: 2

.. module:: conditional
.. highlight:: python

The :class:`~conditional.conditional` context manager comes handy when you
always want to execute a with-block but only conditionally want to apply its
context manager.

If you find yourself writing code like this:

.. code-block:: python

    if CONDITION:
        with CONTEXTMANAGER():
            BODY()
    else:
        BODY()

Consider replacing it with:

.. code-block:: python

    with conditional(CONDITION, CONTEXTMANAGER()):
        BODY()

Asynchronous context managers are supported since version 2.0:

.. code-block:: python

    async with conditional(CONDITION, ASYNCCONTEXTMANAGER()):
        BODY()

The :class:`~conditional.conditional` context manager ships with type
annotations. Type checkers and IDEs can use this information to implement
type safety and auto completion.

API Documentation
=================

.. function:: conditional(condition, contextmanager)

    Wrap a context manager and enter it only if condition is true.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

