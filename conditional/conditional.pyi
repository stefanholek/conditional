from typing import TypeVar, ContextManager
from typing import Optional, Any

_T = TypeVar("_T")


class conditional(ContextManager[_T]):
    condition: Optional[Any]
    contextmanager: ContextManager[_T]

    def __init__(self, condition: Optional[Any], contextmanager: ContextManager[_T]) -> None: ...

    def __enter__(self) -> _T: ...

    def __exit__(self, *args: object) -> Optional[bool]: ...
