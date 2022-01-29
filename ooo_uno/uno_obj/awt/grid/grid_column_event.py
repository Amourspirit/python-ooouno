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


class GridColumnEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridColumn to notify changes in the column.
    
    **since**
    
        OOo 3.3

    See Also:
        `API GridColumnEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridColumnEvent.html>`_


    Note:
        | At runtime GridColumnEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | GridColumnEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, AttributeName: typing.Optional[str] = None, ColumnIndex: typing.Optional[int] = None, NewValue: typing.Optional[object] = None, OldValue: typing.Optional[object] = None):
        self._attribute_name = AttributeName
        self._column_index = ColumnIndex
        self._new_value = NewValue
        self._old_value = OldValue

    @property
    def AttributeName(self) -> str:
        """
        Contains the name of the attributes whose value changed.
        """
        return self._attribute_name
    
    @AttributeName.setter
    def AttributeName(self, value: str) -> None:
        self._attribute_name = value

    @property
    def ColumnIndex(self) -> int:
        """
        Contains the index of the changed column.
        """
        return self._column_index
    
    @ColumnIndex.setter
    def ColumnIndex(self, value: int) -> None:
        self._column_index = value

    @property
    def NewValue(self) -> object:
        """
        Contains the new value.
        """
        return self._new_value
    
    @NewValue.setter
    def NewValue(self, value: object) -> None:
        self._new_value = value

    @property
    def OldValue(self) -> object:
        """
        Contains the old value.
        """
        return self._old_value
    
    @OldValue.setter
    def OldValue(self, value: object) -> None:
        self._old_value = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global GridColumnEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('AttributeName', 'ColumnIndex', 'NewValue', 'OldValue')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.grid.GridColumnEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        GridColumnEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['GridColumnEvent']
