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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class InputEvent(EventObject_a3d70b03):
    """
    Struct Class

    the root event class for all component-level input events.
    
    Input events are delivered to listeners before they are processed normally by the source where they originated.

    See Also:
        `API InputEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1InputEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.InputEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.InputEvent'
    """Literal Constant ``com.sun.star.awt.InputEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``InputEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``InputEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Modifiers (int, optional): Modifiers value
        """
        self._modifiers = None

        key_order = ('Modifiers',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], InputEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("InputEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Modifiers(self) -> int:
        """
        contains the modifier keys which were pressed while the event occurred.
        
        Zero or more constants from the com.sun.star.awt.KeyModifier group.
        """
        return self._modifiers
    
    @Modifiers.setter
    def Modifiers(self, value: int) -> None:
        self._modifiers = value


__all__ = ['InputEvent']
