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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class ChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdbc_1_1ChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdbc.ChangeEvent'
    """Literal Constant ``com.sun.star.sdbc.ChangeEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ChangeEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ChangeEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Action (int, optional): Action value
            Rows (int, optional): Rows value
        """
        self._action = None
        self._rows = None

        key_order = ('Action', 'Rows')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ChangeEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ChangeEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Action(self) -> int:
        """
        indicates the type of change.
        """
        return self._action
    
    @Action.setter
    def Action(self, value: int) -> None:
        self._action = value

    @property
    def Rows(self) -> int:
        """
        indicates the number of rows affected by the change.
        """
        return self._rows
    
    @Rows.setter
    def Rows(self, value: int) -> None:
        self._rows = value


__all__ = ['ChangeEvent']
