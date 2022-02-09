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


class DocumentHeaderField(object):
    """
    Struct Class

    This struct contains a name-value pair of a document header (i.e.
    
    the \"subject\" field and the appropriate value of a MIME message).

    See Also:
        `API DocumentHeaderField <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1DocumentHeaderField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.DocumentHeaderField'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.DocumentHeaderField'
    """Literal Constant ``com.sun.star.ucb.DocumentHeaderField``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DocumentHeaderField`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DocumentHeaderField``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Name (str, optional): Name value
            Value (str, optional): Value value
        """
        self._name = None
        self._value = None

        key_order = ('Name', 'Value')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DocumentHeaderField):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DocumentHeaderField.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Name(self) -> str:
        """
        The name of the header field.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Value(self) -> str:
        """
        The value of the header field.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['DocumentHeaderField']
