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

The :class:`~conditional.conditional` context manager comes handy when you
always want to execute a with-block but only conditionally want to apply its
context manager.

If you find yourself writing code like this::

    if CONDITION:
        with CONTEXTMANAGER():
            BODY()
    else:
        BODY()

Consider replacing it with::

    with conditional(CONDITION, CONTEXTMANAGER()):
        BODY()

API Documentation
=================

.. function:: conditional(condition, contextmanager)

    Wrap a context manager and enter it only if condition is true.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

