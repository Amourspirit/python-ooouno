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
# Namespace: com.sun.star.xml
# Libre Office Version: 7.2


class FastAttribute(object):
    """
    Struct Class

    A struct to keep information of an element's attribute.

    See Also:
        `API FastAttribute <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1FastAttribute.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.FastAttribute'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.xml.FastAttribute'
    """Literal Constant ``com.sun.star.xml.FastAttribute``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``FastAttribute`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``FastAttribute``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Token (int, optional): Token value
            Value (str, optional): Value value
        """
        self._token = None
        self._value = None

        key_order = ('Token', 'Value')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], FastAttribute):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("FastAttribute.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Token(self) -> int:
        """
        the token corresponding to the attribute
        """
        return self._token
    
    @Token.setter
    def Token(self, value: int) -> None:
        self._token = value

    @property
    def Value(self) -> str:
        """
        the attribute value
        """
        return self._value
    
    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['FastAttribute']
