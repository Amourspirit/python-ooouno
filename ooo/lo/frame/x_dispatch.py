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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_status_listener import XStatusListener as XStatusListener_e2740d35
    from ..util.url import URL as URL_57ad07b9

class XDispatch(XInterface_8f010a43):
    """
    serves state information of objects which can be connected to controls (e.g.
    
    toolbox controls).
    
    Each state change is to be broadcasted to all registered status listeners. The first notification should be performed synchronously from XDispatch.addStatusListener(); if not, controls may flicker. State listener must be aware of this synchronous notification.
    
    The state consists of enabled/disabled and a short descriptive text of the function (e.g. \"undo insert character\"). It is to be broadcasted whenever this state changes or the control should re-get the value for the URL it is connected to. Additionally, a context-switch-event is to be broadcasted whenever the object may be out of scope, to force the state listener to requery the XDispatch.

    See Also:
        `API XDispatch <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatch.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDispatch'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDispatch'

    @abstractmethod
    def addStatusListener(self, Control: 'XStatusListener_e2740d35', URL: 'URL_57ad07b9') -> None:
        """
        registers a listener of a control for a specific URL at this object to receive status events.
        
        It is only allowed to register URLs for which this XDispatch was explicitly queried. Additional arguments (\"#...\" or \"?...\") will be ignored.
        
        Note: Notifications can't be guaranteed! This will be a part of interface XNotifyingDispatch.
        """
        ...
    @abstractmethod
    def dispatch(self, URL: 'URL_57ad07b9', Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        dispatches (executes) a URL
        
        It is only allowed to dispatch URLs for which this XDispatch was explicitly queried. Additional arguments (\"'#...\" or \"?...\") are allowed.
        
        Controlling synchronous or asynchronous mode happens via readonly boolean Flag SynchronMode
        
        By default, and absent any arguments, \"SynchronMode\" is considered FALSE and the execution is performed asynchronously (i.e. dispatch() returns immediately, and the action is performed in the background). But when set to TRUE, dispatch() processes the request synchronously
        
        some code for a click-handler (Java)
        """
        ...
    @abstractmethod
    def removeStatusListener(self, Control: 'XStatusListener_e2740d35', URL: 'URL_57ad07b9') -> None:
        """
        unregisters a listener from a control.
        """
        ...

__all__ = ['XDispatch']

