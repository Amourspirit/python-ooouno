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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
import uno
from .sql_exception import SQLException as SQLException_acc90b43
from ..uno.x_interface import XInterface as XInterface_8f010a43

class BatchUpdateException(SQLException_acc90b43):
    """
    Exception Class

    is thrown when an error occurs during a batch update operation.
    
    In addition to the information provided by com.sun.star.sdbc.SQLException , a BatchUpdateException provides the update counts for all commands that were executed successfully during the batch update, that is, all commands that were executed before the error occurred. The order of elements in an array of update counts corresponds to the order in which commands were added to the batch.

    See Also:
        `API BatchUpdateException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdbc_1_1BatchUpdateException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.BatchUpdateException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdbc.BatchUpdateException'
    __pyunostruct__: str = 'com.sun.star.sdbc.BatchUpdateException'

    typeName: str = 'com.sun.star.sdbc.BatchUpdateException'
    """Literal Constant ``com.sun.star.sdbc.BatchUpdateException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, SQLState: typing.Optional[str] = '', ErrorCode: typing.Optional[int] = 0, NextException: typing.Optional[object] = None, UpdateCounts: typing.Optional[uno.ByteSequence] = ()) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
            UpdateCounts (uno.ByteSequence, optional): UpdateCounts value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "SQLState": SQLState,
            "ErrorCode": ErrorCode,
            "NextException": NextException,
            "UpdateCounts": UpdateCounts,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._update_counts = kwargs["UpdateCounts"]
        inst_keys = ('UpdateCounts',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def UpdateCounts(self) -> uno.ByteSequence:
        """
        is an array of long , with each element indicating the update count for a SQL command that executed successfully before the exception was thrown.
        """
        return self._update_counts
    
    @UpdateCounts.setter
    def UpdateCounts(self, value: uno.ByteSequence) -> None:
        self._update_counts = value


__all__ = ['BatchUpdateException']

