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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.connection.acceptor import Acceptor as Acceptor
except ImportError:
    pass
try:
    from ...dyn.connection.already_accepting_exception import AlreadyAcceptingException as AlreadyAcceptingException
except ImportError:
    pass
try:
    from ...dyn.connection.connection_setup_exception import ConnectionSetupException as ConnectionSetupException
except ImportError:
    pass
try:
    from ...dyn.connection.connector import Connector as Connector
except ImportError:
    pass
try:
    from ...dyn.connection.no_connect_exception import NoConnectException as NoConnectException
except ImportError:
    pass
try:
    from ...dyn.connection.socket_permission import SocketPermission as SocketPermission
except ImportError:
    pass
try:
    from ...dyn.connection.x_acceptor import XAcceptor as XAcceptor
except ImportError:
    pass
try:
    from ...dyn.connection.x_connection import XConnection as XConnection
except ImportError:
    pass
try:
    from ...dyn.connection.x_connection2 import XConnection2 as XConnection2
except ImportError:
    pass
try:
    from ...dyn.connection.x_connection_broadcaster import XConnectionBroadcaster as XConnectionBroadcaster
except ImportError:
    pass
try:
    from ...dyn.connection.x_connector import XConnector as XConnector
except ImportError:
    pass
