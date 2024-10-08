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
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from .transfer_info import TransferInfo as TransferInfo_a4600b13
import typing


class TransferInfo2(TransferInfo_a4600b13):
    """
    Struct Class

    extends TransferInfo structure to give some additional parameters for transfers.

    See Also:
        `API TransferInfo2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferInfo2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.TransferInfo2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.TransferInfo2'
    """Literal Constant ``com.sun.star.ucb.TransferInfo2``"""

    def __init__(self, MoveData: typing.Optional[bool] = False, SourceURL: typing.Optional[str] = '', NewTitle: typing.Optional[str] = '', NameClash: typing.Optional[int] = 0, MimeType: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            MoveData (bool, optional): MoveData value.
            SourceURL (str, optional): SourceURL value.
            NewTitle (str, optional): NewTitle value.
            NameClash (int, optional): NameClash value.
            MimeType (str, optional): MimeType value.
        """

        if isinstance(MoveData, TransferInfo2):
            oth: TransferInfo2 = MoveData
            self.MoveData = oth.MoveData
            self.SourceURL = oth.SourceURL
            self.NewTitle = oth.NewTitle
            self.NameClash = oth.NameClash
            self.MimeType = oth.MimeType
            return

        kargs = {
            "MoveData": MoveData,
            "SourceURL": SourceURL,
            "NewTitle": NewTitle,
            "NameClash": NameClash,
            "MimeType": MimeType,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mime_type = kwargs["MimeType"]
        inst_keys = ('MimeType',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the source of the action
        """
        return self._mime_type

    @MimeType.setter
    def MimeType(self, value: str) -> None:
        self._mime_type = value


__all__ = ['TransferInfo2']
