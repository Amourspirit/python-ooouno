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
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_model import XModel as XModel_7a6e095c
    from ..ucb.x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78

class XTransientDocumentsDocumentContentIdentifierFactory(XInterface_8f010a43):
    """
    a factory for identifiers of com.sun.star.ucb.TransientDocumentsDocumentContents.
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API XTransientDocumentsDocumentContentIdentifierFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XTransientDocumentsDocumentContentIdentifierFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XTransientDocumentsDocumentContentIdentifierFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XTransientDocumentsDocumentContentIdentifierFactory'

    @abstractmethod
    def createDocumentContentIdentifier(self, Model: 'XModel_7a6e095c') -> 'XContentIdentifier_edc90d78':
        """
        creates a com.sun.star.ucb.XContentIdentifier based on a given com.sun.star.document.OfficeDocument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XTransientDocumentsDocumentContentIdentifierFactory']

