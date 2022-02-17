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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing


class LinguServiceEvent(EventObject_a3d70b03):
    """
    Struct Class

    represents a linguistic service event.
    
    This type of event may be broadcast by a spell checker or hyphenator service implementation to inform its listeners (clients) that the results of previous function calls may be different now. It is possible to suggest that hyphenation should be done again and/or the spelling of previously incorrect or correct words should be checked again.

    See Also:
        `API LinguServiceEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1LinguServiceEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.LinguServiceEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.linguistic2.LinguServiceEvent'
    """Literal Constant ``com.sun.star.linguistic2.LinguServiceEvent``"""

    def __init__(self, nEvent: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``nEvent`` can be another ``LinguServiceEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            nEvent (int, optional): nEvent value
        """
        super().__init__(**kwargs)
        if isinstance(nEvent, LinguServiceEvent):
            oth: LinguServiceEvent = nEvent
            self._n_event = oth.nEvent
            return
        else:
            self._n_event = nEvent



    @property
    def nEvent(self) -> int:
        """
        The type of event.
        
        The value may be combined via logical OR from those values defined in com.sun.star.linguistic2.LinguServiceEventFlags
        """
        return self._n_event
    
    @nEvent.setter
    def nEvent(self, value: int) -> None:
        self._n_event = value


__all__ = ['LinguServiceEvent']