import os

from typing import Iterator, ContextManager, Optional, Any

from contextlib import contextmanager
from conditional import conditional


@contextmanager
def setenv(key: str, value: str) -> Iterator[str]:
    saved = os.environ.get(key)
    os.environ[key] = value
    yield value
    if saved is not None:
        os.environ[key] = saved
    else:
        del os.environ[key]


@contextmanager
def setint(key: str, value: int) -> Iterator[int]:
    saved = os.environ.get(key)
    os.environ[key] = str(value)
    yield value
    if saved is not None:
        os.environ[key] = saved
    else:
        del os.environ[key]


class setbool(ContextManager[bool]):
    key: str
    value: bool
    saved: Optional[str]

    def __init__(self, key: str, value: bool) -> None:
        self.key = key
        self.value = value

    def __enter__(self) -> bool:
        self.saved = os.environ.get(self.key)
        os.environ[self.key] = str(self.value)
        return self.value

    def __exit__(self, *args: object) -> Optional[bool]:
        if self.saved is not None:
            os.environ[self.key] = self.saved
        else:
            del os.environ[self.key]
        return None


class inverted(conditional[Any]):
    def __init__(self, condition: Optional[Any], contextmanager: ContextManager[Any]) -> None:
        return super(inverted, self).__init__(not condition, contextmanager)


def f() -> None:
    with setenv('foo', '23') as n:
        n is None
        n == '23'
        n == 23

    with conditional(True, setenv('foo', '23')) as n:
        n is None
        n == '23'
        n == 23

    with conditional(None, setenv('foo', '23')) as n:
        n is None
        n == '23'
        n == 23

    with conditional([1, 2, 3], setenv('foo', '23')) as n:
        n is None
        n == '23'
        n == 23

    with conditional(True, setint('bar', 42)) as n:
        n is None
        n == 42
        n == '42'

    with conditional(True, setbool('baz', True)) as n:
        n is None
        n == False
        n == '42'

    with conditional(True, contextmanager=None) as n:
        n is None
