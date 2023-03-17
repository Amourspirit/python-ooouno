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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.runtime_exception import RuntimeException as RuntimeException_d7390ced
from ..uno.x_interface import XInterface as XInterface_8f010a43

class WrappedTargetRuntimeException(RuntimeException_d7390ced):
    """
    Exception Class

    This is a runtime exception that wraps any other exception thrown by the original target.
    
    This exception should not be declared at interfaces, use WrappedTargetException instead. It was defined to transport an exception via interface-methods, that do not specify the appropriate exceptions (so using this exception should in general be avoided).

    See Also:
        `API WrappedTargetRuntimeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetRuntimeException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.WrappedTargetRuntimeException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.lang.WrappedTargetRuntimeException'
    __pyunostruct__: str = 'com.sun.star.lang.WrappedTargetRuntimeException'

    typeName: str = 'com.sun.star.lang.WrappedTargetRuntimeException'
    """Literal Constant ``com.sun.star.lang.WrappedTargetRuntimeException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, TargetException: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TargetException (object, optional): TargetException value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "TargetException": TargetException,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._target_exception = kwargs["TargetException"]
        inst_keys = ('TargetException',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def TargetException(self) -> object:
        """
        The exception is thrown by the target.
        """
        return self._target_exception
    
    @TargetException.setter
    def TargetException(self, value: object) -> None:
        self._target_exception = value


__all__ = ['WrappedTargetRuntimeException']

