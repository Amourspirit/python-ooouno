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
# Namespace: com.sun.star.task
# Libre Office Version: 7.2
import typing
from .classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..security.document_signature_information import DocumentSignatureInformation as DocumentSignatureInformation_f36c13f7

class DocumentMacroConfirmationRequest(ClassifiedInteractionRequest_9f72121b):
    """
    describes the request to approve or deny the execution of macros contained in a document.

    See Also:
        `API DocumentMacroConfirmationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentMacroConfirmationRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.DocumentMacroConfirmationRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.DocumentMacroConfirmationRequest'
    __pyunostruct__: str = 'com.sun.star.task.DocumentMacroConfirmationRequest'

    typeName: str = 'com.sun.star.task.DocumentMacroConfirmationRequest'
    """Literal Constant ``com.sun.star.task.DocumentMacroConfirmationRequest``"""

    DocumentStorage: 'XStorage_8e460a32' = None
    """
        refers to the storage related to the last committed version of the document.
        
        This storage is necessary e.g. for displaying the existing signatures to the user, to allow him a decision whether or not to trust those signatures and thus the signed macros.
    """

    DocumentURL: str = None
    """
        specifies the URL of the document which contains macros whose execution should be approved or rejected.
    """

    DocumentVersion: str = None
    """
        contains information about the ODF version of the document
    """

    DocumentSignatureInformation: 'typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]' = None
    """
    contains information about the signatures in the document
    """


