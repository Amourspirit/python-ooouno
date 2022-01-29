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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ItemStatus(object):
    """
    Struct Class

    describes a state of a property.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ItemStatus <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ItemStatus.html>`_


    Note:
        | At runtime ItemStatus will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ItemStatus is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, State: typing.Optional[int] = None, aStateData: typing.Optional[object] = None):
        self._state = State
        self._a_state_data = aStateData

    @property
    def State(self) -> int:
        """
        numerical value which describes the current state of an item.
        """
        return self._state
    
    @State.setter
    def State(self, value: int) -> None:
        self._state = value

    @property
    def aStateData(self) -> object:
        """
        optional data which can be used by an implementation to send additional information.
        
        The content is dependent on the specific implementation.
        """
        return self._a_state_data
    
    @aStateData.setter
    def aStateData(self, value: object) -> None:
        self._a_state_data = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ItemStatus
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('State', 'aStateData')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.frame.status.ItemStatus')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ItemStatus = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ItemStatus']
