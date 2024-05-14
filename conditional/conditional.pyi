import sys

from typing import Any, AsyncContextManager, ContextManager, Optional, Type, TypeVar
from types import TracebackType

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")


class conditional(ContextManager[_T], AsyncContextManager[_T]):
    condition: Optional[Any]
    contextmanager: ContextManager[_T] | AsyncContextManager[_T]

    def __init__(
        self,
        condition: Optional[Any],
        contextmanager: ContextManager[_T] | AsyncContextManager[_T],
    ) -> None: ...

    def __enter__(self) -> _T: ...

    async def __aenter__(self) -> _T: ...

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]: ...

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]: ...

    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, params: Any) -> GenericAlias: ...
