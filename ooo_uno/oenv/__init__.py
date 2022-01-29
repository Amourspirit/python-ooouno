# coding: utf-8
try:
    import uno
except ImportError:
    pass
import sys
from typing import TYPE_CHECKING
UNO_ENVIRONMENT = False
if not TYPE_CHECKING:
    UNO_ENVIRONMENT = ('uno' in sys.modules and hasattr(
        sys.modules['uno'], 'getComponentContext')) and callable(sys.modules['uno'].getComponentContext)

__all__ = ['UNO_ENVIRONMENT']
