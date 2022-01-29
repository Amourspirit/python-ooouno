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
# Namespace: com.sun.star.awt.grid
# Libre Office Version: 7.2
import os
from ...lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class GridSelectionEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridControl to notify changes in its row selection.

    See Also:
        `API GridSelectionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridSelectionEvent.html>`_


    Note:
        | At runtime GridSelectionEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | GridSelectionEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, SelectedColumnIndexes: 'typing.Optional[typing.List[int]]' = None, SelectedRowIndexes: 'typing.Optional[typing.List[int]]' = None):
        self._selected_column_indexes = SelectedColumnIndexes
        self._selected_row_indexes = SelectedRowIndexes

    @property
    def SelectedColumnIndexes(self) -> 'typing.List[int]':
        """
        denotes the indexes of the columns being selected at the time the event was fired.
        """
        return self._selected_column_indexes
    
    @SelectedColumnIndexes.setter
    def SelectedColumnIndexes(self, value: 'typing.List[int]') -> None:
        self._selected_column_indexes = value

    @property
    def SelectedRowIndexes(self) -> 'typing.List[int]':
        """
        denotes the indexes of the rows being selected at the time the event was fired.
        """
        return self._selected_row_indexes
    
    @SelectedRowIndexes.setter
    def SelectedRowIndexes(self, value: 'typing.List[int]') -> None:
        self._selected_row_indexes = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global GridSelectionEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('SelectedColumnIndexes', 'SelectedRowIndexes')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.grid.GridSelectionEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        GridSelectionEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['GridSelectionEvent']
