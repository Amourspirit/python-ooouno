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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class SpinEvent(EventObject_a3d70b03):
        """
        Struct Class

        specifies a spin button event.

        See Also:
            `API SpinEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1SpinEvent.html>`_


        Note:
            | At runtime SpinEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | SpinEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, dummy1: typing.Optional[int] = None):
            self._dummy1 = dummy1

        @property
        def dummy1(self) -> int:
            """
            This is a dummy field only.
            
            Please ignore.
            """
            return self._dummy1
        
        @dummy1.setter
        def dummy1(self, value: int) -> None:
            self._dummy1 = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global SpinEvent
        order = ('dummy1',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.SpinEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        SpinEvent = _struct_init

    _dynamic_struct()

__all__ = ['SpinEvent']
