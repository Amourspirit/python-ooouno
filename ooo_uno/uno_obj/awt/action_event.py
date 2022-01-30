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


    class ActionEvent(EventObject_a3d70b03):
        """
        Struct Class

        a semantic event which indicates that a component-defined action occurred.
        
        This high-level event is generated by a component (such as a Button) when the component-specific action occurs (such as being pressed). The event is passed to every XActionListener object that registered to receive such events using the component's addActionListener method.
        
        The object that implements the XActionListener interface gets this ActionEvent when the event occurs. The listener is therefore spared the details of processing individual mouse movements and mouse clicks, and can instead process a \"meaningful\" (semantic) event like \"button pressed\".

        See Also:
            `API ActionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ActionEvent.html>`_


        Note:
            | At runtime ActionEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | ActionEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, ActionCommand: typing.Optional[str] = None):
            self._action_command = ActionCommand

        @property
        def ActionCommand(self) -> str:
            """
            contains the command string associated with this action.
            """
            return self._action_command
        
        @ActionCommand.setter
        def ActionCommand(self, value: str) -> None:
            self._action_command = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global ActionEvent
        order = ('ActionCommand',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.ActionEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ActionEvent = _struct_init

    _dynamic_struct()

__all__ = ['ActionEvent']
