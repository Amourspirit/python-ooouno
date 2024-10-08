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
# Namespace: com.sun.star.document
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class OwnLockOnDocumentRequest(Exception_85530a09):
    """
    Exception Class

    Is used for interaction handle to query user decision regarding locked document.
    
    **since**
    
        OOo 3.1

    See Also:
        `API OwnLockOnDocumentRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1OwnLockOnDocumentRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.OwnLockOnDocumentRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.document.OwnLockOnDocumentRequest'
    __pyunostruct__: str = 'com.sun.star.document.OwnLockOnDocumentRequest'

    typeName: str = 'com.sun.star.document.OwnLockOnDocumentRequest'
    """Literal Constant ``com.sun.star.document.OwnLockOnDocumentRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, DocumentURL: typing.Optional[str] = '', TimeInfo: typing.Optional[str] = '', IsStoring: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            DocumentURL (str, optional): DocumentURL value.
            TimeInfo (str, optional): TimeInfo value.
            IsStoring (bool, optional): IsStoring value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "DocumentURL": DocumentURL,
            "TimeInfo": TimeInfo,
            "IsStoring": IsStoring,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._document_url = kwargs["DocumentURL"]
        self._time_info = kwargs["TimeInfo"]
        self._is_storing = kwargs["IsStoring"]
        inst_keys = ('DocumentURL', 'TimeInfo', 'IsStoring')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def DocumentURL(self) -> str:
        """
        The URL of the locked document.
        """
        return self._document_url
    
    @DocumentURL.setter
    def DocumentURL(self, value: str) -> None:
        self._document_url = value

    @property
    def TimeInfo(self) -> str:
        """
        The time from which the document is locked.
        """
        return self._time_info
    
    @TimeInfo.setter
    def TimeInfo(self, value: str) -> None:
        self._time_info = value

    @property
    def IsStoring(self) -> bool:
        """
        Whether the request is related to storing process.
        """
        return self._is_storing
    
    @IsStoring.setter
    def IsStoring(self, value: bool) -> None:
        self._is_storing = value


__all__ = ['OwnLockOnDocumentRequest']

