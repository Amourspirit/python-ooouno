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
import os
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class LinguServiceEvent(EventObject_a3d70b03):
    """
    Struct Class

    represents a linguistic service event.
    
    This type of event may be broadcast by a spell checker or hyphenator service implementation to inform its listeners (clients) that the results of previous function calls may be different now. It is possible to suggest that hyphenation should be done again and/or the spelling of previously incorrect or correct words should be checked again.

    See Also:
        `API LinguServiceEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1LinguServiceEvent.html>`_


    Note:
        | At runtime LinguServiceEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | LinguServiceEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, nEvent: typing.Optional[int] = None):
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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global LinguServiceEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('nEvent',)
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.linguistic2.LinguServiceEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        LinguServiceEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['LinguServiceEvent']
