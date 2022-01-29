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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
import os
import typing
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
    from ..view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ContextMenuExecuteEvent(object):
    """
    Struct Class

    contains all information about the requested context menu.

    See Also:
        `API ContextMenuExecuteEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ContextMenuExecuteEvent.html>`_


    Note:
        | At runtime ContextMenuExecuteEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ContextMenuExecuteEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, ActionTriggerContainer: 'typing.Optional[XIndexContainer_1c040ebe]' = None, ExecutePosition: 'typing.Optional[Point_5fb2085e]' = None, Selection: 'typing.Optional[XSelectionSupplier_fed20e15]' = None, SourceWindow: 'typing.Optional[XWindow_713b0924]' = None):
        self._action_trigger_container = ActionTriggerContainer
        self._execute_position = ExecutePosition
        self._selection = Selection
        self._source_window = SourceWindow

    @property
    def ActionTriggerContainer(self) -> 'XIndexContainer_1c040ebe':
        """
        enables the access to the menu content.
        
        The implementing object has to support the service com.sun.star.ui.ActionTriggerContainer;
        """
        return self._action_trigger_container
    
    @ActionTriggerContainer.setter
    def ActionTriggerContainer(self, value: 'XIndexContainer_1c040ebe') -> None:
        self._action_trigger_container = value

    @property
    def ExecutePosition(self) -> 'Point_5fb2085e':
        """
        contains the position the context menu will be executed at.
        """
        return self._execute_position
    
    @ExecutePosition.setter
    def ExecutePosition(self, value: 'Point_5fb2085e') -> None:
        self._execute_position = value

    @property
    def Selection(self) -> 'XSelectionSupplier_fed20e15':
        """
        provides the current selection inside the source window.
        """
        return self._selection
    
    @Selection.setter
    def Selection(self, value: 'XSelectionSupplier_fed20e15') -> None:
        self._selection = value

    @property
    def SourceWindow(self) -> 'XWindow_713b0924':
        """
        contains the window where the context menu has been requested
        """
        return self._source_window
    
    @SourceWindow.setter
    def SourceWindow(self, value: 'XWindow_713b0924') -> None:
        self._source_window = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ContextMenuExecuteEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('ActionTriggerContainer', 'ExecutePosition', 'Selection', 'SourceWindow')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ui.ContextMenuExecuteEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ContextMenuExecuteEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ContextMenuExecuteEvent']
