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
# Namespace: com.sun.star.ui
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..awt.point import Point as Point_5fb2085e
from ..awt.x_window import XWindow as XWindow_713b0924
from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
from ..view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15


class ContextMenuExecuteEvent(object):
    """
    Struct Class

    contains all information about the requested context menu.

    See Also:
        `API ContextMenuExecuteEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ContextMenuExecuteEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ContextMenuExecuteEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.ContextMenuExecuteEvent'
    """Literal Constant ``com.sun.star.ui.ContextMenuExecuteEvent``"""

    def __init__(self, SourceWindow: typing.Optional[XWindow_713b0924] = None, ExecutePosition: typing.Optional[Point_5fb2085e] = UNO_NONE, ActionTriggerContainer: typing.Optional[XIndexContainer_1c040ebe] = None, Selection: typing.Optional[XSelectionSupplier_fed20e15] = None) -> None:
        """
        Constructor

        Arguments:
            SourceWindow (XWindow, optional): SourceWindow value.
            ExecutePosition (Point, optional): ExecutePosition value.
            ActionTriggerContainer (XIndexContainer, optional): ActionTriggerContainer value.
            Selection (XSelectionSupplier, optional): Selection value.
        """
        super().__init__()

        if isinstance(SourceWindow, ContextMenuExecuteEvent):
            oth: ContextMenuExecuteEvent = SourceWindow
            self.SourceWindow = oth.SourceWindow
            self.ExecutePosition = oth.ExecutePosition
            self.ActionTriggerContainer = oth.ActionTriggerContainer
            self.Selection = oth.Selection
            return

        kargs = {
            "SourceWindow": SourceWindow,
            "ExecutePosition": ExecutePosition,
            "ActionTriggerContainer": ActionTriggerContainer,
            "Selection": Selection,
        }
        if kargs["ExecutePosition"] is UNO_NONE:
            kargs["ExecutePosition"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._source_window = kwargs["SourceWindow"]
        self._execute_position = kwargs["ExecutePosition"]
        self._action_trigger_container = kwargs["ActionTriggerContainer"]
        self._selection = kwargs["Selection"]


    @property
    def SourceWindow(self) -> XWindow_713b0924:
        """
        contains the window where the context menu has been requested
        """
        return self._source_window

    @SourceWindow.setter
    def SourceWindow(self, value: XWindow_713b0924) -> None:
        self._source_window = value

    @property
    def ExecutePosition(self) -> Point_5fb2085e:
        """
        contains the position the context menu will be executed at.
        """
        return self._execute_position

    @ExecutePosition.setter
    def ExecutePosition(self, value: Point_5fb2085e) -> None:
        self._execute_position = value

    @property
    def ActionTriggerContainer(self) -> XIndexContainer_1c040ebe:
        """
        enables the access to the menu content.
        
        The implementing object has to support the service com.sun.star.ui.ActionTriggerContainer;
        """
        return self._action_trigger_container

    @ActionTriggerContainer.setter
    def ActionTriggerContainer(self, value: XIndexContainer_1c040ebe) -> None:
        self._action_trigger_container = value

    @property
    def Selection(self) -> XSelectionSupplier_fed20e15:
        """
        provides the current selection inside the source window.
        """
        return self._selection

    @Selection.setter
    def Selection(self, value: XSelectionSupplier_fed20e15) -> None:
        self._selection = value


__all__ = ['ContextMenuExecuteEvent']
