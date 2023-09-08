import sys

from typing import TypeVar, ContextManager
from typing import Optional, Any

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")


class conditional(ContextManager[_T]):
    condition: Optional[Any]
    contextmanager: ContextManager[_T]

    def __init__(self, condition: Optional[Any], contextmanager: ContextManager[_T]) -> None: ...

    def __enter__(self) -> _T: ...

    def __exit__(self, *args: object) -> Optional[bool]: ...

    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, params: Any) -> GenericAlias: ...
