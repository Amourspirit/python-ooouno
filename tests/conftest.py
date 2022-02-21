# coding: utf-8
import sys
from pathlib import Path

import pytest
import gc
import functools
from typing import List, Union
from typing import TYPE_CHECKING


@pytest.fixture(scope='module')
def uno_env() -> bool:
    if TYPE_CHECKING:
        return False
    return ('uno' in sys.modules and hasattr(sys.modules['uno'], 'getComponentContext')) and callable(sys.modules['uno'].getComponentContext)

@pytest.fixture(scope='session')
def clear_lru_cache_cache():
    def _clear():
        gc.collect()
        wrappers = [
            obj for obj in gc.get_objects()
            if isinstance(obj, functools._lru_cache_wrapper)]
        for wrapper in wrappers:
            wrapper.cache_clear()
    return _clear


@pytest.fixture(scope='session')
def project_root() -> str:
    return str(Path(__file__).parent.parent)

@pytest.fixture(scope='session')
def fixture_dir(project_root) -> str:
    return str(Path(project_root, 'tests', 'fixture'))