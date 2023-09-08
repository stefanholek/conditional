import sys
import os

from typing import TYPE_CHECKING
from typing import Iterator, ContextManager, Optional, Any

from contextlib import contextmanager
from conditional import conditional

if sys.version_info >= (3, 9):
    from types import GenericAlias


@contextmanager
def setstr(key: str, value: str) -> Iterator[str]:
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

    def __exit__(self, *exc_info: object) -> Optional[bool]:
        if self.saved is not None:
            os.environ[self.key] = self.saved
        else:
            del os.environ[self.key]
        return None


class inverted(conditional[Any]):
    def __init__(self, condition: Optional[Any], contextmanager: ContextManager[Any]) -> None:
        super().__init__(not condition, contextmanager)

    @classmethod
    def __class_getitem__(cls, params: Any) -> GenericAlias:
        return super().__class_getitem__(params)


def f() -> None:
    with setstr('foo', '23') as n:
        n is None
        n == '23'

    with conditional(True, setstr('foo', '23')) as n:
        n is None
        n == '23'

    with conditional(None, setstr('foo', '23')) as n:
        n is None
        n == '23'

    with conditional([1, 2, 3], setstr('foo', '23')) as n:
        n is None
        n == '23'

    with conditional(True, setint('bar', 42)) as n:
        n is None
        n == 42

    with conditional(True, setbool('baz', True)) as n:
        n is None
        n == True
        assert n is True

    with inverted(False, setbool('baz', True)) as n:
        n is None
        n == True
        assert n is True

    assert issubclass(inverted, conditional)


def g() -> None:
    c = conditional(True, setstr('foo', '23'))
    c.condition == True
    c.contextmanager is None

    assert os.environ.get('foo') is None

    n = c.__enter__()
    n == '23'
    assert n == '23'
    assert os.environ.get('foo') == '23'

    c.__exit__(None, None, None)

    assert os.environ.get('foo') is None

    c.__exit__(RuntimeError, None, None)
    c.__exit__(None, RuntimeError(), None)


def h() -> None:
    c = conditional(True, setbool('foo', True))
    c.condition == True
    c.contextmanager is None

    assert os.environ.get('foo') is None

    n = c.__enter__()
    n == True
    assert n == True
    assert os.environ.get('foo') == 'True'

    c.__exit__(None, None, None)

    assert os.environ.get('foo') is None

    if TYPE_CHECKING:
        c.__exit__(RuntimeError, None, None)
        c.__exit__(None, RuntimeError(), None)


def i() -> None:
    c = conditional(False, setbool('foo', True))
    c.condition == False

    assert os.environ.get('foo') is None

    with c as n:
        n == None
        assert n == None
        assert os.environ.get('foo') is None


if __name__ == '__main__':
    f()
    g()
    h()
    i()
