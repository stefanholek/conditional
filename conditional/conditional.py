"""Conditionally enter a context manager."""

import sys

if sys.version_info >= (3, 9):
    from types import GenericAlias


class conditional(object):
    """Wrap another context manager and enter it only if condition is true.
    """

    def __init__(self, condition, contextmanager):
        self.condition = condition
        self.contextmanager = contextmanager

    def __enter__(self):
        if self.condition:
            return self.contextmanager.__enter__()

    async def __aenter__(self):
        if self.condition:
            return await self.contextmanager.__aenter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.condition:
            return self.contextmanager.__exit__(exc_type, exc_val, exc_tb)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.condition:
            return await self.contextmanager.__aexit__(exc_type, exc_val, exc_tb)

    if sys.version_info >= (3, 9):
        __class_getitem__ = classmethod(GenericAlias)
