===========
conditional
===========
-------------------------------------------------------------------
Conditionally enter a context manager
-------------------------------------------------------------------

Package Contents
================

conditional(condition, contextmanager)
    Enter contextmanager only if condition is true.

Overview
========

The `conditional` context manager comes handy when you always want to
execute a with-block but only conditionally want to apply its context
manager.

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

Typing
======

The context manager ships with type annotations. Type checkers and IDEs can
use this information to implement type safety and auto completion.

Examples
========

Say we want to ignore signals when a pager application is in the
foreground, but not otherwise:

.. code-block:: python

    from conditional import conditional

    with conditional(has_pager(cmd), ignoresignals()):
        os.system(cmd)

Documentation
=============

For further details please refer to the `API Documentation`_.

.. _`API Documentation`: https://conditional.readthedocs.io/en/stable/

