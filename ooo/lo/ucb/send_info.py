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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2


class SendInfo(object):
    """
    Struct Class

    contains information related to a send protocol.
    
    It can contain any string values (server names, user names, passwords, ...).

    See Also:
        `API SendInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SendInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.SendInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.SendInfo'
    """Literal Constant ``com.sun.star.ucb.SendInfo``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``SendInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``SendInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ProtocolType (str, optional): ProtocolType value
            Value (str, optional): Value value
        """
        self._protocol_type = None
        self._value = None

        key_order = ('ProtocolType', 'Value')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], SendInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("SendInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def ProtocolType(self) -> str:
        """
        the protocol to which the info is related (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """
        return self._protocol_type
    
    @ProtocolType.setter
    def ProtocolType(self, value: str) -> None:
        self._protocol_type = value

    @property
    def Value(self) -> str:
        """
        the value.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['SendInfo']
