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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class TitleChangedEvent(EventObject_a3d70b03):
    """
    Struct Class

    Contains the information about a changed title.

    See Also:
        `API TitleChangedEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1TitleChangedEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.TitleChangedEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.TitleChangedEvent'
    """Literal Constant ``com.sun.star.frame.TitleChangedEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``TitleChangedEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``TitleChangedEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Title (str, optional): Title value
        """
        self._title = None

        key_order = ('Title',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], TitleChangedEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("TitleChangedEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Title(self) -> str:
        """
        The new title.
        """
        return self._title
    
    @Title.setter
    def Title(self, value: str) -> None:
        self._title = value


__all__ = ['TitleChangedEvent']
