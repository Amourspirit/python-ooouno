# coding: utf-8
import subprocess
import tempfile
import os
import signal
from typing import Union
import uuid
import time
import uno
import shutil
from kwhelp import KwargsHelper, BeforeAssignEventArgs
from distutils.dir_util import copy_tree
from pathlib import Path
from unotools import Pipe, connect_with_pipe
from unotools.context import LocalContext, ScriptContext
# from com.sun.star.connection import NoConnectException
NoConnectException = uno.getClass('com.sun.star.connection.NoConnectException')


class LoSocketStart(object):
    PORT_NUM = 8100
    def __init__(self, **kwargs):
        '''
        @soffice_path: (optional) Type:str, the path to soffice: Default: `/usr/bin/soffice`
        @cache_path: (optional) Type:str, the path where the current profile resides to copy into the LO
        workding dir for current instance of LO
        @working_dir: (optional) Type:str
        '''
        # https://medium.com/analytics-vidhya/starting-libreoffice-with-python-macro-programming-in-openoffice-libreoffice-with-using-10310f9e69f1
        # https://www.linuxquestions.org/questions/blog/sag47-492023/headless-file-conversion-using-libreoffice-as-a-service-35310/
        self.profile_cached = False
        self._soffice_process = None
        self._soffice_process_shutdown = None
        self._desktop = None
        self._service_manager = None
        self._working_dir = ""
        self._profile_path_user = None
        self._profile_dir_name = 'profile'
        self._profile_user_name = 'user'
        self._soffice_path = '/usr/bin/soffice'
        self._working_dir = ""
        self._cache_path = None
        self._host = 'localhost'
        self._port = 2083
        self._invisible = False
        self._start_as_service = False
        def _kw_cb_before(_, arg: BeforeAssignEventArgs):
            if arg.key == 'soffice_path':
                if isinstance(arg.field_value, Path):
                    arg.field_value = str(arg._field_value)
                if not os.path.exists(arg.field_value):
                    arg.cancel = True
            elif arg.key == 'working_dir':
                if arg.field_value == "":
                    arg.field_value = tempfile.mkdtemp()
            elif arg.key == 'cache_path':
                if arg.field_value is None:
                    arg.field_value = os.getenv(
                        'XDG_CACHE_DIR', f"{os.environ['HOME']}{os.sep}.cache{os.sep}lo_profile_cache")

        # change this path if not the default
        kw = KwargsHelper(originator=self, obj_kwargs={**kwargs})
        kw.add_handler_before_assign(_kw_cb_before)
        kw.assign(key='soffice_path', types=[
                  str], default=self._soffice_path)
        kw.assign(key='working_dir', types=[
                  str], default=self._working_dir)
        kw.assign(key='cache_path', types=[
                  str, None], default=self._cache_path)
        kw.assign(key='port', types=[int], default=self._port)
        self._user_profie = f"{self._working_dir}{os.sep}{self._profile_dir_name}"
        
        self._envirnment = os.environ
        self._envirnment['TMPDIR'] = self._working_dir
        self._conn_try_count = 200
        self._conn_try_time_sleep = 0.1
        self._pid_file = os.path.join(self._working_dir, 'soffice.pid')
        self._script_content: Union[ScriptContext, None] = None

    def _copy_cache_to_profile(self):
        if os.path.isdir(self._cache_path):
            # shutil.copytree(cacheDir, userProfile)
            copy_tree(self._cache_path, self._user_profie)
            self.profile_cached = True
        else:
            os.mkdir(self._user_profie)
            self.profile_cached = False

    def _popen(self, shutdown=False):
        args = [
            self._soffice_path,
            '-env:UserInstallation=file://' + self._user_profie,
            '--pidfile=' + self._pid_file,
            '--norestore',
            # '--nofirststartwizard',
            # '--nologo'
            ]
        if self._invisible:
            args.append('--invisible')
        if shutdown == True:
            prefix = '--unaccept='
        else:
            prefix = '--accept='
        conn_suf = f"socket,host={self._host},port={self._port},tcpNoDelay=1;urp;"
        if self._start_as_service == True:
            conn_suf = conn_suf + 'StarOffice.Service'
        conn = f"{prefix}{conn_suf!r}"
        args.append(conn)
        if shutdown == True:
            self._soffice_process_shutdown = subprocess.Popen(
                args, env=self._envirnment, preexec_fn=os.setsid)
        else:
            self._soffice_process = subprocess.Popen(
                args, env=self._envirnment, preexec_fn=os.setsid)

    def _connect(self):
        
        identifier = f"socket,host={self._host},port={self._port}"
        conn_str = f"uno:{identifier};urp;StarOffice.ServiceManager"
        # ctx = resolver.resolve( "uno:socket, host = localhost, port= 2002; urp; StarOffice.ComponentContext" )
        
        for i in range(self._conn_try_count):
            try:
                localContext = uno.getComponentContext()
                resolver = localContext.ServiceManager.createInstanceWithContext(
                    "com.sun.star.bridge.UnoUrlResolver", localContext)
                smgr = resolver.resolve(conn_str)
                self._script_content = smgr.getPropertyValue("DefaultContext")
                break
            except NoConnectException as e:
                time.sleep(self._conn_try_time_sleep)
                if i == self._conn_try_count - 1:
                    raise e

    def _cache_current_profile(self):
        if self.profile_cached == False:
            copy_tree(self._user_profie, self._cache_path)
     
    def connect(self):
        '''
        Makes a connection to soffice
        @error: Raises NoConnectException if unable to obtain a connection to soffice
        '''
        self._copy_cache_to_profile()
        self._popen()
        try:
            self._connect()
        except NoConnectException as e:
            self.kill_soffice()
            raise e
            
        self._cache_current_profile()

    def get_soffice_pid(self):
        '''
        Gets the pid of soffice
        @return: `int` of pid if found; Otherwise, `None`
        '''
        pid = None
        try:
            with open(self._pid_file, 'r') as f:
                pid = f.read()
                pid = int(pid)
        except:
            pid = None
        return pid

    def check_pid(self, pid: int):
        """ Check For the existence of a unix pid. """
        if pid <= 0:
            return False
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        else:
            return True

    def kill_soffice(self) -> None:
        '''
        Attempts to kill instance of soffice created by this instance
        '''
        try:
            # self._popen(shutdown=True)
            # if self._soffice_process_shutdown:
            #     self._soffice_process_shutdown.kill()
            # if self._soffice_process:
            #     self._soffice_process.kill()
            pid = self.get_soffice_pid()
            if pid is None:
                return None
            # print("pid:", pid)
            if self.check_pid(pid=pid):
                os.kill(pid, signal.SIGKILL)
            # cls.lo_start.soffice_process.kill()
        except Exception as e:
            # print(e)
            raise e

    def del_working_dir(self):
        '''
        Deletes the current working directory of instance
        '''
        if os.path.exists(self.working_dir):
            shutil.rmtree(self.working_dir)

    @property
    def desktop(self):
        if self._desktop is None:
            self._desktop = self.service_manager.createInstanceWithContext(
                "com.sun.star.frame.Desktop", self.ctx)
        return self._desktop

    @property
    def service_manager(self):
        if self._service_manager is None:
            self._service_manager = self.ctx.getServiceManager()
        return self._service_manager

    @property
    def soffice_process(self):
        return self._soffice_process

    @property
    def working_dir(self) -> str:
        return self._working_dir

    @property
    def port(self) -> int:
        return self._port
    
    @property
    def host(self) -> str:
        return self._host

    @property
    def profile_path(self) -> str:
        '''
        Gets the profile path for the current instance. Usually working_dir + '/profile'
        '''
        return self._user_profie

    @property
    def profile_path_user(self):
        '''
        Gets the profile user path for the current instance. Usually working_dir + '/profile/user'
        '''
        if self._profile_path_user is None:
            self._profile_path_user = f"{self.profile_path}{os.sep}{self._profile_user_name}"
        return self._profile_path_user

    @property
    def ctx(self) -> Union[object, None]:
        return self._script_content


class LoPipeStart(object):
    def __init__(self, **kwargs):
        '''
        @soffice_path: (optional) Type:str, the path to soffice: Default: `/usr/bin/soffice`
        @cache_path: (optional) Type:str, the path where the current profile resides to copy into the LO
        workding dir for current instance of LO
        '''
        # https://medium.com/analytics-vidhya/starting-libreoffice-with-python-macro-programming-in-openoffice-libreoffice-with-using-10310f9e69f1
        # https://www.linuxquestions.org/questions/blog/sag47-492023/headless-file-conversion-using-libreoffice-as-a-service-35310/
        self.profile_cached = False
        self._soffice_process = None
        self._soffice_process_shutdown = None
        self._desktop = None
        self._service_manager = None
        self._working_dir = ""
        self._profile_path_user = None
        self._profile_dir_name = 'profile'
        self._profile_user_name = 'user'
        self._soffice_path = '/usr/bin/soffice'
        self._working_dir = ""
        self._cache_path = None
        self._invisible = True
        self._headless = False
        self._start_as_service = False
        def _kw_cb_before(_, arg: BeforeAssignEventArgs):
            if arg.key == 'soffice_path':
                if not os.path.exists(arg.field_value):
                    arg.cancel = True
            elif arg.key == 'working_dir':
                if arg.field_value == "":
                    arg.field_value = tempfile.mkdtemp()
            elif arg.key == 'cache_path':
                if arg.field_value is None:
                    arg.field_value = os.getenv(
                        'XDG_CACHE_DIR', f"{os.environ['HOME']}{os.sep}.cache{os.sep}lo_profile_cache")
        # change this path if not the default
        kw = KwargsHelper(originator=self, obj_kwargs={**kwargs})
        kw.add_handler_before_assign(_kw_cb_before)
        kw.assign(key='soffice_path', types=[str], default=self._soffice_path)
        kw.assign(key='working_dir', types=[str], default=self._working_dir)
        kw.assign(key='cache_path', types=[
                  str, None], default=self._cache_path)
        
        self._user_profie = f"{self._working_dir}{os.sep}{self._profile_dir_name}"

        self._pipe_name = uuid.uuid4().hex
        self._envirnment = os.environ
        self._envirnment['TMPDIR'] = self._working_dir
        self._conn_try_count = 150
        self._conn_try_time_sleep = 0.2
        self._pid_file = os.path.join(self._working_dir, 'soffice.pid')
        self._script_content: Union[ScriptContext, None] = None

    def _copy_cache_to_profile(self):
        if os.path.isdir(self._cache_path):
            # shutil.copytree(cacheDir, userProfile)
            copy_tree(self._cache_path, self._user_profie)
            self.profile_cached = True
        else:
            os.mkdir(self._user_profie)
            self.profile_cached = False

    def _popen(self, **kwargs):
        args = [
            self._soffice_path,
            '-env:UserInstallation=file://' + self._user_profie,
            '--pidfile=' + self._pid_file,
            '--accept=pipe,name=' + self._pipe_name + ';urp;',
            '--norestore',
            '--invisible']
        self._soffice_process = subprocess.Popen(
            args, env=self._envirnment, preexec_fn=os.setsid)
    
    def _popen_new(self, shutdown=False):
        args = [
            self._soffice_path,
            '-env:UserInstallation=file://' + self._user_profie,
            '--pidfile=' + self._pid_file,
            '--norestore',
            '--nofirststartwizard',
            '--nologo'
            # '--writer'
            ]
        if self._invisible:
            args.append('--invisible')
        if self._headless:
            args.append('--headless')
        
        if shutdown == True:
            prefix = '--unaccept='
        else:
            prefix = '--accept='
        conn_suf = f"pipe,name={self._pipe_name};urp;"
        if self._start_as_service == True:
            conn_suf = conn_suf + 'StarOffice.Service'
        conn = f"{prefix}{conn_suf!r}"
        args.append(conn)
        if shutdown == True:
            self._soffice_process_shutdown = subprocess.Popen(
                args, env=self._envirnment, preexec_fn=os.setsid)
        else:
            self._soffice_process = subprocess.Popen(
                args, env=self._envirnment, preexec_fn=os.setsid)

    def _connect_new(self):
        for i in range(self._conn_try_count):
            try:
                localContext = uno.getComponentContext()
                resolver = localContext.ServiceManager.createInstanceWithContext(
                    "com.sun.star.bridge.UnoUrlResolver", localContext)
                if resolver:
                    self._script_content = connect_with_pipe(
                        Pipe(self._pipe_name))
                if self._script_content is None:
                    continue
                break
            except Exception as e:
                time.sleep(self._conn_try_time_sleep)
                if i == self._conn_try_count - 1:
                    raise e

    def _connect(self):
        for i in range(self._conn_try_count):
            try:
                localContext = uno.getComponentContext()
                resolver = localContext.ServiceManager.createInstanceWithContext(
                    "com.sun.star.bridge.UnoUrlResolver", localContext)
                self._script_content = resolver.resolve(
                    "uno:pipe,name=%s;urp;StarOffice.ComponentContext" % self._pipe_name)
                break
            except NoConnectException as e:
                time.sleep(self._conn_try_time_sleep)
                if i == self._conn_try_count - 1:
                    raise e

    def _cache_current_profile(self):
        if self.profile_cached == False:
            copy_tree(self._user_profie, self._cache_path)

    def connect(self):
        '''
        Makes a connection to soffice
        @error: Raises NoConnectException if unable to obtain a connection to soffice
        '''
        self._copy_cache_to_profile()
        self._popen()
        try:
            self._connect()
        except NoConnectException as e:
            self.kill_soffice()
            raise e
        self._cache_current_profile()

    def get_soffice_pid(self):
        '''
        Gets the pid of soffice
        @return: `int` of pid if found; Otherwise, `None`
        '''
        pid = None
        try:
            with open(self._pid_file, 'r') as f:
                pid = f.read()
                pid = int(pid)
        except:
            pid = None
        return pid

    def check_pid(self, pid: int):
        """ Check For the existence of a unix pid. """
        if pid <= 0:
            return False
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        else:
            return True

    def kill_soffice(self) -> None:
        '''
        Attempts to kill instance of soffice created by this instance
        '''
        try:
            self._popen(shutdown=True)
            if self._soffice_process_shutdown:
                self._soffice_process_shutdown.kill()
            if self._soffice_process:
                self._soffice_process.kill()
            if self._soffice_process:
                self._soffice_process.kill()
                
            pid = self.get_soffice_pid()
            if pid is None:
                return None
            # print("pid:", pid)
            if self.check_pid(pid=pid):
                os.kill(pid, signal.SIGKILL)
            # cls.lo_start.soffice_process.kill()
        except Exception as e:
            # print(e)
            raise e

    def del_working_dir(self):
        '''
        Deletes the current working directory of instance
        '''
        if os.path.exists(self.working_dir):
            shutil.rmtree(self.working_dir)

    @property
    def desktop(self):
        if self._desktop is None:
            self._desktop = self.service_manager.createInstanceWithContext(
                "com.sun.star.frame.Desktop", self.ctx)
        return self._desktop

    @property
    def service_manager(self):
        if self._service_manager is None:
            self._service_manager = self.ctx.getServiceManager()
        return self._service_manager

    @property
    def soffice_process(self):
        return self._soffice_process

    @property
    def working_dir(self) -> str:
        return self._working_dir

    @property
    def pipe_name(self) -> str:
        return self._pipe_name

    @property
    def profile_path(self) -> str:
        '''
        Gets the profile path for the current instance. Usually working_dir + '/profile'
        '''
        return self._user_profie

    @property
    def profile_path_user(self):
        '''
        Gets the profile user path for the current instance. Usually working_dir + '/profile/user'
        '''
        if self._profile_path_user is None:
            self._profile_path_user = f"{self.profile_path}{os.sep}{self._profile_user_name}"
        return self._profile_path_user
    
    @property
    def ctx(self) -> Union[ScriptContext, None]:
        return self._script_content
