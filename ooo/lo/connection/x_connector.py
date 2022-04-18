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
# Libre Office Version: 7.3
# Namespace: com.sun.star.connection
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection import XConnection as XConnection_f2320da0

class XConnector(XInterface_8f010a43):
    """
    allows to actively establish an interprocess connection.

    See Also:
        `API XConnector <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1connection_1_1XConnector.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.connection'
    __ooo_full_ns__: str = 'com.sun.star.connection.XConnector'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.connection.XConnector'

    @abstractmethod
    def connect(self, sConnectionDescription: str) -> 'XConnection_f2320da0':
        """
        creates a new connection interprocess connection.
        
        Tries to connect to an XAcceptor. Behavior is unspecified if a call to connect is made when another call to connect either has not yet returned or has returned successfully without raising an exception.

        Raises:
            NoConnectException: ``NoConnectException``
            ConnectionSetupException: ``ConnectionSetupException``
        """

__all__ = ['XConnector']

