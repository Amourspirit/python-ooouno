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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2


class ItemStatus(object):
    """
    Struct Class

    describes a state of a property.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ItemStatus <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ItemStatus.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.ItemStatus'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.ItemStatus'
    """Literal Constant ``com.sun.star.frame.status.ItemStatus``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ItemStatus`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ItemStatus``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            State (int, optional): State value
            aStateData (object, optional): aStateData value
        """
        self._state = None
        self._a_state_data = None

        key_order = ('State', 'aStateData')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ItemStatus):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ItemStatus.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def State(self) -> int:
        """
        numerical value which describes the current state of an item.
        """
        return self._state
    
    @State.setter
    def State(self, value: int) -> None:
        self._state = value

    @property
    def aStateData(self) -> object:
        """
        optional data which can be used by an implementation to send additional information.
        
        The content is dependent on the specific implementation.
        """
        return self._a_state_data
    
    @aStateData.setter
    def aStateData(self, value: object) -> None:
        self._a_state_data = value


__all__ = ['ItemStatus']
