# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.connection.acceptor import Acceptor as Acceptor
with suppress(ImportError):
    from ...dyn.connection.already_accepting_exception import AlreadyAcceptingException as AlreadyAcceptingException
with suppress(ImportError):
    from ...dyn.connection.connection_setup_exception import ConnectionSetupException as ConnectionSetupException
with suppress(ImportError):
    from ...dyn.connection.connector import Connector as Connector
with suppress(ImportError):
    from ...dyn.connection.no_connect_exception import NoConnectException as NoConnectException
with suppress(ImportError):
    from ...dyn.connection.socket_permission import SocketPermission as SocketPermission
with suppress(ImportError):
    from ...dyn.connection.x_acceptor import XAcceptor as XAcceptor
with suppress(ImportError):
    from ...dyn.connection.x_connection import XConnection as XConnection
with suppress(ImportError):
    from ...dyn.connection.x_connection2 import XConnection2 as XConnection2
with suppress(ImportError):
    from ...dyn.connection.x_connection_broadcaster import XConnectionBroadcaster as XConnectionBroadcaster
with suppress(ImportError):
    from ...dyn.connection.x_connector import XConnector as XConnector
