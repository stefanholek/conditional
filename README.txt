===========
conditional
===========
-------------------------------------------------------------------
Conditionally enter context managers
-------------------------------------------------------------------

Package Contents
================

conditional(condition, contextmanager)
    Enter contextmanager only if condition is true.

Overview
========

The *conditional* context manager comes handy when you want to always
execute a with block, but only conditionally apply its context
manager.

Examples
========

Using conditional you can write code like this::

    from conditional import conditional

    with conditional(has_pager(cmd), ignoresignals()):
        os.system(cmd)

Which is equivalent to::

    if has_pager(cmd):
        with ignoresignals():
            os.system(cmd)
    else:
        os.system(cmd)

