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

The *conditional* context manager comes handy when you want to always
execute a with block, but only conditionally want to apply its context
manager.

Examples
========

In this example os.system should always be called, but the ignoresignals
context manager should only be entered if has_pager returns a true value::

    if has_pager(cmd):
        with ignoresignals():
            os.system(cmd)
    else:
        os.system(cmd)

Using conditional we can write this without duplicating the statement body::

    from conditional import conditional

    with conditional(has_pager(cmd), ignoresignals()):
        os.system(cmd)

