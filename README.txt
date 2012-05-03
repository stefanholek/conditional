===========
conditional
===========
-------------------------------------------------------------------
Wrap another context manager and enter it only if condition is true
-------------------------------------------------------------------

Package Contents
================

conditional(condition, contextmanager)
    Enter contextmanager only if condition is true.

Overview
========

Lorem ipsum.

Examples
========

conditional is used like this::

    from conditional import conditional

    with conditional(should_ignore_signals(cmd), ignoresignals()):
        os.system(cmd)

In the above example os.system is always called, but the ignoresignals context
manager is only entered (and exited) if should_ignore_signals returns True.

