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
# Namespace: com.sun.star.mail
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..datatransfer.x_transferable import XTransferable as XTransferable_2d800f38


class MailAttachment(object):
    """
    Struct Class

    A MailAttachment specifies a mail message attachment.
    
    **since**
    
        OOo 2.0

    See Also:
        `API MailAttachment <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mail_1_1MailAttachment.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mail'
    __ooo_full_ns__: str = 'com.sun.star.mail.MailAttachment'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.mail.MailAttachment'
    """Literal Constant ``com.sun.star.mail.MailAttachment``"""

    def __init__(self, Data: XTransferable_2d800f38 = None, ReadableName: str = '') -> None:
        """
        Constructor

        Other Arguments:
            ``Data`` can be another ``MailAttachment`` instance,
                in which case other named args are ignored.

        Arguments:
            Data (XTransferable, optional): Data value
            ReadableName (str, optional): ReadableName value
        """
        if isinstance(Data, MailAttachment):
            oth: MailAttachment = Data
            self._data = oth.Data
            self._readable_name = oth.ReadableName
            return
        else:
            self._data = Data
            self._readable_name = ReadableName



    @property
    def Data(self) -> XTransferable_2d800f38:
        """
        The actual data which should be attached to a mail message.
        
        It is expected that the transferable delivers the data as sequence of bytes. Although a transferable may support multiple data flavors only the first data flavor supplied will be used to retrieve the data and it is expected that the type of the data is a sequence of bytes.
        """
        return self._data
    
    @Data.setter
    def Data(self, value: XTransferable_2d800f38) -> None:
        self._data = value

    @property
    def ReadableName(self) -> str:
        """
        The name of the attachment as seen by the recipient of the mail message.
        
        ReadableName must not be empty.
        """
        return self._readable_name
    
    @ReadableName.setter
    def ReadableName(self, value: str) -> None:
        self._readable_name = value


__all__ = ['MailAttachment']
