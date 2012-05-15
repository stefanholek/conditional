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

The *conditional* context manager comes handy when you always want to
execute a with-block but only conditionally want to apply its context
manager.

If you find yourself writing code like this::

    if CONDITION:
        with CONTEXTMANAGER():
            BODY()
    else:
        BODY()

Consider replacing it with::

    with conditional(CONDITION, CONTEXTMANAGER()):
        BODY()

Examples
========

Say we want to ignore signals when a pager application is in the
foreground, but not otherwise::

    from conditional import conditional

    with conditional(has_pager(cmd), ignoresignals()):
        os.system(cmd)
