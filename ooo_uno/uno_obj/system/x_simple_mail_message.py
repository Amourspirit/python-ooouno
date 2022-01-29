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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.system
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSimpleMailMessage(XInterface_8f010a43):
    """
    This interface lets a client set or get the information of a simple mail message.

    See Also:
        `API XSimpleMailMessage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1system_1_1XSimpleMailMessage.html>`_
    """

    @abstractmethod
    def getAttachement(self) -> 'typing.List[str]':
        """
        To get the attachment of a simple mail message.
        """
    @abstractmethod
    def getBccRecipient(self) -> 'typing.List[str]':
        """
        To get the BCC recipients of a simple mail message.
        
        If no BCC recipients have been specified an empty sequence will be returned.
        """
    @abstractmethod
    def getCcRecipient(self) -> 'typing.List[str]':
        """
        To get the cc recipients of a simple mail message.
        
        If no cc recipients have been specified an empty sequence will be returned.
        """
    @abstractmethod
    def getOriginator(self) -> str:
        """
        To get the email address of the originator of a simple mail message.
        
        If no originator has been specified an empty string will be returned.
        """
    @abstractmethod
    def getRecipient(self) -> str:
        """
        To get the recipient of the simple mail message.
        """
    @abstractmethod
    def getSubject(self) -> str:
        """
        To get the subject of a simple mail message.
        
        If no subject has been specified an empty string will be returned.
        """
    @abstractmethod
    def setAttachement(self, aAttachement: 'typing.List[str]') -> None:
        """
        To set an attachment of a simple mail message.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setBccRecipient(self, aBccRecipient: 'typing.List[str]') -> None:
        """
        To set the BCC recipient of a simple mail message.
        """
    @abstractmethod
    def setCcRecipient(self, aCcRecipient: 'typing.List[str]') -> None:
        """
        To set the cc recipients of a simple mail message.
        
        The method does not check if the given addresses are valid. An empty sequence means there are no cc recipients.
        """
    @abstractmethod
    def setOriginator(self, aOriginator: str) -> None:
        """
        To set the email address of the originator of a simple mail message.
        """
    @abstractmethod
    def setRecipient(self, aRecipient: str) -> None:
        """
        To set the recipient of the simple mail message.
        """
    @abstractmethod
    def setSubject(self, aSubject: str) -> None:
        """
        To set the subject of a simple mail message.
        """

__all__ = ['XSimpleMailMessage']

