# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.system
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class SystemShellExecuteException(Exception_85530a09):
    """
    Exception Class

    May be thrown in cases of errors executing a command using the SystemShellExecute service.
    
    com.sun.star.uno.Exception.Message may contain a system error message, but it is not mandatory. The member PosixError specifies a POSIX conforming error code or -1 for unknown errors.

    See Also:
        `API SystemShellExecuteException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1system_1_1SystemShellExecuteException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.system'
    __ooo_full_ns__: str = 'com.sun.star.system.SystemShellExecuteException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.system.SystemShellExecuteException'
    __pyunostruct__: str = 'com.sun.star.system.SystemShellExecuteException'

    typeName: str = 'com.sun.star.system.SystemShellExecuteException'
    """Literal Constant ``com.sun.star.system.SystemShellExecuteException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, PosixError: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            PosixError (int, optional): PosixError value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "PosixError": PosixError,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._posix_error = kwargs["PosixError"]
        inst_keys = ('PosixError',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def PosixError(self) -> int:
        """
        A POSIX conforming error code or -1 for unknown errors.
        """
        return self._posix_error
    
    @PosixError.setter
    def PosixError(self, value: int) -> None:
        self._posix_error = value


