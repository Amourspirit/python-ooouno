# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
from .sql_warning import SQLWarning as SQLWarning_96f10a6a
from ..uno.x_interface import XInterface as XInterface_8f010a43

class DataTruncation(SQLWarning_96f10a6a):
    """
    Exception Class

    reports a DataTruncation warning, on reads, or is thrown as a DataTruncation exception, on writes, when a data value is unexpectedly truncated.
    
    The SQL state for a DataTruncation is 01004.

    See Also:
        `API DataTruncation <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdbc_1_1DataTruncation.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.DataTruncation'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdbc.DataTruncation'
    __pyunostruct__: str = 'com.sun.star.sdbc.DataTruncation'

    typeName: str = 'com.sun.star.sdbc.DataTruncation'
    """Literal Constant ``com.sun.star.sdbc.DataTruncation``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, SQLState: typing.Optional[str] = '', ErrorCode: typing.Optional[int] = 0, NextException: typing.Optional[object] = None, Index: typing.Optional[int] = 0, IsParameter: typing.Optional[bool] = False, DuringRead: typing.Optional[bool] = False, DataSize: typing.Optional[int] = 0, TransferSize: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
            Index (int, optional): Index value.
            IsParameter (bool, optional): IsParameter value.
            DuringRead (bool, optional): DuringRead value.
            DataSize (int, optional): DataSize value.
            TransferSize (int, optional): TransferSize value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "SQLState": SQLState,
            "ErrorCode": ErrorCode,
            "NextException": NextException,
            "Index": Index,
            "IsParameter": IsParameter,
            "DuringRead": DuringRead,
            "DataSize": DataSize,
            "TransferSize": TransferSize,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._index = kwargs["Index"]
        self._is_parameter = kwargs["IsParameter"]
        self._during_read = kwargs["DuringRead"]
        self._data_size = kwargs["DataSize"]
        self._transfer_size = kwargs["TransferSize"]
        inst_keys = ('Index', 'IsParameter', 'DuringRead', 'DataSize', 'TransferSize')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Index(self) -> int:
        """
        is the index of the parameter or column value.
        """
        return self._index
    
    @Index.setter
    def Index(self, value: int) -> None:
        self._index = value

    @property
    def IsParameter(self) -> bool:
        """
        is TRUE if a parameter value is truncated.
        """
        return self._is_parameter
    
    @IsParameter.setter
    def IsParameter(self, value: bool) -> None:
        self._is_parameter = value

    @property
    def DuringRead(self) -> bool:
        """
        is TRUE if a read was truncated.
        """
        return self._during_read
    
    @DuringRead.setter
    def DuringRead(self, value: bool) -> None:
        self._during_read = value

    @property
    def DataSize(self) -> int:
        """
        contains the number of bytes of data that should have been transferred.
        
        This number may be approximate if data conversions were being performed. The value may be -1 if the size is unknown.
        """
        return self._data_size
    
    @DataSize.setter
    def DataSize(self, value: int) -> None:
        self._data_size = value

    @property
    def TransferSize(self) -> int:
        """
        contains the number of bytes of data actually transferred.
        
        The value may be -1 if the size is unknown.
        """
        return self._transfer_size
    
    @TransferSize.setter
    def TransferSize(self, value: int) -> None:
        self._transfer_size = value


__all__ = ['DataTruncation']

