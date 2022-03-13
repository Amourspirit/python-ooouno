import os
import sys
import pytest
import tempfile
import time
import shutil
from pathlib import Path
from .lo import LoSocketStart, LoPipeStart
from unotools import Pipe, Socket, connect_with_pipe, connect_with_socket
from unotools.unohelper import convert_path_to_url
from unotools.component.writer import Writer
sys.path.insert(0, os.path.abspath('.'))
from . import unohlp as d_lib
# from ooo.dyn.connection.no_connect_exception import NoConnectException
from com.sun.star.connection import NoConnectException

_PIPE_NAME = None

@pytest.fixture(autouse=True, scope='module')
def set_default_doc_scope():
    os.environ['doc_scope'] = 'module'


@pytest.fixture(autouse=True, scope='module')
def slow_down_tests():
    yield
    time.sleep(1.2)


@pytest.fixture(scope='function')
def f_slow_down_tests():
    yield
    time.sleep(0.7)

@pytest.fixture(scope='session')
def tmp_path_soffice():
    result = Path(tempfile.mkdtemp())
    yield result
    if os.path.exists(result):
        shutil.rmtree(result)

#project_root
@pytest.fixture(scope='session')
def lo_cache_path(project_root) -> str:
    root = Path(project_root)
    p = root / 'tests' / 'fixture' / 'LO' / '6x'
    return str(p)

@pytest.fixture(scope='session')
def start_soffice(tmp_path_soffice, lo_cache_path: str) -> LoPipeStart:
    global _PIPE_NAME

    lo = LoPipeStart(cache_path=lo_cache_path,
                     working_dir=str(tmp_path_soffice))
    lo.connect()
    _PIPE_NAME = lo.pipe_name
    yield lo
    lo.kill_soffice()


@pytest.fixture(scope='module')
def start_soffice_port(tmp_path_soffice, lo_cache_path: str) -> LoSocketStart:
    LoSocketStart.PORT_NUM+= 1
    lo = LoSocketStart(cache_path=lo_cache_path,
                       working_dir=str(tmp_path_soffice), port=LoSocketStart.PORT_NUM)
    try:
        lo.connect()
    except Exception as e:
        lo.kill_soffice()
        raise e
    yield lo
    lo.kill_soffice()

# region get writer internal methods
def _writer_create_instance(start_soffice, file_path=None, set_lib=True):
    def _wait_for_doc(instance: Writer):
        '''
        Waits for current writer document to become avaialble to read.
        @instance: current instance of `Writer` Class
        @return: `True` if document becomes available; Otherwise, `False`
        '''
        _frame_try_count = 20
        _frame_try_sleep = 0.5
        result = False
        for i in range(_frame_try_count):
            frm = instance.desktop.getCurrentFrame()
            if frm is None:
                time.sleep(_frame_try_sleep)
            else:
                result = True
                break
            if i == _frame_try_count - 1:
                break
            # print("wait_for_doc(): ", i)
        if result:
            return
        raise TimeoutError(
            "wait_for_doc() Not able to find document window")
    # writer = Writer(start_soffice.ctx)
    # writer = Writer(connect_with_socket(Socket(start_soffice.host, start_soffice.port)))
    if file_path:
        url = convert_path_to_url(file_path)
        writer = Writer(connect_with_pipe(
            Pipe(start_soffice.pipe_name)), url)
    else:
        try:
            writer = Writer(connect_with_pipe(Pipe(start_soffice.pipe_name)))
        except NoConnectException:
            writer = Writer(connect_with_pipe(Pipe(start_soffice.pipe_name)))
    _wait_for_doc(writer)
    if set_lib == True:
        d_lib.set_globals(desktop=writer.desktop,
                                sm=writer.context.getServiceManager())
    return writer


def _reset_ooo_cache():
    d_lib.reset_cached()

# endregion get writer internal methods

# region writer module level
@pytest.fixture(scope='module')
def writer_factory(start_soffice, reset_cache_values):
    def _create_instance(file_path=None, set_lib=True):
        return _writer_create_instance(start_soffice=start_soffice, file_path=file_path, set_lib=set_lib)
    return _create_instance


@pytest.fixture(scope='module')
def reset_cache_values():
    _reset_ooo_cache()


@pytest.fixture(scope='module')
def get_writer(writer_factory):
    writer = writer_factory(file_path=None, set_lib=True)
    yield writer
    writer.close(False)
    writer = None

@pytest.fixture(scope='module')
def get_desktop(get_writer):
    return d_lib.get_desktop()

@pytest.fixture(scope='module')
def get_xframe(get_desktop):
    frame = get_desktop.getCurrentFrame()
    return frame


@pytest.fixture(scope='module')
def get_document(get_xframe):
    model = get_xframe.getController().getModel()
    return model
    
# endregion writer module level

# region writer function level


@pytest.fixture(scope='function')
def f_reset_cache_values():
    _reset_ooo_cache()

@pytest.fixture(scope="function")
def f_writer_factory(start_soffice, f_reset_cache_values):
    def _create_instance(file_path=None, set_lib=True):
        return _writer_create_instance(start_soffice=start_soffice, file_path=file_path, set_lib=set_lib)
    return _create_instance


@pytest.fixture(scope='function')
def f_get_writer(f_writer_factory, f_slow_down_tests):
    writer = f_writer_factory(file_path=None, set_lib=True)
    yield writer
    writer.close(False)
    writer = None


# endregion writer function level

