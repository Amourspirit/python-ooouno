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
import typing
from ...lang.event_object import EventObject as EventObject_a3d70b03


class GridSelectionEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridControl to notify changes in its row selection.

    See Also:
        `API GridSelectionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridSelectionEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.GridSelectionEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.grid.GridSelectionEvent'
    """Literal Constant ``com.sun.star.awt.grid.GridSelectionEvent``"""

    SelectedRowIndexes: typing.TypeAlias = typing.Tuple[int, ...]
    """
    denotes the indexes of the rows being selected at the time the event was fired.
    """
    SelectedColumnIndexes: typing.TypeAlias = typing.Tuple[int, ...]
    """
    denotes the indexes of the columns being selected at the time the event was fired.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``GridSelectionEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``GridSelectionEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
        """

        key_order = ()
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], GridSelectionEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("GridSelectionEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


__all__ = ['GridSelectionEvent']
