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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .interactive_io_exception import InteractiveIOException as InteractiveIOException_27a60f07
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from .io_error_code import IOErrorCode as IOErrorCode_96ab0a5f

class InteractiveAugmentedIOException(InteractiveIOException_27a60f07):
    """
    Exception Class

    An input/output error with arguments.

    See Also:
        `API InteractiveAugmentedIOException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1InteractiveAugmentedIOException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    __pyunostruct__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'

    typeName: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    """Literal Constant ``com.sun.star.ucb.InteractiveAugmentedIOException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Code: typing.Optional[IOErrorCode_96ab0a5f] = IOErrorCode_96ab0a5f.ABORT, Arguments: typing.Optional[typing.Tuple[object, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Code (IOErrorCode, optional): Code value.
            Arguments (typing.Tuple[object, ...], optional): Arguments value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Code": Code,
            "Arguments": Arguments,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._arguments = kwargs["Arguments"]
        inst_keys = ('Arguments',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Arguments(self) -> typing.Tuple[object, ...]:
        """
        Additional arguments.
        
        See com.sun.star.task.InteractionHandler for a description of well-known arguments.
        """
        return self._arguments
    
    @Arguments.setter
    def Arguments(self, value: typing.Tuple[object, ...]) -> None:
        self._arguments = value


__all__ = ['InteractiveAugmentedIOException']

