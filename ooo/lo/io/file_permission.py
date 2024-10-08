# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.io
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class FilePermission(object):
    """
    Struct Class

    This permission represents access to a file or directory.
    
    A FilePermission consists of a file url and a set of actions valid for that url.
    
    The path of the file url that ends in \"/*\" indicates all the files and directories contained in that directory. A path that ends with \"/-\" indicates (recursively) all files and subdirectories contained in that directory. A file url string consisting of the special token \"<<ALL FILES>>\" matches any file. Note: A file url string consisting of a single \"*\" indicates all the files in the current directory, while a string consisting of a single \"-\" indicates all the files in the current directory and (recursively) all files and subdirectories contained in the current directory. The actions to be granted is a list of one or more comma-separated keywords. The possible keywords are \"read\", \"write\", \"execute\", and \"delete\". Their meaning is defined as follows:
    
    The actions string is processed case-insensitive.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API FilePermission <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1io_1_1FilePermission.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.FilePermission'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.io.FilePermission'
    """Literal Constant ``com.sun.star.io.FilePermission``"""

    def __init__(self, URL: typing.Optional[str] = '', Actions: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            URL (str, optional): URL value.
            Actions (str, optional): Actions value.
        """
        super().__init__()

        if isinstance(URL, FilePermission):
            oth: FilePermission = URL
            self.URL = oth.URL
            self.Actions = oth.Actions
            return

        kargs = {
            "URL": URL,
            "Actions": Actions,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._url = kwargs["URL"]
        self._actions = kwargs["Actions"]


    @property
    def URL(self) -> str:
        """
        target file url
        """
        return self._url

    @URL.setter
    def URL(self, value: str) -> None:
        self._url = value

    @property
    def Actions(self) -> str:
        """
        comma separated actions list
        """
        return self._actions

    @Actions.setter
    def Actions(self, value: str) -> None:
        self._actions = value


__all__ = ['FilePermission']
