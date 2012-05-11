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
execute a with block, but only conditionally want to apply its context
manager.

Examples
========

If you find yourself writing code like this::

    if has_pager(cmd):
        with ignoresignals():
            os.system(cmd)
    else:
        os.system(cmd)

Consider replacing it with::

    from conditional import conditional

    with conditional(has_pager(cmd), ignoresignals()):
        os.system(cmd)

