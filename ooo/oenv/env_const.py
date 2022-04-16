# coding: utf-8
try:
    import uno
except ImportError:
    pass
import sys
import os
from typing import TYPE_CHECKING

UNO_ENVIRONMENT = False
if not TYPE_CHECKING:
    UNO_ENVIRONMENT = (
        "uno" in sys.modules and hasattr(sys.modules["uno"], "getComponentContext")
    ) and callable(sys.modules["uno"].getComponentContext)

UNO_RUNTIME = (
    False
    if (
        UNO_ENVIRONMENT is False
        or os.environ.get("ooouno_ignore_runtime", None) == "True"
    )
    else True
)

UNO_NONE = object()

__all__ = ["UNO_ENVIRONMENT", "UNO_RUNTIME", "UNO_NONE"]
