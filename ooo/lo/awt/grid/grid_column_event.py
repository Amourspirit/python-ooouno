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
from ...lang.event_object import EventObject as EventObject_a3d70b03


class GridColumnEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridColumn to notify changes in the column.
    
    **since**
    
        OOo 3.3

    See Also:
        `API GridColumnEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridColumnEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.GridColumnEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.grid.GridColumnEvent'
    """Literal Constant ``com.sun.star.awt.grid.GridColumnEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``GridColumnEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``GridColumnEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            AttributeName (str, optional): AttributeName value
            OldValue (object, optional): OldValue value
            NewValue (object, optional): NewValue value
            ColumnIndex (int, optional): ColumnIndex value
        """
        self._attribute_name = None
        self._old_value = None
        self._new_value = None
        self._column_index = None

        key_order = ('AttributeName', 'OldValue', 'NewValue', 'ColumnIndex')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], GridColumnEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("GridColumnEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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
    def OldValue(self) -> object:
        """
        Contains the old value.
        """
        return self._old_value
    
    @OldValue.setter
    def OldValue(self, value: object) -> None:
        self._old_value = value

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
    def ColumnIndex(self) -> int:
        """
        Contains the index of the changed column.
        """
        return self._column_index
    
    @ColumnIndex.setter
    def ColumnIndex(self, value: int) -> None:
        self._column_index = value


__all__ = ['GridColumnEvent']
