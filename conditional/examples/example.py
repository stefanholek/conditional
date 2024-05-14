import os

from typing import TYPE_CHECKING
from typing import Any, AsyncContextManager, ContextManager, Iterator, Optional, TypeVar

from contextlib import contextmanager
from conditional import conditional


@contextmanager
def setstr(key: str, value: str) -> Iterator[str]:
    saved = os.environ.get(key)
    os.environ[key] = value
    try:
        yield value
    finally:
        if saved is not None:
            os.environ[key] = saved
        else:
            del os.environ[key]


@contextmanager
def setint(key: str, value: int) -> Iterator[int]:
    saved = os.environ.get(key)
    os.environ[key] = str(value)
    try:
        yield value
    finally:
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


if TYPE_CHECKING:
    class setfloat(ContextManager[setfloat]):
        key: str
        value: float
        saved: Optional[str]

        def __init__(self, key: str, value: float) -> None:
            pass

        def __enter__(self) -> setfloat:
            return self

        def __exit__(self, *exc_info: object) -> Optional[bool]:
            return None

    class asetfloat(AsyncContextManager[asetfloat]):
        key: str
        value: float
        saved: Optional[str]

        def __init__(self, key: str, value: float) -> None:
            pass

        async def __aenter__(self) -> asetfloat:
            return self

        async def __aexit__(self, *exc_info: object) -> Optional[bool]:
            return None


# Inherit from conditional
_T = TypeVar('_T')


class inverted(conditional[_T]):
    def __init__(self, condition: Optional[Any], contextmanager: ContextManager[_T]) -> None:
        super().__init__(not condition, contextmanager)


def f() -> None:
    with setstr('foo', '23') as n:
        n == None
        n == '23'
        assert n == '23'

    with conditional(True, setstr('foo', '23')) as n:
        n == None
        n == '23'
        assert n == '23'

    with conditional(None, setstr('foo', '23')) as n:
        n == None
        n == '23'
        assert n == None

    with conditional([1, 2, 3], setstr('foo', '23')) as n:
        n == None
        n == '23'
        assert n == '23'

    with conditional(False, setstr('foo', '23')) as n:
        n == None
        n == '23'
        assert n == None

    with conditional(True, setint('bar', 42)) as n:
        n == None
        n == 42
        assert n == 42

    with inverted(False, setint('bar', 42)) as n:
        n == None
        n == 42
        assert n == 42

    with conditional(True, setbool('baz', True)) as n:
        n == None
        n == True
        assert n == True

    with inverted(False, setbool('baz', True)) as n:
        n == None
        n == True
        assert n == True

    with conditional[str](True, setstr('foo', '23')) as n:
        n == None
        n == '23'
        assert n == '23'

    with inverted[bool](False, setbool('baz', True)) as n:
        n == None
        n == True
        assert n == True

    assert issubclass(inverted, conditional)


if TYPE_CHECKING:
    with conditional(True, setfloat('quux', 42.0)) as c:
        c == None
        c.key == 'quux'
        c.value == 42.0
        c.saved == None
        c.saved == ''
        c.__enter__
        c.__exit__

    with inverted(False, setfloat('quux', 42.0)) as c:
        c == None
        c.key == 'quux'
        c.value == 42.0
        c.saved == None
        c.saved == ''
        c.__enter__
        c.__exit__

    async def a() -> None:
        async with conditional(True, asetfloat('quux', 42.0)) as c:
            c == None
            c.key == 'quux'
            c.value == 42.0
            c.saved == None
            c.saved == ''
            c.__aenter__
            c.__aexit__


if TYPE_CHECKING:
    conditional.__class_getitem__(None)
    inverted.__class_getitem__(None)


def g() -> None:
    c = conditional(True, setstr('foo', '23'))
    c.condition == True
    c.contextmanager == None

    assert os.environ.get('foo') is None

    n = c.__enter__()
    n == '23'
    try:
        assert n == '23'
        assert os.environ.get('foo') == '23'
    finally:
        c.__exit__(None, None, None)

    assert os.environ.get('foo') is None

    c.__exit__(RuntimeError, None, None)
    c.__exit__(None, RuntimeError(), None)


def h() -> None:
    c = conditional(True, setbool('foo', True))
    c.condition == True
    c.contextmanager == None

    assert os.environ.get('foo') is None

    n = c.__enter__()
    n == True
    try:
        assert n == True
        assert os.environ.get('foo') == 'True'
    finally:
        c.__exit__(None, None, None)

    assert os.environ.get('foo') is None

    if TYPE_CHECKING:
        c.__exit__(RuntimeError, None, None)
        c.__exit__(None, RuntimeError(), None)


if __name__ == '__main__':
    f()
    g()
    h()
