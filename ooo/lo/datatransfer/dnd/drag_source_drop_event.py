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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from .drag_source_event import DragSourceEvent as DragSourceEvent_8ccf115c
import typing


class DragSourceDropEvent(DragSourceEvent_8ccf115c):
    """
    Struct Class

    The DragSourceDropEvent is delivered from an object that implements XDragSourceContext to its currently registered drag source listener's.
    
    It contains sufficient information for the originator of the operation to provide appropriate feedback to the end user when the operation completes.

    See Also:
        `API DragSourceDropEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragSourceDropEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DragSourceDropEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DragSourceDropEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DragSourceDropEvent``"""

    def __init__(self, DropAction: int = 0, DropSuccess: bool = False, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``DropAction`` can be another ``DragSourceDropEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            DropAction (int, optional): DropAction value
            DropSuccess (bool, optional): DropSuccess value
        """
        super().__init__(**kwargs)
        if isinstance(DropAction, DragSourceDropEvent):
            oth: DragSourceDropEvent = DropAction
            self._drop_action = oth.DropAction
            self._drop_success = oth.DropSuccess
            return
        else:
            self._drop_action = DropAction
            self._drop_success = DropSuccess



    @property
    def DropAction(self) -> int:
        """
        The action performed by the target on the subject of the drop.
        """
        return self._drop_action
    
    @DropAction.setter
    def DropAction(self, value: int) -> None:
        self._drop_action = value

    @property
    def DropSuccess(self) -> bool:
        """
        Indicates if the drop was successful.
        """
        return self._drop_success
    
    @DropSuccess.setter
    def DropSuccess(self, value: bool) -> None:
        self._drop_success = value


__all__ = ['DragSourceDropEvent']