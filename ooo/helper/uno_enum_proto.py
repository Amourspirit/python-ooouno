from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Protocol
else:
    Protocol = object

class UnoEnumProto(Protocol):
    typeName: str
    value: Any
    
    def __init__(self, *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, that: Any) -> bool: ...
    def __ne__(self,other: Any) -> bool: ...