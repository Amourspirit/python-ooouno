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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
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

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, State: typing.Optional[PrintableState_c9fb0c65] = PrintableState_c9fb0c65.JOB_STARTED) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            State (PrintableState, optional): State value.
        """

        if isinstance(Source, PrintableStateEvent):
            oth: PrintableStateEvent = Source
            self.Source = oth.Source
            self.State = oth.State
            return

        kargs = {
            "Source": Source,
            "State": State,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._state = kwargs["State"]
        inst_keys = ('State',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


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
