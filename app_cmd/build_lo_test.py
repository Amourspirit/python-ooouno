# coding: utf-8
import os
import sys
import subprocess
import __main__
from typing import Union
from config import AppConfig
from pathlib import Path

class builder:
    def __init__(self, config: AppConfig):
        self._config = config
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__main__.__file__).parent
        self._src_file_name = 'lo_test.py'
        self._src_file = self._root_dir / self._src_file_name
        self._dest_dir = self._root_dir / Path(*self._config.tmp_dir)
        self._dest_file = self._dest_dir / self._src_file_name
        self._include_dir = self._root_dir.joinpath(*self._config.inc_dir)
        self._include_file = self._include_dir / 'exports.txt'
        sticky = Path(*self._config.stickytape)
        if sticky.is_absolute():
            self._sticky = sticky
        else:
            self._sticky = self._root_dir.joinpath(sticky)
    
    def mkdirp(dest_dir: Union[str, Path]):
        """
        Creates directory and all child directories if needed

        Args:
            dest_dir (Union[str, Path]): path to create directories for.
                Must be dir path only. No checking is done for file names.
        """
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)
    
    def build(self):
        if not self._dest_dir.exists():
            self.mkdirp(self._dest_dir)
        cmd_str = f"{self._sticky} {self._src_file} --output-file {self._dest_file}"
        cmd = [sys.executable] + cmd_str.split()
        # print(cmd)
        res = subprocess.run(cmd)
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr)
        
        # Append Exports
        with open(self._include_file, 'r') as f:
            ex_contents = f.read()
        
        with open(self._dest_file, "a") as tmpfile:
            tmpfile.write('\n')
            tmpfile.write(ex_contents)
