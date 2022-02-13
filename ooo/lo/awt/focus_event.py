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
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class FocusEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a keyboard focus event.
    
    There are two levels of focus change events: permanent and temporary. Permanent focus change events occur when focus is directly moved from one component to another, such as through calls to requestFocus() or as the user uses the Tab key to traverse components. Temporary focus change events occur when focus is gained or lost for a component as the indirect result of another operation, such as window deactivation or a scrollbar drag. In this case, the original focus state will automatically be restored once that operation is finished, or for the case of window deactivation, when the window is reactivated. Both permanent and temporary focus events are delivered using the FOCUS_GAINED and FOCUS_LOST event ids; the levels may be distinguished in the event using the isTemporary() method.

    See Also:
        `API FocusEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1FocusEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.FocusEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.FocusEvent'
    """Literal Constant ``com.sun.star.awt.FocusEvent``"""

    def __init__(self, FocusFlags: int = 0, NextFocus: XInterface_8f010a43 = None, Temporary: bool = False, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``FocusFlags`` can be another ``FocusEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            FocusFlags (int, optional): FocusFlags value
            NextFocus (XInterface, optional): NextFocus value
            Temporary (bool, optional): Temporary value
        """
        super().__init__(**kwargs)
        if isinstance(FocusFlags, FocusEvent):
            oth: FocusEvent = FocusFlags
            self._focus_flags = oth.FocusFlags
            self._next_focus = oth.NextFocus
            self._temporary = oth.Temporary
            return
        else:
            self._focus_flags = FocusFlags
            self._next_focus = NextFocus
            self._temporary = Temporary



    @property
    def FocusFlags(self) -> int:
        """
        specifies the reason for the focus change as an arithmetic-or combination of FocusChangeReason.
        """
        return self._focus_flags
    
    @FocusFlags.setter
    def FocusFlags(self, value: int) -> None:
        self._focus_flags = value

    @property
    def NextFocus(self) -> XInterface_8f010a43:
        """
        contains the window which gets the focus on a lose focus event.
        """
        return self._next_focus
    
    @NextFocus.setter
    def NextFocus(self, value: XInterface_8f010a43) -> None:
        self._next_focus = value

    @property
    def Temporary(self) -> bool:
        """
        specifies if this focus change event is a temporary change.
        """
        return self._temporary
    
    @Temporary.setter
    def Temporary(self, value: bool) -> None:
        self._temporary = value


__all__ = ['FocusEvent']
