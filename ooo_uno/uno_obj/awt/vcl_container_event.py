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
if typing.TYPE_CHECKING:
    from ..uno.x_interface import XInterface as XInterface_8f010a43
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class VclContainerEvent(EventObject_a3d70b03):
        """
        Struct Class

        specifies a container event.
        
        These events are provided only for notification purposes.

        See Also:
            `API VclContainerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1VclContainerEvent.html>`_


        Note:
            | At runtime VclContainerEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | VclContainerEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Child: 'typing.Optional[XInterface_8f010a43]' = None):
            self._child = Child

        @property
        def Child(self) -> 'XInterface_8f010a43':
            """
            returns the child component that was added or removed.
            """
            return self._child
        
        @Child.setter
        def Child(self, value: 'XInterface_8f010a43') -> None:
            self._child = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global VclContainerEvent
        order = ('Child',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.VclContainerEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        VclContainerEvent = _struct_init

    _dynamic_struct()

__all__ = ['VclContainerEvent']
