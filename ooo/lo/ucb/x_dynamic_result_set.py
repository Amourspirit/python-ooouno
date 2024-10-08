# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..sdbc.x_result_set import XResultSet as XResultSet_98e30aa7
    from .x_dynamic_result_set_listener import XDynamicResultSetListener as XDynamicResultSetListener_56e41050

class XDynamicResultSet(XComponent_98dc0ab5):
    """
    Provides read access to a ContentResultSet.
    
    You can either get a simple static ContentResultSet or you can listen to change-notifications and then swap from the old to a new ContentResultSet.
    
    The following describes the dynamic use:
    
    XDynamicResultSet provides the possibility to get notifications about changes on a ContentResultSet and have an listener-controlled update from one version to the next version. Two ContentResultSet implementations were given to the listener in the first notification as interface com.sun.star.sdbc.XResultSet.
    
    To get notifications the listener has to be of type XDynamicResultSetListener.
    
    After registration you will get notifications for events of type ListEvent.
    
    The calling of XDynamicResultSetListener.notify() has to happen in an own thread, because it could take a longer time and any actions ??? until the listener returns the call. So don't block the notify-causing action.
    
    While one notify-call is going on:
    
    After the listener has returned the notify-call:

    See Also:
        `API XDynamicResultSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XDynamicResultSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XDynamicResultSet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XDynamicResultSet'

    @abstractmethod
    def connectToCache(self, Cache: XDynamicResultSet) -> None:
        """
        Connects this to a CachedDynamicResultSet for optimized remote data transport.
        
        This method creates a CachedDynamicResultSetStub and sets it as Source to the given cache.
        
        After this method has returned you can and have to use the given result set cache for further access.

        Raises:
            : ````
            : ````
            com.sun.star.ucb.ServiceNotFoundException: ``ServiceNotFoundException``
        """
        ...
    @abstractmethod
    def getCapabilities(self) -> int:
        """
        Using this method you can get information, whether the offered ContentResultSets are sorted or filtered etc correctly as demanded during the creation of the XDynamicResultSet.
        """
        ...
    @abstractmethod
    def getStaticResultSet(self) -> XResultSet_98e30aa7:
        """
        Call this, if you don't care about any changes.

        Raises:
            com.sun.star.ucb.ListenerAlreadySetException: ``ListenerAlreadySetException``
        """
        ...
    @abstractmethod
    def setListener(self, Listener: XDynamicResultSetListener_56e41050) -> None:
        """
        Call this, if you want to get notifications about changes.
        
        The implementor has to call com.sun.star.lang.XComponent.addEventListener() in this method, so that we can call com.sun.star.lang.XEventListener.disposing() at the listener

        Raises:
            com.sun.star.ucb.ListenerAlreadySetException: ``ListenerAlreadySetException``
        """
        ...

__all__ = ['XDynamicResultSet']

