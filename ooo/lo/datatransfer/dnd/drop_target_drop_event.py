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
from .drop_target_event import DropTargetEvent as DropTargetEvent_8d651169
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..x_transferable import XTransferable as XTransferable_2d800f38
from .x_drop_target_drop_context import XDropTargetDropContext as XDropTargetDropContext_10e81439


class DropTargetDropEvent(DropTargetEvent_8d651169):
    """
    Struct Class

    The DropTargetDropEvent is delivered from the drop target to its currently registered drop target listener.
    
    It contains sufficient information for the originator of the operation to provide appropriate feedback to the end user when the operation completes.

    See Also:
        `API DropTargetDropEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DropTargetDropEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DropTargetDropEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DropTargetDropEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DropTargetDropEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Dummy: typing.Optional[int] = 0, Context: typing.Optional[XDropTargetDropContext_10e81439] = None, DropAction: typing.Optional[int] = 0, LocationX: typing.Optional[int] = 0, LocationY: typing.Optional[int] = 0, SourceActions: typing.Optional[int] = 0, Transferable: typing.Optional[XTransferable_2d800f38] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Dummy (int, optional): Dummy value.
            Context (XDropTargetDropContext, optional): Context value.
            DropAction (int, optional): DropAction value.
            LocationX (int, optional): LocationX value.
            LocationY (int, optional): LocationY value.
            SourceActions (int, optional): SourceActions value.
            Transferable (XTransferable, optional): Transferable value.
        """
        kargs = {
            "Source": Source,
            "Dummy": Dummy,
            "Context": Context,
            "DropAction": DropAction,
            "LocationX": LocationX,
            "LocationY": LocationY,
            "SourceActions": SourceActions,
            "Transferable": Transferable,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._context = kwargs["Context"]
        self._drop_action = kwargs["DropAction"]
        self._location_x = kwargs["LocationX"]
        self._location_y = kwargs["LocationY"]
        self._source_actions = kwargs["SourceActions"]
        self._transferable = kwargs["Transferable"]
        inst_keys = ('Context', 'DropAction', 'LocationX', 'LocationY', 'SourceActions', 'Transferable')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Context(self) -> XDropTargetDropContext_10e81439:
        """
        The drop target context of the current drag operation.
        """
        return self._context
    
    @Context.setter
    def Context(self, value: XDropTargetDropContext_10e81439) -> None:
        self._context = value

    @property
    def DropAction(self) -> int:
        """
        This value represents the action or actions selected by the user at the time of the drop.
        
        If more than one action is specified, the XDropTargetListener should raise a dialog to ask the user which action to use.
        """
        return self._drop_action
    
    @DropAction.setter
    def DropAction(self, value: int) -> None:
        self._drop_action = value

    @property
    def LocationX(self) -> int:
        """
        The cursor's current x location within the window's coordinates.
        """
        return self._location_x
    
    @LocationX.setter
    def LocationX(self, value: int) -> None:
        self._location_x = value

    @property
    def LocationY(self) -> int:
        """
        The cursor's current y location within the window's coordinates.
        """
        return self._location_y
    
    @LocationY.setter
    def LocationY(self, value: int) -> None:
        self._location_y = value

    @property
    def SourceActions(self) -> int:
        """
        This value represents the action or actions supported by the source.
        """
        return self._source_actions
    
    @SourceActions.setter
    def SourceActions(self, value: int) -> None:
        self._source_actions = value

    @property
    def Transferable(self) -> XTransferable_2d800f38:
        """
        The transferable object associated with the drop.
        """
        return self._transferable
    
    @Transferable.setter
    def Transferable(self, value: XTransferable_2d800f38) -> None:
        self._transferable = value


__all__ = ['DropTargetDropEvent']
