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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
if typing.TYPE_CHECKING:
    from .data_editor_event_type import DataEditorEventType as DataEditorEventType_b080e4b


class DataEditorEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event broadcasted by an XDataEditor.

    See Also:
        `API DataEditorEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DataEditorEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.DataEditorEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.DataEditorEvent'
    """Literal Constant ``com.sun.star.util.DataEditorEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DataEditorEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DataEditorEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Type (DataEditorEventType, optional): Type value
        """
        self._type = None

        key_order = ('Type',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DataEditorEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DataEditorEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Type(self) -> 'DataEditorEventType_b080e4b':
        """
        specifies the type of the event.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: 'DataEditorEventType_b080e4b') -> None:
        self._type = value


__all__ = ['DataEditorEvent']
