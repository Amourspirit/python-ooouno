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
# Namespace: com.sun.star.linguistic2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_lingu_service_event_listener import XLinguServiceEventListener as XLinguServiceEventListener_fda313e5

class XLinguServiceEventBroadcaster(XInterface_8f010a43):
    """
    is used to register a listener for LinguServiceEvents.
    
    This interface may be used by spell checker or hyphenator implementations to allow clients to be registered and informed about com.sun.star.linguistic2.LinguServiceEvents.
    
    Note: The LinguServiceManager forwards the com.sun.star.linguistic2.LinguServiceEvents it receives (from spell checkers or hyphenators) to its own listeners. Thus, there should be no need to register as a listener for a specific implementation./P>

    See Also:
        `API XLinguServiceEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XLinguServiceEventBroadcaster.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XLinguServiceEventBroadcaster'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XLinguServiceEventBroadcaster'

    @abstractmethod
    def addLinguServiceEventListener(self, xLstnr: 'XLinguServiceEventListener_fda313e5') -> bool:
        """
        """
        ...
    @abstractmethod
    def removeLinguServiceEventListener(self, xLstnr: 'XLinguServiceEventListener_fda313e5') -> bool:
        """
        """
        ...

__all__ = ['XLinguServiceEventBroadcaster']

