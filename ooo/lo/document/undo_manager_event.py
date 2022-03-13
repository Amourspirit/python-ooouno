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
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


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

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, UndoActionTitle: typing.Optional[str] = '', UndoContextDepth: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            UndoActionTitle (str, optional): UndoActionTitle value.
            UndoContextDepth (int, optional): UndoContextDepth value.
        """

        if isinstance(Source, UndoManagerEvent):
            oth: UndoManagerEvent = Source
            self.Source = oth.Source
            self.UndoActionTitle = oth.UndoActionTitle
            self.UndoContextDepth = oth.UndoContextDepth
            return

        kargs = {
            "Source": Source,
            "UndoActionTitle": UndoActionTitle,
            "UndoContextDepth": UndoContextDepth,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._undo_action_title = kwargs["UndoActionTitle"]
        self._undo_context_depth = kwargs["UndoContextDepth"]
        inst_keys = ('UndoActionTitle', 'UndoContextDepth')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


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
