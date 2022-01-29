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
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection import XConnection as XConnection_a36a0b0c
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XIsolatedConnection(XInterface_8f010a43):
    """
    is used for establishing isolated connections via a factory.
    
    The XIsolatedConnection allows to create connections which are not shared among others as it is the case when creating connections in normal way.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XIsolatedConnection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XIsolatedConnection.html>`_
    """

    @abstractmethod
    def getIsolatedConnection(self, user: str, password: str) -> 'XConnection_a36a0b0c':
        """
        attempts to establish a database connection.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def getIsolatedConnectionWithCompletion(self, handler: 'XInteractionHandler_bf80e51') -> 'XConnection_a36a0b0c':
        """
        attempts to establish a database connection.
        
        If information is missing, such as a user's password, they are completed by user interaction.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XIsolatedConnection']

