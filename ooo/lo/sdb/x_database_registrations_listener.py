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
# Namespace: com.sun.star.sdb
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .database_registration_event import DatabaseRegistrationEvent as DatabaseRegistrationEvent_56721053

class XDatabaseRegistrationsListener(XEventListener_c7230c4a):
    """
    implemented by components which want to be notified of changes in the application-wide registered databases.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XDatabaseRegistrationsListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XDatabaseRegistrationsListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XDatabaseRegistrationsListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XDatabaseRegistrationsListener'

    @abstractmethod
    def changedDatabaseLocation(self, Event: 'DatabaseRegistrationEvent_56721053') -> None:
        """
        called when the location of a registered database changed
        
        Note that this talks about registration data only. That is, if the actual file denoted by the database registration is moved, this is in no way monitored or reported. Only (successful) calls to XDatabaseRegistrations.changeDatabaseLocation() are reported here.
        """
    @abstractmethod
    def registeredDatabaseLocation(self, Event: 'DatabaseRegistrationEvent_56721053') -> None:
        """
        called when a database has been registered
        """
    @abstractmethod
    def revokedDatabaseLocation(self, Event: 'DatabaseRegistrationEvent_56721053') -> None:
        """
        called when a database registration has been revoked
        """

__all__ = ['XDatabaseRegistrationsListener']

