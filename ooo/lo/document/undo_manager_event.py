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
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class UndoManagerEvent(EventObject_a3d70b03):
    """
    Struct Class

    is an event sent by an XUndoManager implementation when the Undo/Redo stacks of the manager are modified.
    
    **since**
    
        OOo 3.4

    See Also:
        `API UndoManagerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1UndoManagerEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.UndoManagerEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.UndoManagerEvent'
    """Literal Constant ``com.sun.star.document.UndoManagerEvent``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``UndoManagerEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``UndoManagerEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            UndoActionTitle (str, optional): UndoActionTitle value
            UndoContextDepth (int, optional): UndoContextDepth value
        """
        self._undo_action_title = None
        self._undo_context_depth = None

        key_order = ('UndoActionTitle', 'UndoContextDepth')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], UndoManagerEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("UndoManagerEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def UndoActionTitle(self) -> str:
        """
        the title of the undo action which is described by the event
        """
        return self._undo_action_title
    
    @UndoActionTitle.setter
    def UndoActionTitle(self, value: str) -> None:
        self._undo_action_title = value

    @property
    def UndoContextDepth(self) -> int:
        """
        denotes the number of Undo contexts which are open, and not yet closed, at the time the event is fired.
        """
        return self._undo_context_depth
    
    @UndoContextDepth.setter
    def UndoContextDepth(self, value: int) -> None:
        self._undo_context_depth = value


__all__ = ['UndoManagerEvent']
