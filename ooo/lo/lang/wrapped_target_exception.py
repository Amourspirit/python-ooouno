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
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class WrappedTargetException(Exception_85530a09):
    """
    Exception Class

    This is a checked exception that wraps an exception thrown by the original target.
    
    Normally this exception is declared for generic methods.

    See Also:
        `API WrappedTargetException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.WrappedTargetException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.lang.WrappedTargetException'
    __pyunostruct__: str = 'com.sun.star.lang.WrappedTargetException'

    typeName: str = 'com.sun.star.lang.WrappedTargetException'
    """Literal Constant ``com.sun.star.lang.WrappedTargetException``"""

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


