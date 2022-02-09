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
from ...lang.event_object import EventObject as EventObject_a3d70b03


class DropTargetEvent(EventObject_a3d70b03):
    """
    Struct Class

    This class is the base class for DropTargetDragEvent and DropTargetDropEvent.
    
    To access the XDropTarget that originated this event, use the com.sun.star.lang.EventObject.Source member of this object.

    See Also:
        `API DropTargetEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DropTargetEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DropTargetEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DropTargetEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DropTargetEvent``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DropTargetEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DropTargetEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Dummy (int, optional): Dummy value
        """
        self._dummy = None

        key_order = ('Dummy',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DropTargetEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DropTargetEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Dummy(self) -> int:
        """
        UNO specification does not allow empty struct definitions.
        """
        return self._dummy
    
    @Dummy.setter
    def Dummy(self, value: int) -> None:
        self._dummy = value


__all__ = ['DropTargetEvent']
