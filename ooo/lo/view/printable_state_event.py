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
# Namespace: com.sun.star.view
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from .printable_state import PrintableState as PrintableState_c9fb0c65


class PrintableStateEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies the print progress of an XPrintable.
    
    com.sun.star.lang.EventObject.Source contains the XPrintable having changed its state
    
    .

    See Also:
        `API PrintableStateEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1view_1_1PrintableStateEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.PrintableStateEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.view.PrintableStateEvent'
    """Literal Constant ``com.sun.star.view.PrintableStateEvent``"""

    def __init__(self, State: PrintableState_c9fb0c65 = PrintableState_c9fb0c65.JOB_STARTED, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``State`` can be another ``PrintableStateEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            State (PrintableState, optional): State value
        """
        super().__init__(**kwargs)
        if isinstance(State, PrintableStateEvent):
            oth: PrintableStateEvent = State
            self._state = oth.State
            return
        else:
            self._state = State



    @property
    def State(self) -> PrintableState_c9fb0c65:
        """
        contains the current state.
        """
        return self._state
    
    @State.setter
    def State(self, value: PrintableState_c9fb0c65) -> None:
        self._state = value


__all__ = ['PrintableStateEvent']
