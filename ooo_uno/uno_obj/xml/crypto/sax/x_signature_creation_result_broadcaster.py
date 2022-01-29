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
# Namespace: com.sun.star.xml.crypto.sax
import typing
from abc import abstractmethod
from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_signature_creation_result_listener import XSignatureCreationResultListener as XSignatureCreationResultListener_c35f17a6

class XSignatureCreationResultBroadcaster(XInterface_8f010a43):
    """
    Interface of Signature Creation Result Broadcaster.
    
    This interface is used to manipulate signature creation result listener.

    See Also:
        `API XSignatureCreationResultBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XSignatureCreationResultBroadcaster.html>`_
    """

    @abstractmethod
    def addSignatureCreationResultListener(self, listener: 'XSignatureCreationResultListener_c35f17a6') -> None:
        """
        Adds a new signature creation result listener.
        
        When the signature is created, the result information will be sent to this listener.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def removeSignatureCreationResultListener(self, listener: 'XSignatureCreationResultListener_c35f17a6') -> None:
        """
        Removes a signature creation result listener.
        
        After a listener is removed, no result information will be sent to it.
        """

__all__ = ['XSignatureCreationResultBroadcaster']

