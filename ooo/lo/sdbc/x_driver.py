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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .driver_property_info import DriverPropertyInfo as DriverPropertyInfo_fd970e01
    from .x_connection import XConnection as XConnection_a36a0b0c

class XDriver(XInterface_8f010a43):
    """
    is the interface that every driver class must implement.
    
    Each driver should supply a service that implements the Driver interface.
    
    The DriverManager will try to load as many drivers as it can find, and then for any given connection request, it will ask each driver in turn to try to connect to the target URL.
    
    It is strongly recommended that each Driver object should be small and standalone so that the Driver object can be loaded and queried without bringing in vast quantities of supporting code.

    See Also:
        `API XDriver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XDriver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XDriver'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XDriver'

    @abstractmethod
    def acceptsURL(self, url: str) -> bool:
        """
        returns TRUE if the driver thinks that it can open a connection to the given URL.
        
        Typically drivers will return TRUE if they understand the subprotocol specified in the URL and FALSE if they do not.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def connect(self, url: str, info: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XConnection_a36a0b0c':
        """
        attempts to make a database connection to the given URL.
        
        The driver should return NULL if it realizes it is the wrong kind of driver to connect to the given URL. This will be common, as when the driver manager is asked to connect to a given URL it passes the URL to each loaded driver in turn.
        
        The driver should raise a com.sun.star.sdbc.SQLException if it is the right driver to connect to the given URL, but has trouble connecting to the database.
        
        The info argument can be used to pass arbitrary string tag/value pairs as connection arguments. Normally at least \"user\" and \"password\" properties should be included in the Properties. For a JDBC driver also the Java class must be supplied in the property named JavaDriverClass, and a class path (a space-separated list of URLs) needed to locate that class can optionally be supplied in a property named JavaDriverClassPath. Possible property value names are when supported by the driver:

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getMajorVersion(self) -> int:
        """
        gets the driver's major version number.
        
        Initially this should be 1.
        """
        ...
    @abstractmethod
    def getMinorVersion(self) -> int:
        """
        gets the driver's minor version number.
        
        Initially this should be 0.
        """
        ...
    @abstractmethod
    def getPropertyInfo(self, url: str, info: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[DriverPropertyInfo_fd970e01, ...]':
        """
        gets information about the possible properties for this driver.
        
        The getPropertyInfo method is intended to allow a generic GUI tool to discover what properties it should prompt a human for in order to get enough information to connect to a database. Note that depending on the values the human has supplied so far, additional values may become necessary, so it may be necessary to iterate though several calls to getPropertyInfo.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XDriver']

