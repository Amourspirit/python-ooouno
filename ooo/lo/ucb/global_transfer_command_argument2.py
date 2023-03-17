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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from .global_transfer_command_argument import GlobalTransferCommandArgument as GlobalTransferCommandArgument_9ae711da
from .transfer_command_operation import TransferCommandOperation as TransferCommandOperation_486a0ff7
import typing


class GlobalTransferCommandArgument2(GlobalTransferCommandArgument_9ae711da):
    """
    Struct Class

    This struct extends the one for transfers arguments by adding a Mime type and a Document Id property to it.

    See Also:
        `API GlobalTransferCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1GlobalTransferCommandArgument2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.GlobalTransferCommandArgument2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.GlobalTransferCommandArgument2'
    """Literal Constant ``com.sun.star.ucb.GlobalTransferCommandArgument2``"""

    def __init__(self, Operation: typing.Optional[TransferCommandOperation_486a0ff7] = TransferCommandOperation_486a0ff7.COPY, SourceURL: typing.Optional[str] = '', TargetURL: typing.Optional[str] = '', NewTitle: typing.Optional[str] = '', NameClash: typing.Optional[int] = 0, MimeType: typing.Optional[str] = '', DocumentId: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Operation (TransferCommandOperation, optional): Operation value.
            SourceURL (str, optional): SourceURL value.
            TargetURL (str, optional): TargetURL value.
            NewTitle (str, optional): NewTitle value.
            NameClash (int, optional): NameClash value.
            MimeType (str, optional): MimeType value.
            DocumentId (str, optional): DocumentId value.
        """

        if isinstance(Operation, GlobalTransferCommandArgument2):
            oth: GlobalTransferCommandArgument2 = Operation
            self.Operation = oth.Operation
            self.SourceURL = oth.SourceURL
            self.TargetURL = oth.TargetURL
            self.NewTitle = oth.NewTitle
            self.NameClash = oth.NameClash
            self.MimeType = oth.MimeType
            self.DocumentId = oth.DocumentId
            return

        kargs = {
            "Operation": Operation,
            "SourceURL": SourceURL,
            "TargetURL": TargetURL,
            "NewTitle": NewTitle,
            "NameClash": NameClash,
            "MimeType": MimeType,
            "DocumentId": DocumentId,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mime_type = kwargs["MimeType"]
        self._document_id = kwargs["DocumentId"]
        inst_keys = ('MimeType', 'DocumentId')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the source object.
        """
        return self._mime_type
    
    @MimeType.setter
    def MimeType(self, value: str) -> None:
        self._mime_type = value

    @property
    def DocumentId(self) -> str:
        """
        contains the DocumentId of the source object.
        """
        return self._document_id
    
    @DocumentId.setter
    def DocumentId(self, value: str) -> None:
        self._document_id = value


__all__ = ['GlobalTransferCommandArgument2']
