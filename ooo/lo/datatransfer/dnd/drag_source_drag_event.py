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
from .drag_source_event import DragSourceEvent as DragSourceEvent_8ccf115c


class DragSourceDragEvent(DragSourceEvent_8ccf115c):
    """
    Struct Class

    The DragSourceDragEvent is delivered from an object that implements the XDragSourceContext to the currently registered drag source listener.
    
    It contains state regarding the current state of the operation to enable the operations initiator to provide the end user with the appropriate drag over feedback.

    See Also:
        `API DragSourceDragEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragSourceDragEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DragSourceDragEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DragSourceDragEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DragSourceDragEvent``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DragSourceDragEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DragSourceDragEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            DropAction (int, optional): DropAction value
            UserAction (int, optional): UserAction value
        """
        self._drop_action = None
        self._user_action = None

        key_order = ('DropAction', 'UserAction')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DragSourceDragEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DragSourceDragEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def DropAction(self) -> int:
        """
        The drag action selected by the current drop target.
        """
        return self._drop_action
    
    @DropAction.setter
    def DropAction(self, value: int) -> None:
        self._drop_action = value

    @property
    def UserAction(self) -> int:
        """
        The user's currently selected drop action.
        """
        return self._user_action
    
    @UserAction.setter
    def UserAction(self, value: int) -> None:
        self._user_action = value


__all__ = ['DragSourceDragEvent']
